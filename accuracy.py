# read the json file, and generate the pair data for DSSM. 

from __future__ import division
import json
import numpy as np
from vqa_utils import process_string, most_common, save_json, load_json, gen_tokens, gen_mapping
from collections import defaultdict
import operator
from PreProcess import get_top_ans
from vqa_utils import process_string, most_common, save_json, load_json, gen_tokens, gen_mapping
import pdb




#top_ans_num = 1000
#top_answers = get_top_ans(top_ans_num)


tv = 'val'#'train'

#train_anno_path = '../data/VQA_data/mscoco_' + tv + '2014_annotations.json'
#train_ques_path = '../data/VQA_data/MultipleChoice_mscoco_'+ tv +'2014_questions.json'
VQA_pair_path = '../data/VQA_data/VQA_pair_val.new.txt'
prediction_result_path_new = '../data/VQA_data/IQ_A_predict.txt'
ground_truth_path = '../data/VQA_data/VQA_pair_val.txt'

print 'reading %s' %(prediction_result_path_new)
prediction_result_all = open(prediction_result_path_new).readlines()
print 'reading %s' %(VQA_pair_path)
VQA_pair = open(VQA_pair_path).readlines()
print 'reading %s' %(ground_truth_path)
ground_truth = open(ground_truth_path).readlines()

#print 'reading %s' %(train_ques_path)
#train_ques = json.load(open(train_ques_path, 'r'))	
#print 'reading %s' %(train_anno_path)
#train_anno = json.load(open(train_anno_path, 'r'))

k=0
A=[]
max_ind = 0
batch = 1
flag=0
prediction_list=[]
answer_list=[]

f = open('prediction_list.txt', 'ab')
f1 = open('answer_list.txt', 'ab')

for i,line in enumerate(prediction_result_all):
#	if i> 50:
#		break	
	A.append(line)
	if line == max(A): 
		max_ind = i 
	if i>2 and i % 18 == 0:
#		print 'maximum of batch     '+ str(batch) + '  is:  ' + max(A)
#		print max_ind
		prediction_list.append(max_ind+1) 
		f.write(str(max_ind+1)+'\n')
#		print '\n'
#		print 'corresponding line is: ' + line2
#		print '-------------\n\n'
		A=[]
		batch +=1


for i,line in enumerate (VQA_pair):
#	if i > 50:
#		break
	#print 'truth' + ground_truth[flag]
	#print 'line' + line	
	#if any(line in s for s in ground_truth):
	if line == (ground_truth[flag]) and len(line) == len (ground_truth[flag]):
		answer_list.append(i+1)
		f1.write(str(i+1)+'\n')
		#print flag
		if flag <= 104536:
			flag+=1



	
#print prediction_list
#print answer_list
#f.write(prediction_list)
#f1.write(answer_list)


num =  len(set(prediction_list) & set(answer_list))
den = 104537

accuracy  = (num/den)*100


print num
print den
print 'accuracy is : \n'
print accuracy

#	ques = process_string(train_ques['questions'][i]['question'].encode('utf-8').lower())
#	multi =  train_ques['questions'][i]['multiple_choices']
	#print multi

#	process_multi = []
	
#	ques_id = train_ques['questions'][i]['question_id']
#	img_id = train_ques['questions'][i]['image_id']
#	img_name = 'COCO_'+tv+'2014_'+'000000'+str(img_id)+'.jpg'
#	list_of_ans = train_anno['annotations'][i]['answers']

#	for m in multi:
#		f.write(ques+'\t')
#		this_m=m.encode('utf-8').lower()
#		f.write(this_m+'\n')
#		f1.write(str(ques_id)+'\t')
#		f1.write(img_name+'\n')


#	process_ans = []
#	for ans in list_of_ans:
#		this_ans = ans['answer'].encode('utf-8').lower()
#		process_ans.append(this_ans)
#		#print this_ans
#	common_ans = most_common(process_ans)
#	
#	pdb.set_trace()
#	if common_ans in top_answers:
#	pdb.set_trace()
	
#		for m in multi:
#			f.write(ques+'\t')
#			this_m=m.encode('utf-8').lower()
#			f.write(this_m+'\n')
#			f1.write(str(ques_id)+'\t')
#			f1.write(img_name+'\n')

f.close()
f1.close()
