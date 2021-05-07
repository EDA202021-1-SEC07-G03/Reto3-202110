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
    analyzer = {'artists':None,'info':None,'tracks':None,'created_at':None,'instrumentalness':None,'acousticness':None,'liveness':None,'speechiness':None,'energy':None,'danceability':None,'valence':None,'tempo':None}
    analyzer['info']=mp.newMap(130000,maptype='PROBING')
    analyzer['tracks'] = lt.newList('SINGLE_LINKED')
    analyzer['artists'] = lt.newList('SINGLE_LINKED')
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists':
            analyzer[car] = om.newMap(omaptype='RBT',comparefunction=compare)
    return analyzer
# Funciones para agregar informacion al catalogo
def add(analyzer,track,hashtags,sentiments):
    lt.addLast(analyzer['tracks'],track)
    if lt.isPresent(analyzer['artists'],track['artist_id'])==0:
        lt.addLast(analyzer['artists'],track['artist_id'])
    mp.put(analyzer['info'],track['track_id'],create_map(analyzer,track,hashtags,sentiments))
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists': 
            if car=='created_at':
                track[car]=(track[car][-8:]).replace(':','')
            update(analyzer,analyzer[car],track,car)
    return analyzer
def update(analyzer,map,track,car):
    '''data hace referencia al valor de la característica, siendo la llave de los mapas'''
    data = float(track[car])
    entry = om.get(map, data)
    if entry is None:
        lst=lt.newList('ARRAY_LIST')
    else:
        lst = me.getValue(entry)
    info_track=me.getValue(mp.get(analyzer['info'],track['track_id']))
    lt.addLast(lst,info_track)
    om.put(map, data, lst)
    return map
# Funciones para creacion de datos
def hashtags(file):
    temp=mp.newMap(180000,maptype='PROBING')
    for line in file:
        if lt.isPresent(mp.keySet(temp),line['track_id'])==0:
            mp.put(temp,line['track_id'],lt.newList('ARRAYLIST'))
        lista=me.getValue(mp.get(temp,line['track_id']))
        if lt.isPresent(lista, line['hashtag'])==0:
            lt.addLast(lista,line['hashtag'])
    print(mp.size(temp))
    return temp
def sentiments(file):
    temp=mp.newMap(11500,maptype='PROBING')
    for line in file:
        mp.put(temp,line['hashtag'],line['vader_avg'])
    return temp
def create_map(analyzer,track,hashtags,sentiments):
    temp=mp.newMap(maptype='PROBING')
    vader=None
    mp.put(temp,'track_id',track['track_id'])
    mp.put(temp,'artist_id',track['artist_id'])
    mp.put(temp,'hashtag',me.getValue(mp.get(hashtags,track['track_id'])))
    '''track_hashtag=me.getValue(mp.get(hashtags,track['track_id']))
    if lt.isPresent(mp.keySet(sentiments),track_hashtag)!=0:
        vader=me.getValue(mp.get(sentiments,track_hashtag))
    mp.put(temp,'vader_avg',vader)'''
    for car in analyzer:
        if car!='tracks' and car!='info'and car!='artists' and car!='created_at':
            mp.put(temp,car,track[car])
        elif car=='created_at'
    return temp
# Funciones de consulta
#****************************************REQ 1*********************************************************************
def rep_car(analyzer,car,min_value,max_value):
    artist=lt.newList('ARRAY_LIST')
    validas=om.values(analyzer[car],min_value,max_value)#nlog(n)
    reps=0 #suma de tracks validos
    for i in range(1,lt.size(validas)+1):#o(nlog(n))  caso prom o mejor caso log(n)
        lista_interna=lt.getElement(validas,i)
        reps+=lt.size(lista_interna)     
        lst_artist=artistas_unicos(lista_interna)
        for x in range(1,lt.size(lst_artist)+1):
            artist_id=lt.getElement(lst_artist,x)
            if lt.isPresent(artist,artist_id)==0:
                lt.addLast(artist,artist_id)
    return reps,lt.size(artist)
#****************************************REQ 2*********************************************************************
def festejar(analyzer,min_energy,max_energy,min_danceability,max_danceability):
    canciones=lt.newList('ARRAY_LIST')
    ids=lt.newList('ARRAY_LIST')
    energy_maps=herramienta_lista(om.values(analyzer['energy'],min_energy,max_energy))
    valores_dance=om.keys(analyzer['danceability'],min_danceability,max_danceability)
    for i in range(1,lt.size(energy_maps)+1):
        cancion=lt.getElement(energy_maps,i)
        id=me.getValue(mp.get(cancion,'track_id'))
        valor_dance=float(me.getValue(mp.get(cancion,'danceability')))
        if lt.isPresent(valores_dance,valor_dance) and lt.isPresent(ids,id)==0:
            lt.addLast(ids,id)
            if lt.size(canciones)<5:
                lt.addLast(canciones,cancion)
    return canciones,lt.size(ids)
#****************************************REQ 3*********************************************************************
def estudiar(analyzer,min_instrumentalness,max_instrumentalness,min_tempo,max_tempo):
    canciones=lt.newList('ARRAY_LIST')
    ids=lt.newList('ARRAY_LIST')
    tempo_maps=herramienta_lista(om.values(analyzer['tempo'],min_tempo,max_tempo))
    valores_instrumentalness=om.keys(analyzer['instrumentalness'],min_instrumentalness,max_instrumentalness)
    for i in range(1,lt.size(tempo_maps)+1):
        cancion=lt.getElement(tempo_maps,i)
        id=me.getValue(mp.get(cancion,'track_id'))
        valor_instrumentalness=float(me.getValue(mp.get(cancion,'instrumentalness')))
        if lt.isPresent(valores_instrumentalness,valor_instrumentalness) and lt.isPresent(ids,id)==0:
            lt.addLast(ids,id)
            if lt.size(canciones)<5:
                lt.addLast(canciones,cancion)
    return canciones,lt.size(ids)

#****************************************REQ 4*********************************************************************
def tracks_por_genero(analyzer,diccionario,lista_generos):
    clasificados=mp.newMap(numelements=20,maptype='PROBING',loadfactor=0.5)
    for genero in lista_generos:
        info=mp.newMap(5)
        tracks=herramienta_lista(om.values(analyzer['tempo'],diccionario[genero][0],diccionario[genero][1]))
        artistas=artistas_unicos(tracks)
        mp.put(info,'tracks',tracks)
        mp.put(info,'artists',artistas)
        mp.put(clasificados,genero,info)
    return clasificados
#****************************************REQ 5*********************************************************************
def genero_por_tiempo(analyzer,hora_min,hora_max):
    
    canciones=lt.newList('ARRAY_LIST')
    ids=lt.newList('ARRAY_LIST')
    
    horas=om.keys(analyzer['created_at'],hora_min,hora_max)
    
    
    for i in range(0,lt.size(horas)):
        hora=lt.getElement(horas,i)
        '''id=me.getValue(mp.get(hora,'track_id'))'''
        
        
        '''lt.addLast(ids,id)'''
        if lt.size(canciones)<5:
            lt.addLast(canciones,hora)
        print(canciones,lt.size(ids))
    return canciones,lt.size(ids)

    



# Funciones copmlementarias
def artistas_unicos(lista_mapas):
    '''Se le da una lista con los mapas de los tracks y se retorna una lista con los artistas unicos y sin repeticiones'''
    lista=lt.newList('ARRAY_LIST')
    for x in range(1,lt.size(lista_mapas)+1):
        mapa_interno=lt.getElement(lista_mapas,x)
        user=me.getValue(mp.get(mapa_interno,'artist_id'))
        if lt.isPresent(lista,user)==0:
            lt.addLast(lista,user)
    return lista
def herramienta_lista(lista):
    temp=lt.newList('ARRAY_LIST')
    for i in range(1,lt.size(lista)+1):
        sub=lt.getElement(lista,i)
        for x in range(1,lt.size(sub)+1):
            mapa=lt.getElement(sub,x)
            lt.addLast(temp,mapa)
    return temp
# Funciones de ordenamiento
def compare(dato1, dato2):
    if (dato1 == dato2):
        return 0
    elif (dato1 > dato2):
        return 1
    else:
        return -1