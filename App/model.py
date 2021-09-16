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


import config as cf
import time 
import datetime
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mes
from DISClib.Algorithms.Sorting import quicksort as quis
assert cf


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'artists': None,
               }

    catalog['artworks'] = lt.newList()
    catalog['artists'] = lt.newList("LINKED_LIST"
                                    )
    

    return catalog

# Funciones para agregar informacion al catalogo

def addArtwork(catalog, artwork):
    
    lt.addLast(catalog['artworks'], artwork)
    
def addArtist(catalog, artistname):
    lt.addLast(catalog['artists'], artistname)
    
# Funciones para creacion de datos

def newArtist(name):
    
    artist = {'name': ""}
    artist['name'] = name
    
    return artist

def newArtwork(name):
    
    artwork = {'artwork': ""}
    artwork['artwork'] = name
    
    return artwork

# Funciones de consulta

def lastArtists(catalog):
    
    artists = ""
    size = lt.size(catalog["artists"])
    for artist in range(0,3):
        artists += str((lt.getElement(catalog["artists"], size - artist)))

    return artists

def lastArtworks(catalog):
    
    artworks = ""
    size = lt.size(catalog["artworks"])
    for artwork in range(0,3):
        artworks += str((lt.getElement(catalog["artworks"], size - artwork)))

    return artworks

"""
def listChronoArtists(catalog, initialYear, finalYear):

    totalArtists = 0
    FirstsLastsA = lt.newList("ARRAY_LIST")
    DataArtists = catalog["artists"]

    for artist in range(0, lt.size(DataArtists)):
        element = DataArtists.getElement(artist)
        if element >= initialYear or element <= finalYear:
"""

def cmpArterokByDateAcquired(artwork1, artwork2):

    Result = True

    if artwork1["DateAcquired"] == "" or artwork2["DateAcquired"] == "":
        return False
    
    else:
        Date1 = artwork1['DateAcquired'].split("-")
        Date2 = artwork2['DateAcquired'].split("-")
        Date1F = []
        Date2F = []

        for element in Date1:
            Date1F.append(int(element))
    
        for element in Date2:
            Date2F.append(int(element))

        Date1_ = datetime.datetime(Date1F[0], Date1F[1], Date1F[2])
        Date2_ = datetime.datetime(Date2F[0], Date2F[1], Date2F[2])

    return Date1_ < Date2_

def sortArtworks(catalog, size, sortingtype):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if sortingtype == 1:
        sorted_list = sa.sort(sub_list, cmpArterokByDateAcquired)
    elif sortingtype == 2:
        sorted_list = ins.sort(sub_list, cmpArterokByDateAcquired)
    elif sortingtype == 3:
        sorted_list = mes.sort(sub_list, cmpArterokByDateAcquired)
    elif sortingtype == 4:
        sorted_list = quis.sort(sub_list, cmpArterokByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, sorted_list







