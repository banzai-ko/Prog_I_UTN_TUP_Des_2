# pylint: disable=C0200
# pylint: disable=C0123
"""_summary_
Funciones auxiliares y soporte Desafio 03 App
"""
from validaciones import validar_eleccion


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
                elif sub_indice == 3:
                    texto += f'{matriz[sub_indice][indice]:12} | '
                else:
                    texto += f'{matriz[sub_indice][indice]:20} | '
            elif type(matriz[sub_indice][indice]) == int:
                texto += f'{matriz[sub_indice][indice]:03} | '
            elif type(matriz[sub_indice][indice]) == float:
                texto += f'{matriz[sub_indice][indice]:08.2f} | '
        texto = texto[0:-3]

        print(texto)


def mostrar_sublista(indices: list, lista_para_mostrar: list[list]) -> None:
    """
    Muestra elementos filtrados previamente
    Arguments:
        indices -- Elementos a ser mostrados (índices)
        lista_para_mostrar -- Lista total (lista de listas)
    """
    texto = ''
    for i in range(len(indices)):
        for j in range(len(lista_para_mostrar)):
            if type(lista_para_mostrar[j][indices[i]]) == str:
                if len(lista_para_mostrar[j][indices[i]]) > 20:
                    texto_original = lista_para_mostrar[j][indices[i]]
                    texto_saneado = texto_original[0:20]
                    texto += f'{texto_saneado} | '
                else:
                    texto += f'{lista_para_mostrar[j][indices[i]]:20} | '
            elif type(lista_para_mostrar[j][indices[i]]) == int:
                texto += f'{lista_para_mostrar[j][indices[i]]:03} | '
            elif type(lista_para_mostrar[j][indices[i]]) == float:
                texto += f'{lista_para_mostrar[j][indices[i]]:08.2f} | '
        texto = texto[:-3]
        print(texto)
        texto = ''


def buscar(matriz: list[list], tipo: str, valor: str) -> list:
    """
    _summary_
    Funcion de filtrado, busqueda por valor
    Arguments:
        matriz -- Dataset
        tipo -- Lista en la cual buscar: Nombre, Identidad, Apodo, Genero, Poder, Altura
        valor -- el campo a buscar

    Returns:
        _description_ Lista de resultados, como indice de la lista dataset
    """
    res = []
    lista = tipo.lower()
    for i in range(len(matriz[0])):
        if lista == 'nombre':
            if lista == matriz[0][i]:
                res.append(i)
        elif lista == 'identidad':
            if valor == matriz[1][i]:
                res.append(i)
        elif lista == 'apodo':
            if valor == matriz[2][i]:
                res.append(i)
        elif lista == 'genero':
            if valor == matriz[3][i]:
                res.append(i)
        elif lista == 'poder':
            if valor == str(matriz[4][i]):
                res.append(i)
        elif lista == 'altura':
            if valor == str(matriz[5][i]):
                res.append(i)

    return res


def contar(valor: str, matriz: list) -> int:
    """
    _summary_ Contar elementos en una lista
    Arguments:
        valor -- valor a contar
        matriz -- dataset
    """
    count = 0
    apariciones = []
    for i in range(len(matriz)):
        if valor == matriz[i]:
            count += 1
            apariciones.append(i)
    return count, apariciones


def filtrar(
    matriz_entrada: list[list],
    nombre_lista_a_buscar: str,
    modo: str,
    valor_a: str,
    valor_b: str = None
) -> list:
    """
    _summary_
    Filtrar elementos en una lista
    Según el modo, devuelve una lista con los indices
    Menor: devuelve los elementos menores al valor
    Mayor: devuelve los elementos superiores al valor
    Rango: devuelve los elementos dentro del rango
    Arguments:
        matriz -- _description_ Dataset
        lim_inferior -- _description_ Valor minimo del rango o menor
        lim_superior -- _description_ Valor maximo del rango o mayor
        modo -- _description_ Opción de funcionamiento

    Returns:
        _description_ Lista de indices
    """

    nombre_lista = nombre_lista_a_buscar.lower()

    if nombre_lista == 'poder':
        lista = matriz_entrada[4]
    elif nombre_lista == 'altura':
        lista = matriz_entrada[5]

    res = []

    valor_a = int(valor_a)
    if valor_b is not None:
        valor_b = int(valor_b)
    for i in range(len(lista)):
        elemento = int(lista[i])

        if modo == 'menor' and elemento < valor_a:
            res.append(i)
        elif modo == 'mayor' and elemento > valor_a:
            res.append(i)
        elif modo == 'rango' and valor_a <= elemento <= valor_b:
            res.append(i)

    return res


def ordenar_heroes(matriz: list[list], modo: str, lista: list) -> list[list]:
    """
    _summary_
    Ordenar los elementos alfabeticamente
    Arguments:
        matriz -- Dataset
        modo -- 'ASC' / 'DES', Ascendente o Descendente 
        lista -- la lista por la cual ordenar

    Returns:
        _description_
    """

    lista_nombres, lista_identidades, lista_apodos, \
        lista_generos, lista_alturas, lista_poderes,  = matriz
   # Selection Sort
    for i in range(len(lista) - 1):
        indice_minimo = i
        for j in range(i + 1, len(lista)):
            if (modo == 'ASC' and lista[j] < lista[indice_minimo]) or \
                    (modo == 'DES' and lista[j] > lista[indice_minimo]):
                indice_minimo = j

        if indice_minimo != i:
            ordenar_listas(i, indice_minimo, lista_nombres)
            ordenar_listas(i, indice_minimo, lista_identidades)
            ordenar_listas(i, indice_minimo, lista_apodos)
            ordenar_listas(i, indice_minimo, lista_generos)
            ordenar_listas(i, indice_minimo, lista_poderes)
            ordenar_listas(i, indice_minimo, lista_alturas)

    lista_resultado = [
        lista_nombres, lista_identidades, lista_apodos,
        lista_generos, lista_poderes, lista_alturas
    ]
    return lista_resultado


def entrada_orden_usuario() -> str:
    """
    _summary_ Solicitar y validar selección del usuario

    Returns:
        _description_ Devuelve la entrada del usuario, siempre que esté en la lista
    """
    print('Ordenar por: ')
    return validar_eleccion(['ASC', 'DES'])


def interseccion_listas(lista1: list, lista2: list) -> list:
    """
    _summary_
    Devuelve la intersección de dos listas
    Arguments:
        lista1 -- _description_ Lista de indices
        lista2 -- _description_ Lista de indices

    Returns:
        _description_ Lista de indices de elementos comunes
    """
    interseccion = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in interseccion:
            interseccion.append(elemento)
    return interseccion


def ordenar_listas(i: int, j: int, lista_orden: list) -> list:
    """
    _summary_
    Funcion auxiliar para ordenar elementos de una lista
    Arguments:
        i -- _description_ Indice a intercambiar
        j -- _description_  Indice a intercambiar
        lista_orden -- _description_ Lista a definir orden

    Returns:
        _description_
    """
    lista_orden[i], lista_orden[j] =\
        lista_orden[j], lista_orden[i]

    return lista_orden
