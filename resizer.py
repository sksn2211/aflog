import os
import glob
import PIL
from PIL import Image
import pathlib

path = "/home/sksn/Desktop/images/flowers"
export_path = "/home/sksn/Desktop/images/flowers/final_img"

if not os.path.exists(export_path):
    os.makedirs(export_path)
count = 0   
files = os.listdir(path)
for file in glob.glob('/home/sksn/Desktop/images/flowers/*'):
    if file.endswith(".png") or file.endswith(".PNG") or file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".jpeg")or file.endswith(".JPEG"):
        img = Image.open(file)
        img = img.resize((800,800),PIL.Image.ANTIALIAS)
        # H,W =img.size
        print('resizing...')    
        file_extension = pathlib.Path(file).suffix
        replace = file.replace(file_extension,'')
        rename = replace + '.png'
        img.save('{}{}{}'.format(export_path,'/',os.path.split(rename)[1]),)
        count = count+1        
print(count,'done!')    
