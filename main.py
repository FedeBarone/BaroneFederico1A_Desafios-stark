from data_stark import lista_personajes
from heroes import *
from output import *
from informes import *
from busquedas import *
from calculos import *
from stark import *
import os
#===========================================FEDERICO BARONE 1A==========================================================
#ACLARACION: El desafio stark 02 esta en el modulo "stark_biblioteca". 
#tengo que pulir algunas funciones del stark 00 y 01, pero creo que en general esta todo bien
#El desafio 3/4 lo estoy haciendo
#===========================================================================================================================
#=======================================================Desafío Stark #00=================================================================
# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener
#=======================================================Desafío Stark #01=================================================================
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los
# superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los
# superhéroes de
# género F
# I.
# Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia

# for heroe in lista_personajes:
#     lista_personajes_copia.append(heroe.copy())#Para tener dos listas separadas y no tener que modificar la original.

lista_menu_principal_stark_00 = ["1- Mostrar nombre de cada superhéroe", 
                                "2- Mostrar nombre de cada superhéroe y su altura",
                                "3- Determinar el superhéroe más alto", "4- Determinar el superhéroe más bajo",
                                "5- Calcular altura promedio de los superhéroes", "6- Mostrar el superhéroe más alto",
                                "7- Mostrar el superhéroe más bajo", "8- Calcular e informar superhéroe más y menos pesado",
                                "9- Acceder sub menu stark 01", "10- Salir"]
lista_submenu_stark_01 = []
nombre_mas_alto = None
altura_mas_alto = None
nombre_mas_bajo = None
altura_mas_bajo = None

while True:
    os.system("cls")

    match mostrar_menu_principal(lista_menu_principal_stark_00):
        case '1':
            mostrar_nombre_de_cada_heroe(lista_personajes, "nombre", "Nombre")
        case '2':
            mostrar_nombre_altura_cada_heroe(lista_personajes, "nombre", "altura", "Nombre", "Altura")
        case '3':
            nombre_mas_alto, altura_mas_alto = determinar_el_heroe_mas_alto(lista_personajes, "nombre", "altura")
        case '4':
            nombre_mas_bajo , altura_mas_bajo = determinar_el_heroe_mas_bajo(lista_personajes, "nombre", "altura")
        case '5':
            calcular_altura_promedio_de_los_heroes(lista_personajes, "altura")
        case '6':
            if not nombre_mas_alto == None:
                mostrar_el_heroe_mas_alto(nombre_mas_alto, altura_mas_alto)
            else:
                print("Para mostrar, primero debe encontrar al heroe mas alto")
        case '7':
            if not nombre_mas_bajo == None:
                mostrar_el_heroe_mas_bajo(nombre_mas_bajo, altura_mas_bajo)
            else:
                print("Para mostrar, primero debe encontrar al heroe mas bajo")
        case '8':
            calcular_e_informar_heroe_mas_y_menos_pesado(lista_personajes, "nombre", "peso")
        case '9':
            ejecutar_opcion_sub_menu(lista_submenu_stark_01)
        case '10':
            salir = salir_del_menu()
            if salir == 's':
                break

    os.system("pause")
