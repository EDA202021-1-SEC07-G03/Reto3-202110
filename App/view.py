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
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as mp
import datetime
import time
import tracemalloc
filename='context_content_features-small.csv'
filename2='user_track_hashtag_timestamp-small.csv'
filename3='sentiment_values.csv'
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
def mostrar_opciones():
    print('1-Consultar lista de generos\n2-Crear nuevo genero')
    return input('Ingrese la accion a realizar: ')
def getTime():
    return float(time.perf_counter()*1000)
def getMemory():
    return tracemalloc.take_snapshot()
def deltaMemory(start_memory, stop_memory):
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    delta_memory = delta_memory/1024.0
    return delta_memory
def horas(hora):
            if len(hora)==5:
                hora='0'+hora
            i=2
            x='pm'
            if int(hora)<120000:
                x='am'
            while i<len(hora):
                hora=hora[:i]+':'+hora[i:]
                i+=3
            return hora+x
cont = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        cont = controller.init()
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

#**************************************** CARGA *********************************************************************
    elif int(inputs[0]) == 2:
        print("\nCargando información de tracks ....")
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        controller.loadData(cont,filename,filename2,filename3)
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        #-------------------------------------------------
        print('Primeros tracks:')
        for i in range(5):
            cancion=lt.getElement(cont['tracks'],i)
            print('\nTrack',i,cancion)
        print('\nUltimos tracks:')
        for i in range(5):
            x=lt.size(cont['tracks'])-i
            cancion=cancion=lt.getElement(cont['tracks'],x)
            print('\nTrack',x,cancion)
        print('Eventos cargados: ' + str(om.size(cont['created_at'])))
        print('Tracks cargados: ' + str(mp.size(cont['info'])))
        print('Artistas cargados: ' + str(mp.size(cont['artists'])))
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

#****************************************REQ 1*********************************************************************
    elif int(inputs[0]) == 3:
        '''
        car=input('Ingrese la característica a consultar: ').lower()
        min_value=float(input('Ingrese el valor mínimo para el rango de la característica: '))
        max_value=float(input('Ingrese el valor máximo para el rango de la característica: '))
        '''
        #pruebas
        car='instrumentalness'
        min_value=float(0.75)
        max_value=float(1)
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        funcion=controller.rep_car(cont,car,min_value,max_value)
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        #-------------------------------------------------
        reps=funcion[0]
        artistas=funcion[1]
        print('*'*60)
        print('La característica',car,'está en el rango de',min_value,'a',max_value)
        print('Reproducciones:',reps)
        print('Artistas:',artistas)
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

#****************************************REQ 2*********************************************************************

    elif int(inputs[0]) == 4:
        '''
        min_energy=float(input('Ingrese el valor mínimo para Energy: '))
        max_energy=float(input('Ingrese el valor máximo para Energy: '))
        min_danceability=float(input('Ingrese el valor mínimo para Danceability: '))
        max_danceability=float(input('Ingrese el valor máximo para Danceability: '))
        '''
        min_energy=float(0.5)
        max_energy=float(0.75)
        min_danceability=float(0.75)
        max_danceability=float(1)
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        funcion=controller.festejar(cont,min_energy,max_energy,min_danceability,max_danceability)
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        
        #-------------------------------------------------
        
        total=funcion[1]
        sub=funcion[0]
        num=0
        print('Hay un total de canciones de:',total)
        for i in range(1,lt.size(sub)+1):
            num+=1
            info=lt.getElement(sub,i)
            track_id=me.getValue(mp.get(info,'track_id'))
            user_id=me.getValue(mp.get(info,'artist_id'))
            energy=me.getValue(mp.get(info,'energy'))
            dance=me.getValue(mp.get(info,'danceability'))
            print('Track',num,':',track_id,'con energia de',energy,'y danceability de',dance)
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

#****************************************REQ 3*********************************************************************
    elif int(inputs[0]) == 5:
        min_instrumentalness=float(0)
        max_instrumentalness=float(10)
        min_tempo=float(40)
        max_tempo=float(60)

        '''
        min_instrumentalness=float(input('Ingrese el valor mínimo para instrumentalness: '))
        max_instrumentalness=float(input('Ingrese el valor máximo para instrumentalness: '))
        min_tempo=float(input('Ingrese el valor mínimo para tempo: '))
        max_tempo=float(input('Ingrese el valor máximo para tempo: '))
        '''
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        funcion=controller.estudiar(cont,min_instrumentalness,max_instrumentalness,min_tempo,max_tempo)
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        
        #-------------------------------------------------
        
        total=funcion[1]
        sub=funcion[0]
        num=0
        print('Hay un total de canciones de:',total)
        for i in range(1,lt.size(sub)+1):
            num+=1
            info=lt.getElement(sub,i)
            track_id=me.getValue(mp.get(info,'track_id'))
            user_id=me.getValue(mp.get(info,'artist_id'))
            tempo=me.getValue(mp.get(info,'tempo'))
            instrumentalness=me.getValue(mp.get(info,'instrumentalness'))
            print('Track',num,':',track_id,'con tempo de',tempo,'y instrumentalness de',instrumentalness)
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)


#****************************************REQ 4*********************************************************************

    elif int(inputs[0]) == 6:
        inputs1=mostrar_opciones()
        diccionario={'reggae':(60,90),'down-tempo':(70,100),'chill-out':(90,120),'hip-hop':(85,115),'jazz and funk':(120,125),'pop':(100,130),'r&b':(60,80),'rock':(110,140),'metal':(100,160)}
        if inputs1=='1':
            generos=input('Ingrese la lista de generos separados por ",": ').split(',')
            funcion=controller.tracks_por_genero(cont,generos,diccionario)
        while inputs1=='2':
            nuevo=input('Ingrese el nombre del nuevo genero: ')
            min_nuevo=input('Ingrese el valor del tempo mínimo: ')
            max_nuevo=input('Ingrese el valor del tempo máximo: ')
            diccionario[nuevo]=(min_nuevo,max_nuevo)
            inputs1=mostrar_opciones()
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        for genero in generos:
            size_tracks=lt.size(me.getValue(mp.get(me.getValue(mp.get(funcion,genero)),'tracks')))
            size_artists=lt.size(me.getValue(mp.get(me.getValue(mp.get(funcion,genero)),'artists')))
            artists=lt.subList(me.getValue(mp.get(me.getValue(mp.get(funcion,genero)),'artists')),0,10)
            print('='*30,genero.upper(),'='*30)
            print('Para el genero',genero,'el tempo se encuentra entre',float(diccionario[genero][0]),'BPM y',float(diccionario[genero][1]),'BPM')
            print('Reproducciones:',size_tracks,'de',size_artists,'artistas')
            print('-'*50)
            for i in range(1,lt.size(artists)+1):
                print('Artista #',i,':',lt.getElement(artists,i))

        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        #-------------------------------------------------
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

#****************************************REQ 5*********************************************************************

    elif int(inputs[0]) == 7:
        hora_min=int('071500')
        hora_max=int('094500')
        '''
        hora_min=int(input('Ingrese el valor mínimo de hora: '))
        hora_max=int(input('Ingrese el valor máximo de hora: '))
        '''
        diccionario={'reggae':(60,90),'down-tempo':(70,100),'chill-out':(90,120),'hip-hop':(85,115),'jazz and funk':(120,125),'pop':(100,130),'r&b':(60,80),'rock':(110,140),'metal':(100,160)}
        #------------------------------------------------
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #***************************************
        funcion=controller.genero_por_tiempo(cont,diccionario,hora_min,hora_max)
        #**************************************
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        
        #-------------------------------------------------
        hora_min=horas(str(hora_min))
        hora_max=horas(str(hora_max))
        print('Hay un total de',funcion[1],'reproducciones entre',hora_min,'y',hora_max)
        print('='*30,'Generos y reproducciones','='*30)
        r=1
        for i in range(om.size(funcion[2])):
            reps=om.maxKey(funcion[2])
            genero=me.getValue(om.get(funcion[2],reps))
            print('TOP '+str(r)+':',genero,'con',reps,'reps')
            om.deleteMax(funcion[2])
            r+=1
        print('El genero con más reps es',funcion[3],'con',lt.size(me.getValue(mp.get(funcion[5],funcion[3]))),'reps...')
        print('='*30,funcion[3].upper(),'SENTIMENT ANALISIS','='*30)
        print(funcion[3],'tiene',funcion[4],'tracks unicos..')
        print('Los top',lt.size(funcion[0]),'tracks son:\n')
        r=1
        for i in range(1,lt.size(funcion[0])+1):
            track_id=lt.getElement(funcion[0],i)[0]
            vader=lt.getElement(funcion[0],i)[2]
            hashtags=lt.getElement(funcion[0],i)[1]
            print('TOP '+str(r)+' track:',track_id,'con',hashtags,'hahtags y VADER =',vader)
            r+=1
        print("\nTiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)

    else:
        sys.exit(0)
sys.exit(0)
