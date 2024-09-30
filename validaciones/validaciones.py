
"""_summary_
    Modulo de validaciones
"""


def validar_opcion(num_min: int, num_max: int):
    """_summary_
Funcion para validar entrada del usuario
Debe ser numerica y este entre el minimo y el maximo
Argumentos:
num_min: Entero minimo
num_max: Entero maximo

Retorna: un entero con la entrada del usuario, 
"""
    opcion = input(f'Elija una opcion entre {num_min} y {num_max}: ')

    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)

    return int(opcion)


def validar_eleccion(posibles: list[str]) -> str:
    """_summary_
Funcion para validar entrada del usuario
Recibe una lista de posibles elecciones
Retorna: un string con la entrada del usuario
"""
    seleccion_usuario = input(f'Ingrese opcion: {posibles} ').upper()
    if seleccion_usuario not in posibles:
        print("Opción no valida, reingrese.")
        return validar_eleccion(posibles)

    return seleccion_usuario
