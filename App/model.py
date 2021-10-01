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
    catalog['artists'] = lt.newList("ARRAY_LIST"
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

def firstAndlastArtworks(catalog, filterlist):
    
    artworks = lt.newList()
    size = lt.size(filterlist)
    for artwork in range(0,3):
        element = (lt.getElement(filterlist, artwork))
        element["Artista(s)"] = getArtistsName(catalog, element["ConstituentID"])
        lt.addLast(artworks, element)

    for artwork in range(0,3):
        element = (lt.getElement(filterlist, size - artwork))
        element["Artista(s)"] = getArtistsName(catalog, element["ConstituentID"])
        lt.addLast(artworks, element)

    return artworks

def listChronoArtists(catalog, initialYear, finalYear):
    DataArtists = catalog["artists"]
    sorted(DataArtists, key=lambda Date: Date["BeginDate"])
    finalList = lt.newList()

    for artist in range(0, lt.size(DataArtists)):
        element = DataArtists.getElement(artist)
        if element["BeginDate"] >= initialYear or element["BeginDate"] <= finalYear:
            finalList.addFirst(element)
    
    TotalSize = finalList.size()
    firstThree = finalList[:3]
    LastOneThree = finalList[-3:]
    returnList = [firstThree]
    returnList.append(LastOneThree)

    return TotalSize, returnList

def strDateToInt(Date):

    """Convierte una fecha dada a int para comparación"""

    if Date != "":
        DateF = Date.split("-")
        Date1F = []
        for element in DateF:
            Date1F.append(int(element))
        
        Date_ = datetime.datetime(Date1F[0], Date1F[1], Date1F[2])
        
        return Date_
    return None

#Funciones de ordenamiento

def cmpArterokByDateAcquired(artwork1, artwork2):

    """Compara las fechas de adquisición para ordenarlas ascendentemente"""

    Result = True

    if artwork1["DateAcquired"] == "" or artwork2["DateAcquired"] == "":
        return False
    
    else:
        Date1 = strDateToInt(artwork1['DateAcquired'])
        Date2 = strDateToInt(artwork2['DateAcquired'])

    return Date1 < Date2

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

def cmpArterokByDate(artwork1, artwork2):
    
    Result = True

    if artwork1["Date"] == "" or artwork2["Date"] == "":
        return False
    
    else:
        Date1 =  artwork1['Date']
        Date2 = artwork2['Date']

    return Date1 < Date2

def sortArtworksByDate(catalog, size):
    sub_list = lt.subList(catalog['artworks'], 1, lt.size(catalog['artworks']))
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = mes.sort(sub_list, cmpArterokByDate)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return elapsed_time_mseg, sorted_list

def cmpArterokByCost(artwork1, artwork2):
    
    if artwork1['elementCost'] == None or artwork2['elementCost'] == None:
        print(artwork1)
    Cost1 =  artwork1['elementCost']
    Cost2 = artwork2['elementCost']

    return Cost1 > Cost2

def getArtistsName(catalog, constituentID):
    
    listconstituentID = constituentID[1:len(constituentID) - 1].split(", ")
    listconstituentIDn = lt.newList()
    for element in listconstituentID:
        lt.addLast(listconstituentIDn, element)
    i = 0
    j = 0
    artistNames = ""
    artistList = catalog["artists"]
    while i < lt.size(listconstituentIDn):
        element = lt.getElement(listconstituentIDn, i)
        if element == "-1":
            return "Anónimo"
        while j < lt.size(artistList):
            artist = lt.getElement(artistList, j)
            if element == artist["ConstituentID"]:
                artistNames += artist["DisplayName"] + " , "
                break
            j += 1
        i += 1
    
    return artistNames

def filterDatesArtworks(catalog, InitialDate, FinalDate):
    
    result = sortArtworks(catalog, lt.size(catalog["artworks"]), 3)
    filterListDate = lt.newList()
    i=0
    while i < lt.size(result[1]):
        element = lt.getElement(result[1],i)
        dateAcquired = strDateToInt(element['DateAcquired'])
        if dateAcquired != None and dateAcquired >= strDateToInt(InitialDate) and dateAcquired <= strDateToInt(FinalDate):
            lt.addLast(filterListDate,element)
        i = i + 1

    filterListPurchase = lt.newList()
    i=0
    while i < lt.size(filterListDate):
        element = lt.getElement(filterListDate,i)
        creditLine = element['CreditLine']
        if creditLine == "Purchase":
            lt.addLast(filterListPurchase,element)
        i = i + 1

    sizeFilterListDate = lt.size(filterListDate)
    sizeFilterListPurchase = lt.size(filterListPurchase)
    firstandlast = firstAndlastArtworks(catalog, filterListPurchase)

    return sizeFilterListDate, sizeFilterListPurchase, firstandlast

def filterTechnicArtists(catalog, ArtistName):

    filterListArtist = lt.newList()
    mediumList = lt.newList()
    newmedium = {}
    i = 0
    dataArtist = catalog["artists"]
    dataArtwork = catalog["artworks"]
    while i < lt.size(dataArtist):
        element = lt.getElement(dataArtist, i)
        artist = element["DisplayName"]
        if artist.lower() == ArtistName.lower():
            artistID = element["ConstituentID"]
            lt.addLast(filterListArtist, element)
        i = i + 1
    
    i = 0
    while i < lt.size(dataArtwork):
        element = lt.getElement(dataArtwork, i)
        artworkID = element["ConstituentID"] 
        if artistID in artworkID:
            medium = element["Medium"]
            if medium in newmedium:
                artworkmed = newmedium[medium]
                lt.addLast(artworkmed, element)
                newmedium[medium] = artworkmed
            else:
                artworkmed = lt.newList()
                lt.addLast(artworkmed, element)
                newmedium[medium] = artworkmed
                lt.addLast(mediumList, element)
        i = i + 1

    totalArtworks = 0
    mostTimes = 0
    for medium in newmedium:
        actual = lt.size(newmedium[medium])
        totalArtworks += actual
        if actual > mostTimes:
            mostTimes = actual
            granMedium = medium

    totalMediums = lt.size(mediumList)

    return totalArtworks, totalMediums, granMedium, mostTimes, newmedium

def transportArtworks(catalog, department):

    result = sortArtworksByDate(catalog, lt.size(catalog["artworks"]))
    listCost = lt.newList()

    filterListDept = lt.newList()
    i=0
    while i < lt.size(result[1]):
        element = lt.getElement(result[1],i)
        departmenti = element['Department']
        if departmenti.lower() == department.lower():
            lt.addLast(filterListDept,element)
        i = i + 1

    totalCost = 0
    totalWeight = 0
    i=0
    while i <= lt.size(filterListDept):
        element = lt.getElement(filterListDept,i)
        weight = element['Weight (kg)']
        height = element["Height (cm)"]
        lenght = element["Length (cm)"]
        width = element["Width (cm)"]
        if weight == "":
            kg = 0
            if height != "" and width != "":
                if lenght != "":
                    m3 = (float(height) * float(width) * float(lenght)) * 72
                else:
                    m2 = (float(height) * float(width)) * 72
                    m3 = 0
            else:
                m2 = 0
        else:
            kg = float(weight)
            totalWeight += kg
        sumx = kg + m2 + m3
        elementCost = 0
        if sumx != 0:
            elementCost = max(kg, m2, m3)
        else:
            elementCost = 48
        totalCost += elementCost
        element["elementCost"] = elementCost
        lt.addLast(listCost, element)
        i = i + 1

    sizeFilterListDept = lt.size(filterListDept)
    listByCost = mes.sort(listCost, cmpArterokByCost)

    return sizeFilterListDept, totalCost, totalWeight, filterListDept, listByCost












