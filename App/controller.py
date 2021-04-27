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
def loadData(analyzer, filename, filename2):
    filename = cf.data_dir + filename
    input_file = csv.DictReader(open(filename, encoding="utf-8"),delimiter=",")
    filename2 = cf.data_dir + filename2
    input_file2 = csv.DictReader(open(filename2, encoding="utf-8"),delimiter=",")
    hashtags=model.hashtags(input_file2)
    for line in input_file:
        model.add(analyzer,line,hashtags)
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
'''#Funciones complementarias
def crear_diccionario(nuevo):
    temp=mp.newMap(maptype='PROBING')
    diccionario={'reggae':(60,90),'down-tempo':(70,100),'chill-out':(90,120),'hip-hop':(85,115),'jazz and funk':(120,125),'pop':(100,130),'r&b':(60,80),'rock':(110,140),'metal':(100,160)}
    for genero in diccionario:
        mapa_genero=mp.newMap(5,maptype='PROBING')
        mp.put('minimo',diccionario[genero][0])
        mp.put('maximo',diccionario[genero][1])
        mp.put(temp,mapa_genero)
    if nuevo!={}:'''