from data_stark import lista_personajes
from output import*
from busquedas import *
from calculos import *
import os

def calcular_promedio_lista(lista:list, key:str)->float:
    """_summary_
    Calcula el promedio de un campo determinado en una lista de diccionarios

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista a acumular

    Returns:
        float: resultado de la division
    """
    acumulador = 0
    contador = 0
    if type(lista) == list and len(lista) > 0:
        for elemento in lista:
            acumulador += float(elemento[key])
            contador = contador + 1
        return acumulador / contador
    else:
        return -1

def contar_tipo_de_dato(lista: list, keys: list, values: list)-> dict:
    """_summary_
    Declara un contador de tipo diccionario que recorre los valores, los agrega al mismo e inicializa en 0. Luego recorre los heroes y
    por cada heroe se recorre la lista de keys que contienen los valores. A lo ultimo verifica si la key del heroe esta en el diccionario, y
    si es asi acumula los valores.

    Args:
        lista (list): lista a recorrer
        keys (list): lista a recorrer
        values (list): lista a recorrer

    Returns:
        _type_(dict): la cantidad de cada valor
    """
    contador = {}
    for value in values:
        contador[value] = 0

    for heroe in lista:
        for key in keys:
            print(key)
            print(keys[key])
            if heroe[key] in contador:
                contador[heroe[key]] += 1
    return contador



