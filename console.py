from distutils.log import error
from re import X
import sys
import change_useful as one
import create_good_img as two
import create_video as three
import create_lots_videos as four

Siga = True
while Siga:
    print("Bienvenido al creador de videos automático :)")
    print("---------------------x-----------------------")
    print("oprima 1 para escoger el tipo de imagenes que \n" +
          "quiere hacer imágenes compatibles, crear el fondo para \n" +
          "las imágenes y finalmente crear las imágenes finales\n")
    print("oprima 2 para crear el video\n")
    print("oprima 3 para borrar los archivos\n")
    print("oprima 4 para crear muchos videos\n")
    print("oprima cualquier otro número para salir del programa\n")

    r1 = int(input("¿Qué desea hacer?\n"))
    if r1 == 1:
        print(" *--- Distintos tipos de imagenes ---*")
        print("    - 1) Clásicas")
        print("    - 2) Minecraft")
        print("    - 3) Pokemon")
        print("    - 4) Lofi")
        img_type = int(input("¿Qué tipo de video quieres hacer?: "))
        print("\nCambiando imagenes para ser compatibles...")
        one.cambiar_imagenes(img_type)
        print("¡Imagenes cambiadas exitosamente! \n")
        print("Creando fondo para las imágenes...")
        one.create_background(img_type)
        print("Fondo creado exitosamente! \n")
        print("Creando imágenes finales...")
        two.create_img_final()
        print("Imágenes creadas exitosamente!")
    elif r1 == 2:
        print("¡Vamos a crear un videito!")
        cant_img = int(
            input("¿Cuantas imágenes quieres que tenga el video?: "))
        r2 = int(input(
            "¿Quieres que el videito tenga sonido de ambiente?: (Respuesta debe ser 0 o 1) "))
        if r2 != 0:
            print(" *--- Distintos tipos de background sound ---*")
            print("    - 0) Nada, soy aburrido")
            print("    - 1) Lluvia")
            print("    - 2) Fuego/Fogata")
            print("    - 3) Ambos")
            r2 = int(input("Cual opción quieres?: "))

        print(" *--- Distintos tipos de videos ---*")
        print("    - 1) música clásica - largo")
        print("    - 2) música minecraft - largo")
        print("    - 3) música pokemón - largo ")
        print("    - 4) música lo-fi - largo ")
        type_video = int(input("¿Qué tipo de video quieres crear?: "))
        try:
            three.create_video(type_video, cant_img, r2)
        except:
            print("Tuvimos un error, volvamos a intentarlo")
            three.create_video(type_video, cant_img, r2)
    elif r1 == 3:
        print("¡Vamos a borrar los archivos!")
        three.delete_all()
    elif r1 == 4:
        print(" *--- Vamos a hacer muchos videitos :D ---*")
        classics = int(input("¿Cuantos videitos quieres de música clásica?: "))
        minecraft = int(
            input("¿Cuantos videitos quieres de música de Minecraft?: "))
        pokemon = int(
            input("¿Cuantos videitos quieres de música de Pokemón?: "))
        lofi = int(input("¿Cuantos videitos quieres de música lofi?: "))
        r2 = int(input(
            "¿Quieres que el videito tenga sonido de ambiente?: (Respuesta debe ser 0 o 1) "))
        if r2 != 0:
            print(" *--- Distintos tipos de background sound ---*")
            print("    - 0) Nada, soy aburrido")
            print("    - 1) Lluvia")
            print("    - 2) Fuego/Fogata")
            print("    - 3) Ambos")
            r2 = int(input("Cual opción quieres?: "))
        print(" *--- Vamos a hacer " + str(classics +
              minecraft+pokemon+lofi) + " videitos :D ---*")
        four.create_a_lot_videos(classics, minecraft, pokemon, lofi, r2)
    else:
        Siga = False
    print("-"*10+" Acabamos :D "+"-"*10+"\n")
