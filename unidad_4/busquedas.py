from pelicula import Pelicula, inicializarPeliculas

peliculas = inicializarPeliculas()

def busquedaSecuencial(codigo):
    i = 0
    for p in peliculas:
        i = i + 1
        if p.codigo == int(codigo):
            print("Cantidad de vueltas:", i)
            return p
    
    print("Cantidad de vueltas:", i)
    return None

def busquedaBinaria(codigo):
    iDesde = 0
    iHasta = len(peliculas) - 1
 
    i = 0
    while iDesde <= iHasta:
        i = i + 1
        imedio = (iDesde + iHasta) // 2
        p = peliculas[imedio]
        if p.codigo == int(codigo):
            print("Cantidad de vueltas:", i)
            return p
        elif int(codigo) < p.codigo :
            iHasta = imedio - 1
        else:
            iDesde = imedio + 1
    
    print("Cantidad de vueltas:", i)
    return None


print("Busqueda Secuencial")
while True:
    cod = input("Ingrese Codigo:")
    if cod == "":
        break
    prod = busquedaSecuencial(cod)
    print(prod)

print("Busqueda Binaria")
while True:
    cod = input("Ingrese Codigo:")
    if cod == "":
        break
    prod = busquedaBinaria(cod)
    print(prod)
