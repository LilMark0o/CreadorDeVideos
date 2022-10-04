from genericpath import isfile
import os
file_path = "folder_pruebas/hola.txt"
f = open("folder_pruebas/hola.txt","w")
if os.path.isfile(file_path):
    answer=input("lo quieres borrar hermano?\n")
    if int(answer)==1:
        os.remove(file_path)
        print("borrao'")
    else:
        print("q puto")
else:
    print("No encontrao'")