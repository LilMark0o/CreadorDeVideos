import code
from distutils.dir_util import remove_tree
from email.mime import audio
from tabnanny import filename_only
from unicodedata import name
from moviepy.editor import *
from fileinput import filename
from importlib.metadata import files
from conf import SAMPLE_OUTPUTS, SAMPLE_INPUTS
from random import random
import download_music as help
import os
from shutil import rmtree, Error


de_donde = os.path.join(SAMPLE_OUTPUTS,"final_images")
a_donde= os.path.join(SAMPLE_OUTPUTS,"videos_brutos")
os.makedirs(a_donde,exist_ok=True)


def create_video (typevideo, num=3):
    data_audio = help.download_audio(typevideo)
    print(" *--- YA CREAMOS EL VIDEITO DEL AUDIO ---* ")
    cant_images = len(os.listdir(de_donde))
    if num>cant_images:
        return print("No puedes usar más imagenes de las que hay")
    names = []
    i=0
    while i<num:
        x = round(random()*cant_images)
        name_file = "img"+str(x)+".jpg"
        if not(name_file in names):
            if x!=0:
                names.append(name_file)        
                i+=1
    paths = []

    for f_names in names:
        path = os.path.join(de_donde,f_names)
        paths.append(path)

    print(" *--- YA SELECCIONAMOS LAS IMAGENES PARA EL VIDEO ---* ")
    clips = []
    for_dur = VideoFileClip(data_audio[0])
    n = (for_dur.duration)/num
    for f_path in paths:
        clip = ImageClip(f_path).set_duration(n).fx(vfx.fadein,1).fx(vfx.fadeout,1)
        clips.append(clip)
    
    print(" *--- YA CONCATENAMOS LOS CLIPS ---* ")

    existe = True
    i = 1
    while existe:
        # name = "video_"+str(i)+".mp4"
        final_name = data_audio[3]+"("+str(i)+")"+".mp4"
        if final_name in (os.listdir(a_donde)):
            i+=1
        else:
            existe = False



    # video_clip = concatenate_videoclips(clips,method='compose')
    # where = os.path.join(a_donde,name)
    # video_clip.write_videofile(where,fps=30)

    # videoclip = VideoFileClip(where)
    # audioclip = AudioFileClip(data_audio[0])

    # new_audioclip = CompositeAudioClip([audioclip])
    # videoclip.audio = new_audioclip
    # where_2 = os.path.join(a_donde,final_name)
    # videoclip.write_videofile(where_2)
    

    #INTENTO
    
    video_clip = concatenate_videoclips(clips,method='compose')
    #where = os.path.join(a_donde,name)
    #video_clip.write_videofile(where,fps=30)

    #videoclip = VideoFileClip(where)
    audioclip = AudioFileClip(data_audio[0])

    new_audioclip = CompositeAudioClip([audioclip])
    video_clip.audio = new_audioclip
    where_2 = os.path.join(a_donde,final_name)
    video_clip.write_videofile(where_2, fps=24)

def delete_all():
    
    audio_dir= os.path.join(SAMPLE_INPUTS,"audios_descargas")
    img_1_dir= os.path.join(SAMPLE_OUTPUTS,"final_images")
    img_2_dir= os.path.join(SAMPLE_OUTPUTS,"images_rezised")
    video_dir = a_donde
    folder = [audio_dir,img_1_dir,img_2_dir,video_dir]

    #   ESTO VA A SER UNA PRUEBA
    for dir in folder:
        liston = os.listdir(dir)
        for file in liston:
            borrable = os.path.join(dir,file)
            os.remove(borrable)




    # for file_path in folder:
    #     try:
    #         if os.path.isfile(file_path) or os.path.islink(file_path):
    #             os.unlink(file_path)
    #         elif os.path.isdir(file_path):
    #             rmtree(file_path)
    #     except Exception as e:
    #         print('Failed to delete %s. Reason: %s' % (file_path, e))
