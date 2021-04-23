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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
import datetime
assert config
# Construccion de modelos
def newAnalyzer():
    analyzer = {'tracks':None,'instrumentalness':None,'acousticness':None,'liveness':None,'speechiness':None,'energy':None,'danceability':None,'valence':None}
    analyzer['tracks'] = lt.newList('SINGLE_LINKED', compareIds)
    for car in analyzer:
        if car!='tracks':
            analyzer[car] = om.newMap(omaptype='RBT',comparefunction=compare)
    return analyzer
# Funciones para agregar informacion al catalogo
def add(analyzer, track):
    lt.addLast(analyzer['tracks'], track)
    for car in analyzer:
        if car!='tracks':
            update(analyzer[car],track,car)
    return analyzer
def update(map,track,car):
    #data hace referencia al valor de la característica, siendo la llave de los mapas
    data = float(track[car])
    entry = om.get(map, data)
    if entry is None:
        lst=lt.newList('ARRAY_LIST')
    else:
        lst = me.getValue(entry)
    info_track=newDataEntry(track)
    lt.addLast(lst,info_track)
    om.put(map, data, lst)
    return map
# Funciones para creacion de datos
def newDataEntry(track):
    entry = mp.newMap(numelements=2,maptype='PROBING',loadfactor=1)
    mp.put(entry,'user_id',track['user_id'])
    mp.put(entry,'track_id',track['track_id'])
    return entry
# Funciones de consulta
def rep_car(analyzer,car,min_value,max_value):
    arbol=analyzer[car]
    artist=lt.newList('ARRAY_LIST')
    validas=om.values(arbol,min_value,max_value)
    reps=0 #suma de tracks validos
    for i in range(1,lt.size(validas)):
        lista_interna=lt.getElement(validas,i)
        reps+=lt.size(lista_interna)
        for x in range(1,lt.size(lista_interna)):
            mapa_interno=lt.getElement(lista_interna,x)
            user=me.getValue(mp.get(mapa_interno,'user_id'))
            if lt.isPresent(artist,user)==0:
                lt.addLast(artist,user)
    return reps,lt.size(artist)
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compare(dato1, dato2):
    #print('dato1:',dato1,'\ndato2:',dato2)
    if (dato1 == dato2):
        return 0
    elif (dato1 > dato2):
        return 1
    else:
        return -1