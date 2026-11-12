from pelicula import Pelicula, inicializarPeliculas


def ordenarBurbuja(peliculas):
    pasadas = 0
    for i in range(len(peliculas) - 1):
        flagCambio = False
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

def ordenarInsercion(peliculas):
    pasadas = 0
    for i in range(1, len(peliculas)):
        actual = peliculas[i]
        j = i - 1

        while j >= 0 and peliculas[j].titulo > actual.titulo:
            pasadas = pasadas + 1
            peliculas[j + 1] = peliculas[j]
            j -= 1

        peliculas[j + 1] = actual
    print(pasadas)

peliculas = inicializarPeliculas()
ordenarBurbuja(peliculas)
print("Burbuja")
for p in peliculas:
    print(p)
print()
peliculas = inicializarPeliculas()
ordenarSeleccion(peliculas)
print("Seleccion")
for p in peliculas:
    print(p)
print()
peliculas = inicializarPeliculas()
print("Insercion")
ordenarInsercion(peliculas)
for p in peliculas:
    print(p)

