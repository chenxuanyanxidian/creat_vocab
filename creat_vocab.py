# -*- coding: utf-8 -*-
import codecs
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def create_vocab(input_file,output_file):#,keep_fre = 0):
	input_data = codecs.open(input_file,'r','utf-8').read().split('\n')
	output_data = codecs.open(output_file,'w','utf-8')
	tt = []
    
	for line in input_data:
		for word in line:
			tt.append(word)
	aa = sorted(set(tt))
	for t in aa:
		output_data.write(t+'\n')
if __name__ == '__main__':
	create_vocab('poetry.txt','vocab.data')
