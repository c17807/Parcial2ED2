# Definimos la matriz de libros

import unidecode

libros = [
    {"titulo": "Cien años de soledad", "genero": "Realismo mágico", "longitud": 417, "autor": "Gabriel García Márquez"},
    {"titulo": "1984", "genero": "Distopía", "longitud": 328, "autor": "George Orwell"},
    {"titulo": "El gran Gatsby", "genero": "Novela clásica", "longitud": 180, "autor": "F. Scott Fitzgerald"},
    {"titulo": "Orgullo y prejuicio", "genero": "Romance", "longitud": 432, "autor": "Jane Austen"},
    {"titulo": "Crónicas de una muerte anunciada", "genero": "Novela corta", "longitud": 120, "autor": "Gabriel García Márquez"},
    {"titulo": "El alquimista", "genero": "Ficción contemporánea", "longitud": 208, "autor": "Paulo Coelho"},
    {"titulo": "Fahrenheit 451", "genero": "Ciencia ficción", "longitud": 160, "autor": "Ray Bradbury"},
    {"titulo": "El nombre de la rosa", "genero": "Misterio histórico", "longitud": 500, "autor": "Umberto Eco"},
    {"titulo": "La sombra del viento", "genero": "Novela histórica", "longitud": 575, "autor": "Carlos Ruiz Zafón"},
    {"titulo": "El viejo y el mar", "genero": "Ficción", "longitud": 128, "autor": "Ernest Hemingway"},
    {"titulo": "Moby Dick", "genero": "Aventura", "longitud": 720, "autor": "Herman Melville"},
    {"titulo": "En el camino", "genero": "Beat", "longitud": 320, "autor": "Jack Kerouac"},
    {"titulo": "Siddhartha", "genero": "Filosófico", "longitud": 152, "autor": "Hermann Hesse"},
    {"titulo": "El juego del ángel", "genero": "Novela histórica", "longitud": 512, "autor": "Carlos Ruiz Zafón"},
    {"titulo": "La casa de los espíritus", "genero": "Realismo mágico", "longitud": 384, "autor": "Isabel Allende"},
    {"titulo": "Drácula", "genero": "Horror", "longitud": 400, "autor": "Bram Stoker"},
    {"titulo": "Los miserables", "genero": "Novela clásica", "longitud": 1232, "autor": "Victor Hugo"},
    {"titulo": "El retrato de Dorian Gray", "genero": "Ficción gótica", "longitud": 240, "autor": "Oscar Wilde"},
    {"titulo": "El proceso", "genero": "Ficción", "longitud": 256, "autor": "Franz Kafka"},
    {"titulo": "La tregua", "genero": "Novela contemporánea", "longitud": 160, "autor": "Mario Benedetti"},
    {"titulo": "Las aventuras de Huckleberry Finn", "genero": "Novela clásica", "longitud": 366, "autor": "Mark Twain"},
    {"titulo": "Cumbres borrascosas", "genero": "Novela gótica", "longitud": 416, "autor": "Emily Brontë"},
    {"titulo": "Un mundo feliz", "genero": "Distopía", "longitud": 268, "autor": "Aldous Huxley"},
    {"titulo": "Los ojos de mi princesa", "genero": "Romance", "longitud": 288, "autor": "Carlos Cuauhtémoc Sánchez"},
    {"titulo": "El maestro y Margarita", "genero": "Ficción", "longitud": 400, "autor": "Mijaíl Bulgákov"},
    {"titulo": "El silencio de los corderos", "genero": "Thriller", "longitud": 368, "autor": "Thomas Harris"},
    {"titulo": "La metamorfosis", "genero": "Ficción", "longitud": 191, "autor": "Franz Kafka"},
    {"titulo": "El guardián entre el centeno", "genero": "Novela contemporánea", "longitud": 277, "autor": "J.D. Salinger"},
    {"titulo": "En busca del tiempo perdido", "genero": "Novela moderna", "longitud": 3200, "autor": "Marcel Proust"},
    {"titulo": "Rayuela", "genero": "Novela experimental", "longitud": 620, "autor": "Julio Cortázar"},
    {"titulo": "Los pilares de la Tierra", "genero": "Novela histórica", "longitud": 973, "autor": "Ken Follett"},
    {"titulo": "La chica del tren", "genero": "Thriller psicológico", "longitud": 395, "autor": "Paula Hawkins"},
    {"titulo": "El cuento de la criada", "genero": "Distopía", "longitud": 311, "autor": "Margaret Atwood"},
    {"titulo": "El bosque de los árboles muertos", "genero": "Horror", "longitud": 288, "autor": "Joan Carles Muntaner"},
    {"titulo": "Las aventuras de Sherlock Holmes", "genero": "Misterio", "longitud": 307, "autor": "Arthur Conan Doyle"},
    {"titulo": "Las uvas de la ira", "genero": "Novela social", "longitud": 464, "autor": "John Steinbeck"},
    {"titulo": "El perfume", "genero": "Ficción histórica", "longitud": 255, "autor": "Patrick Süskind"},
    {"titulo": "Cazadores de sombras", "genero": "Fantasía", "longitud": 480, "autor": "Cassandra Clare"},
    {"titulo": "El hombre en busca de sentido", "genero": "No ficción", "longitud": 200, "autor": "Viktor Frankl"},
    {"titulo": "La historia interminable", "genero": "Fantasía", "longitud": 528, "autor": "Michael Ende"},
    {"titulo": "El tambor de hojalata", "genero": "Novela contemporánea", "longitud": 544, "autor": "Günter Grass"},
    {"titulo": "La guerra de los mundos", "genero": "Ciencia ficción", "longitud": 192, "autor": "H.G. Wells"},
    {"titulo": "Los hombres que no amaban a las mujeres", "genero": "Thriller", "longitud": 465, "autor": "Stieg Larsson"},
    {"titulo": "La chica que soñaba con una cerilla y un bidón de gasolina", "genero": "Thriller", "longitud": 569, "autor": "Stieg Larsson"},
    {"titulo": "Harry Potter y la piedra filosofal", "genero": "Fantasía", "longitud": 223, "autor": "J.K. Rowling"},
    {"titulo": "El Hobbit", "genero": "Fantasía", "longitud": 310, "autor": "J.R.R. Tolkien"},
    {"titulo": "La sombra de los otros", "genero": "Ficción contemporánea", "longitud": 200, "autor": "Antonio Skármeta"},
    {"titulo": "Bajo la misma estrella", "genero": "Romance juvenil", "longitud": 313, "autor": "John Green"},
    {"titulo": "El tiempo entre costuras", "genero": "Novela histórica", "longitud": 600, "autor": "María Dueñas"},
    {"titulo": "El lado oscuro del corazón", "genero": "Ficción", "longitud": 272, "autor": "Mario Benedetti"}
]

def normalizar(texto):
    return unidecode.unidecode(texto).lower()

def buscar_por_titulo(titulo):
    titulo_normalizado = normalizar(titulo)
    resultados = [libro for libro in libros if normalizar(libro["titulo"]) == titulo_normalizado]
    return resultados

def buscar_por_criterios(genero=None, autor=None, longitud=None):
    rango_min = longitud - 100 if longitud else None
    rango_max = longitud + 100 if longitud else None

    genero_normalizado = normalizar(genero) if genero else None
    autor_normalizado = normalizar(autor) if autor else None


    libros_filtrados = [libro for libro in libros if
                        (genero_normalizado is None or normalizar(libro["genero"]) == genero_normalizado) and
                        (longitud is None or (rango_min <= libro["longitud"] <= rango_max))]


    if autor_normalizado:
        libros_ordenados = sorted(libros_filtrados, key=lambda x: (
        normalizar(x["autor"]) != autor_normalizado, normalizar(x["autor"]), x["longitud"]))
    else:
        libros_ordenados = sorted(libros_filtrados, key=lambda x: (normalizar(x["autor"]), x["longitud"]))


    if len(libros_ordenados) < 20:
        print(
            "No se encontraron suficientes libros que cumplan con los criterios especificados. Mostrando los primeros 20 libros del catálogo:")
        libros_ordenados = libros_ordenados + libros[:20 - len(libros_ordenados)]

    return libros_ordenados


def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Buscar por título")
    print("2. Buscar por criterios (género, autor, longitud)")
    print("3. Ver todo el catálogo")
    print("4. Salir")


def ver_catalogo():
    return libros


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Ingresa el título del libro: ")
            resultados = buscar_por_titulo(titulo)
            print(f"\nResultados de búsqueda por título '{titulo}':")
            for libro in resultados:
                print(libro)
            if not resultados:
                print("No se encontraron libros con ese título.")

        elif opcion == "2":
            genero = input("Ingresa el género del libro (o deja en blanco para omitir): ")
            autor = input("Ingresa el autor del libro (o deja en blanco para omitir): ")
            longitud = input("Ingresa la longitud del libro (o deja en blanco para omitir): ")
            genero = genero if genero else None
            autor = autor if autor else None
            longitud = int(longitud) if longitud else None
            resultados = buscar_por_criterios(genero, autor, longitud)
            print(f"\nResultados de búsqueda por género '{genero}', autor '{autor}', y longitud {longitud}:")
            for libro in resultados:
                print(libro)
            if not resultados:
                print("No se encontraron libros que cumplan con los criterios especificados.")

        elif opcion == "3":
            catalogo = ver_catalogo()
            print("\nCatálogo completo de libros:")
            for libro in catalogo:
                print(libro)

        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")


if __name__ == "__main__":
    main()
