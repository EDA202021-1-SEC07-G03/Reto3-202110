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
    analyzer = {'artists':None,'info':None,'tracks':None,'instrumentalness':None,'acousticness':None,'liveness':None,'speechiness':None,'energy':None,'danceability':None,'valence':None,'tempo':None}
    analyzer['info']=mp.newMap(130000,maptype='PROBING')
    analyzer['tracks'] = lt.newList('SINGLE_LINKED')
    analyzer['artists'] = lt.newList('SINGLE_LINKED')
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists':
            analyzer[car] = om.newMap(omaptype='RBT',comparefunction=compare)
    return analyzer
# Funciones para agregar informacion al catalogo
def add(analyzer,track,hashtags):
    lt.addLast(analyzer['tracks'],track)
    if lt.isPresent(analyzer['artists'],track['artist_id'])==0:
        lt.addLast(analyzer['artists'],track['artist_id'])
    mp.put(analyzer['info'],track['track_id'],create_map(analyzer,track,hashtags))
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists':
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
def hashtags(file):
    temp=mp.newMap(180000,maptype='PROBING')
    for line in file:
        mp.put(temp,line['track_id'],line['hashtag'])
    return temp
def create_map(analyzer,track,hashtags):
    temp=mp.newMap(maptype='PROBING')
    mp.put(temp,'track_id',track['track_id'])
    mp.put(temp,'artist_id',track['artist_id'])
    mp.put(temp,'created_at',track['created_at'])
    mp.put(temp,'hashtag',me.getValue(mp.get(hashtags,track['track_id'])))
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists':
            mp.put(temp,car,track[car])
    return temp
def newDataEntry(analyzer,track):
    entry= me.getValue(mp.get(analyzer['info'],track['track_id']))
    return entry
# Funciones de consulta
#****************************************REQ 1*********************************************************************
def rep_car(analyzer,car,min_value,max_value):
    artist=lt.newList('ARRAY_LIST')
    validas=om.values(analyzer[car],min_value,max_value)
    reps=0 #suma de tracks validos
    for i in range(1,lt.size(validas)+1):
        lista_interna=lt.getElement(validas,i)
        reps+=lt.size(lista_interna)
        for x in range(1,lt.size(lista_interna)+1):
            mapa_interno=lt.getElement(lista_interna,x)
            user=me.getValue(mp.get(mapa_interno,'artist_id'))
            unicos(artist,user)
    return reps,lt.size(artist)
#****************************************REQ 2*********************************************************************
def festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability):
    mapas_canciones=lt.newList('ARRAY_LIST')
    energy_maps=herramienta_lista(om.values(analyzer['energy'],min_energy,max_energy))
    dance_maps=herramienta_lista(om.values(analyzer['danceability'],min_danceability,max_danceability))
    validas_energy=lista_car(energy_maps,'track_id')
    validas_dance=lista_car(dance_maps,'track_id')
    for i in range(1,lt.size(energy_maps)+1):
        cancion=lt.getElement(energy_maps,i)
        if me.getValue(mp.get(cancion,'danceability'))in range(min_danceability,max_danceability+0.00001):
            lt.addLast(canciones,cancion)
    return mapas_canciones
#****************************************REQ 3*********************************************************************



#****************************************REQ 4*********************************************************************
def tracks_por_genero(analyzer,diccionario,lista_generos):
    clasificados=lt.newList('ARRAY_LIST')
    for genero in lista_generos:
        tracks=validos_por_genero(genero,diccionario[genero][0],diccionario[genero][1],analyzer['tempo'])
        mapa=mp.newMap(numelements=1000,maptype='PROBING',loadfactor=0.5)
        mp.put(mapa,genero,tracks)
        lt.addLast(mapa)
    return clasificados
#****************************************REQ 5*********************************************************************

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