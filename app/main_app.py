from funciones_utn import (
    mostrar_menu,
    play_sound,
    limpiar_pantalla

)
from validaciones import (
    validar_opcion
)
from funciones_utn import (
    utn_mostrar_nombres_heroes,
    utn_mostrar_identidades_heroes,
    utn_mostrar_heroe_mayor_altura,
    utn_filtrar_heroes_genero,
    utn_mostrar_heroes_poder_superior_promedio,
    utn_mostrar_heroes_poder_ascendente,
    utn_mostrar_heroes_altura_descendente,
    utn_mostrar_heroes_poder_usuario
)

def utn_heroes_app(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()
        match opcion:
            case 1:
                utn_mostrar_nombres_heroes(lista_nombres)
            case 2:
                utn_mostrar_identidades_heroes(lista_identidades) 
            case 3:
                utn_mostrar_heroe_mayor_altura(lista_alturas, lista_nombres)
            case 4:
                pass
            case 5:
                utn_filtrar_heroes_genero(lista_generos, lista_nombres)
            case 6:
                utn_filtrar_heroes_genero(lista_generos, lista_nombres, "Masculino")
            case 7:
                utn_filtrar_heroes_genero(lista_generos, lista_nombres, 'No-Binario')
            case 8:
                utn_mostrar_heroes_poder_superior_promedio(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
            case 9:
                pass
            case 10:
                utn_mostrar_heroes_poder_ascendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
            case 11:
               utn_mostrar_heroes_altura_descendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
            case 12:
                utn_mostrar_heroes_poder_usuario(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
            case 13:
                print("Saliendo...")
                break
            case _:
                print('Opcion no valida')

        limpiar_pantalla()
