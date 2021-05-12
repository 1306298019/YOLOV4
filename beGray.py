from PIL import Image
import os
path = r'C:\Users\DD\Desktop\加油\数据处理\gray'
file_list = os.listdir(path)
for file in file_list:
    I = Image.open(path+"/"+file)
    L = I.convert('L')
    L.save(path+"/"+file)
    #print(file)

