"""_summary_
    Modulo Mostrar menu de la aplicacion
    """


def mostrar_menu():
    """
    Muestra por pantalla el menu estático
    """
    opciones = \
        """
        1 - Mostrar la cantidad de Heroes Femeninos.
        2 - Mostrar la cantidad de Heroes Masculinos.
        3 - Mostrar a los heroes con mas de 75 de poder.
        4 - Mostrar al/los heroe/s con mas de 160 de altura.
        5 - Filtrar a los heroes Femeninos con mas de 60 de poder.
        6 - Filtrar a los heroes Masculinos con menos de 60 de poder.
        7 - Filtrar a los personajes No-Binarios con poder entre 10 y 50 inclusive.
        8 - Determinar cual es el minimo de poder y mostrar cuantos heroes tienen 
        un poder igual al minimo.
        9 - Determinar cual es el maximo de altura y mostrar cuantos heroes tienen dicha altura.
        10 - Ordenar los heroes Alfabeticamente ASCENDENTE segun su nombre.
        11 - Ordenar los heroes Alfabeticamente DESCENDENTE segun su apodo.
        12 - Ordenar los heroes por Altura y que el usuario decida ASC o DES.
        13 - Salir.
        """
    print(opciones)


if __name__ == "__main__":
    mostrar_menu()
