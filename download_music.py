from math import floor
from pytube import YouTube
from conf import SAMPLE_INPUTS
import os
import shutil
from info import *
from random import * 


a_donde= os.path.join(SAMPLE_INPUTS,"audios_descargas")
os.makedirs(a_donde,exist_ok=True)

def download_audio(type_video):
    if type_video==1:
        x = floor(random()*len(Classic_short))
        link = Classic_short[x]
    elif type_video==2:
        x = floor(random()*len(Classic_long))
        link = Classic_long[x]
    x = floor(random()*len(possible_titles))

    if (type_video==1 or type_video==2):
        final_name = possible_titles[x]+" | "+genere_music[0] #type_music[0] es musica clasica
    elif (type_video==3 & type_video==4):
        final_name = possible_titles[x]+" | "+genere_music[1] #type_music[0] es musica clasica
    else:
        final_name = possible_titles[x]
    
    i=0
    while i <3:
        x = floor(random()*len(Emojis))
        final_name+= " "+str(Emojis[x])
        i +=1

    yt = YouTube(link)
    #se podía hacer más fácil usando la linea de codigo que sigue :/, soy bobolon
    name= yt.title+".mp4"

    yt = yt.streams.get_lowest_resolution()
    print(" *--- VAMOS A DESCARGAR EL VIDEITO DEL AUDIO ---* ")
    yt.download(a_donde)
    print(" *--- YA ESTÁ DESCARGADO EL VIDEITO DEL AUDIO ---* ")

    liston = os.listdir(a_donde)
    
    existe = True
    i = 1
    while existe:
        newname = "audio_"+str(i)+".mp4"
        if newname in liston:
            i+=1
        else:
            existe = False

    for y in liston:
        if name[0:3]==y[0:3]:
            x_path = os.path.join(a_donde,y)
            newname_path = os.path.join(a_donde,newname)
            os.rename(x_path, newname_path)
    return (newname_path,newname, a_donde, final_name)

def delete_audio(name):
    new_destiny = os.path.join(a_donde,name)
    os.remove(new_destiny)

# nombre = download_audio()
# delete_audio(nombre)