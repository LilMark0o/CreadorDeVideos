from pytube import YouTube
import os
import shutil

ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
CARPETA_FINAL = "folder_pruebas"
#con BASE_DIR ya sabemos donde estamos parados

yt = YouTube("https://www.youtube.com/watch?v=VMRbxPWrptw")

#se podía hacer más fácil usando la linea de codigo que sigue :/, soy bobolon
#print(yt.title)

yt = yt.streams.get_highest_resolution()

destiny_path =  os.path.join(BASE_DIR,CARPETA_FINAL)
out_file = yt.download(destiny_path)
lalo = int(input("¿Lo quieres renombrar pa'?: "))
if lalo==1:
    name = input("¿Qué nombre quieres ponerle pa'?: ")
    name = name + ".mp4"
    os.rename(out_file, name)
    actual = os.path.join(BASE_DIR,name)
    final= os.path.join(destiny_path,name)
    shutil.move(actual, final)

#ASÍ SE DESCARGA EN UN DIRECTORIO ESCOGIDO
print("listo pa, descargadisimo")
pregunta = int(input("¿Quieres borrar el video?: "))
if pregunta==1:
    new_destiny =  os.path.join(destiny_path,name)
    os.remove(new_destiny)