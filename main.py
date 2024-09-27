from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from UTN_Heroes_Dataset.utn_funciones import (
    saludo, clear_console, play_sound
)
lista_nombres_heroes, lista_identidades_heroes, lista_alturas_heroes, lista_poder_heroes, lista_generos_heroes = ['a'], ['a'], ['a'], ['a'], ['a']
from app import utn_heroes_app

if __name__ == "__main__":
    # for fila in matriz_data_heroes:

    #     for columna in fila:
    #         print( 'Data: ', columna )
    columnas = len(matriz_data_heroes[0])
    filas = len(matriz_data_heroes)
    for indice in range(columnas):
        texto = ''
        
        for sub_indice in range(filas):
            if type(matriz_data_heroes[sub_indice][indice]) == str:
                if len(matriz_data_heroes[sub_indice][indice]) > 20:
                    texto_original = matriz_data_heroes[sub_indice][indice]
                    texto_saneado = texto_original[0:20]
                    texto += f'{texto_saneado} | '
                else:
                    texto += f'{matriz_data_heroes[sub_indice][indice]:20} | '
            elif type(matriz_data_heroes[sub_indice][indice]) == int:
                texto += f'{matriz_data_heroes[sub_indice][indice]:03} | '
            elif type(matriz_data_heroes[sub_indice][indice]) == float:
                texto += f'{matriz_data_heroes[sub_indice][indice]:08.2f} | '
        texto = texto[0:-3]
        
        print(texto)
    #   utn_heroes_app(
    #     lista_nombres_heroes,
    #     lista_identidades_heroes,
    #     lista_alturas_heroes,
    #     lista_poder_heroes,
    #     lista_generos_heroes,
    #   )

    #   print(len(matriz_data_heroes))
