from distutils.log import error
from re import X
import sys
import change_useful as one
import create_good_img as two
import create_video as three


def create_a_lot_videos(classics, minecraft, pokemon, lofi, background_sound=0):
    dataCantidad = {"clasicos": {"cuantos_videos": classics, "type_video": 1, "type_images": 1},
                    "minecraft": {"cuantos_videos": minecraft, "type_video": 2, "type_images": 2},
                    "pokemon": {"cuantos_videos": pokemon, "type_video": 3, "type_images": 3},
                    "lofi": {"cuantos_videos": lofi, "type_video": 4, "type_images": 4}
                    }
    j = 1
    errors = 0
    for genero in dataCantidad:
        if dataCantidad[genero]["cuantos_videos"] != 0:
            i = 0
            while i < dataCantidad[genero]["cuantos_videos"]:
                try:
                    print("*"*10 + " Vamos a hacer el videito número: " +
                          str(j)+" "+"*"*10)
                    three.delete_almost_all()
                    one.cambiar_imagenes(dataCantidad[genero]["type_images"])
                    one.create_background(dataCantidad[genero]["type_images"])
                    two.create_img_final()
                    three.create_video(
                        dataCantidad[genero]["type_video"], 3, background_sound)
                    print("*"*10 + " Acabamos con el " +
                          str(j)+" videito "+"*"*10)
                    j += 1
                    i += 1
                except Exception as e:
                    print("Volvamos a intentar :D")
                    errors += 1
                    print("este fue el error N°: "+str(errors))
                    continue
                    # print("Que poronga paso")
                    # print(e)
    print("Hicimos: "+str(j-1)+" videos\nY tuvimos: "+str(errors)+" errores, god")
