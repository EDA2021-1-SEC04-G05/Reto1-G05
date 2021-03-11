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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as sels
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.DataStructures import listiterator as lit
assert cf
import time
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(ltype):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
                'countries':None,
               'categories': None}
    if ltype==2: 
        print("Usted escogio: SINGLE_LINKED")
        catalog['videos'] = lt.newList('SINGLE_LINKED',cmpfunction=None)#compareViews)
        catalog['countries']=lt.newList('SINGLE_LINKED',compareCountries) 
        catalog['categories'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=None)
    elif ltype==1: 
        print("Usted escogio: ARRAY_LIST")
        catalog['videos'] = lt.newList('ARRAY_LIST', compareViews)
        catalog['countries']=lt.newList('ARRAY_LIST',compareCountries) 
        catalog['categories'] = lt.newList('ARRAY_LIST')
 
    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    countryname=video['country']
    addVideoCountry(catalog,countryname, video)

def addVideoCountry(catalog, countryname, video):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    countries = catalog['countries']
    pos = lt.isPresent(countries, countryname)
    if pos > 0:
        country = lt.getElement(countries, pos)
    else:
        country = newCountry(countryname)
        lt.addLast(countries, country)
    lt.addLast(country['videos'], video)    
    
# Funciones para creacion de datos
def newCountry(countryname):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    country = {'name': "", "videos": None}
    country['name'] = countryname
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def addCat(catalog, category):
    """
    Adiciona una categoria a la lista de categorias
    """
    lt.addLast(catalog['categories'], category)
    

def newCat(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat


# Funciones de consulta

def getVideosByCountry(catalog, country):
    """
    Retorna un pais con sus videos a partir del nombre del pais
    """
    pos = lt.isPresent(catalog['countries'], country)
    if pos > 0:
        country1 = lt.getElement(catalog['countries'], pos)
        return country1

def getCat(catalog,category):
    cat_id=0
    b=lit.newIterator(catalog['categories'])
    while lit.hasNext(b):
        a=lit.next(b)
        if a['name']==str(category):
            cat_id=a['id ']
            return cat_id
    if cat_id == 0:
        print("esta categoria no existe")
        return cat_id

def getVideosbyCat(catalog,countryname,category):
    country=getVideosByCountry(catalog,countryname)
    result=lt.newList('ARRAY_LIST',compareViews)
    cat_id=getCat(catalog,category)
    countrysize=lt.size(country['videos'])
    if cat_id != 0:
        for i in range (1,countrysize):
            video=lt.getElement(country['videos'],i)
            if video["category_id"]==cat_id: 
                lt.addLast(result, video)
    re=sortVideos(result)
    return re

def getTendencyTime(catalog,category):
    cat=getCat(catalog,category)
    lis= lt.newList('ARRAY_LIST')
    b=lit.newIterator(catalog['videos'])
    while lit.hasNext(b):
        video=lit.next(b)
        if video["category_id"]==cat: 
            lt.addLast(lis, video)
            
    a=lit.newIterator(lis)
    l=lt.newList("ARRAY_LIST",compareName)
    x=lt.newList("ARRAY_LIST")
    while lit.hasNext(a):
        e=lit.next(a)
        dic={}
        r =lt.isPresent(l,e['title'])
        if r == 0: 
            dic['title']=e['title']
            dic['channel_title']=e['channel_title']
            dic['category_id']=e['category_id']
            dic['days']=1
            lt.addLast(x,dic)
            lt.addLast(l,e['title'])
            
        else:
            dic=lt.getElement(x,r)
            dic['days']+=1
    dic_sort=sortDays(x)
    #print(lt.getElement(dic_sort,1))
    return lt.getElement(dic_sort,1)

def Req2 (catalog, country):
    """
    Se ordena la lista de videos con mergesort por pais
    """
    OrdenarPorPais= ms.sort (catalog ['videos'], compareVideosCountries)
    
    """
    Se busca si la ciudad entrada por parametro se encuentra en la lista
    """

    inicio = 1
    while country not in lt.getElement(OrdenarPorPais, inicio)['country'] :
        inicio += 1
    fin = inicio
    while country == lt.getElement(OrdenarPorPais, fin)['country'] :
        fin += 1
        if fin > lt.size(OrdenarPorPais):
            break
    
    """
    Se ordena la lista de videos con mergesort por nombre
    """
    sub_list = lt.subList(OrdenarPorPais, inicio, fin-inicio)
    OrdenarPorNombre = ms.sort (sub_list, compareVideosCountries)

    """
    Se crea un contador para saber cuantas veces el video aparece 
    """
    name = ""
    max_index = 0
    max_contador = 0
    contador = 0
    index = 0
    i = 1

    """
    Se aumenta el contador para obtener las veces que el video esta en trending y se comparan los nombres
    """

    while i <= lt.size(OrdenarPorNombre):
        if name.lower() == lt.getElement(OrdenarPorNombre, i)['title']:
            contador += 1
        else:
            name = lt.getElement(OrdenarPorNombre, i)['title']
            index = i
            contador = 1
        if contador > max_contador:
            max_index = index
            max_contador = contador
        i += 1
    
    """
    Se retorna la pelicula con el contador 
    """

    return [lt.getElement(OrdenarPorNombre, max_index), max_contador]

def Req4(catalog, country, numeroDeTop, tag):

    OrdenarPorPais= ms.sort (catalog ['videos'], compareVideosCountries)

    inicio = 1
    while country not in lt.getElement(OrdenarPorPais, inicio)['country'] :
        inicio += 1
    fin = inicio
    while country == lt.getElement(OrdenarPorPais, fin)['country'] :
        fin += 1
        if fin > lt.size(OrdenarPorPais):
            break
    
     
    sub_list = lt.subList(OrdenarPorPais, inicio, fin-inicio)
    OrdenarPorTag = ms.sort (sub_list, compareVideosCountries)

    max_index = 0
    max_contador = 0
    contador = 0
    index = 0
    i = 1
    listaDeVideos= lt.newList("ARRAY_LIST")
    

    while i <= numeroDeTop:
        if tag == lt.getElement(OrdenarPorNombre, i)['tag']:
            listaDeVideos.addLast(lt.getElement((OrdenarPorNombre, i)))
        else:
            index = i
        i += 1
    
 

    return [listaDeVideos]

    

    


    
# Funciones utilizadas para comparar elementos dentro de una lista
def compareViews (video1,video2):
    return (float(video1['views']) > float(video2['views']))

def compareCountries(countryname, country):
    if (countryname.lower() in country['name'].lower()):
        return 0
    return -1

def compareVideosCountries(video1, video2):
    if video1['country'].lower() > video2['country'].lower():
        return True
    return False 

def compareNames(video1, video2):
    if (video1['title'].lower() > video2['title'].lower()):
        return True
    return False
def compareName(video1,video2):
    if ((video1) == (video2)): 
        return 0
    elif ((video1) > (video2)): 
        return 1
    else: 
        return -1
def compareDays (video1,video2):
    return (float(video1['days']) > float(video2['days']))
# Funciones de ordenamiento

def sortVideos(catalog, size,tsort):
    sub_list = lt.subList(catalog['videos'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if tsort==1:
        sorted_list = ss.sort(sub_list, compareViews)
    elif tsort==2:
        sorted_list = ins.sort(sub_list, compareViews)
    elif tsort==3:
        sorted_list = sels.sort(sub_list, compareViews)
    elif tsort==4:
        sorted_list = qs.sort(sub_list, compareViews)
    elif tsort==5:
        sorted_list = ms.sort(sub_list, compareViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

def sortVideos(catalog):
    sub_list = catalog.copy()
    sorted_list = qs.sort(sub_list, compareViews)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list
def sortDays(catalog):
    sub_list = catalog.copy()
    sorted_list = qs.sort(sub_list, compareDays)
    #stop_time = time.process_time()
    #elapsed_time_mseg = (stop_time - start_time)*1000
    return sorted_list



