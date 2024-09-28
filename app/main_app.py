"""_summary_
Desafio 02 Prog I UTN APP
"""
from UTN_Heroes_Dataset.utn_funciones import (
    clear_console, play_sound
)
from funciones_utn import (
    mostrar_menu,

)
from validaciones import (
    validar_opcion
)
from funciones_utn import (
    mostrar_todos
)


def desafio2(matriz_heroes):
    """_summary_
    Funcion Bucle Principla App
    """

    while True:
        mostrar_menu()
        opcion = validar_opcion(1, 13)
        play_sound()
        match opcion:
            case 1:
                mostrar_todos(matriz_heroes)
                # mostrar_cantidad_de_heroes_fem(matriz_heroes)
            case 2:
                # mostrar_cantidad_de_heroes_masc(matriz_heroes)
                pass
            case 3:
                # mostrar_heroes_poder_mayor_75(matriz_heroes)
                pass
            case 4:
                # mostrar_heroes_altura_mayor_160(matriz_heroes)
                pass
            case 5:
                # filtrar_heroes_masc_poder_menor_60(matriz_heroes)
                pass
            case 6:
                # fitrar_heroes_no_binarios_poder_10_50(matriz_heroes)
                pass
            case 7:
                # determinar_poder_minimo_mostrar_heroes(matriz_heroes)
                pass
            case 8:
                # determinar_altura_maxima_mostrar_heroes(matriz_heroes)
                pass
            case 9:
                pass
            case 10:
                # ordenar_heroes_alfabeticamente_ascendente(matriz_heroes)
                pass
            case 11:
                # ordenar_heroes_alfabeticamente_descendente(matriz_heroes)
                pass
            case 12:
                # mostrar_heroes_mas_fuertes(matriz_heroes)
                pass
            case 13:
                print("Saliendo...")
                break
            case _:
                print('Opcion no valida')

        clear_console()
