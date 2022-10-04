from importlib.metadata import files
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL  import Image
import os

image_dir = os.path.join(SAMPLE_INPUTS,"images")
os.makedirs(image_dir,exist_ok=True)
image_dir_lol = os.path.join(SAMPLE_INPUTS,"images_buenas_experimento")
os.makedirs(image_dir_lol,exist_ok=True)


name="primer_intento.mp4"
output_video = os.path.join(SAMPLE_OUTPUTS,name)

files_names = os.listdir(image_dir_lol)
filepaths=[]
for file_name in files_names:
    path = os.path.join(image_dir_lol,file_name)
    filepaths.append(path)
print(filepaths)


clip = ImageSequenceClip(filepaths,fps=1)
clip.write_videofile(output_video)