import os
import allennlp

for i in range(1,1000):
	infile = 'data_val/val_'+str(i)+'.json'
	outfile = 'out/pred_'+str(i)+'.json'
	os.system('allennlp predict log_bidaf/model.tar.gz ' + infile + ' --output-file ' + outfile)
