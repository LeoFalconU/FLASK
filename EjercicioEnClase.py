#Función que permita ingresar elementos a una lista dentro de un ciclo FOR.
#Función que permita ingresar elementos a un diccionario dentro de un ciclo FOR.
#Función que permita imprimir todos los elementos de una lista y un diccionario dentro de un ciclo FOR.

"""
for i in range(5):
         range(5,15):  #donde inicia y donde termina, empieza en 0
         range(1,10,2)  #donde inicia, donde termina y el numero de saltos)
"""

list = [1,2,3,4,5,6,7,8,9,10]
emptyList =[]
def funcionLista(emptyList):
    for i in range (1,10,2):
        emptyList.append(i)
    return emptyList

print(funcionLista(emptyList))





movies = {
    "0001": {
        "name": "Avengers",
        "genre": "Action",
        "screenings": [1,2,3,4,5],
        "schedule": ['12:00','14:00','16:00','18:00'],
        "3D": True
    },
        "0002": {
        "name": "Star Wars",
        "genre": "Action",
        "screenings": [1,2,3],
        "schedule": ['11:00','13:00','15:00','17:00','19:00'],
        "3D": True
    },
        "0003": {
        "name": "The Shinning (Anniversary)",
        "genre": "Horror",
        "screenings": [1],
        "schedule": ['12:00','16:30','19:00'],
        "3D": False
    },
}


def add_movie(new_movie=None):
    if(movies.get("0001").get("3D")):
        movies["0004"] = {
            "name": "Avengers 3D",
            "genre": "Action",
            "screenings": [1],
            "schedule": ["20:00"],
            "3D": False

        }

add_movie()
print(movies)