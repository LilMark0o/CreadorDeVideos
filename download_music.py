from math import floor
from pytube import YouTube
from conf import SAMPLE_INPUTS
import os
import shutil
from info import *
from random import * 


a_donde= os.path.join(SAMPLE_INPUTS,"audios_descargas")
os.makedirs(a_donde,exist_ok=True)

def download_statics_audios():
    dir_static = os.path.join(SAMPLE_INPUTS,"static_audios")
    os.makedirs(dir_static,exist_ok=True)
    if len(os.listdir(dir_static))<3:
        print("no hay na")
        for element in sounds:
            yt = YouTube(element["link"])
            #se podía hacer más fácil usando la linea de codigo que sigue :/, soy bobolon
            name= yt.title+".mp4"

            yt = yt.streams.get_lowest_resolution()
            print(" *--- VAMOS A DESCARGAR EL VIDEITO DEL AUDIO ---* ")
            yt.download(dir_static)
            print(" *--- YA ESTÁ DESCARGADO EL VIDEITO DEL AUDIO ---* ")
            
            for y in os.listdir(dir_static):
                if name[0:3]==y[0:3]:
                    x_path = os.path.join(dir_static,y)
                    new_name = element["name"]+".mp4"
                    newname_path = os.path.join(dir_static,new_name)
                    os.rename(x_path, newname_path)

def download_audio(type_video):
    download_statics_audios()
    if type_video==1:
        x = floor(random()*len(Classic_long))
        link = Classic_long[x]
    elif type_video==2:
        x = floor(random()*len(minecraft_long))
        link = minecraft_long[x]
    elif type_video==3:
        x = floor(random()*len(pokemon_long))
        link = pokemon_long[x]
    elif type_video==4:
        x = floor(random()*len(lofi_long))
        link = lofi_long[x]

    if (type_video==1):
        x = floor(random()*len(possible_titles_classic))
        final_name = possible_titles_classic[x]+" | "+genere_music[0] #type_music[0] es musica clasica
    elif (type_video==2):
        x = floor(random()*len(possible_titles_minecraft))
        final_name = possible_titles_minecraft[x]+" | "+genere_music[1] #type_music[1] es Minecraft
    elif (type_video==3):
        x = floor(random()*len(possible_titles_pokemon))
        final_name = possible_titles_pokemon[x]+" | "+genere_music[2] #type_music[2] es Lofi
    elif (type_video==4):
        x = floor(random()*len(possible_titles_lofi))
        final_name = possible_titles_lofi[x]+" | "+genere_music[3] #type_music[3] es Pokemon
    else:
        final_name = possible_titles_classic[0]
    
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