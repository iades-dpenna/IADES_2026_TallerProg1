class Pelicula:
    def __init__(self, codigo, titulo, anio, genero, duracion):
        self.codigo = codigo
        self.titulo = titulo
        self.anio = anio
        self.genero = genero
        self.duracion = duracion

    def __str__(self):
        return f"{self.codigo} - {self.titulo} ({self.anio})"


def inicializarPeliculas():
    peliculas = [
        Pelicula(101, "El padrino", 1972, "Drama", 175),
        Pelicula(105, "Star Wars", 1977, "Ciencia ficción", 121),
        Pelicula(112, "Volver al futuro", 1985, "Ciencia ficción", 116),
        Pelicula(118, "Jurassic Park", 1993, "Aventura", 127),
        Pelicula(124, "Forrest Gump", 1994, "Drama", 142),
        Pelicula(131, "Toy Story", 1995, "Animación", 81),
        Pelicula(137, "Titanic", 1997, "Romance", 194),
        Pelicula(143, "Matrix", 1999, "Ciencia ficción", 136),
        Pelicula(150, "Gladiador", 2000, "Acción", 155),
        Pelicula(156, "Shrek", 2001, "Animación", 90),
        Pelicula(163, "Buscando a Nemo", 2003, "Animación", 100),
        Pelicula(170, "Batman: El caballero oscuro", 2008, "Acción", 152),
        Pelicula(178, "Avatar", 2009, "Ciencia ficción", 162),
        Pelicula(185, "El origen", 2010, "Ciencia ficción", 148),
        Pelicula(192, "Intensamente", 2015, "Animación", 95),
        Pelicula(201, "Coco", 2017, "Animación", 105),
        Pelicula(208, "Avengers: Endgame", 2019, "Acción", 181),
        Pelicula(215, "Dune", 2021, "Ciencia ficción", 155),
        Pelicula(223, "Oppenheimer", 2023, "Drama", 180),
        Pelicula(230, "Intensamente 2", 2024, "Animación", 96)
    ]

    return peliculas