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
from DISClib.Algorithms.Sorting import mergesort as mrg
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
def add(analyzer,track,hashtags):
    lt.addLast(analyzer['tracks'],track)
    if lt.isPresent(analyzer['artists'],track['artist_id'])==0:
        lt.addLast(analyzer['artists'],track['artist_id'])
    if mp.contains(analyzer['info'],track['track_id'])==False:
        mp.put(analyzer['info'],track['track_id'],create_map(analyzer,track,hashtags))
    mapa_interno=me.getValue(mp.get(analyzer['info'],track['track_id']))
    lt.addLast(me.getValue(mp.get(mapa_interno,'created_at')),track['created_at'])
    for car in analyzer:
        if car not in['tracks','info','artists']:
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
        if mp.contains(temp,line['track_id'])==False:
            mp.put(temp,line['track_id'],lt.newList('ARRAYLIST'))
        lista=me.getValue(mp.get(temp,line['track_id']))
        if lt.isPresent(lista, line['hashtag'].lower())==0:
            lt.addLast(lista,line['hashtag'].lower())
    return temp
def sentiments(file):
    temp=mp.newMap(11500,maptype='PROBING')
    for line in file:
        if len(line['vader_avg'])>0:
            mp.put(temp,line['hashtag'].lower(),float(line['vader_avg']))
    return temp
def create_map(analyzer,track,hashtags):
    temp=mp.newMap(maptype='PROBING')
    vader=None
    mp.put(temp,'track_id',track['track_id'])
    mp.put(temp,'artist_id',track['artist_id'])
    mp.put(temp,'hashtag',me.getValue(mp.get(hashtags,track['track_id'])))
    for car in analyzer:
        if car not in['tracks','info','artists','created_at']:
            mp.put(temp,car,float(track[car]))
        mp.put(temp,'created_at',lt.newList('ARRAY_LIST'))
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
        valor_dance=me.getValue(mp.get(cancion,'danceability'))
        if lt.isPresent(valores_dance,valor_dance)!=0 and lt.isPresent(ids,id)==0:
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
        valor_instrumentalness=me.getValue(mp.get(cancion,'instrumentalness'))
        if lt.isPresent(valores_instrumentalness,valor_instrumentalness)!=0 and lt.isPresent(ids,id)==0:
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
def genero_por_tiempo(analyzer,diccionario,hora_min,hora_max):
    canciones=lt.newList('ARRAY_LIST',comparebyhashtags)
    ordenados=om.newMap(comparefunction=compare)
    generos=mp.newMap(maptype='PROBING')
    ranking=lt.newList('ARRAY_LIST')
    unicos=lt.newList()
    for genero in diccionario:
        mp.put(generos,genero,lt.newList('ARRAY_LIST'))
    validos=herramienta_lista(om.values(analyzer['created_at'],hora_min,hora_max))
    for i in range(1,lt.size(validos)+1):
        mapa_interno=lt.getElement(validos,i)
        '''if i in [1,4,7]:
            print(lt.getElement(validos,i),'\n','='*80,'\n',mapa_interno,'\n','*'*80,'\n','*'*80,'\n')'''
        tempo=me.getValue(mp.get(mapa_interno,'tempo'))
        for genero in diccionario:
            lista_tracks=me.getValue(mp.get(generos,genero))
            if diccionario[genero][0]<=tempo<=diccionario[genero][1]:
                lt.addLast(lista_tracks,mapa_interno)
    for i in range(1,lt.size(mp.keySet(generos))+1):
        genero=lt.getElement(mp.keySet(generos),i)
        canciones_genero=me.getValue(mp.get(generos,genero))
        om.put(ordenados,lt.size(canciones_genero),genero)
    mayor_cantidad=om.maxKey(ordenados)
    mayor_genero=me.getValue(om.get(ordenados,mayor_cantidad))
    for i in range(1,lt.size(me.getValue(mp.get(generos,mayor_genero)))+1):
        mapa_interno=lt.getElement(me.getValue(mp.get(generos,mayor_genero)),i)
        if lt.isPresent(unicos,me.getValue(mp.get(mapa_interno,'track_id')))==0:
            lt.addLast(unicos,me.getValue(mp.get(mapa_interno,'track_id')))
        cantidad_hashtags=lt.size(me.getValue(mp.get(mapa_interno,'hashtag')))
        lt.addLast(canciones,(mapa_interno,cantidad_hashtags))
    maximo=10
    if lt.size(canciones)<maximo:
        maximo=lt.size(canciones)
    rank_valores=lt.subList(canciones,0,maximo)
    for i in range(1,lt.size(rank_valores)+1):
        num_hashtags=lt.getElement(rank_valores,i)[1]
        track=lt.getElement(rank_valores,i)[0]
        lista_hashtags=me.getValue(mp.get(track,'hashtag'))
        contador=0
        sumatoria=0
        promedio=0
        for i in range(1,lt.size(lista_hashtags)+1):
            hashtag=lt.getElement(lista_hashtags,i)
            if mp.contains(analyzer['sentiments'],hashtag):
                vader=me.getValue(mp.get(analyzer['sentiments'],hashtag))
                sumatoria+=vader
                contador+=1
        if contador!=0:
            promedio=sumatoria/contador
        tupla=(me.getValue(mp.get(track,'track_id')),num_hashtags,promedio)
        lt.addLast(ranking,tupla)
    mrg.sort(ranking,comparebyhashtags)
    return ranking,lt.size(validos),ordenados,mayor_genero,lt.size(unicos),generos

    



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
def comparebyhashtags(dato1, dato2):
    dato1=dato1[1]
    dato2=dato2[1]
    return dato1>dato2