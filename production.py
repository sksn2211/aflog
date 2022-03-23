# import OS module
from fileinput import filename
from importlib.resources import path
from itertools import count
from msilib.schema import File
import os
from tkinter import W
from PIL import Image
import pathlib
import csv
skupool = []
with open(r'C:\Users\shiva\OneDrive\Desktop\image-sheet.csv', 'w', newline='') as csvfile:
    with open(r'C:\Users\shiva\OneDrive\Desktop\enable-product.csv', 'w', newline='') as csvfile2:
        with open(r'C:\Users\shiva\OneDrive\Desktop\vendor-id.csv', 'w', newline='') as csvfile3:

            csvwriter = csv.writer(csvfile)
            csvwriter2 = csv.writer(csvfile2)
            csvwriter3 = csv.writer(csvfile3)            
            csvwriter.writerow(['sku','base_image','base_image_label','small_image','small_image_label','thumbnail_image','thumbnail_image_label','swatch_image','swatch_image_label','hover_image','hover_image_label','additional_images','additional_image_label'])
            csvwriter2.writerow(['sku','status'])
            csvwriter3.writerow(['seller_name','sku','status'])
            count = 0
            input = r'C:\Users\shiva\OneDrive\Desktop\LISHA372'
            maxsize = (600,600)
            for input_img_path in pathlib.Path(input).iterdir():
                # print(input_img_path)
                path = str(input_img_path).replace(' ','')
                output_img_path = str(path).replace("input","output")
                jpeg = '.jpg'
                with Image.open(input_img_path) as im:
                    if input_img_path.suffix == jpeg:
                        # sku = os.path.splitext(input_img_path)
                        im.thumbnail(maxsize)
                        im.save(output_img_path, "JPEG", dpi=(600,600))
                        # print(f"processing file {input_img_path} done...")
                        # print(f"processing file ",count,"done!")
                        filenamepath = output_img_path.split('\\')
                        filename = filenamepath[-1]
                        sku = os.path.splitext(filename)
                        sku = sku[0]
                        skupool.append(sku)
                        status = 1
                        csvwriter.writerow([sku,filename,'',filename,'',filename,'',filename,'',filename,'',filename,''])
                        csvwriter2.writerow([sku,status])
                        csvwriter3.writerow(['149',sku,status])
                        count = count + 1
                        print('>>>>>')
                        print('>>>>>>>>>>>')
                        print('>>>>>')


                    else:
                        print(f'Duplicates found:{input_img_path}')
                        input_img_path.rename

            print(f"processed file:{count}-Done!")
            # print(skupool)
             

