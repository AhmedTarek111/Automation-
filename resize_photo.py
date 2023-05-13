from PIL import Image
import os
new_highet=600
new_width=600
# new_highet=int(input("please enter the highet : "))
# new_width=int(input("please enter the width  : "))
os.chdir(r"C:\Users\Ahmed tareq's pc\OneDrive\Desktop\stock")
open_file=os.listdir(r"C:\Users\Ahmed tareq's pc\OneDrive\Desktop\stock")
for image_name in open_file:
        if not image_name.endswith((".jpg",".png","jpeg")):
                continue
        photo=Image.open(image_name)
        highet,width= photo.size
        resized=photo.resize((new_width,new_highet))
        resized.save(image_name)
        