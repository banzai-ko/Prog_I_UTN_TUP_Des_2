# pylint: disable=C0200
# pylint: disable=C0123

"""_summary_
Funciones auxiliares y soporte Desafio 03 App
"""

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


def filtrar(matriz: list[list], tipo: str, valor: str) -> list:
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

def ordenar_heroes_alfa(matriz: list[list], modo: str, lista: list) -> list[list]:
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


# -------------------------------------------
# Desafio 1. TO DO: CLEAN

def calcular_promedio(lista: list) -> float:
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += int(lista[i])
    promedio = sumatoria / len(lista)
    return promedio


def obtener_mayor(lista: list, i=None) -> int:
    if i is None:
        i = len(lista) - 1

    if i == 0:  # Caso Base
        return 0

    indice_mayor = obtener_mayor(lista, i - 1)  # Caso recursivo

    # Comparar el valor en el índice actual con el valor almacenado
    if lista[i] > lista[indice_mayor]:
        return i
    else:
        return indice_mayor
    lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos


def ordenar_ascendente_poder(lista_nombres: list, lista_identidades: list, lista_alturas: list, lista_poderes: list, lista_generos: list) -> list[list]:
    # BS
    for i in range(len(lista_poderes) - 1):
        for j in range(i + 1, len(lista_poderes)):
            if lista_poderes[i] > lista_poderes[j]:
                ordenar_listas(i, j, lista_poderes)
                ordenar_listas(i, j, lista_nombres)
                ordenar_listas(i, j, lista_identidades)
                ordenar_listas(i, j, lista_alturas)
                ordenar_listas(i, j, lista_generos)

    lista_resultado = [lista_nombres, lista_identidades,
                       lista_alturas, lista_poderes, lista_generos]

    return lista_resultado


def ordenar_descendente_altura(lista_resultado: list[list], lista_mas_grandes: list[list], lista_mas_chicos: list[list]) -> list[list]:
    """
    Ordena los elementos de la lista_para_mostrar usando QS
    Argumentos: Recibe una lista_para_mostrar y dos parametros auxiliares para la recursividad( ver/preguntar posible mejora)
    """
    if len(lista_resultado[2]) < 2:
        return lista_resultado

    pivot_index = len(lista_resultado[2]) - 1
    pivot_altura = lista_resultado[2][pivot_index]

    for i in range(pivot_index):
        altura = lista_resultado[2][i]
        if altura > pivot_altura:
            for j in range(5):
                lista_mas_grandes[j].append(lista_resultado[j][i])
        else:
            for j in range(5):
                lista_mas_chicos[j].append(lista_resultado[j][i])

    sorted_grandes = ordenar_descendente_altura(
        lista_mas_grandes, [[], [], [], [], []], [[], [], [], [], []])
    sorted_chicos = ordenar_descendente_altura(
        lista_mas_chicos, [[], [], [], [], []], [[], [], [], [], []])

    pivot = [lista_resultado[j][pivot_index] for j in range(5)]

    fix_sorted = [
        sorted_grandes[0] + [pivot[0]] + sorted_chicos[0],  # Nombres
        sorted_grandes[1] + [pivot[1]] + sorted_chicos[1],  # Identidad
        sorted_grandes[2] + [pivot[2]] + sorted_chicos[2],  # Altura
        sorted_grandes[3] + [pivot[3]] + sorted_chicos[3],  # Poder
        sorted_grandes[4] + [pivot[4]] + sorted_chicos[4],  # Genero
    ]

    return fix_sorted


def ordenar_listas(i: int, j: int, lista_orden: list) -> list:
    lista_orden[i], lista_orden[j] =\
        lista_orden[j], lista_orden[i]

    return lista_orden


def ordenar_poder_usuario(matriz: list[list], modo: str) -> list[list]:
    lista_nombres, lista_identidades, lista_apodos, \
        lista_generos, lista_alturas, lista_poderes,  = matriz
    # Selection Sort
    for i in range(len(lista_poderes) - 1):
        indice_minimo = i
        for j in range(i + 1, len(lista_poderes)):
            if (modo == 'ASC' and lista_poderes[j] < lista_poderes[indice_minimo]) or \
               (modo == 'DES' and lista_poderes[j] > lista_poderes[indice_minimo]):
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



