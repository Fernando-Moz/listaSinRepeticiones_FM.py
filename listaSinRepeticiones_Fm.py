from collections import Counter

nombres = [
    "Alejandro", "Sofía", "Mateo", "Lucía", "Sebastián", "Valentina", "Daniel", "Martina",
    "Pablo", "María", "Álvaro", "Paula", "Adrián", "Julia", "Diego", "Valeria",
    "Javier", "Daniela", "Carlos", "Alba", "Lucas", "Emma", "Hugo", "Carla",
    "Martín", "Sara", "Manuel", "Carmen", "Pedro", "Noa", "David", "Claudia",
    "Mario", "Elena", "Marcos", "Irene", "Nicolás", "Nerea", "Gabriel", "Rocío",
    "Samuel", "Laura", "Gonzalo", "Marta", "Jorge", "Andrea", "Sergio", "Ana",
    "Luis", "Natalia", "Miguel", "Cristina", "Fernando", "Beatriz", "Raúl", "Patricia",
    "Rubén", "Silvia", "Iván", "Raquel", "Óscar", "Mónica", "Enrique", "Alicia",
    "Alberto", "Marina", "Víctor", "Inés", "Francisco", "Celia", "Antonio", "Nuria",
    "José", "Miriam", "Juan", "Lorena", "Andrés", "Eva", "Rafael", "Teresa",
    "Ramón", "Pilar", "Vicente", "Rosa", "Eduardo", "Ángela", "Ignacio", "Blanca",
    "Guillermo", "Clara", "Roberto", "Victoria", "Jaime", "Lidia", "Arturo", "Verónica",
    "Emilio", "Susana", "Tomás", "Isabel", "Héctor", "Yolanda", "César", "Sonia",
    "Julio", "Olga", "Salvador", "Carolina", "Agustín", "Vanesa", "Félix", "Gema",
    "Rodrigo", "Estefanía", "Iker", "Aitana", "Unai", "Laia", "Aitor", "Ane",
    "Biel", "Ona", "Pol", "Jana", "Arnau", "Abril", "Marc", "Iria",
    "Joel", "Nora", "Eric", "Vera", "Bruno", "Triana", "Leo", "Candela",
    "Gael", "Vega", "Thiago", "Alma", "Dylan", "Lola", "Enzo", "Jimena",
    "Darío", "Olivia", "Álex", "Chloe", "Ian", "Mía", "Oliver", "Zoe",
    "Alejandro", "Lucía", "Mateo", "María", "Daniel", "Sofía", "Pablo", "Paula",
    "Carlos", "Carmen", "Javier", "Laura", "Manuel", "Marta", "David", "Elena",
    "Lucas", "Sara", "Hugo", "Valeria", "Martín", "Alba", "Adrián", "Julia",
    "Diego", "Daniela", "Álvaro", "Martina", "José", "Ana", "Juan", "Isabel",
    "Antonio", "Cristina", "Francisco", "Patricia", "Miguel", "Beatriz", "Luis", "Silvia",
    "Alejandro", "María", "Lucía", "Carlos", "Sofía", "Daniel", "Paula", "Javier",
    "Carmen", "Manuel", "Laura", "David", "Marta", "Pablo", "Elena", "Mateo"
]


def dejar_una_aparicion(lista):
    """Versión 1: deja una única aparición de cada elemento (la primera),
    conservando el orden original."""
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado


def quitar_todas_las_apariciones(lista):
    """Versión 2: elimina todos los elementos que aparecen más de una vez,
    dejando solo los que aparecen exactamente una vez."""
    apariciones = Counter(lista)
    return [elemento for elemento in lista if apariciones[elemento] == 1]


if __name__ == "__main__":
    version1 = dejar_una_aparicion(nombres)
    version2 = quitar_todas_las_apariciones(nombres)

    print(f"Lista original: {len(nombres)} elementos")
    print(f"\nVersión 1 (una aparición de cada uno): {len(version1)} elementos")
    print(version1)
    print(f"\nVersión 2 (sin ninguna aparición de los repetidos): {len(version2)} elementos")
    print(version2)