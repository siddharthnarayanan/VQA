import numpy as np
import pdb

tv = 'train'
#tv = 'val'

# modified by jinchoi, 20151012
train_img_fea_path   = '../../CDSSM/data/vqa/' + tv + '2014_fc7.npy'
train_img_name_path  = '../../CDSSM/data/vqa/img_name_' + tv + '.npy'
train_ques_fea_path  = '../../CDSSM/data/vqa/'+ tv + '.src.seq.fea'
train_ques_name_path = '../../CDSSM/data/vqa/VQA_pair_id_'+ tv + '.txt'

# modified by jinchoi, 20151012
print '%s' %(train_img_fea_path)
print 'reading %s' %(train_img_fea_path)
train_img_fea   = np.load(train_img_fea_path)
print 'reading %s' %(train_img_name_path)
train_img_name  = np.load(train_img_name_path)
print 'reading %s' %(train_ques_fea_path)
train_ques_fea = np.genfromtxt(train_ques_fea_path,delimiter="\n", dtype=None)
print 'reading %s' %(train_ques_name_path)
train_ques_name = np.genfromtxt(train_ques_name_path,delimiter="\n", dtype=None)
print 'reading files done'

#f  = open('../data/combined_feature/' + tv + '.img_plus_ques.src.fea', 'ab')
f  = open('../../CDSSM/data/vqa/' + tv + '.img.src.fea.full', 'ab')
print "Creating image features..."
prev_img_file_name = ' '
for i,line in enumerate(train_ques_fea):
	print i
        line = line.strip()
	ques_img_file_name = train_ques_name[i].split("\t")[1].split('_')[2].strip('0').split('.')[0]
	# matchFlag = False
	if ques_img_file_name == prev_img_file_name:
		f.write(imgLine + '\n')
	else:
		matchFlag = False
		for j in range(len(train_img_name)):
			img_file_name = train_img_name[j].split("/")[-1].split('_')[2].strip('0').split('.')[0]
			#pdb.set_trace()
			# find the corresponding image feature line
			if ques_img_file_name == img_file_name:
				# do concatenation
				matchFlag = True
				imgItems = train_img_fea[j]
				imgConcatItems = []
				for count, item in enumerate(imgItems):
					#sparse format
					if item != 0:
						newKey = count
						imgConcatItems.append(str(newKey) + ':' + str(float(item)))
						#pdb.set_trace()
				imgLine = ' '.join(imgConcatItems)
				#f.write(line + ' ' + imgConcatItems + '\n')
				f.write(imgLine + '\n')
				prev_img_file_name = img_file_name
				break
		if matchFlag == False:
			print "no matched img_file_name with ques_img_file_name%s!" %(ques_img_file_name)

print "Creating image feature file done."

f.close()
