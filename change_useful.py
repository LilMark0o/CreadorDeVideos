import enum
from fileinput import filename
from importlib.metadata import files
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from PIL  import Image
import os

standard_measures= (1920,1080)
image_dir_principal = os.path.join(SAMPLE_INPUTS,"images")
image_dir_final_exp = os.path.join(SAMPLE_OUTPUTS,"images_rezised")


def cambiar_imagenes(img_type_num:int):
    os.makedirs(image_dir_principal,exist_ok=True)
    os.makedirs(image_dir_final_exp,exist_ok=True)

    if img_type_num==1:
        image_dir = os.path.join(image_dir_principal,"classics")
    elif img_type_num==2:
        image_dir = os.path.join(image_dir_principal,"minecraft")
    elif img_type_num==3:
        image_dir = os.path.join(image_dir_principal,"pokemon")
    elif img_type_num==4:
        image_dir = os.path.join(image_dir_principal,"lofi")
    else:
        image_dir = os.path.join(image_dir_principal,"classics")
        print("I've to use the classics, because you used a invalid number :/")
    os.makedirs(image_dir,exist_ok=True)

    files_names = os.listdir(image_dir) #da los nombres de los archivos en x directorio

    #crear una lista con los paths de las imagenes dependiendo si son imágenes o no 
    filepaths=[]
    for file_name in files_names:
        size = len(file_name)
        if (not(file_name=="background.jpg"))and((file_name[size-3:size])=="jpg" or (file_name[size-3:size])=="png" or (file_name[size-3:size])=="jpeg"):
            path = os.path.join(image_dir,file_name)
            filepaths.append(path)

    #dar la información de cada imágen, --prescindible por el momento--
    # for path in filepaths:
    #     im = Image.open(path)
    #     print("{}".format(im.format))
    #     print("size in x: {}".format(im.size[0]))
    #     print("size in y: {}".format(im.size[1]))
    #     print("image mode: {}".format(im.mode))

    #nueva lista para abrir los path en archivos de imagenes
    mientras = []
    for image in filepaths:
        img = Image.open(image)
        mientras.append(img)

    #crea una lista con las imágenes con el nuevo tamaño 
    # para que quepan en x o y, dependiendo la imágen

    finales = []

    #el standard puede variar, depende el fondo a usar

    for image in mientras:
        if (standard_measures[0]/image.size[0])>(standard_measures[1]/image.size[1]):
            scale_img = standard_measures[1]/image.size[1]
            x = int(image.size[0]*scale_img)
            y = int(image.size[1]*scale_img)
            image = image.resize((x,y))
        elif (standard_measures[0]/image.size[0])<(standard_measures[1]/image.size[1]):
            scale_img = standard_measures[0]/image.size[0]
            x = int(image.size[0]*scale_img)
            y = int(image.size[1]*scale_img)
            image = image.resize((x,y))
        if (standard_measures[0]/image.size[0])==(standard_measures[1]/image.size[1]):
            #no cambia nada, da igual si uso x o y
            scale_img = standard_measures[0]/image.size[0]
            x = int(image.size[0]*scale_img)
            y = int(image.size[1]*scale_img)
            image = image.resize((x,y))
        finales.append(image)

    #crea los nuevos archivos de imagenes ordenados por numeros (terminan en JPG y calidad máxima)
    for (i,new) in enumerate(finales):
        new = new.convert('RGB')
        new.save('{}{}{}'.format(image_dir_final_exp+"/img",i+1,'.jpg'),quality=95)

def create_background (img_type_num):
    os.makedirs(image_dir_principal,exist_ok=True)
    os.makedirs(image_dir_final_exp,exist_ok=True)

    if img_type_num==1:
        image_dir = os.path.join(image_dir_principal,"classics")
    elif img_type_num==2:
        image_dir = os.path.join(image_dir_principal,"minecraft")
    elif img_type_num==3:
        image_dir = os.path.join(image_dir_principal,"lofi")
    elif img_type_num==4:
        image_dir = os.path.join(image_dir_principal,"lofi")
    else:
        image_dir = os.path.join(image_dir_principal,"classics")
        print("I've to use the classics, because you used a invalid number :/")
    os.makedirs(image_dir,exist_ok=True)
    fondo_path = os.path.join(image_dir_principal,"background.jpg")
    fondo_img = Image.open(fondo_path)
    fondo_img = fondo_img.resize(standard_measures)
    fondo_img.save('{}'.format(image_dir_final_exp+'/background.jpg'),quality=95)


#LLEVAR A CABO LAS FUNCIONES
#cambiar_imagenes()
#create_background()
