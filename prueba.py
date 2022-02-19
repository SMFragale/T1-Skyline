import lector

def overlap():
    figuras = lector.leer_figuras()
    print(figuras)
    puntos = list(map(lambda e:[(e[0], e[2]), (e[1], 0)], figuras))
    print(puntos)
    contorno(puntos)

def contorno(puntos: list[list[tuple[int]]]):
    if len(puntos) <= 1:
        return

    mitad = len(puntos) // 2
    iz = puntos[:mitad]
    der = puntos[mitad:]
    
    iz = contorno(iz)
    der = contorno(der)

    combinado = combinar(iz, der)
    return combinado
    
def combinar(iz: list[tuple[int]], der: list[tuple[int]]):
    pass

overlap()