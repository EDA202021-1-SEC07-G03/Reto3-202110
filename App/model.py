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
    analyzer = {'tracks':None,'instrumentalness':None,'acousticness':None,'liveness':None,'speechiness':None,'energy':None,'danceability':None,'valence':None,'tempo':None}
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
            update(analyzer,analyzer[car],track,car)
    return analyzer
def update(analyzer,map,track,car):
    #data hace referencia al valor de la característica, siendo la llave de los mapas
    data = float(track[car])
    entry = om.get(map, data)
    if entry is None:
        lst=lt.newList('ARRAY_LIST')
    else:
        lst = me.getValue(entry)
    info_track=newDataEntry(analyzer,track)
    lt.addLast(lst,info_track)
    om.put(map, data, lst)
    return map
# Funciones para creacion de datos
def newDataEntry(analyzer,track):
    entry = mp.newMap(numelements=20,maptype='PROBING',loadfactor=0.6)
    mp.put(entry,'track_id',track['track_id'])
    mp.put(entry,'user_id',track['user_id'])
    for car in analyzer:
        if car!='tracks':
            mp.put(entry,car,track[car])
    return entry
# Funciones de consulta
def rep_car(analyzer,car,min_value,max_value):
    artist=lt.newList('ARRAY_LIST')
    validas=om.values(analyzer[car],min_value,max_value)
    reps=0 #suma de tracks validos
    for i in range(1,lt.size(validas)+1):
        lista_interna=lt.getElement(validas,i)
        reps+=lt.size(lista_interna)
        for x in range(1,lt.size(lista_interna)+1):
            mapa_interno=lt.getElement(lista_interna,x)
            user=me.getValue(mp.get(mapa_interno,'user_id'))
            unicos(artist,user)
    return reps,lt.size(artist)
def festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability):
    canciones=lt.newList('ARRAY_LIST')
    mapas_canciones=lt.newList('ARRAY_LIST')
    energy_maps=herramienta_lista(om.values(analyzer['energy'],min_energy,max_energy))
    dance_maps=herramienta_lista(om.values(analyzer['danceability'],min_danceability,max_danceability))
    validas_energy=lista_car(energy_maps,'track_id')
    validas_dance=lista_car(dance_maps,'track_id')
    for i in range(1,lt.size(validas_energy)+1):
        cancion=lt.getElement(validas_energy,i)
        if lt.isPresent(validas_dance,cancion)!=0 and lt.isPresent(canciones,cancion)==0:
            lt.addLast(canciones,cancion)
    for i in range(1,lt.size(canciones)+1):
        id=lt.getElement(canciones,i)
        unico=True
        for x in range(1,lt.size(energy_maps)+1):
            mapa=lt.getElement(energy_maps,x)
            id_mapa=me.getValue(mp.get(mapa,'track_id'))
            if id==id_mapa and unico==True:
                unico=False
                lt.addLast(mapas_canciones,mapa)
    return mapas_canciones




def generos(diccionario,lista_generos):
    tempo=analyzer['tempo']
    clasificados=lt.newList('ARRAY_LIST')
    for genero in lista_generos:
        tracks=validos_por_genero(genero,diccionario[genero][0],diccionario[genero][1],tempo)
        mapa=mp.newMap(maptype='PROBING')
        mp.put(mapa,genero,tracks)
        lt.addLast(mapa)
    return clasificados
# Funciones utilizadas para comparar elementos dentro de una lista
def unicos(lista,elemento):
    if lt.isPresent(lista,elemento)==0:
        lt.addLast(lista,elemento)
def herramienta_lista(lista):
    temp=lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(lista)+1):
        sub=lt.getElement(lista,i)
        for x in range(1,lt.size(sub)+1):
            mapa=lt.getElement(sub,x)
            lt.addLast(temp,mapa)
    return temp
def lista_car(lista,car):
    temp=lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(lista)+1):
        mapa_interno=lt.getElement(lista,i)
        value=me.getValue(mp.get(mapa_interno,car))
        lt.addLast(temp,value)
    return temp
def validos_por_genero(genero,min_tempo,max_tempo,tempo):#tempo sería analyzer[tempo]
    lista_listas=om.values(tempo,min_tempo,max_tempo)
    return herramienta_lista(lista_listas)
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
    elif type(dato1)==dict or type(dato1)==dict:
        return -1
    elif (dato1 > dato2):
        return 1
    else:
        return -1