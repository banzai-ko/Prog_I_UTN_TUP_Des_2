from funciones_utn.auxiliares import (
    mostrar_sublista,
    filtrar,
    calcular_promedio,
    obtener_mayor,
    ordenar_ascendente_poder,
    ordenar_descendente_altura,
    ordenar_poder_usuario
)


def mostrar_todo(matriz: list[list]) -> None:
    """_summary_
    Mostrar toda la informacion de los heroes
    """
    columnas = len(matriz[0])
    filas = len(matriz)

    for indice in range(columnas):
        texto = ''
        for sub_indice in range(filas):
            if type(matriz[sub_indice][indice]) == str:
                if len(matriz[sub_indice][indice]) > 20:
                    texto_original = matriz[sub_indice][indice]
                    texto_saneado = texto_original[0:20]
                    texto += f'{texto_saneado} | '
                else:
                    texto += f'{matriz[sub_indice][indice]:20} | '
            elif type(matriz[sub_indice][indice]) == int:
                texto += f'{matriz[sub_indice][indice]:03} | '
            elif type(matriz[sub_indice][indice]) == float:
                texto += f'{matriz[sub_indice][indice]:08.2f} | '
        texto = texto[0:-3]

        print(texto)


def mostrar_cantidad_de_heroes_fem(matriz: list[list]) -> None:
    mostrar_sublista(filtrar(matriz, 'genero', 'Femenino'), matriz)

def mostrar_cantidad_de_heroes_masc(matriz: list[list]) -> None:
    mostrar_sublista(filtrar(matriz, 'genero', 'Masculino'), matriz)
# ____________
#     utn_filtrar_heroes_genero, utn_mostrar_heroe_mayor_altura,
#     utn_mostrar_heroes_mas_fuertes, utn_mostrar_identidades_heroes,
#     utn_mostrar_nombres_heroes, utn_mostrar_heroes_poder_superior_promedio,
#     utn_mostrar_heroes_mas_debiles


def utn_filtrar_heroes_genero(lista_generos: list, lista_heroes: list, genero='Femenino') -> None:
    for i in range(len(lista_generos)):
        if lista_generos[i] == genero:
            print(lista_heroes[i])


def utn_mostrar_heroe_mayor_altura(lista: list, lista_nombres_heroes: list) -> None:
    pos = obtener_mayor(lista)
    print(f'El heroe con mayor altura es: {
          lista_nombres_heroes[pos]}, con {lista[pos]}cm de altura')



def utn_mostrar_heroes_poder_superior_promedio(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    promedio = calcular_promedio(lista_poderes)
    for i in range(len(lista_poderes)):
        if lista_poderes[i] > promedio:
            print(mostrar_super_heroes(i, lista_nombres, lista_identidades,
                  lista_alturas, lista_poderes, lista_generos))


def utn_mostrar_heroes_mas_debiles(lista: list[list]):
    pass


def utn_mostrar_heroes_mas_fuertes():
    pass


def utn_mostrar_heroes_poder_ascendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    lista_ordenada = ordenar_ascendente_poder(
        lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos)
    mostrar_todos(lista_ordenada)


def utn_mostrar_heroes_altura_descendente(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    lista_mas_grandes = [[], [], [], [], []]
    lista_mas_chicos = [[], [], [], [], []]
    lista_ordenada = ordenar_descendente_altura(
        [lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos], lista_mas_grandes, lista_mas_chicos)
    mostrar_todos(lista_ordenada)


def utn_mostrar_heroes_poder_usuario(lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos):
    seleccion_usuario = input('Ingrese ASC o DES: ')
    while seleccion_usuario != 'ASC' and seleccion_usuario != 'DES':
        # mejorar en funcion de validacion
        seleccion_usuario = input('Ingrese ASC o DES: ')

    lista_ordenada = ordenar_poder_usuario(
        lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos, seleccion_usuario
    )
    mostrar_todos(lista_ordenada)
    pass
