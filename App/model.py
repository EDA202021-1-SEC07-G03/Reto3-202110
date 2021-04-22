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
from DISClib.ADT import map as m
import datetime
assert config
# Construccion de modelos
def newAnalyzer():
    analyzer = {'tracks': None,'context':None}
    analyzer['tracks'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['context'] = om.newMap(omaptype='BST',comparefunction=compareDates)
    return analyzer
# Funciones para agregar informacion al catalogo
def add(analyzer, track):
    lt.addLast(analyzer['tracks'], track)
    updatecontext(analyzer['context'], track)
    return analyzer
def updatecontext(map, track):
    occurreddate = track['created_at']
    created = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, created.date())
    if entry is None:
        datentry = newDataEntry(track)
        om.put(map, created.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, track)
    return map
def newDataEntry(track):
    entry = {'offenseIndex': None, 'lstcrimes': None}
    entry['offenseIndex'] = m.newMap(numelements=30,maptype='PROBING',comparefunction=compareOffenses)
    entry['lstcrimes'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry
def addDateIndex(datentry, crime):
    lst = datentry['lstcrimes']
    lt.addLast(lst, crime)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, crime['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        entry = newOffenseEntry(crime['OFFENSE_CODE_GROUP'], crime)
        lt.addLast(entry['lstoffenses'], crime)
        m.put(offenseIndex, crime['OFFENSE_CODE_GROUP'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], crime)
    return datentry

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1