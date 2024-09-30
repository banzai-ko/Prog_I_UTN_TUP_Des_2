"""
_summary_ Moudulo de funciones UTN Industries
    """

from funciones_utn.auxiliares import (
    mostrar_todo,
    mostrar_sublista,
    buscar,
    contar,
    filtrar,
    ordenar_heroes,
    entrada_orden_usuario,
    interseccion_listas
)


def mostrar_cantidad_de_heroes_fem(matriz: list[list]) -> None:
    """
    _summary_
    Muestra la cantidad de heroes femeninos
    Arguments:
        matriz -- _description_ Dataset
    """
    lista_femeninos = buscar(matriz, 'genero', 'Femenino')
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
    lista_masculinos = buscar(matriz, 'genero', 'Masculino')
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
    mostrar_todo(ordenar_heroes(matriz, 'ASC', matriz[0]))


def ordenar_heroes_alfabeticamente_descendente(matriz):
    """
    _summary_
    Muestra el dataset ordenado alfabeticamente por apode, 
    descendente
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Ordenados por apodo: ')
    mostrar_todo(ordenar_heroes(matriz, 'ASC', matriz[2]))


def ordenar_heroes_altura_usuario(matriz):
    """
    _summary_
    Ordena el dataset por altura, usando la selección del usuario
    Arguments:
        matriz_heroes -- _description_ Dataset
    """
    entrada = entrada_orden_usuario()
    print(entrada)
    mostrar_todo(ordenar_heroes(matriz, entrada, matriz[5]))


def determinar_altura_maxima_mostrar_heroes(matriz):
    """
    _summary_
    Determina la altura maxima del dataset cuenta la cantidad de 
    apariciones de la altura maxima y muestra los heroes con 
    dicha altura
    Arguments:
        matriz -- _description_ Dataset
    """
    lista_ordenada_altura = ordenar_heroes(matriz, 'DES', matriz[5])
    print(f'La altura maxima es:  {lista_ordenada_altura[4][0]}')
    cantidad, lista = contar(lista_ordenada_altura[4][0], matriz[5])
    print(f'La cantidad de heroes con esa altura es: {cantidad}')
    mostrar_sublista(lista, lista_ordenada_altura)


def determinar_poder_minimo_mostrar_cant_heroes(matriz):
    """
    _summary_
    Determina el poder minimo del dataset cuenta la cantidad de 
    apariciones del poder minimo y muestra los heroes con 
    dicho poder
    Arguments:
        matriz -- _description_ Dataset
    """
    lista_ordenada_poder = ordenar_heroes(matriz, 'ASC', matriz[4])
    print(f'El poder minimo es:  {lista_ordenada_poder[5][0]}')
    cantidad, lista = contar(lista_ordenada_poder[5][0], matriz[4])
    print(f'La cantidad de heroes con ese poder es: {cantidad}')
    mostrar_sublista(lista, lista_ordenada_poder)


def fitrar_heroes_no_binarios_poder_10_50(matriz):
    """
    _summary_
    Filtra el dataset para mostrar solo los heroes no binarios
    con poder entre 10 y 50 inclusive
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Lista de heroes no binarios con poder entre 10 y 50:')
    lista_no_binarios = buscar(matriz, 'genero', 'No-Binario')
    poder_entre_10_50 = filtrar(matriz, 'poder', 'rango', 10, 50)
    mostrar_sublista(interseccion_listas(
        poder_entre_10_50, lista_no_binarios), matriz)


def buscar_heroes_masc_poder_menor_60(matriz):
    """
    _summary_
    Filtra el dataset para mostrar solo los heroes masculinos
    con poder menor a 60
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Lista de heroes con poder menor a 60:')
    poder_menor_60 = filtrar(matriz, 'poder', 'menor', 60)
    lista_masc = buscar(matriz, 'genero', 'Masculino')
    mostrar_sublista(interseccion_listas(poder_menor_60, lista_masc), matriz)


def buscar_heroes_fem_poder_mayor_60(matriz):
    """
    _summary_
    Filtra el dataset para mostrar solo los heroes femeninos
    con poder mayor a 60
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Lista de heroinas con poder mayor a 60:')
    poder_mayor_60 = filtrar(matriz, 'poder', 'mayor', 60)
    lista_fem = buscar(matriz, 'genero', 'Femenino')
    mostrar_sublista(interseccion_listas(poder_mayor_60, lista_fem), matriz)


def mostrar_heroes_altura_mayor_160(matriz):
    """
    _summary_
    Filtra el dataset para mostrar solo los heroes con altura
    mayor a 160
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Lista de heroes con altura mayor a 160:')
    altura_mayor_160 = filtrar(matriz, 'altura', 'mayor', 160)
    mostrar_sublista(altura_mayor_160, matriz)


def mostrar_heroes_poder_mayor_75(matriz_heroes):
    """
    _summary_
    Filtra el dataset para mostrar solo los heroes con poder
    mayor a 75
    Arguments:
        matriz -- _description_ Dataset
    """
    print('Lista de heroes con poder mayor a 75:')
    poder_mayor_75 = filtrar(matriz_heroes, 'poder', 'mayor', 75)
    mostrar_sublista(poder_mayor_75, matriz_heroes)
