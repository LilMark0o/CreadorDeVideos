import enum
from fileinput import filename
from importlib.metadata import files
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from PIL  import Image
import os

de_donde = os.path.join(SAMPLE_OUTPUTS,"images_rezised")
a_donde = os.path.join(SAMPLE_OUTPUTS,"final_images")

def create_img_final():
    os.makedirs(de_donde,exist_ok=True)
    os.makedirs(a_donde,exist_ok=True)
    fondo_path = os.path.join(de_donde,"background.jpg")
    fondo = Image.open(fondo_path)
    files_names = os.listdir(de_donde)
    filepaths=[]
    for file_name in files_names:
        size = len(file_name)
        if (file_name!="background.jpg") and ((file_name[size-3:size])=="jpg" or (file_name[size-3:size])=="png" or (file_name[size-3:size])=="jpeg"):
            path = os.path.join(de_donde,file_name)
            filepaths.append(path)

    final_result = []
    for file_path in filepaths:
        image = Image.open(file_path)
        x = int((fondo.size[0]-image.size[0])/2)
        y = int((fondo.size[1]-image.size[1])/2)
        back_im = fondo.copy()
        back_im.paste(image, (x, y))
        final_result.append(back_im)

    for (i,new) in enumerate(final_result):
        new.save('{}{}{}'.format(a_donde+"/img",i+1,'.jpg', quality=95))

# create_img_final()