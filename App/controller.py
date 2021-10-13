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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los artistas del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga los artistas del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artworksfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

# Funciones de ordenamiento
def filterDatesArtworks(catalog, InitialDate, FinalDate):
    """
    Ordena las obras por fecha de adquisición
    """
    return model.filterDatesArtworks(catalog, InitialDate, FinalDate)

def listChronArtists(catalog, InitialDate, FinalDate):
    
    return model.listChronoArtists(catalog, InitialDate, FinalDate)

def filterTechnicArtists(catalog, ArtistName):

    return model.filterTechnicArtists(catalog, ArtistName)

def transportArtworks(catalog, department):

    return model.transportArtworks(catalog, department)

# Funciones de consulta sobre el catálogo


def lastArtists(catalog):
    
    return model.lastArtists(catalog)

def lastArtworks(catalog):
    
    return model.lastArtworks(catalog)

def getArtistsName(catalog, constituentID):

    return model.getArtistsName(catalog, constituentID)

def sortByBirth(catalog, year0, year1):
    artists = catalog["artists"]

    return model.sortByBirth(artists, year0, year1)

def sortArtworksByAcquiredDate(filtredArtworks):
    """
    Ordena las obras por la fecha en la que fueron adquiridas.
    """

    return model.sortArtworksByAcquiredDate(filtredArtworks)

def filterByDate(catalog, date0, date1):
    artworks = catalog["artworks"]

    return model.filterByDate(artworks, date0, date1)



