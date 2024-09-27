"""_summary_
Funciones auxiliares y soporte Desafio 02 App
"""
def mostrar_lista(lista: list) -> None:
    for i in range(len(lista)):
        print(lista[i])


def calcular_promedio(lista: list) -> float:
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += int(lista[i])
    promedio = sumatoria / len(lista)
    return promedio


def mostrar_super_heroes(indice: int, lista_nombres: list, lista_identidades: list, lista_alturas: list, lista_poderes: list, lista_generos: list) -> str:
    mensaje = f'Nombre: {lista_nombres[indice]:<16} | Poder: {lista_poderes[indice]:<12} ' \
              f'| Altura: {lista_alturas[indice]:<12} | Genero: {lista_generos[indice]:<12} ' \
              f'| Identidad: {lista_identidades[indice]:<22}'
    return mensaje


def obtener_mayor(lista: list, indice=None) -> int:
    if indice is None:
        indice = len(lista) - 1

    if indice == 0:  # Caso Base
        return 0

    indice_mayor = obtener_mayor(lista, indice - 1)  # Caso recursivo

    # Comparar el valor en el índice actual con el valor almacenado
    if lista[indice] > lista[indice_mayor]:
        return indice
    else:
        return indice_mayor
    lista_nombres, lista_identidades, lista_alturas, lista_poderes, lista_generos


def ordenar_ascendente_poder(lista_nombres: list, lista_identidades: list, lista_alturas: list, lista_poderes: list, lista_generos: list) -> list[list]:
    # BS
    for indice in range(len(lista_poderes) - 1):
        for sub_indice in range(indice + 1, len(lista_poderes)):
            if lista_poderes[indice] > lista_poderes[sub_indice]:
                ordenar_listas(indice, sub_indice, lista_poderes)
                ordenar_listas(indice, sub_indice, lista_nombres)
                ordenar_listas(indice, sub_indice, lista_identidades)
                ordenar_listas(indice, sub_indice, lista_alturas)
                ordenar_listas(indice, sub_indice, lista_generos)

    lista_resultado = [lista_nombres, lista_identidades,
                       lista_alturas, lista_poderes, lista_generos]

    return lista_resultado


def ordenar_descendente_altura(lista_resultado: list[list], lista_mas_grandes: list[list], lista_mas_chicos: list[list]) -> list[list]:
    """
    Ordena los elementos de la matriz usando QS
    Argumentos: Recibe una matriz y dos parametros auxiliares para la recursividad( ver/preguntar posible mejora)
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

    sorted_grandes = ordenar_descendente_altura(lista_mas_grandes, [[], [], [], [], []], [[], [], [], [], []])
    sorted_chicos = ordenar_descendente_altura(lista_mas_chicos, [[], [], [], [], []], [[], [], [], [], []])

    pivot = [lista_resultado[j][pivot_index] for j in range(5)]

    fix_sorted = [
        sorted_grandes[0] + [pivot[0]] + sorted_chicos[0],  # Nombres
        sorted_grandes[1] + [pivot[1]] + sorted_chicos[1],  # Identidad
        sorted_grandes[2] + [pivot[2]] + sorted_chicos[2],  # Altura
        sorted_grandes[3] + [pivot[3]] + sorted_chicos[3],  # Poder
        sorted_grandes[4] + [pivot[4]] + sorted_chicos[4],  # Genero
    ]

    return fix_sorted

def ordenar_listas(indice: int, sub_indice: int, lista_orden: list) -> list:
    lista_orden[indice], lista_orden[sub_indice] =\
        lista_orden[sub_indice], lista_orden[indice]

    return lista_orden


def ordenar_poder_usuario(lista_nombres: list, lista_identidades: list, lista_alturas: list, lista_poderes: list, lista_generos: list, modo: str) -> list[list]:
    # Selection Sort
    for indice in range(len(lista_poderes) - 1):
        indice_minimo = indice
        for sub_indice in range(indice + 1, len(lista_poderes)):
            if (modo == 'ASC' and lista_poderes[sub_indice] < lista_poderes[indice_minimo]) or \
               (modo == 'DES' and lista_poderes[sub_indice] > lista_poderes[indice_minimo]):
                indice_minimo = sub_indice

        if indice_minimo != indice:
            ordenar_listas(indice, indice_minimo, lista_poderes)
            ordenar_listas(indice, indice_minimo, lista_nombres)
            ordenar_listas(indice, indice_minimo, lista_identidades)
            ordenar_listas(indice, indice_minimo, lista_alturas)
            ordenar_listas(indice, indice_minimo, lista_generos)

    lista_resultado = [lista_nombres, lista_identidades,
                       lista_alturas, lista_poderes, lista_generos]
    
    return lista_resultado

def mostrar_todos(lista: list[list]):
    for i in range(len(lista[0])):
        print(mostrar_super_heroes(
            i, lista[0], lista[1], lista[2], lista[3], lista[4]))
