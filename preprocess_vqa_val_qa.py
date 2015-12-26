import numpy as np
import pdb
import time

#tv = 'train'
tv = 'val'
timestr = time.strftime("%Y%m%d-%H%M%S")
train_ans_fea_path = '../../CDSSM/data/vqa/'+ tv + '.tgt.seq.fea'
train_ques_fea_path  = '../../CDSSM/data/vqa/'+ tv + '.src.seq.fea'
train_ques_l3g_path  = '../../CDSSM/data/vqa/'+ tv +'.src.l3g.txt'

# modified by siddharth, 20151031
print 'reading %s' %(train_ans_fea_path)
train_ans_fea  = np.genfromtxt(train_ans_fea_path,delimiter="\n", dtype=None)
print 'reading %s' %(train_ques_fea_path)
train_ques_fea = np.genfromtxt(train_ques_fea_path,delimiter="\n", dtype=None)

l3g = open(train_ques_l3g_path).readlines()
print 'reading files done'

numQuesFeats = len(l3g)
print 'offset %s' %numQuesFeats

f  = open('../../CDSSM/data/vqa/' + tv + '.ans_plus_ques.src.fea.full', 'ab')
print "Creating question+answer features..."
prev_img_file_name = ' '
for i,line in enumerate(train_ques_fea):
        print i
	imgItems = train_ans_fea[i]
    	imgConcatItems = []
	temp = imgItems.split(" ")
	for count, item in enumerate(temp):
		parts=item.split(":")
		#sparse format
		newKey = int(parts[0]) + numQuesFeats
		imgConcatItems.append(str(newKey) + ':' + parts[1])	
	#pdb.set_trace()
	imgLine = ' '.join(imgConcatItems)
	f.write(line + ' ' + imgLine + '\n')
					
print "Creating question+image feature file done."

f.close()
