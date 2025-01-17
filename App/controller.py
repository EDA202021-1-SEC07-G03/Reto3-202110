﻿"""
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
def loadData(analyzer, filename, filename2,filename3):
    filename = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding="utf-8"),delimiter=",")
    filename2 = cf.data_dir + filename2
    input_file2 = csv.DictReader(open(filename2, encoding="utf-8"),delimiter=",")
    filename3 = cf.data_dir + filename3
    input_file3 = csv.DictReader(open(filename3, encoding="utf-8"),delimiter=",")
    hashtags=model.hashtags(input_file2)
    sentiments=model.sentiments(input_file3)
    t = 616308
    i = 0
    for line in input_file:
        line['created_at']=(line['created_at'][-8:]).replace(':','')
        model.add(analyzer,line,hashtags)
        print(f"{i}/{t}",end='\r')
        i += 1
    analyzer['sentiments']=sentiments
    return analyzer
# Funciones de consulta sobre el catálogo
def rep_car(analyzer,car,min_value,max_value):
    return model.rep_car(analyzer,car,min_value,max_value)
def festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability):
    return model.festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability)
def estudiar(analyzer,min_instrumentalness,max_instrumentalness,min_tempo,max_tempo):
    return model.estudiar(analyzer,min_instrumentalness,max_instrumentalness,min_tempo,max_tempo)
def tracks_por_genero(analyzer,lista_generos,diccionario):
    return model.tracks_por_genero(analyzer,diccionario,lista_generos)
def genero_por_tiempo(analyzer,diccionario,hora_min,hora_max):
    return model.genero_por_tiempo(analyzer,diccionario,hora_min,hora_max)
