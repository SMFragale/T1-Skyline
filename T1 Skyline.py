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

def overlap():
    figuras = lector.leer_figuras()
    print(figuras)
    puntos = list(map(lambda e:[Point(e[0], e[2]), Point(e[1], 0)], figuras))
    print(puntos)
    contorno(puntos)

def contorno(puntos: list[list[Point]]):
    if len(puntos) <= 1:
        return

    mitad = len(puntos) // 2
    iz = puntos[:mitad]
    der = puntos[mitad:]
    
    iz = contorno(iz)
    der = contorno(der)

    combinado = combinar_puntos(iz, der)
    return combinado

overlap()

#Combina dos figuras (grupos de puntos)
def combinar_puntos(i_figura: list[Point], j_figura: list[Point]):
    retorno: list[Point] = []
    i: int = 0
    j: int = 0

    if i_figura[0].x < j_figura[0].x:
        i += 1
        retorno.append(i_figura[0])
    elif i_figura[0].x == j_figura[0].x:
        retorno.append(i_figura[0]) if i_figura[0].y > j_figura[0].y else retorno.append(j_figura[0])
    else:
        j += 1
        retorno.append(j_figura[0])
    
    while i < len(i_figura) and j < len(j_figura):
        if i_figura[i].x < j_figura[j].x:
            x = i_figura[i].x
            y = max(i_figura[i].y, j_figura[j].y)
            retorno.append(Point(x, y))
            i += 1
        else:
            x = j_figura[j].x
            y = max(i_figura[i].y, j_figura[j].y)
            retorno.append(Point(x, y))
            j += 1
    
    if i >= len(i_figura):
        retorno += j_figura[j:]
    elif j >= len(j_figura):
        retorno += i_figura[i:]

            