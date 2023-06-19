
def buscar_valor_maximo_lista(lista_personajes:list, key:str, key_dos:str)->tuple:
    """_summary_
    Busca el valor maximo en una lista de diccionarios

    Args:
        lista_personajes lista a recorrer
        key (str): primer campo maximo
        key_dos (str): segundo campo maximo

    Returns:
        tuple: retorna los valores maximos de la lista
    """
    primer_personaje = lista_personajes[0]
    altura = float(primer_personaje[key_dos])
    nombre = primer_personaje[key]
    for personajes in lista_personajes:
        altura_personajes = float(personajes[key_dos])
        nombre_personajes = personajes[key]
        if altura_personajes > altura:
            altura = altura_personajes
            nombre = nombre_personajes
    return nombre, altura

def buscar_valor_minimo_lista(lista_personajes:list, key:str, key_dos:str)->tuple:
    """_summary_
    Busca el valor minimo en una lista de diccionarios

    Args:
        lista_personajes lista a recorrer
        key (str): primer campo minimo
        key_dos (str): segundo campo minimo

    Returns:
        tuple: retorna los valores minimos de la lista
    """
    primer_personaje = lista_personajes[0]
    altura = float(primer_personaje[key_dos])
    nombre = primer_personaje[key]
    for personajes in lista_personajes:
        altura_personajes = float(personajes[key_dos])
        nombre_personajes = personajes[key]
        if altura_personajes < altura:
            altura = altura_personajes
            nombre = nombre_personajes
    return nombre, altura

def buscar_elemento_en_lista(lista, elemento_a_buscar):#igual a la func "esta_en_lista" con la diferencia que la recorro con range
    """_summary_
    Verifica si un elemento se encuentra disponible o no en una lista

    Args:
        lista lista a recorrer
        elemento_a_buscar elemento a buscar

    Returns:
        _type_: verdadero si el elemento esta o falso si no esta
    """
    flag_elemento_a_buscar = False
    for i in range(len(lista)):
        if elemento_a_buscar == lista[i]:
            flag_elemento_a_buscar = True
            break
    return flag_elemento_a_buscar

def proyectar_heroe_doble(lista:list, key:str, key_dos:str)->tuple:#igual que proyectar heroe, solo que tiene una key de mas
    lista_filtrada = []
    l= []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
        l.append(heroe[key_dos])
    return lista_filtrada, l


def esta_en_lista(lista:list, item:str)->bool:
    """_summary_
    Verifica si un elemento se encuentra disponible o no en una lista

    Args:
        lista lista a recorrer
        elemento_a_buscar elemento a buscar

    Returns:
        _type_: verdadero si el elemento esta o falso si no esta
    """
    esta = False
    for elemento in lista:
        if elemento == item:
            esta = True
            break
    return esta

def filtrar_heroes_atributo(lista:list, key:str, value:str)->list:
    """_summary_
    Filtra una lista por atributo

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista
        value (str): valor del campo de la lista

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for item in lista:
        if item[key] == value:
            lista_filtrada.append(item)
    return lista_filtrada

def proyectar_heroe(lista:list, key:str)->list:
    """_summary_
    De una lista proyecta un campo determinado

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
    return lista_filtrada

def quitar_repetidos(lista:list)->list:
    """_summary_
    Verifica que una lista no tenga en el mismo elemento repetido

    Args:
        lista (list): _description_

    Returns:
        list: una nueva lista sin los elementos repetidos
    """
    lista_sin_repetidos = []
    for item in lista:
        if not buscar_elemento_en_lista(lista_sin_repetidos,item):
            lista_sin_repetidos.append(item)
    return lista_sin_repetidos

def proyectar_heroe_repetidos(lista:list, key:str, repetido:bool = False)->list:
    """_summary_
    De una lista proyecta un campo determinado y que este repetido

    Args:
        lista (list): lista a recorrer
        key (str): campo de la lista

    Returns:
        list: lista filtrada
    """
    lista_filtrada = []
    for heroe in lista:
        lista_filtrada.append(heroe[key])
        if not repetido:
            lista_aux = []
            for item in lista_filtrada:
                if not buscar_elemento_en_lista(lista_aux, item):
                    lista_aux.append(item)
                lista_filtrada = lista_aux
    return lista_filtrada






