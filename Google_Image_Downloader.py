import requests,os
from PIL import Image
from io import BytesIO

def download_image():
    #inputs 
    url=fr"{input('Enter Url : ')}"
    file_location=fr"{input('File Location : ')}"
    name_of_image=fr"{input('Name of image : ')}"
    #go to the file location
    os.chdir(fr"{file_location}")

    response = requests.get(url)
    # check data in the link is photo or no  
    
    image = Image.open(BytesIO(response.content))
    format = image.format
    if format:
        with open(os.path.join(os.getcwd(), f"{name_of_image}.{format}"), "wb") as f:
         f.write(response.content)
    else:
       print("error")

download_image()