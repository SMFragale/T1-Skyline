def leer_figuras():
    entrada = input("Ingrese el nombre del archivo de entrada: ")
    file = open(entrada)

    lineas = file.readlines()

    figuras: list[list[int]] = []
    for linea in lineas:
        linea = linea.replace("\n", "")
        figuras.append(list(map(int, linea.split(","))))
    return figuras

