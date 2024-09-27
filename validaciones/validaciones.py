
def validar_opcion(num_min: int, num_max: int):
    opcion = input(f'Elija una opcion entre {num_min} y {num_max}: ')

    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)

    return (int(opcion))

def validar_eleccion(posibles: list[str]):
    seleccion_usuario = input(f'Ingrese opciones')
    if seleccion_usuario not in posibles:
        seleccion_usuario = input('Ingrese ASC o DES: ')
        
    return (seleccion_usuario)