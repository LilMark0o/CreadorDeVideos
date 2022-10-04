import change_useful as one
import create_good_img as two
import create_video as three

Siga = True
while Siga:
    print("Bienvenido al creador de videos automático :)")
    print("---------------------x-----------------------")
    print("oprima 1 para hacer imágenes compatibles")
    print("oprima 2 para crear el fondo para las imágenes")
    print("oprima 3 para crear las imagenes finales")
    print("oprima 4 para hacer las opciones 1, 2 y 3 a la vez")
    print("oprima 5 para crear el video")
    print("oprima 6 para borrar los archivos")

    r1 = int(input("¿Qué desea hacer?\n"))
    if r1==1:
        print("\nCambiando imagenes para ser compatibles...")
        one.cambiar_imagenes()
        print("¡Imagenes cambiadas exitosamente! \n")
    elif r1==2:
        print("Creando fondo para las imágenes...")
        one.create_background()
        print("Fondo creado exitosamente! \n")
    elif r1==3:
        print("Creando imágenes finales...")
        two.create_img_final()
        print("Imágenes creadas exitosamente! \n")
    elif r1==4:
        print("\nCambiando imagenes para ser compatibles...")
        one.cambiar_imagenes()
        print("¡Imagenes cambiadas exitosamente! \n")
        print("Creando fondo para las imágenes...")
        one.create_background()
        print("Fondo creado exitosamente! \n")
        print("Creando imágenes finales...")
        two.create_img_final()
        print("Imágenes creadas exitosamente!")
    elif r1==5:
        print("¡Vamos a crear un videito!")
        cant_img = int(input("¿Cuantas imágenes quieres que tenga el video?: "))
        print(" *--- Distintos tipos de videos ---*")
        print("    - 1) música clásica - corto")
        print("    - 2) música clásica - largo")
        print("    - 3) música lo-fi - corto  *** En Construcción ***")
        print("    - 4) música lo-fi - largo *** En Construcción ***")
        print("    - 5) música minecraft - corto  *** En Construcción ***")
        print("    - 6) música minecraft - largo *** En Construcción ***")
        type_video = int(input("¿Qué tipo de video quieres crear?: "))
        three.create_video(type_video,cant_img)
    elif r1==6: 
        print("¡Vamos a borrar los archivos!")
        three.delete_all()
    else:
        Siga = False
    print("-"*10+" Acabamos :D "+"-"*10+"\n")