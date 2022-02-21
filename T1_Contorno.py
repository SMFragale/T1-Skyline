import lector

class Point:
    def __init__(self, x, y) -> None:
        self.x: int = x
        self.y: int = y
    
    def en_rango(self, figura: list):
        iz = figura[0].x
        der = figura[-1].x
        
        return self.x <= der and self.x >= iz
    
    def compare_get(self, other):
        if self.x < other.x:
            return self
        elif self.x > other.x:
            return other
        else:
            return self if self.y > other.y else other

    def __str__(self) -> str:
        return "({}, {})".format(self.x, self.y)

class Figura:
    def __init__(self, puntos) -> None:
        self.puntos: list['Point'] = puntos

    def __str__(self) -> str:
        figs = "["
        for p in self.puntos:
            figs += str(p) + " "
        figs += "]"
        return figs


def overlap():
    figuras = lector.leer_figuras()
    print(figuras)
    figuras = list(map(lambda e: Figura([Point(e[0], e[2]), Point(e[1], 0)]), figuras))
    for f in figuras:
        print(str(f), end=" ")
    print()
    l = contorno(figuras)
    print(str(l))

#Combina dos figuras (grupos de puntos)
def combinar_puntos(i_figura: Figura, j_figura: Figura):
    retorno: list[Point] = []
    i: int = 0
    j: int = 0

    hi = 0
    hj = 0
    h = 0

    while i < len(i_figura.puntos) and j < len(j_figura.puntos):
        xi = i_figura.puntos[i].x
        xj = j_figura.puntos[j].x
        if xi <= xj:
            hi = i_figura.puntos[i].y
            i += 1
        if xj <= xi:
            hj = j_figura.puntos[j].y
            j += 1
        if max(hi, hj) != h:
            h = max(hi, hj)
            retorno.append(Point(min(xi, xj), h))
    
    if i >= len(i_figura.puntos):
        retorno += j_figura.puntos[j:]
    elif j >= len(j_figura.puntos):
        retorno += i_figura.puntos[i:]
    return Figura(retorno)


def contorno(figuras: list[Figura]):
    if not figuras:
        return []
    if len(figuras) == 1:
        return figuras[0]

    mitad = len(figuras) // 2
    iz = figuras[:mitad]
    der = figuras[mitad:]
    
    iz = contorno(iz)
    der = contorno(der)

    combinado = combinar_puntos(iz, der)
    return combinado

overlap()



            