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
def mostrar_opciones():
    print('1-Consultar lista de generos\n2-Crear nuevo genero')
    return input('Ingrese la accion a realizar: ')
cont = None
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
        print("\nCargando información de tracks ....")
        controller.loadData(cont, filename)
        print('Eventos cargados: ' + str(controller.contador(cont)[0]))
        print('Tracks cargados: ' + str(controller.contador(cont)[1]))
        print('Artistas cargados: ' + str(controller.contador(cont)[2]))
        '''
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        '''
    
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
        
        funcion=controller.rep_car(cont,car,min_value,max_value)
        reps=funcion[0]
        artistas=funcion[1]
        print('*'*60)
        print('La característica',car,'está en el rango de',min_value,'a',max_value)
        print('Reproducciones:',reps)
        print('Artistas:',artistas)
        print('*'*60)
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
        
        funcion=controller.festejar(cont,min_energy,max_energy,min_danceability,max_danceability)
        total=lt.size(funcion)
        size=5
        if total<5:
            size=total
        sub=lt.subList(funcion,0,size)
        num=0
        print('Hay un total de canciones de:',total)
        for i in range(1,lt.size(sub)+1):
            num+=1
            info=lt.getElement(funcion,i)
            track_id=me.getValue(mp.get(info,'track_id'))
            user_id=me.getValue(mp.get(info,'user_id'))
            energy=me.getValue(mp.get(info,'energy'))
            dance=me.getValue(mp.get(info,'danceability'))
            print('Track',num,':',track_id,'con energia de',energy,'y danceability de',dance)
    elif int(inputs[0]) == 6:
        diccionario={'reggae':(60,90),'down-tempo':(70,100),
             'chill-out':(90,120),'hip-hop':(85,115),
             'jazz and funk':(120,125),'pop':(100,130),
             'r&b':(60,80),'rock':(110,140),
             'metal':(100,160)}
        inputs1=mostrar_opciones()
        if inputs1=='1':
            generos=input('Ingrese la lista de generos separados por ",": ').split(',')
            #'reggae,hip-hop,pop'
            funcion=controller.tracks_por_genero(cont,generos)
        while inputs1!='1':
            mostrar_opciones()
            nuevo=input('Ingrese el nombre del nuevo genero: ')
            min_nuevo=input('Ingrese el valor del tempo mínimo: ')
            max_nuevo=input('Ingrese el valor del tempo máximo: ')
            diccionario[nuevo]=(min_nuevo,max_nuevo)
        for i in range(1,lt.size(funcion)+1):
            mapa_genero=lt.getElement(funcion,i)
            genero=lt.firstElement(mp.keySet(mapa_genero))
            lista_tracks=me.getValue(mp.get(mapa_genero,genero))
            size=lt.size(lista_tracks)
            print('='*10,genero.upper(),'='*10)
            print(size)

    else:
        sys.exit(0)
sys.exit(0)
