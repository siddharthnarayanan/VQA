# read the json file, and generate the pair data for DSSM. 

import json
import numpy as np
from vqa_utils import process_string, most_common, save_json, load_json, gen_tokens, gen_mapping
from collections import defaultdict
import operator
from PreProcess import get_top_ans
from vqa_utils import process_string, most_common, save_json, load_json, gen_tokens, gen_mapping
import pdb
top_ans_num = 1000

top_answers = get_top_ans(top_ans_num)


tv = 'val'#'train'

train_anno_path = '../data/VQA_data/mscoco_' + tv + '2014_annotations.json'
train_ques_path = '../data/VQA_data/MultipleChoice_mscoco_'+ tv +'2014_questions.json'

print 'reading %s' %(train_ques_path)
train_ques = json.load(open(train_ques_path, 'r'))	
print 'reading %s' %(train_anno_path)
train_anno = json.load(open(train_anno_path, 'r'))

f = open('VQA_pair_'+ tv +'.new.txt', 'ab')
f1 = open('VQA_pair_id_'+tv +'.new.txt', 'ab')
for i in range(len(train_ques['questions'])):
	#if i==1:
	#	break
	ques = process_string(train_ques['questions'][i]['question'].encode('utf-8').lower())
	multi =  train_ques['questions'][i]['multiple_choices']
	#print multi
	process_multi = []
	
	ques_id = train_ques['questions'][i]['question_id']
	img_id = train_ques['questions'][i]['image_id']
	img_name = 'COCO_'+tv+'2014_'+'000000'+str(img_id)+'.jpg'
	list_of_ans = train_anno['annotations'][i]['answers']

#	for m in multi:
#		f.write(ques+'\t')
#		this_m=m.encode('utf-8').lower()
#		f.write(this_m+'\n')
#		f1.write(str(ques_id)+'\t')
#		f1.write(img_name+'\n')


	process_ans = []
	for ans in list_of_ans:
		this_ans = ans['answer'].encode('utf-8').lower()
		process_ans.append(this_ans)
#		#print this_ans
	common_ans = most_common(process_ans)
#	
#	pdb.set_trace()
	if common_ans in top_answers:
#	pdb.set_trace()
	
		for m in multi:
			f.write(ques+'\t')
			this_m=m.encode('utf-8').lower()
			f.write(this_m+'\n')
			f1.write(str(ques_id)+'\t')
			f1.write(img_name+'\n')

f.close()
f1.close()
