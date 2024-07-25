
from PIL import Image,ImageStat,ImageEnhance,UnidentifiedImageError
import matplotlib.pyplot as plt
import random
import os
import numpy as np
from datetime import datetime
import cv2
# addPrefix
addPrefix=lambda content,prefix,check :prefix+" "+check  if check ==content else check
 #check is Image
isImage= lambda path:True if os.path.basename(path).lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) else False
#covert image format (grayscale?)
pil_IMAGEConvert=lambda image,convert='L':image.convert(convert) if convert in ('L','RGB','1','RGBA',"P","CMYK","HSV") else print("Invalid convert") 
# resize image


resize_image =lambda size,image=None,imagepath=None:Image.open(imagepath).resize(size) if image==None else image.resize(size)

# resize of folder of images
def resize_image_folder(ImageSetPaths,size=(150,150)):
    for pathname in ImageSetPaths:
        if os.path.exists(pathname):
            file_size = os.path.getsize(pathname)
            if file_size > 100:
                    try:
                        with Image.open(pathname) as image:
                            img= image.resize(size)
                            img.save(pathname)
                    except UnidentifiedImageError:
                        print(f'error{pathname}')
            else:
                print(f"File '{pathname}' seems too small, possibly truncated.")
        else:
            print(pathname)
    print("resized all images")
# rotate Image
rotate_image =lambda rotate=90,image=None,imagepath=None:Image.open(imagepath).rotate(rotate) if image==None else image.rotate(rotate)
# flip image
Flip_image =lambda FlipMode=Image.FLIP_LEFT_RIGHT,image=None,imagepath=None:Image.open(imagepath).transpose(FlipMode) if image==None else image.transpose(FlipMode)
# random convert
def random_convert(image):
    converts=('L','RGB','1')
    convert=random.choice(converts)
    return image.convert(convert)

# random rotate

def random_rotate(image):
    rotate=random.uniform(0,360)
    return image.rotate(rotate)

#random flip

def random_flip(image):
    flip_option=[Image.ROTATE_90,Image.ROTATE_180,Image.ROTATE_270,Image.FLIP_TOP_BOTTOM,Image.FLIP_LEFT_RIGHT]
    flip=flip_option[random.randint(1,4)]
    return image.transpose(flip)
# random brightness
def random_Bright(image):
    enhancer = ImageEnhance.Brightness(image)
    factor=random.uniform(0.5, 0.8)
    return enhancer.enhance(factor)
# random Contract level

def random_contrast(image):
    enhancer = ImageEnhance.Contrast(image)
    factor=random.uniform(0.5, 0.8)
    return enhancer.enhance(factor)
# random image

def randomImage(Imageset,count=1):
    if len(Imageset)<count:
        raise Exception("Imageset must bigger than expect count")
    randomSample=0
    if count !=1:
        randomSample=random.sample(Imageset,count)
    else:
        randomSample=random.choice(Imageset)
    return randomSample

# ayush Image Class
class AyushImage:
    def __init__(self,imagepath):
        if  not os.path.exists(imagepath) or not os.path.isfile(imagepath):
            raise Exception("In valid Path")
        self._image=Image.open(imagepath)
        self._path=imagepath
    def  size(self):
       return self._image.size
    def image(self):
        return self._image
    def show(self):
        self._image.show()
    def name(self):
        return os.path.basename(self._path)
    def save(self,savepath=None):
        save =savepath if savepath !=None else os.path.basename(self._path)
        if os.path.isdir(save)  and not os.path.exists(save):
            os.makedirs(save)
            save=os.path.join(save,os.path.basename(self._path))
        self._image.save(save)
    def dirctory(self):
        return os.path.basename(self.path)
    def exe(self):
        return os.path.splitext(self._path)[1]
    def volume(self,unit='b'):
        cap=os.path.getsize(self._path)
        if unit=='kb':
            cap=cap/1024
        if unit=='mb':
            cap=cap/(1024**2)
        if unit =='gb':
            cap=cap/(1024**3)
        return cap
    def path(self):
        return self._path
    def relativepath(self,relative):
        return os.path.relpath(self._path,relative)
    def createtime(self):
        return os.path.getctime(self._path)
    def data(self):
        return {
            'size':self._image.size,
            'name':os.path.basename(self._path),
            'volume_kb':os.path.getsize(self._path)/1024,
            'create_at':os.path.getctime(self._path),
            'dir':os.path.basename(self._path),
            'res':self._image.info.get('dpi'),
            'mode':self._image.mode
        }
    def info(self):
        return self._image.info
    def mode(self):
        return self._image.mode
    def histrogram(self):
        return self._image.convert('L').histogram()    

# image Dataset muniplication
def DataSetManuplication(pathList,manuplicationfunction,tool='PIL'):
    for path in pathList:
        if not os.path.isfile(path):
            raise Exception(f"Process items invalid{path}")
        if not os.path.exists(path):
            raise Exception(f'{path} Not found')
        if not isImage(path):
            raise Exception(f'{path} Not found')
        if tool  =='PIL':
            with Image.open(path) as image:
                modifyimage=manuplicationfunction(image)
                modifyimage.save(path)
        else:
            image=cv2.imread(path)
            modifyimage=manuplicationfunction(image)
            cv2.imwrite(path,modifyimage)
    print('action complete')

# image genration
def DataSetgenration(pathList,genrationFun,target_count=10,tool="PIL",save_dir=None):
    for path in pathList:
        if not os.path.isfile(path):
            raise Exception(f"Process items invalid{path}")
        if not os.path.exists(path):
            raise Exception(f'{path} Not found')
        if not isImage(path):
            raise Exception(f'{path} Not found')
    for path in pathList:
        if os.path.dirname(path) in 'gen':
            pathList.remove(path)
    if save_dir !=None and not os.path.exists(save_dir):
            os.makedirs(save_dir)
    count=1
    while count <=target_count:
        random_image=random.choice(pathList)
        saving_dir =os.path.dirname(random_image) if save_dir==None else save_dir
        base_name,exe=os.path.splitext(os.path.basename(random_image))
        split_name=base_name.split("_")
        split_name.insert(-1,'gen')
        name='_'.join(split_name)
        saving=os.path.join(saving_dir,f'{name}.png')
        image=Image.open(random_image)
        for function in genrationFun:
            image=function(image)
        image.save(saving) 
        count=count+1
        
    print('action complete')

# Historgaram
def DrawHistrogram(histrogram,name,show=True,save="histrogram.jpg",fig=(4,4)):
    plt.figure(figsize=fig)
    plt.hist(histrogram, bins=256, range=(0, 256), color='gray')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    title="Histrogram"
    if name:
        title=name
    plt.title(title)
    if show:
        plt.show()
