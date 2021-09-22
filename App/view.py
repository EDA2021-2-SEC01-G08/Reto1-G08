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

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("0- Salir")

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

def printSortResults(ord_artworks, sample=10):
    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeras ", sample, " obras ordenadas son:")
        i = 1
        while i <= sample:
            artworks = lt.getElement(ord_artworks, i)
            print("Titulo: " + artworks["Title"] + " Dimensiones : " + 
            artworks["Dimensions"] + " Fecha de adquisición : " + artworks["DateAcquired"])
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
        pass

    elif int(inputs[0]) == 3:
        initialDate = input("Indique la fecha inicial en formato (AAAA-MM-DD): ")
        finalDate = input("Indique la fecha final en formato (AAAA-MM-DD): ")
        result = controller.filterDatesArtworks(catalog, initialDate, finalDate)
        """print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",
                                          str(result[0]))"""
        print("\nEl MoMA adquirió un total de ", str(result[0]), " obras entre ", initialDate, " y ", finalDate)
        print("El número total de obras adquiridas por -purchase- fue de ", str(result[1]))
        print("Las primeras y tres últimas obras dentro del rango son: ", str(result[2]))
    
    elif int(inputs[0]) == 4:
        ArtistName = input("Indique el nombre del artista a consultar: ")
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
            print("Título: ", element["Title"], " Fecha: ", element["Date"], " Medio: ", element["Medium"], " Dimensiones: "
            , element["Dimensions"])
            i += 1

    else:
        sys.exit(0)
sys.exit(0)

