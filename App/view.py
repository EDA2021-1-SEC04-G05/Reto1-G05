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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
default_limit=1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos ordenados por views")
    print("3- REQ. 1: Encontrar buenos videos por categoría y país")
    print("4- REQ. 2: Encontrar video tendencia por país")
    print("5- ")
    print("6- REQ. 4: Encontrar vidoes con mas likes")
    print("0- Salir")

def initCatalog(ltype):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(ltype)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)
    
def printing(ordlist,sample=10): 
        for i in range(0,10):
            video=lt.getElement(ordlist,i)
            print ("Titulo: {0} Views: {1} ".format(video['title'],video['views']) )


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        listype=int(input(("Seleccione el tipo de lista para cargar los datos: \n 1- ARRAY_LIST \n 2-LINKED_LIST \n")))
        print("Cargando información de los archivos ....")
        catalog = initCatalog(listype)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(catalog['categories']))
    elif int(inputs[0]) == 2:
        
        size =int( input("Indique tamaño de la muestra: "))
        stype= int(input (("Seleccione el tipo de sorting para cargar los datos: \n 1- Shellsort \n 2-Insertionsort \n 3-Selectionsort \n 4-Quicksort \n 5-Mergesort \n")))
        result = controller.sortVideos(catalog, int(size),int(stype))
        print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))
        printing(result[1],size)
    elif int(inputs[0]) == 3:
        print (a)
    elif int(inputs[0]) == 4:
        country = input ("Ingrese el país para el cual desea realizar la consulta: ")
        [result, count] = controller.Req2(catalog, country)
        video = result
        print( "Titulo: "+ video['title'] + " | Canal: " + video['channel_title'] + " | Ciudad: " + video['country'] + " | Días: "+ str(count))
        print("")
    elif int(inputs[0]) == 5:
        print("")
    elif int(inputs[0])==6:
        country = input ("Ingrese el país para el cual desea realizar la consulta: ")
        numeroDeTop = input ("Ingrese el numero de videos a enlistar: ")
        tag = input ("Ingrese el tag de los videos: ")
        [result] = controller.Req4(catalog, country, numeroDeTop, tag)
        video = result 
        print("Titulo: "+ video['title'] + " | Canal: "+ video['channel_title'] + " | Dia de publicación: "+ video['views'] + " | Likes: "+ video['likes'] + " | Dislikes: "+ video['dislikes'] + " | Tags: "+ video['tags'])
        print("")
    else:
        sys.exit(0)
sys.exit(0)
 
