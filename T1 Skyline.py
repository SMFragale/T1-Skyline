input = [[1,3,4], [2,4,2], [5,8,2], [6,7,1]]

input2: list = []
for r in input:
    input2.append((r[0], r[2]))
    input2.append((r[1], r[2]))
    input2.append((r[1], 0))

input2.sort(key = lambda x: (x[0], -x[1]))
print(input2)

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
        

#Precondiciones: Las figuras están ordenadas del más pequeño en x al más grande y si son iguales, del más pequeño en y al más grande
def combinar(i_figura: list[Point], j_figura: list[Point]):
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

    #Acaba cuando alguna de las dos figuras termina de analizarse
    while i < len(i_figura) and j < len(j_figura):
        i_punto = i_figura[i]
        j_punto = j_figura[j]
        if i_punto.y == 0:
            if i_punto.en_rango(j_figura):
                i += 1
            else:
                i += 1
                retorno.append(i_punto)
        else:
            anterior = retorno[-1]
            siguiente = i_figura[i+1].compare_get(j_figura[j+1])
            if i_punto.y > anterior.y and i_punto.y < siguiente.y:
                #intersection
                pass
            else:
                #no hay intersection
                nuevo_punto = i_punto.compare_get(j_punto)
                if nuevo_punto == i_punto:
                    #Si está en la misma altura que el punto anterior, se descarta y se toma el otro
                    if anterior.y == nuevo_punto.y:
                        retorno.append(j_punto)
                        j += 1
                        i += 1
                    else:
                        retorno.append(i_punto)
                        i += 1
                else:
                    #Si está en la misma altura que el punto anterior, se descarta y se toma el otro
                    if anterior.y == nuevo_punto.y:
                        retorno.append(i_punto)
                        i += 1
                        j += 1
                    else:
                        retorno.append(j_punto)
                        j += 1
            
    #Cuando alguna de las dos figuras termina de analizarse, la que queda restante puede terminar de poner el resto de sus puntos pues no hay más comparaciones necesarias
    if i >= len(i_figura):
        retorno += j_figura[j:]
    elif j >= len(j_figura):
        retorno += i_figura[i:]

                
        

            