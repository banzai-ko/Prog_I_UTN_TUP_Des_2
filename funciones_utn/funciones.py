"""
_summary_ Moudulo de funciones UTN Industries
    """

from funciones_utn.auxiliares import (
    mostrar_todo,
    filtrar,
    ordenar_heroes_alfa,
    calcular_promedio,
    obtener_mayor,
    ordenar_ascendente_poder,
    ordenar_descendente_altura,
    ordenar_poder_usuario,
)


def mostrar_cantidad_de_heroes_fem(matriz: list[list]) -> None:
    """
    _summary_
    Muestra la cantidad de heroes femeninos
    Arguments:
        matriz -- _description_ Dataset
    """
    lista_femeninos = filtrar(matriz, 'genero', 'Femenino')
    msg = f'La cantidad de heroes femeninos es: {len(lista_femeninos)}'
    print(msg)
    # mostrar_sublista(lista_femeninos, matriz)


def mostrar_cantidad_de_heroes_masc(matriz: list[list]) -> None:
    """
    _summary_
    Muestra la cantidad de heroes masculinos
    Arguments:
        matriz -- _description_ Dataset
    """
    lista_masculinos = filtrar(matriz, 'genero', 'Masculino')
    msg = f'La cantidad de heroes masculinos es: {len(lista_masculinos)}'
    print(msg)
    # mostrar_sublista(lista_masculinos, matriz)


def ordenar_heroes_alfabeticamente_ascendente(matriz):
    """
    _summary_
    Muestra el dataset ordenado alfabeticamente por nombre, 
    ascendente
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Ordenados por nombre: ')
    mostrar_todo(ordenar_heroes_alfa(matriz, 'ASC', matriz[0]))


def ordenar_heroes_alfabeticamente_descendente(matriz):
    """
    _summary_
    Muestra el dataset ordenado alfabeticamente por apode, 
    descendente
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Ordenados por apodo: ')
    mostrar_todo(ordenar_heroes_alfa(matriz, 'ASC', matriz[2]))

# --------------
# Desafio 1 - TO DO: CLEAN


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
