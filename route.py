import scipy 
from scipy import misc 
import os 
import time 
import glob 
from scipy import ndimage 

def get_image_paths(folder): 
    return glob.glob(os.path.join(folder, '*.png')) 

def create_read_img(filename): 
    im = misc.imread(filename) 
    img_rote_90 = ndimage.rotate(im, 90)  
    scipy.misc.imsave(filename[:-4]+'_90.png',img_rote_90) 
    
    img_rote_180 = ndimage.rotate(im, 180) 
    scipy.misc.imsave(filename[:-4]+'_180.png',img_rote_180) 

    img_rote_270 = ndimage.rotate(im, 270) 
    scipy.misc.imsave(filename[:-4]+'_270.png',img_rote_270) 
    print(filename)
img_path = '/media/wxy/000F8E4B0002F751/test/' 
imgs = get_image_paths(img_path) 
#print (imgs) 

for i in imgs: 
    create_read_img(i)
