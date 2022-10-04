import enum
from fileinput import filename
from importlib.metadata import files
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from PIL  import Image
import os

image_dir = os.path.join(SAMPLE_INPUTS,"images")
os.makedirs(image_dir,exist_ok=True)
image_dir_lol = os.path.join(SAMPLE_INPUTS,"images_buenas_experimento")
os.makedirs(image_dir_lol,exist_ok=True)
image_dir_final_exp = os.path.join(SAMPLE_OUTPUTS,"images_rezised")
os.makedirs(image_dir_final_exp,exist_ok=True)


files_names = os.listdir(image_dir_lol)
filepaths=[]
for file_name in files_names:
    size = len(file_name)
    if (file_name[size-3:size])=="jpg" or (file_name[size-3:size])=="png" or (file_name[size-3:size])=="jpeg":
        path = os.path.join(image_dir_lol,file_name)
        filepaths.append(path)
print(filepaths)

for path in filepaths:
    im = Image.open(path)
    print("{}".format(im.format))
    print("size: {}".format(im.size))
    print("image mode: {}".format(im.mode))

mientras = []
for image in filepaths:
    img = Image.open(image)
    mientras.append(img)

finales = []
for image in mientras:
    image = image.resize((900,900))
    image.show()
    finales.append(image)

for (i,new) in enumerate(finales):
    new.save('{}{}{}'.format(image_dir_final_exp+"/img",i+1,'.jpg'))
