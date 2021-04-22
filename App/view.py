"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
filename='context_content_features-small.csv'
cont=None
def printMenu():
    print("Bienvenido")
    print("1- Iniciar el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar reproducciones en rango de carácteristica de contenido")
    print("4- Encontrar musica para festejar")
    print("5- Encontrar musica para estudiar")
    print("6- Estudiar los generos musicales")
    print("7- Genero musical mas escuchado en el tiempo")
    print(len(["instrumentalness","liveness","speechiness","danceability","valence","loudness","tempo","acousticness","energy","mode","key","artist_id","tweet_lang","track_id","created_at","lang","time_zone","user_id","id"]))
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        cont = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        controller.loadData(cont, filename)
        print('Tracks cargados: ' + str(controller.crimesSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
    else:
        sys.exit(0)
sys.exit(0)
