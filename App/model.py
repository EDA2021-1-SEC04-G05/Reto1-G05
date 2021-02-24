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
assert cf
import time

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
               'categories': None}
    if ltype==2: 
        print("2")
        catalog['videos'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=None)
        catalog['categories'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=None)
    elif ltype==1: 
        print("1")
        catalog['videos'] = lt.newList('ARRAY_LIST')
        catalog['categories'] = lt.newList('ARRAY_LIST')
 

    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    
  
def addCat(catalog, category):
    """
    Adiciona una categoria a la lista de categorias
    """
    lt.addLast(catalog['categories'], category)
    
 

# Funciones para creacion de datos
def newCat(name, id):
    """
    Esta estructura almancena los tags utilizados para marcar libros.
    """
    cat = {'name': '', 'id': ''}
    cat['name'] = name
    cat['id'] = id
    return cat


# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def compareViews (video1,video2):
    return (float(video1['views']) < float(video2['views']))

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
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list
