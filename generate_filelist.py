

'''
python extract_features.py \
  --config_path delf_config_example.pbtxt \
  --list_images_path list_images.txt \
  --output_dir data/oxford5k_features

'''


import os

#test

FILEPATH = "/media/mmlab/hdd/Shin/retrieval/test"
test_filelist = os.listdir("/media/mmlab/hdd/Shin/retrieval/test")
test_txt = open("total_test_list.txt", "w")

#train
# FILEPATH = "/media/mmlab/hdd/Shin/recognition/train"
# train_filelist = os.listdir("/media/mmlab/hdd/Shin/recognition/train")
# train_txt = open("total_train_list.txt", "w")


print len(test_filelist)
for item in test_filelist:
	filepath = os.path.join(FILEPATH, item)
	test_txt.write("{}\n".format(filepath))
test_txt.close()

# print len(train_filelist)
# for item in train_filelist:
# 	filepath = os.path.join(FILEPATH, item)
# 	train_txt.write("{}\n".format(filepath))
# train_txt.close()

