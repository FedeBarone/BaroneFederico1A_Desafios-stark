from data_stark import lista_personajes
import re
import os

lista_aux_heroes = []
for heroe in lista_personajes:
    lista_aux_heroes.append(heroe.copy())

def es_genero(genero: str)-> bool:
    return_aux = False
    if re.match("^(NB|nb|F|f|M|m)$", genero):
        return_aux = True
    return return_aux

def es_entero(entero: int)-> bool:
    return_aux = False
    if re.match("^[0-9]+$", str(entero)):
        return_aux = True
    return return_aux
#=======================================================Desafío Stark #02=================================================================
# Desafío #02: (con biblioteca propia: stark_biblioteca)
# En base a lo resuelto en el desafío #00, deberás mejorar la calidad de tus funciones.
# Es por ello que te proponemos lo siguiente:
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
# escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
# un string, etc y que contendrá) y que es lo que retorna la función!

# 0. Crear la función 'stark_normalizar_datos' la cual recibirá por parámetro la lista
#    de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
#   las keys que representan datos numéricos)
# ● Validar primero que el tipo de dato no sea del tipo al cual será
#   casteado. Por ejemplo si una key debería ser entero (ejemplo edad)
#   verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá imprimir como
#   mensaje ‘Datos normalizados’, caso contrario no imprimirá nada.
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
#   caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”

# 1.1.
# Crear la función 'obtener_nombre' la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y devolverá un string el cual
# contenga su nombre formateado de la siguiente manera:
# Nombre: Howard the Duck

# 1.2.
# Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
# deberá imprimirlo en la consola. La función no tendrá retorno.

# 1.3.
# Crear la función 'stark_imprimir_nombres_heroes' la cual recibirá por
# parámetro la lista de héroes y deberá imprimirla en la consola. Reutilizar las
# funciones hechas en los puntos 1.1 y 1.2. Validar que la lista no esté vacía
# para realizar sus acciones, caso contrario no hará nada y retornara -1.
# Con este se resuelve el Ej 1 del desafío #00

# 2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.

# ● La función deberá devolver un string el cual contenga el nombre y dato
#   (key) del héroe a imprimir. El dato puede ser 'altura', 'fuerza', 'peso' O
#   CUALQUIER OTRO DATO.
# ● El string resultante debe estar formateado de la siguiente manera:
#   (suponiendo que la key es fuerza)
#   Nombre: Venom | fuerza: 500

# 3. Crear la función 'stark_imprimir_nombres_alturas' la cual recibirá por 
# parámetro la lista de héroes, la cual deberá iterar e imprimir sus nombres y
# alturas USANDO la función creada en el punto 2. Validar que la lista de héroes
# no esté vacía para realizar sus acciones, caso contrario no hará nada y
# retornara -1.
# Con este se resuelve el Ej 2 del desafío #00

# 4.1.
# Crear la función 'calcular_max' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el máximo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más alto.

# Ejemplo de llamada:
# calcular_max(lista, 'edad')

# 4.2.
# Crear la función 'calcular_min' la cual recibirá por parámetro la lista de
# héroes y una key (string) la cual representará el dato que deberá ser evaluado
# a efectos de determinar cuál es el mínimo de la lista. Por ejemplo la función
# deberá poder calcular: el peso, la altura o fuerza máximas y retornar el héroe
# que tenga el dato más bajo.

# Ejemplo de llamada:
# calcular_min(lista, 'edad')

# 4.3.
# Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:

# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar los 
#   valores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
#  ‘peso’, ‘edad’, etc.

# La función deberá retornar el héroe que cumpla con la condición pedida.
# Reutilizar las funciones hechas en los puntos 4.1 y 4.2

# Ejemplo de llamada:
# calcular_max_min_dato(lista, "maximo", "edad")

# 4.4.
# Crear la función 'stark_calcular_imprimir_heroe' la cual recibirá tres parámetros:

# ● La lista de héroes
# ● El tipo de cálculo a realizar: es un valor string que puede tomar losvalores ‘maximo’ o ‘minimo’
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
# Con este se resuelve el Ej 3, Ej 4, Ej 6 y Ej 7 del desafío #00
# La función deberá obtener el héroe que cumpla dichas condiciones, imprimir
# su nombre y el valor calculado. Reutilizar las funciones de los puntos:
# punto 1.2, punto: 2 y punto 4.3

# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara -1.

# Ejemplo de llamada:
# stark_calcular_imprimir_heroe (lista, "maximo", "edad")

# Ejemplo de salida:
# Mayor altura: Nombre: Howard the Duck | altura: 79.34

# 5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
# lista de héroes y un string que representara el dato/key de los héroes que se
# requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un 
# diccionario vacío antes de hacer la suma. La función deberá retornar la suma
# de todos los datos según la key pasada por parámetro

# 5.2. Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo,
# retornar 0, caso contrario realizar la división entre los parámetros y retornar el
# resultado

# 5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
# lista de héroes y un string que representa el dato del héroe que se requiere
# calcular el promedio. La función debe retornar el promedio del dato pasado
# por parámetro

# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 5.1 y 5.2

# 5.4. Crear la función 'stark_calcular_imprimir_promedio_altura' la cual recibirá
# una lista de héroes y utilizando la función del punto 5.3 calcula y mostrará la
# altura promedio. Validar que la lista de héroes no esté vacía para realizar sus
# acciones, caso contrario no hará nada y retornara -1.

# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 1.2, 5.1 y
# 5.3
# Con este se resuelve el Ej 5 del desafío #00

# 6.1. Crear la función "imprimir_menu" que imprima el menú de opciones por
# pantalla, el cual permite utilizar toda la funcionalidad ya programada. Se
# deberá reutilizar la función antes creada encargada de imprimir un string (1.2)

# 6.2. Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente
# por dígitos. Retornara True en caso de serlo, False caso contrario

# 6.3. Crear la función 'stark_menu_principal' la cual se encargará de imprimir el
# menú de opciones y le pedirá al usuario que ingrese el número de una de las
# opciones elegidas y deberá validarlo. En caso de ser correcto dicho número,
# lo retornara casteado a entero, caso contrario retorna -1. Reutilizar las
# funciones del ejercicio 6.1 y 6.2

# 7. Crear la función 'stark_marvel_app' la cual recibirá por parámetro la lista de
# héroes y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+). Debe informar por consola en caso de seleccionar una opción incorrecta y volver a pedir el dato al usuario. 
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

def stark_normalizar_datos(lista_personajes: list)-> None: #0
    """_summary_
    Recorre la lista de heroes y convierte al tipo de dato correcto las keys que representan datos numéricos

    Args:
        lista_personajes (list): lista a recorrer
    """
    if len(lista_personajes) > 0:
        normalizado = False
        for heroe in lista_personajes:
            if not(type(heroe["altura"]) == type(float())) or type(heroe["peso"]) == type(float()) or type(heroe["fuerza"]) == type(int()):
                heroe["altura"] = float(heroe["altura"])
                heroe["peso"] = float(heroe["peso"])
                heroe["fuerza"] = int(heroe["fuerza"])
                normalizado = True

        if normalizado:
            print("Normalizado")
        else:
            print("No normalizado")
    else:
        print("La lista esta vacia")

def obtener_nombre(heroe: dict)-> str: #1.1
    """_summary_
    Obtiene el nombre de un heroe

    Args:
        heroe (dict): diccionario que representa a un heroe

    Returns:
        str: el nombre del heroe
    """
    if type(heroe) == type(dict()):
        return  f"Nombre: {heroe['nombre']}"

def imprimir_dato(dato: str)-> None: #1.2
    """_summary_
    Muestra un dato

    Args:
        dato (str): dato a mostrar
    """
    if type(dato) == type(str()):
        print(dato)

def stark_imprimir_nombres_heroes(lista_heroes: list)-> None: # 1.3
    """_summary_
    Imprime los nombres de los heroes
    Args:
        lista_heroes (list): lista a recorrer
    """
    if type(lista_heroes) == type(list()) and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))
    else:
        return -1

def obtener_nombre_y_dato(diccionario: dict, key: str)-> str: #2
    """_summary_
    Obtiene el nombre y un campo específico de un héroe
    Args:
        diccionario (dict): diccionario que representa al heroe
        key (str): campo del diccionario

    Returns:
        str: el nombre y un campo específico del heroe
    """
    if type(diccionario) == type(dict()) and type(key) == type(str()):
        return f"Nombre: {diccionario['nombre']} | {key}: {diccionario[key]}"

def stark_imprimir_nombres_alturas(lista_heroes: list)-> None or -1: # 3
    """_summary_
    Imprime los nombres y alturas de los heroes

    Args:
        lista (list): lista a recorrer

    Returns:
        str: -1
    """
    if type(lista_heroes) == type(list()) and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            print(obtener_nombre_y_dato(heroe, "altura"))
    else:
        return -1

def calcular_max(lista_heroes: list, key: str)-> str: # 4.1.
    """_summary_
    Calcula el dato mas alto de un heroe

    Args:
        lista_heroes (list): lista a recorrer
        key (str): campo a evaluar

    Returns:
        str: el nombre del heroe con el dato mas alto
    """
    if type(lista_heroes) == type(list()) and type(key) == type(str()):
        stark_normalizar_datos(lista_heroes)
        heroe_mayor = lista_heroes[0]
        max_value = heroe_mayor[key]
        nombre_maximo = None
        for heroe in lista_heroes:
            if heroe[key] > max_value:
                max_value = heroe[key]
                nombre_maximo = heroe["nombre"]
    return nombre_maximo

def calcular_min(lista_heroes: list, key: str)-> str: # 4.2
    """_summary_
    Calcula el dato mas bajo de un heroe

    Args:
        lista_heroes (list): lista a recorrer
        key (str): campo a evaluar

    Returns:
        str: el nombre del heroe con el dato mas bajo
    """
    if type(lista_heroes) == type(list()) and type(key) == type(str()):
        stark_normalizar_datos(lista_heroes)
        heroe_menor = lista_heroes[0]
        min_value = heroe_menor[key]
        nombre_minimo = None
        for heroe in lista_heroes:
            if heroe[key] <= min_value:
                min_value = heroe[key]
                nombre_minimo = heroe["nombre"]
    return nombre_minimo

def calcular_max_min_dato(lista_aux: list, tipo_calculo: str, key: str)-> str: # 4.3
    """_summary_
    Calcula el max o min dependiendo el valor que se pase a traves de los parametros

    Args:
        lista_aux (list): lista a recorrer
        tipo_calculo (str): toma el valor maximo o minimo
        key (str): campo o atributo de la lista

    Returns:
        _type_(str): el valor maximo o minimo
    """
    if tipo_calculo == "maximo":
        return_aux = calcular_max(lista_aux, key)
    elif tipo_calculo == "minimo":
        return_aux = calcular_min(lista_aux, key)
    return return_aux

def stark_calcular_imprimir_heroe(lista_heroes: list, tipo_calculo: str, key: str)->None or -1: # 4.4
    """_summary_
    Calcula el max o min dependiendo el valor que se pase a traves de los parametros y muestra el nombre junto con el valor max o min

    Args:
        lista_aux (list): lista a recorrer
        tipo_calculo (str): toma el valor maximo o minimo
        key (str): campo o atributo de la lista

    Returns:
        _type_(str): -1 si la lista esta vacia, sino no retorna nada
    """
    if len(lista_heroes) > 0:
        nombre_max_o_min = calcular_max_min_dato(lista_heroes, tipo_calculo, key)
        for heroe in lista_heroes:
            if heroe["nombre"] == nombre_max_o_min:
                r = obtener_nombre_y_dato(heroe, key)
        if tipo_calculo == "maximo":
            imprimir_dato(f"Mayor altura: {r}")
        elif tipo_calculo == "minimo":
            imprimir_dato(f"Menor altura: {r}")
    else:
        return -1
    
def sumar_dato_heroe(lista_aux: list, key: str)-> int: # 5.1
    """_summary_
    Suma los valores de un diccionario según la key pasada por parámetro

    Args:
        lista_aux (list): lista a recorrer
        key (str): campo o atributo de la lista

    Returns:
        int: el resultado de la suma
    """
    acum_key = 0
    for heroe in lista_aux:
        if type(heroe) == type(dict()) and heroe:
            acum_key += float(heroe[key])
    return acum_key

def dividir(dividendo: int, divisor: int)-> float: # 5.2
    """_summary_
    Divide dos numeros

    Args:
        dividendo (int): número que se va a dividir.
        divisor (int): número por el cual se va a dividir el dividendo.

    Returns:
        float: resultado de la division
    """
    if divisor != 0:
        return_aux = dividendo / divisor
    else:
        return_aux = 0
    return return_aux


def calcular_promedio(lista_aux: list, key: str)-> float: # 5.3
    """_summary_
    Calcula el promedio de campo de la lista

    Args:
        lista_aux (list): lista a recorrer
        key (str): campo de la lista

    Returns:
        float: promedio
    """
    return dividir(sumar_dato_heroe(lista_aux, key), len(lista_aux))

def stark_calcular_imprimir_promedio_altura(lista_aux : list)-> None or -1: # 5.4
    """_summary_
    Calcula y muestra la altura promedio de los heroes

    args:
        lista_aux(lista): lista a recorrer
    Returns:
        _type_: 1- si la lista esta vacia, sino none
    """
    if len(lista_aux) > 0:
        promedio_altura = calcular_promedio(lista_aux, "altura")
        imprimir_dato(f"La altura promedio de los heroes es: {promedio_altura:.2f}")      
    else:
        return -1

def imprimir_menu()-> None: # 6.1
    """_summary_
    Muestra el menu
    """
    imprimir_dato("1- Mostrar nombre de cada superhéroe\n2- Mostrar nombre de cada superhéroe y su altura\n3- Determinar el superhéroe más alto\n4- Determinar el superhéroe más bajo\n5- Calcular altura promedio de los superhéroes\n6- Mostrar el superhéroe más alto\n7- Mostrar el superhéroe más bajo\n8- Calcular e informar superhéroe más y menos pesado\n9- Acceder sub menu stark 01\n10- Salir\n")

def validar_entero(numero_string: str)-> bool: # 6.2
    """_summary_
    Valida que solo se puedan ingresar numeros
    Args:
        numero_string (str): numero a verificar

    Returns:
        bool: True si es un numero, False si no lo es
    """
    return_aux = False
    if numero_string.isdigit():
        return_aux = True
    return return_aux

def stark_menu_principal()-> str or -1 : # 6.3
    """_summary_
    Muestra el menu y pide la opcion al usuario

    Returns:
        _type_: la opcion o -1
    """
    imprimir_menu()
    opcion = input("Ingrese opcion: ")
    if validar_entero(opcion):
        return opcion
    else:
        return -1
    
def stark_marvel_app(lista_heroes: list)-> None: # 7 #solo probe un par de func en los cases para comprobar que funcione la fun marvel app
                                                    #pero ya tengo mi propio menu, asi que no la necesito
    """_summary_                                     
    Ejecuta el menu
    Args:
        lista_heroes (list): lista a recorrer
    """
    while True:
        match stark_menu_principal():
            case '1':
                stark_imprimir_nombres_heroes(lista_heroes)
            case '2':
                stark_imprimir_nombres_alturas(lista_heroes)
            case '3':
                stark_calcular_imprimir_promedio_altura(lista_heroes)
            case '4':
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                pass
            case '8':
                pass
            case '9':
                pass
            case '10':
                pass
            case _:
                print("Error, no existe esa opcion")

#=======================================================Desafío Stark #03=================================================================
# 1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# La función deberá validar:
# ● Que el string recibido no se encuentre vacío
# Devolver ‘N/A’ en caso de no cumplirse la validación

# Ejemplo de la salida de la función para Howard the Duck:
# H.D.


# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True


# 1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: lista de personajes
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# La función deberá iterar la lista_heroes pasándole cada héroe a la función
# definir_iniciales_nombre.
# En caso que la función definir_iniciales_nombre() retorne False entonces se
# deberá detener la iteración e informar por pantalla el siguiente mensaje:
# ‘El origen de datos no contiene el formato correcto’
# La función deberá devolver True en caso de haber finalizado con éxito o False
# en caso de que haya ocurrido un error


# 1.4. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
# como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
# las iniciales a los diccionarios contenidos en la lista_heroes
# Luego deberá imprimir la lista completa de los nombres de los personajes
# seguido de las iniciales encerradas entre paréntesis ()
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.)
# ...
# La función no retorna nada


# 2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como parámetros:
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# ● genero_heroe: un string que representa el género del héroe ( puede
# tomar los valores ‘M’, ‘F’ o ‘NB’)
# La función deberá generar un string con el siguiente formato:
# GENERO-000...000ID
# Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
# último el identificador recibido. Todos los códigos generados deben tener
# como máximo 10 caracteres (contando todos los caracteres, inclusive el
# guión). Se deberá completar con ceros para que todos queden del mismo
# largo
# Algunos ejemplos:
# F-00000001
# M-00000002
# NB-0000010
# La función deberá validar:
# ● El identificador del héroe sea numérico.
# ● El género no se encuentre vacío y este dentro de los valores esperados
# (‘M’, ‘F’ o ‘NB’)
# En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
# correctamente retornar el código generado


# 2.2. Crear la función ‘agregar_codigo_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al
# diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código
# utilizando la función ‘generar_codigo_heroe’
# La función deberá validar:
# ● Que el diccionario recibido como parámetro no se encuentre vacío.
# ● Que el código recibido mediante generar_codigo_heroe tenga
# exactamente 10 caracteres
# En caso de pasar las validaciones correctamente la función deberá retornar
# True, en caso de encontrarse un error retornar False


# 2.3. Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y agregarle el código a cada
# uno de los personajes.
# El código del héroe (id_heore) surge de la posición del mismo dentro de la
# lista_heroes (comenzando por el 1).
# Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
# héroe que se está iterando y el id_heroe
# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (## representa la cantidad de códigos generados):
# Se asignaron ## códigos
# * El código del primer héroe es: M-00000001
# * El código del del último héroe es: M-00001224
# La función deberá validar::
# ● La lista contenga al menos un elemento
# ● Todos los elementos de la lista sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’
# La función no retorna ningún valor.


# 3.1. Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número entero
# La función deberá analizar el string recibido y determinar si es un número
# entero positivo. La función debe devolver distintos valores según el problema
# encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# entero positivo, retornarlo convertido en entero


# 3.2. Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número decimal
# La función deberá analizar el string recibido y determinar si es un número
# flotante positivo. La función debe devolver distintos valores según el
# problema encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# flotante positivo, retornarlo convertido en flotante


# 3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
# ● valor_str: un string que representa el texto a validar
# ● valor_por_defecto: un string que representa un valor por defecto
# (parámetro opcional, inicializarlo con ‘-’)
# La función deberá analizar el string recibido y determinar si es solo texto (sin
# números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un
# espacio
# El espacio es un caracter válido
# En caso que se verifique que el parámetro recibido es solo texto, se deberá
# retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
# un valor por defecto, entonces retornar el valor por defecto convertido a
# minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en
# caso que los tuviese


# 3.4. Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
# ● heroe: un diccionario con los datos del personaje
# ● clave: un string que representa el dato a sanitizar (la clave del
# diccionario). Por ejemplo altura
# ● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
# tomar los valores: ‘string’, ‘entero’ y ‘flotante’
# La función deberá sanitizar el valor del diccionario correspondiente a la clave
# y al tipo de dato recibido
# Para sanitizar los valores se deberán utilizar las funciones creadas en los
# puntos 3.1, 3.2, 3.3 y 3.4

# Se deberá validar:
# ● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
# ‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
# minúsculas. En caso de encontrarse un valor no válido informar por
# pantalla: ‘Tipo de dato no reconocido’
# ● Que clave exista como clave dentro del diccionario heroe. En caso de
# no encontrarse, informar por pantalla: ‘La clave especificada no
# existe en el héroe’. (en este caso la validación es sensible a
# mayúsculas o minúsculas)
# Ejemplo de llamada a la función válida:
# sanitizar_dato(dict_personaje, “altura”, “Flotante”)
# La función deberá devolver True en caso de haber sanitizado algún dato y
# False en caso contrario.


# 3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
# siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
# ‘inteligencia’
# ● Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’,
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
# ● La función no retorna nada
# ● Reutilizar la función sanitizar_dato


# 4.1. Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y generar una lista donde cada
# elemento es cada palabra que componen el nombre de los personajes.
# Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
# [‘Howard’, ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, ... ]
# La función deberá validar que:
# ● La lista contenga al menos un elemento
# ● Todos los elementos de lista_heroes sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘nombre’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’


# 4.2. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá mostrar por pantalla el índice generado por la función
# generar_indice_nombres con todos los nombres separados con un guión.
# Por ejemplo:
# Howard-the-duck-Rocket-Raccoon-Wolverine...


# 5.1. Crear la función ‘convertir_cm_a_mtrs’ la cual recibirá como parámetro:
# ● valor_cm: Un número que representa una medida en centímetros
# La función deberá retornar el número recibido, pero convertido a la unidad
# metros. La función deberá validar que el número recibido sea un número
# flotante positivo, en caso de no serlo retornar -1


# 5.2. Crear la función ‘generar_separador’ la cual recibirá como parámetro
# ● patron: un carácter que se utilizará como patrón para generar el
# separador
# ● largo: un número que representa la cantidad de caracteres que va
# ocupar el separador.
# ● imprimir: un parámetro opcional del tipo booleano (por default definir
# en True)
# La función deberá generar un string que contenga el patrón especificado
# repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
# al otro, sin salto de línea)
# Si el parámetro booleano recibido se encuentra en False se deberá solo
# retornar el separador generado. Si se encuentra en True antes de retornarlo,
# imprimirlo por pantalla
# La función deberá validar:
# ● Que el parámetro patrón tenga al menos un carácter y como máximo
# dos
# ● Que el parámetro largo sea un entero entre 1 y 235 inclusive
# En caso de no verificarse las validaciones devolver ‘N/A’
# Ejemplo de llamada:
# generar_separador(‘*’, 10)
# Ejemplo de salida:
# **********


# 5.3. Crear la función ‘generar_encabezado’ la cual recibirá como parámetro
# ● titulo: un string que representa el título de una sección de la ficha
# La función deberá devolver un string que contenga el título envuelto entre dos
# separadores (estimar el largo requerido para tu pantalla).
# Ejemplo de salida:
# ********************************************************************************
# PRINCIPAL
# ********************************************************************************
# La función deberá convertir el titulo recibido en todas letras mayúsculas


# 5.4. Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del héroe
# La función deberá a partir los datos del héroe generar un string con el
# siguiente formato e imprimirlo por pantalla::
# ***************************************************************************************
# PRINCIPAL
# ***************************************************************************************
#       NOMBRE DEL HÉROE: Spider-Man (S.M.)
#       IDENTIDAD SECRETA: Peter Parker
#       CONSULTORA: Marvel Comics
#       CÓDIGO DE HÉROE : M-00000001
# ***************************************************************************************
# FISICO
# ***************************************************************************************
#       ALTURA: 1,78 Mtrs.
#       PESO: 74,25 Kg.
#       FUERZA: 55 N
# ***************************************************************************************
# SEÑAS PARTICULARES
# ***************************************************************************************
#       COLOR DE OJOS: Hazel
#       COLOR DE PELO: Brown


# 5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá comenzar imprimiendo la ficha del primer personaje de la
# lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
# [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
# ● Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en
# la posición anterior en la lista (en caso de estar en el primero, ir al
# último)

# ● Si el usuario ingresa ‘2’: se debe mostrar el héroe que se encuentra en
# la posición siguiente en la lista (en caso de estar en el último, ir al
# primero)

# ● Si ingresa ‘S’: volver al menú principal
# ● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
# ingrese un valor válido


# 6.1. Crear la función ‘imprimir_menu’ que imprima las siguientes opciones por
# pantalla:
# """

# 1 - Imprimir la lista de nombres junto con sus iniciales
# 2 - Generar códigos de héroes
# 3 - Normalizar datos
# 4 - Imprimir índice de nombres
# 5 - Navegar fichas
# S - Salir

# ____________________________________________________________
# """


# 6.2. Crear la función ‘stark_menu_principal'. No recibe parámetros.
# La función deberá imprimir el menú de opciones y le pedirá al usuario que
# ingrese una.
# La función deberá retornar la respuesta del usuario


# 6.3. Crear la función ‘stark_marvel_app_3’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera (match solo para los que cuentan con
# python 3.10+).
# Debe informar por consola en caso de seleccionar una opción incorrecta y
# volver a pedir el dato al usuario.
# Reutilizar las funciones con prefijo 'stark_' donde crea correspondiente.

def extraer_iniciales(nombre_heroe: str)-> str:# 1.1
    if type(nombre_heroe) == type(str()):
        lista = re.findall("[A-Z]", nombre_heroe)
        nuevo_string = ".".join(lista)+"."
        return nuevo_string
    

def definir_iniciales_nombre(heroe: dict)-> bool:# 1.2
    return_aux = False
    if type(heroe) == type(dict()):
        if "nombre" in heroe:
            heroe["iniciales"] = extraer_iniciales(heroe["nombre"])
            return_aux = True
    return return_aux

def agregar_iniciales_nombre(lista_aux)-> bool:# 1.3
    return_aux = False
    if type(lista_aux) == type(list()) and len(lista_aux) > 0:
        for heroe in lista_aux:
            if not definir_iniciales_nombre(heroe):
                print("El origen de datos no contiene el formato correcto")
                break
            else:
                definir_iniciales_nombre(heroe)
                return_aux = True
    return return_aux

def stark_imprimir_nombres_con_iniciales(lista_aux)-> None:# 1.4
    if agregar_iniciales_nombre(lista_aux):
        for heroe in lista_aux:
            heroe = heroe["iniciales"]
        for heroe in lista_aux:
            print(f"* {heroe['nombre']} ({heroe['iniciales']})")

def generar_codigo_heroe(id_heroe: int, genero_heroe: str)-> str:# 2.1
    return_aux = "N/A"
    if es_genero(genero_heroe) and len(genero_heroe) > 0 and es_entero(id_heroe):
        codigo_generado = f"{genero_heroe}-{str(id_heroe).zfill(7)}"
        if len(codigo_generado) <= 10:
            return_aux = codigo_generado
    return return_aux

def agregar_codigo_heroe(heroe: dict, id_heroe: int)-> bool:# 2.2
    return_aux = False
    if len(heroe) > 0:
        heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe, heroe["genero"])
        if len(generar_codigo_heroe(id_heroe, heroe["genero"])) <= 10:
            return_aux = True
    return return_aux

def stark_generar_codigos_heroes(lista_heroes: list)-> None:# 2.3
    todo_ok = False
    if len(lista_heroes) > 0:
        for i in range(len(lista_heroes)):
            if type(lista_heroes[i]) == type(dict()) and "genero" in lista_heroes[i]:
                agregar_codigo_heroe(lista_heroes[i], i+1)
                todo_ok = True
    if todo_ok:
        print(f"Se asignaron: {len(lista_heroes)} codigos")
        print(f"* El código del primer héroe es: {lista_heroes[0]['codigo_heroe']}")
        print(f"* El código del del último héroe es: {lista_heroes[-1]['codigo_heroe']}")
    else:
        print("el origen de datos no contiene el formato correcto")

def sanitizar_entero(numero_str: str)-> int:# 3.1
    if re.match("^[A-Za-z]+$", numero_str):
        numero_str = numero_str.strip()
        return -1
    elif re.match("^-[\d]+$", numero_str):
        return -2
    elif re.match("^[^\d]+$", numero_str):
        return -3
    else:
        return int(numero_str)

def sanitizar_flotante(numero_str: str)-> float:# 3.2
    numero_str = numero_str.strip()
    if re.match("^[^0-9]+$", numero_str):
        return -1
    elif re.match("^-[\d]+$", numero_str):
        return -2
    else:
        try:
            flotante_positivo = float(numero_str)
        except ValueError:
            return -3
    return flotante_positivo

def sanitizar_string(valor_str: str, valor_por_defecto: str = '-')-> str:# 3.3
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    if re.match("^[A-Za-z\s/]+$", valor_str):
        if "/" in valor_str:
            valor_str = re.sub("/", " ", valor_str)
        return valor_str.lower()
    elif valor_str == "" and valor_por_defecto:
        return valor_por_defecto.lower()
    else:
        return "N/A"

def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str)-> bool:# 3.4
    return_aux = False
    tipo_dato = tipo_dato.lower()
    if tipo_dato == "entero":
        if clave in heroe:
            heroe[clave] = sanitizar_entero(heroe[clave])
            return_aux = True
        else:
            print("La clave especificada no existe en el héroe")
    elif tipo_dato == "flotante":
        if clave in heroe:
            heroe[clave] = sanitizar_flotante(heroe[clave])
            return_aux = True
        else:
            print("La clave especificada no existe en el héroe")
    elif tipo_dato == "string":
        if clave in heroe:
            heroe[clave] = sanitizar_string(heroe[clave])
            return_aux = True
        else:
            print("La clave especificada no existe en el héroe")
    else:
        print("Tipo de dato no reconocido")
    return return_aux

def stark_normalizar_datos(lista_heroes: list)-> None:# 3.5
    todo_ok = False
    if len(lista_heroes) > 0:
        for heroe in lista_heroes:
            sanitizar_dato(heroe, "altura", "flotante")
            sanitizar_dato(heroe, "peso", "flotante")
            sanitizar_dato(heroe, "color_ojos", "string")
            sanitizar_dato(heroe, "color_pelo", "string")
            sanitizar_dato(heroe, "fuerza", "entero")
            sanitizar_dato(heroe, "inteligencia", "string")
            todo_ok = True
        if todo_ok:
            print("Datos normalizados")
        else:
            print("salio todo mal!")
    else:
        print("lista de heroes vacia")

def generar_indice_nombres(lista_heroes: list)-> list:# 4.1
    todo_ok = False
    nueva_lista = []
    for heroe in lista_heroes:
        if "nombre" in heroe and type(heroe) == type(dict()):
            nueva_lista.extend(re.split("[\s-]+", heroe["nombre"]))
            todo_ok = True
    if not todo_ok:
        print("El origen de datos no contiene el formato correcto")
    return nueva_lista

def stark_imprimir_indice_nombre(lista_heroes: list)-> None:# 4.2
    string = "-".join(generar_indice_nombres(lista_heroes))
    print(string)

def convertir_cm_a_mtrs(valor_cm: float)-> float:# 5.1
    mtrs = valor_cm / 100
    if re.match("^[+\d.]+$", str(valor_cm)):
        return mtrs
    else:
        return -1

def generar_separador(patron: str, largo: int, imprimir: True)-> str:# 5.2
    string_generador = "N/A"
    if len(patron)> 0 and len(patron) < 3 and largo > 0 and largo < 236:
        if imprimir:
            string_generador = patron * largo
            print(string_generador)
        else:
            string_generador = patron * largo
    return string_generador

def generar_encabezado(titulo: str)-> str:# 5.3
    titulo_upper = titulo.upper()
    titulo_con_separadores = f"{generar_separador('*', 70, False)}\n{titulo_upper}\n{generar_separador('*', 70, False)}"
    return titulo_con_separadores

def imprimir_ficha_heroe(heroe: dict)-> None:# 5.4
    string_formateado = f"""{generar_encabezado('principal')}\n      NOMBRE DEL HÉROE: {heroe['nombre']:^10s} ({heroe['iniciales']:^1s})\n      IDENTIDAD SECRETA: {heroe['identidad']:^20s}
      CONSULTORA: {heroe['empresa']:^10s}\n      CÓDIGO DE HÉROE: {heroe['codigo_heroe']:^16s}\n{generar_encabezado('fisico')}\n      ALTURA: {heroe['altura']:^16s}
      PESO: {heroe['peso']:^16s}\n      FUERZA: {heroe['fuerza']:^4s}\n{generar_encabezado('señas particulares')}\n      COLOR DE OJOS: {heroe['color_ojos']:^8s}
      COLOR DE PELO: {heroe['color_pelo']:^8s}"""
    print(string_formateado)

def salir_del_menu():
    while True:
        salir = input("Confirma salida?[S/N]")
        if salir.isalpha():
            if not (salir != 'S' and salir != 'N'):
                break
            else:
                print(
                    "Solo puede seleccionar 'S' para salir o 'N' para volver al menu principal")
        else:
            print("No se pueden ingresar numeros")
    return salir

def imprimir_menu_fichas():# 6.1
    print("1-Ir a la izquierda")
    print("2-Ir a la derecha")
    print("S-Salir")
    print("____________________________________________________________")

def stark_menu_fichas():# 6.2
    imprimir_menu_fichas()
    opcion = input("Ingrese opcion: ")
    return opcion

def stark_navegar_fichas(lista_heroes: list):# 5.5
    for i in range(len(lista_heroes)):
        imprimir_ficha_heroe(lista_heroes[0])
        break
    while True:
        match stark_menu_fichas():
            case "1":
                imprimir_ficha_heroe(lista_heroes[i-1])
            case "2":
                imprimir_ficha_heroe(lista_heroes[i+1])
            case "S":
                salir = salir_del_menu()
                if salir == 'S':
                    break
        os.system("pause")

def imprimir_menu():# 6.1
    print("1 - Imprimir la lista de nombres junto con sus iniciales")
    print("2 - Generar códigos de héroes")
    print("3 - Normalizar datos")   
    print("4 - Imprimir índice de nombres")
    print("5 - Navegar fichas")
    print("S - Salir")
    print("____________________________________________________________")

def stark_menu_principal():# 6.2
    imprimir_menu()
    opcion = input("Ingrese opcion: ")
    return opcion

def stark_marvel_app_3(lista_heroes: list):# 6.3
    while True:
        os.system("cls")
        match stark_menu_principal():
            case '1':
                stark_imprimir_nombres_con_iniciales(lista_heroes)
            case '2':
                stark_generar_codigos_heroes(lista_heroes)
            case '3':
                stark_normalizar_datos(lista_heroes)
            case '4':
                stark_imprimir_indice_nombre(lista_heroes)
            case '5':
                stark_navegar_fichas(lista_heroes)
            case 'S':
                salir = salir_del_menu()
                if salir == 'S':
                    break

        os.system("pause")

#stark_marvel_app_3(lista_aux_heroes)




