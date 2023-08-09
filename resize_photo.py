from PIL import Image
import os
new_highet=int(input("please enter the highet : "))
new_width=int(input("please enter the width  : "))
filelocation=input("enter the path of the file ")
os.chdir(rf"{filelocation}")
open_file=os.listdir(rf"{filelocation}")
for image_name in open_file:
        if not image_name.endswith((".jpg",".png","jpeg")):
                continue
        photo=Image.open(image_name)
        highet,width= photo.size
        resized=photo.resize((new_width,new_highet))
        resized.save(image_name)
        