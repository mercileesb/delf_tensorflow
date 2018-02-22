import glob
import os


f = open("total_train_list.txt")


a = f.readlines()[5000:10000]

samplefile = open("delf/examples/sample_list_5000_2.txt","w")

for item in a:
	samplefile.write(item)

samplefile.close()


f.close()






