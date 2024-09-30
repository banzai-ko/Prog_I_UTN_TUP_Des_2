"""_summary_
Desafio 02 Prog I
Grupo 03
 UTN APP
"""
from UTN_Heroes_Dataset.utn_funciones import (
    clear_console, play_sound
)
from validaciones import (
    validar_opcion
)
from funciones_utn import (
    mostrar_menu,
    mostrar_cantidad_de_heroes_fem,
    mostrar_cantidad_de_heroes_masc,
    ordenar_heroes_alfabeticamente_ascendente,
    ordenar_heroes_alfabeticamente_descendente,
    ordenar_heroes_altura_usuario,
    determinar_altura_maxima_mostrar_heroes,
    determinar_poder_minimo_mostrar_cant_heroes,
    fitrar_heroes_no_binarios_poder_10_50,
    buscar_heroes_masc_poder_menor_60,
    buscar_heroes_fem_poder_mayor_60,
    mostrar_heroes_altura_mayor_160,
    mostrar_heroes_poder_mayor_75

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
                mostrar_cantidad_de_heroes_fem(matriz_heroes)
            case 2:
                mostrar_cantidad_de_heroes_masc(matriz_heroes)
            case 3:
                mostrar_heroes_poder_mayor_75(matriz_heroes)
            case 4:
                mostrar_heroes_altura_mayor_160(matriz_heroes)
            case 5:
                buscar_heroes_fem_poder_mayor_60(matriz_heroes)
            case 6:
                buscar_heroes_masc_poder_menor_60(matriz_heroes)
            case 7:
                fitrar_heroes_no_binarios_poder_10_50(matriz_heroes)
            case 8:
                determinar_poder_minimo_mostrar_cant_heroes(matriz_heroes)
            case 9:
                determinar_altura_maxima_mostrar_heroes(matriz_heroes)
            case 10:
                ordenar_heroes_alfabeticamente_ascendente(matriz_heroes)
            case 11:
                ordenar_heroes_alfabeticamente_descendente(matriz_heroes)
            case 12:
                ordenar_heroes_altura_usuario(matriz_heroes)
            case 13:
                print("Saliendo...")
                break
            case _:
                print('Opcion no valida')

        clear_console()
