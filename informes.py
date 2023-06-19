from data_stark import lista_personajes
from heroes import *
from busquedas import *
from calculos import calcular_promedio_lista, contar_tipo_de_dato, contar_tipo_de_dato
import os
#=======================================================INFORMES STARK 00===============================================================#
def mostrar_nombre_de_cada_heroe(lista:list, key:str, title:str)->None:#B
    """_summary_
    Muestra los nombres de una lista de heroes

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        title (str): titulo de la lista
    """
    if type(lista) == list and type(key) == str and type(title) == str:
        mostrar_lista(proyectar_heroe(lista_personajes, key), title)

def mostrar_nombre_altura_cada_heroe(lista:list, key:str, key_dos:str, title:str, title_dos:str)->None:#C
    """_summary_
    Muestra los nombres y las alturas de una lista de heroes

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        title (str): titulo de la lista
    """
    if type(lista) == list and type(key) == str and type(title) == str and type(title_dos) == str:
        lista_principal, lista_filtrada = proyectar_heroe_doble(lista, key, key_dos)
        mostrar_listas(lista_principal, lista_filtrada,  title, title_dos)

def determinar_el_heroe_mas_alto(lista, key, key_dos)->tuple:#D
    """_summary_
    Invoca a la funcion que se encarga de buscar al heroe mas bajo de la lista

    Args:
        lista (_type_): lista a recorrer
        key (_type_): campo de la lista
        key_dos (_type_): campo de la lista

    Returns:
        tuple: devuelve la altura y el nombre del heroe mas alto
    """
    if type(lista) == list and type(key) == str and type(key_dos) == str:
        print("Heroe mas alto encontrado!")
        return buscar_valor_maximo_lista(lista, key, key_dos)
    

def determinar_el_heroe_mas_bajo(lista, key, key_dos)->tuple:#E
    """_summary_
    Invoca a la funcion que se encarga de buscar al heroe mas bajo de la lista

    Args:
        lista (_type_): lista a recorrer
        key (_type_): campo de la lista
        key_dos (_type_): campo de la lista

    Returns:
        tuple: devuelve la altura y el nombre del heroe mas bajo
    """
    if type(lista) == list and type(key) == str and type(key_dos) == str:
        print("Heroe mas bajo encontrado!")
        return buscar_valor_minimo_lista(lista, key, key_dos)

def calcular_altura_promedio_de_los_heroes(lista:list, key:str)->float:#F
    """_summary_
    Invoca a la funcion que calcula la altura promedio de los heroes de la lista

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista

    Returns:
        float: _description_
    """
    if type(lista) == list and type(key) == str:
        print("Promedio de alturas calculado!")
        return calcular_promedio_lista(lista, key)
    
def mostrar_el_heroe_mas_alto(nombre_max:str, altura_max:float)->None:#G
    """_summary_
    Muestra el nombre y la altura del heroe mas alto

    Args:
        nombre_max (str): nombre del heroe mas alto
        altura_max (float): altura del heroe mas alto
    """
    print(f"El nombre del heroe mas alto es {nombre_max} con una altura de {altura_max}")

def mostrar_el_heroe_mas_bajo(nombre_min:str, altura_min:float)->None:#H
    """_summary_
    Muestra el nombre y la altura del heroe mas bajo

    Args:
        nombre_max (str): _description_
        altura_max (float): _description_
    """
    print(f"El nombre del heroe mas bajo es {nombre_min} con una altura de {altura_min}")

def determinar_el_heroe_mas_pesado(lista: list, key:str, key_dos:str)->tuple:#I
    """_summary_
    Invoca una funcion para que encuentre al heroe mas pesado

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        key_dos (str): campo de la lista

    Returns:
        tuple: el nombre y la altura del heroe mas pesado
    """
    if type(lista) == list and type(key) == str and type(key_dos) == str:
        print("Heroe mas pesado encontrado!")
        return buscar_valor_maximo_lista(lista, key, key_dos)

def determinar_el_heroe_menos_pesado(lista, key, key_dos)->tuple:#I
    """_summary_
    Invoca una funcion para que encuentre al heroe menos pesado

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        key_dos (str): campo de la lista

    Returns:
        tuple: el nombre y la altura del heroe menos pesado
    """
    if type(lista) == list and type(key) == str and type(key_dos) == str:
        print("Heroe menos pesado encontrado!")
        return buscar_valor_minimo_lista(lista, key, key_dos)

def calcular_e_informar_heroe_mas_y_menos_pesado(lista, key, key_dos)->None:#I
    """_summary_
    Invoca la funcion que encuentra a los heroes mas y menos pesados y los muestra

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        key_dos (str): campo de la lista
    """
    print(determinar_el_heroe_mas_pesado(lista, key, key_dos))
    print(determinar_el_heroe_menos_pesado(lista, key, key_dos))

#=====================================================INFORMES STARK 01=================================================================#
def imprimir_heroes_genero_m(lista:list, key:str, value:str, key_dos:str, title:str)->None:#A
    """_summary_
    Filtra los heroes de genero masculino, proyecta sus nombres y los muestra
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
        title (str): titulo de la lista
    """
    lista_filtrada = filtrar_heroes_atributo(lista, key, value)
    lista_proyectada = proyectar_heroe(lista_filtrada, key_dos)
    mostrar_lista(lista_proyectada, title)

def imprimir_heroes_genero_f(lista:list, key:str, value:str, key_dos:str, title:str)->None:#B
    """_summary_
    Filtra los heroes de genero femenino, proyecta sus nombres y los muestra
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
        title (str): titulo de la lista
    """
    lista_filtrada = filtrar_heroes_atributo(lista, key, value)
    lista_proyectada = proyectar_heroe(lista_filtrada, key_dos)
    mostrar_lista(lista_proyectada, title)

def determinar_heroe_mas_alto_genero_m(lista, key, value, key_tres, key_cuatro):#C
    """_summary_
    Filtra los heroes de genero masculino y se los pasa a la funcion que busca al heroe mas alto de la lista
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_masculinos = filtrar_heroes_atributo(lista, key, value)
    print("Heroe mas alto genero m encontrado")
    return buscar_valor_maximo_lista(lista_filtrada_masculinos, key_tres, key_cuatro)
    
def determinar_heroe_mas_alto_genero_f(lista, key, value, key_tres, key_cuatro):#D
    """_summary_
    Filtra los heroes de genero femenino y se los pasa a la funcion que busca al heroe mas alto de la lista
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_femeninos = filtrar_heroes_atributo(lista, key, value)
    print("Heroe mas alto genero f encontrado")
    return buscar_valor_maximo_lista(lista_filtrada_femeninos, key_tres, key_cuatro)
    
def determinar_heroe_mas_bajo_genero_m(lista, key, value, key_tres, key_cuatro):#E
    """_summary_
    Filtra los heroes de genero masculino y se los pasa a la funcion que busca al heroe mas bajo de la lista
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_masculinos = filtrar_heroes_atributo(lista, key, value)
    print("Heroe mas bajo genero m encontrado")
    return buscar_valor_minimo_lista(lista_filtrada_masculinos, key_tres, key_cuatro)

def determinar_heroe_mas_bajo_genero_f(lista, key, value, key_tres, key_cuatro):#F
    """_summary_
    Filtra los heroes de genero femenino y se los pasa a la funcion que busca al heroe mas bajo de la lista
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_femeninos = filtrar_heroes_atributo(lista, key, value)
    print("Heroe mas bajo genero f encontrado")
    return buscar_valor_minimo_lista(lista_filtrada_femeninos, key_tres, key_cuatro)

def determinar_altura_promedio_heroes_genero_m(lista, key, value, key_dos):#G
    """_summary_
    Filtra los heroes de genero masculino y se los pasa a la funcion que calcula promedios
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_masculinos = filtrar_heroes_atributo(lista, key, value)
    print("altura promedio heroes masculinos calculada ")
    return calcular_promedio_lista(lista_filtrada_masculinos, key_dos)

def determinar_altura_promedio_heroes_genero_f(lista, key, value, key_dos):#H
    """_summary_
    Filtra los heroes de genero femenino y se los pasa a la funcion que calcula promedios
    Args:
        lista (list): lista a filtrar
        key (str): campo de la lista
        value (str): valor del campo
        key_dos (str): campo de la lista
    """
    lista_filtrada_femeninas = filtrar_heroes_atributo(lista, key, value)
    print("altura promedio heroes femeninos calculada ")
    return calcular_promedio_lista(lista_filtrada_femeninas, key_dos)

def informar_nombre_del_heroe_asociado_a_indicadores_anteriores(c, d, e, f, g, h)->None:#I
    """_summary_
    Muestra los nombres de los puntos anteriores, en los que solo se buscaba o calculaba
    """
    print(f"El nombre del heroe mas alto de genero 'M' es: {c}")
    print(f"El nombre del heroe mas alto de genero 'F' es: {d}")
    print(f"El nombre del heroe mas bajo de genero 'M' es: {e}")
    print(f"El nombre del heroe mas bajo de genero 'F' es: {f}")
    print(f"La altura promedio de los heroes de genero 'M' es: {g}")
    print(f"La altura promedio de los heroes de genero 'F' es: {h}")

def determinar_cuantos_heroes_tienen_cada_tipo_de_color_de_ojos(lista: list, keys: list, values: list)->None:#J
    """_summary_
    Invoca a la funcion que se encarga de contar cuantos heroes tiene cada tipo de inteligencia y muestra la cantidad de cada uno 

    Args:
        lista (list): lista de heroes a recorrer
        keys (list): lista de campos a recorrer
        values (list): lista de valores a recorrer
    """                                                                     
    contador = contar_tipo_de_dato(lista, keys, values)
    for value in values:
        cantidad = contador[value]
        print(f"Hay {cantidad} heroes con color {value} en el campo {keys}.")

def determinar_cuantos_heroes_tienen_cada_tipo_de_color_de_pelo(lista: list, keys: list, values: list):#K
    """_summary_
    Invoca a la funcion que se encarga de contar cuantos heroes tiene cada tipo de inteligencia y muestra la cantidad de cada uno 

    Args:
        lista (list): lista de heroes a recorrer
        keys (list): lista de campos a recorrer
        values (list): lista de valores a recorrer
    """
    contador = contar_tipo_de_dato(lista, keys, values)
    for value in values:
        cantidad = contador[value]
        print(f"Hay {cantidad} heroes con color {value} en el campo{keys}.")

def determinar_cuantos_heroes_tienen_cada_tipo_de_inteligencia(lista: list, keys: list, values: list):#L
    """_summary_
    Invoca a la funcion que se encarga de contar cuantos heroes tiene cada tipo de inteligencia y muestra la cantidad de cada uno 

    Args:
        lista (list): lista de heroes a recorrer
        keys (list): lista de campos a recorrer
        values (list): lista de valores a recorrer
    """
    contador = contar_tipo_de_dato(lista, keys, values)
    for value in values:
        contador[value]
        print(f"Hay {contador[value]} heroes con inteligencia {value} en el campo {keys}.")

def listar_todos_los_heroes_agrupados_por_color_de_ojos(listas: list, key: str, key_dos):
    lista_aux = proyectar_heroe_repetidos(lista_personajes, key)
    for color_ojos in lista_aux:
        print("Color ojos: "+ color_ojos)
        mostrar_campos(listas, key, color_ojos, key_dos)

def listar_todos_los_heroes_agrupados_por_color_de_pelo(listas: list, key: str, key_dos):
    lista_aux = proyectar_heroe_repetidos(lista_personajes, key)
    for color_pelo in lista_aux:
        print("Color pelo: "+ color_pelo)
        mostrar_campos(listas, key, color_pelo, key_dos)

def listar_todos_los_heroes_agrupados_por_tipo_de_inteligencia(listas: list, key: str, key_dos:str):
    lista_aux = proyectar_heroe_repetidos(listas, key)
    for inteligencia in lista_aux:
        print("Inteligencia: "+ inteligencia)
        mostrar_campos(listas, key, inteligencia, key_dos)