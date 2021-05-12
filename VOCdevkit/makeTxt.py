from sklearn.model_selection import train_test_split
import os
name_path = r'.\data\VOCdevkit2007\VOC2007\JPEGImages'
name_list = os.listdir(name_path)
names = []
for i in name_list:
	# 获取图像名
    names.append(i.split('.')[0])
trainval,test = train_test_split(names,test_size=0.5,shuffle=10)
val,train = train_test_split(trainval,test_size=0.5,shuffle=10)
with open('ImageSets/Main/trainval.txt','w') as fw:
    for i in trainval:
        fw.write(i+'\n')

with open('ImageSets/Main/test.txt','w') as fw:
    for i in test:
        fw.write(i+'\n')

with open('ImageSets/Main/val.txt','w') as fw:
    for i in val:
        fw.write(i+'\n')

with open('ImageSets/Main/train.txt','w') as fw:
    for i in train:
        fw.write(i+'\n')

print('done!')
