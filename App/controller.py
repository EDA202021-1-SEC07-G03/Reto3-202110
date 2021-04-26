"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
from App import model
import datetime
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo 
def init():
    analyzer = model.newAnalyzer()
    return analyzer
# Funciones para la carga de datos
def loadData(analyzer, filename):
    filename = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding="utf-8"),delimiter=",")
    for line in input_file:
        model.add(analyzer, line)
    return analyzer
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def rep_car(analyzer,car,min_value,max_value):
    return model.rep_car(analyzer,car,min_value,max_value)
def festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability):
    return model.festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability)


def validos_por_genero(lista_generos,diccionario):
    return model.validos_por_genero(lista_generos,diccionario)


def contador_tracks(analyzer):
    return lt.size(analyzer['tracks'])
'''
user="user_track_hashtag_timestamp-small.csv"
user= cf.data_dir + user
input_file2 = csv.DictReader(open(user, encoding="utf-8"),delimiter=",")
lst=[]
for hashtag in input_file2:
    lst+=[hashtag["hashtag"]]
i=0
for track in input_file:
    track["hashtag"]=lst[i]
    model.addTrack(analyzer, track)
    i+=1'''