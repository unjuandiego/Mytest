class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


def Bresenham(p1, p2):
    puntos = []
    dx = (p2.x - p1.x)
    dy = (p2.y - p1.y)

    # Determinar que punto usar para empezar y cual para terminar.
    if dy < 0:
        dy = -dy
        stepy = -1
    else:
        stepy = 1
    if dx < 0:
        dx = -dx
        stepx = -1
    else:
        stepx = 1
    x = p1.x
    y = p1.y

    # Bucle hasta llegar al otro extremo de la linea.
    if dx > dy:
        p = 2*dy-dx
        while x != p2.x:
            x += stepx
            if p < 0:
                p += 2*dy
            else:
                y += stepy
                p += 2*(dy-dx)
            puntos.append(Punto(x, y))
    else:
        p = 2*dx-dy
        while y != p2.y:
            y = y + stepy
            if p < 0:
                p += 2*dx
            else:
                x += stepx
                p += 2*(dx-dy)
            puntos.append(Punto(x, y))
    return puntos


p = Punto(2, 3)
q = Punto(9, 6)
puntos = []
puntos = Bresenham(p, q)
print puntos
for i in range(len(puntos)):
    r = puntos[i]
print r[1]
