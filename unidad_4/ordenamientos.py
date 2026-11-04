from pelicula import Pelicula, inicializarPeliculas

peliculas = inicializarPeliculas()

def ordenarBurbuja(peliculas):
    pasadas = 0
    flagCambio = False
    for i in range(len(peliculas) - 1):
        for j in range(len(peliculas) - 1 - i):
            pasadas = pasadas + 1
            if peliculas[j].titulo > peliculas[j+1].titulo:
                peliculas[j], peliculas[j + 1] = peliculas[j + 1], peliculas[j]
                flagCambio = True
        if not(flagCambio):
            break
    print(pasadas)


def ordenarSeleccion(peliculas):
    pasadas = 0
    for i in range(len(peliculas) - 1):
        posMenor = i
        for j in range(i + 1, len(peliculas)):
            pasadas = pasadas + 1
            if peliculas[j].titulo < peliculas[posMenor].titulo:
                posMenor = j

        peliculas[i], peliculas[posMenor] = peliculas[posMenor], peliculas[i]
    print(pasadas)



ordenarBurbuja(peliculas)
#ordenarSeleccion(peliculas)
for p in peliculas:
    print(p)

