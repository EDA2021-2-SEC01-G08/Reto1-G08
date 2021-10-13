﻿"""
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
import time 
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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Transportar obras de un departamento")
    print("0- Salir")

def isDead(Date):
    if Date == "0":
        retorno = "Sigue con vida (o no se sabe la fecha de su muerte)."
    else:
        retorno = Date
    return retorno

def printSortedArtists(ord_artists, sample=3):
    size = lt.size(ord_artists)
    if size == 0:
        print("\nNo se encontraron obras adquiridas dentro del rango ingresado.\n")
    elif size > sample:
        print("\nEl número de artistas que nacieron entre esos años es de ", size ," artistas.")
        print("\nLas primeras ", sample, " obras ordenadas son:")
        i=1
        while i <= sample:
            artist = lt.getElement(ord_artists,i)
            print('\nNombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' + artist['BeginDate'] + ', Año de fallecimiento: ' + isDead(artist['EndDate']) + ', Nacionalidad: ' + artist['Nationality'] + ", Género: " + artist["Gender"])
            i+=1
        print("\nLas últimas ", sample, " obras ordenadas son:")
        j=size-(sample-1)
        k=1
        while k <= sample:
            artist = lt.getElement(ord_artists,j)
            print('\nNombre: ' + artist['DisplayName'] + ', Año de nacimiento: ' + artist['BeginDate'] + ', Año de fallecimiento: ' + isDead(artist['EndDate']) + ', Nacionalidad: ' + artist['Nationality'] + ", Género: " + artist["Gender"])
            j+=1
            k+=1

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def lastArtists(catalog):

    return controller.lastArtists(catalog)

def lastArtworks(catalog):
    
    return controller.lastArtworks(catalog)

def getArtistsName(catalog, constituentID):
    
    return controller.getArtistsName(catalog, constituentID)

def printSortResults(ord_artworks, sample=10):
    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeras ", sample, " obras ordenadas son: ")
        i = 1
        while i <= sample:
            artworks = lt.getElement(ord_artworks, i)
            print("Titulo: " + artworks["Title"] + " Dimensiones : " + 
            artworks["Dimensions"] + " Fecha de adquisición : " + artworks["DateAcquired"])
            i += 1

def printFirstFive(listA):
    i = 1
    while i <= 5:
        elementA = lt.getElement(listA, i)
        constituentID = elementA["ConstituentID"]
        artistName = getArtistsName(catalog, constituentID)
        print("Título: ", elementA["Title"], ", Artista(s): ", artistName, ", Fecha: ", elementA["Date"], ", Medio: ", elementA["Medium"], ", Dimensiones: "
        , elementA["Dimensions"], ", Clasificación: ", elementA["Classification"], ", Costo: ",  elementA["elementCost"])
        i += 1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        lastArtists_ = lastArtists(catalog)
        lastArtworks_ = lastArtworks(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        print("Últimos tres artistas cargados: " + str(lastArtists_))
        print("Últimas tres obras cargados: " + str(lastArtworks_))

    elif int(inputs[0]) == 2:
        year0 = input("Ingrese el año inicial\n")
        year1 = input("Ingrese el año final\n")

        sortedArtists = controller.sortByBirth(catalog, year0, year1)

        print("La operación tardó ", sortedArtists[1], " milisegundos.")
        printSortedArtists(sortedArtists[0])

    elif int(inputs[0]) == 3:
        date0 = input("Ingrese la fecha desde la cual filtrar (en forma AAAA-MM-DD): ")
        date1 = input("Ingrese la fecha hasta la cual filtrar (en forma AAAA-MM-DD): ")
        filtredArtworks = controller.filterByDate(catalog, date0, date1)
        result = controller.sortArtworksByAcquiredDate(filtredArtworks)
        print("La operación tardó: ", result[0], " milisegundos.")
        printSortResults(result[1])

    elif int(inputs[0]) == 4:
        ArtistName = input("Indique el nombre del artista a consultar: ")
        start_time = time.process_time()
        result = controller.filterTechnicArtists(catalog, ArtistName)
        dictT = result[4]
        listT = dictT[result[2]]
        print(ArtistName, " tiene un total de ", str(result[0]), " obras dentro del museo.")
        print("Existe un total de ", str(result[1]), " de medios utilizados en sus obras.")
        print("El medio más utilizado fue: ", str(result[2]), " con ", str(result[3]), " piezas. ")
        print("El listado de obras de dicha técnica es: ")
        i = 1
        while i <= lt.size(listT):
            element = lt.getElement(listT, i)
            print("Título: ", element["Title"], ", Fecha: ", element["Date"], ", Medio: ", element["Medium"], ", Dimensiones: "
            , element["Dimensions"])
            i += 1
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("El tiempo en mseg es: ", str(elapsed_time_mseg))
        
    elif int(inputs[0]) == 5:
        department = input("Indique el nombre del departamento a consultar: ")
        start_time = time.process_time()
        result = controller.transportArtworks(catalog, department)
        listA = result[3]
        listC = result[4]
        print("El total de obras para transportar de ", department, " es de: ", result[0])
        print("El costo estimado en USD es de: ", str(result[1]))
        print("EL peso estimado en Kg es de: ", str(result[2]))
        print("Los 5 items más antiguos para transportar son: ")
        printFirstFive(listA)
        print("-------------------------------------------------")
        print("Los 5 items más costosos para transportar son: ")
        printFirstFive(listC)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        print("El tiempo en mseg es: ", str(elapsed_time_mseg))
        

    else:
        sys.exit(0)
sys.exit(0)


