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
    print("4- ")
    print("5- REQ. 3: Video con más días como tendencia")
    print("6- ")
    print("0- Salir")

def initCatalog(ltype):
    """
    Inicializa el catalogo de Videos
    """
    return controller.initCatalog(ltype)


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)
    

def printinga(ordlist,total): 
        for i in range(0,total):
            video=lt.getElement(ordlist,i)
            print ("Titulo: {0}\nChannel_title:{1}\ntrending_date: {2}\nCountry: {3}\nViews: {4}\n Likes:{5}\n Dislikes:{6}\n ".format(video['title'],video['channel_title'],video['trending_date'],video['country'],video['views'],video['likes'],video['dislikes']))
        
def printing(ordlist,total): 
        for i in range(1,total+1):
            video=lt.getElement(ordlist,i)
            print ("Titulo: {0}\ntrending_date: {1}\n Nombre del canal:{2}\n publish_time: {3}\n Views: {4}\n Likes:{5}\n Dislikes:{6}\n ".format(video['title'],video['trending_date'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes']) )


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
       
        print(' El primer video cargado es:')
        printinga(catalog['videos'],1)
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
        country=str(input("Ingrese el Pais de su eleccion:"))
        category=" " + (str(input("Ingrese la categoria de eleccion:")))
        number=int(input("Ingrese la cantidad de videos que quiere ver:"))
        result=controller.getVideosbyCat(catalog,country,category)
        printing(result,number)
    elif int(inputs[0]) == 4:
        print("")
    elif int(inputs[0]) == 5:
        category=" " + (str(input("Ingrese la categoria de eleccion:")))
        answer= controller.getTendencyTime(catalog,category)
        a="Title: {0}\nChannel_title:{1}\nCategory_id:{2}\nDays: {3} ".format(answer['title'],answer['channel_title'],answer['category_id'],answer['days'])
        print(a)
        
    elif int(inputs[0])==6:
        print("")
    else:
        sys.exit(0)
sys.exit(0)
 
