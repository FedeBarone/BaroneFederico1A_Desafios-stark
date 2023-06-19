from data_stark import lista_personajes 
from informes import*
from busquedas import*
import os

def mostrar_menu_principal(lista_menu: list)->str:
    """_summary_
    Muestra un menu con opciones de manera dinamica

    Args:
        lista_menu (list): lista a recorrer

    Returns:
        str: la opcion elegida
    """
    print("========================================================================================================")
    print("|███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗  ██████╗░██████╗░██╗███╗░░██╗░█████╗░██╗██████╗░░█████╗░██╗░░░░░|")
    print("|████╗░████║██╔════╝████╗░██║██║░░░██║  ██╔══██╗██╔══██╗██║████╗░██║██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░|")
    print("|██╔████╔██║█████╗░░██╔██╗██║██║░░░██║  ██████╔╝██████╔╝██║██╔██╗██║██║░░╚═╝██║██████╔╝███████║██║░░░░░|")
    print("|██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║  ██╔═══╝░██╔══██╗██║██║╚████║██║░░██╗██║██╔═══╝░██╔══██║██║░░░░░|")
    print("|██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝  ██║░░░░░██║░░██║██║██║░╚███║╚█████╔╝██║██║░░░░░██║░░██║███████╗|")
    print("|╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝|")
    print("========================================================================================================")
    for i in range(len(lista_menu)):
        print(f"|{lista_menu[i]:53s}|")
        print("=======================================================")
    opcion = input("Ingrese una opcion: ")
    return opcion

def mostrar_sub_menu(lista_sub_menu: list)->str:
    """_summary_
    Muestra un menu con opciones de manera dinamica

    Args:
        lista_menu (list): lista a recorrer

    Returns:
        str: la opcion elegida
    """
    print("+==============================================================================================+")
    print("|                                         ꜱᴜʙ ᴍᴇɴᴜ                                             |")
    print("+==============================================================================================+")
    for i in range(len(lista_sub_menu)):
        print(f"|{lista_sub_menu[i]:94s}|")
        print("================================================================================================")
    opcion_dos = input("Ingrese una opcion: ")
    return opcion_dos

def ejecutar_opcion_sub_menu(lista_sub_menu:list)->None:
    """_summary_
    Ejecuta un menu con opciones para cada case

    Args:
        lista_sub_menu (list): lista a recorrer
    """
    os.system("cls")
    lista_sub_menu  =  ["1- Imprimir superhéroes de género M", "2- Imprimir superhéroes de género F",
                        "3- determinar cuál es el superhéroe más alto de género M",
                        "4- determinar cuál es el superhéroe más alto de género F",
                        "5- determinar cuál es el superhéroe más bajo de género M",
                        "6- determinar cuál es el superhéroe más bajo de género F",
                        "7- determinar la altura promedio de los superhéroes de género M",
                        "8- determinar la altura promedio de los superhéroes de género F",
                        "9- Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores",
                        "10- Determinar cuántos superhéroes tienen cada tipo de color de ojos",
                        "11- Determinar cuántos superhéroes tienen cada tipo de color de pelo",
                        "12- Determinar cuántos superhéroes tienen cada tipo de inteligencia",
                        "13- Listar todos los superhéroes agrupados por color de ojos",
                        "14- Listar todos los superhéroes agrupados por color de pelo",
                        "15- Listar todos los superhéroes agrupados por tipo de inteligencia",
                        "16- Salir"]
    c = None
    d = None
    e = None
    f = None
    g = None
    h = None
    
    while True:
        match mostrar_sub_menu(lista_sub_menu):
            case '1':
                imprimir_heroes_genero_m(lista_personajes, "genero", "M", "nombre", "Nombre heroes M")
            case '2':
                imprimir_heroes_genero_f(lista_personajes, "genero", "F", "nombre", "Nombre heroes F")
            case '3':
                c, a = determinar_heroe_mas_alto_genero_m(lista_personajes, "genero", "M", "nombre", "altura")
            case '4':
                d, i = determinar_heroe_mas_alto_genero_f(lista_personajes, "genero", "F", "nombre", "altura")
            case '5':
                e, p = determinar_heroe_mas_bajo_genero_m(lista_personajes, "genero", "M", "nombre", "altura")
            case '6':
                f, o = determinar_heroe_mas_bajo_genero_f(lista_personajes, "genero", "F", "nombre", "altura")
            case '7':
                g = determinar_altura_promedio_heroes_genero_m(lista_personajes, "genero", "M", "altura")
            case '8':
                h = determinar_altura_promedio_heroes_genero_f(lista_personajes, "genero", "F", "altura")
            case '9':
                informar_nombre_del_heroe_asociado_a_indicadores_anteriores(c, d, e, f, g, h)
            case '10':
                determinar_cuantos_heroes_tienen_cada_tipo_de_color_de_ojos(lista_personajes, ['color_ojos'], ['Brown', 'Blue', 'Green', 
                                                                            'Yellow (without irises)', 'Hazel', 'Yellow', 'Silver', 'Red'])
            case '11':
                determinar_cuantos_heroes_tienen_cada_tipo_de_color_de_pelo(lista_personajes,['color_pelo'], ['Yellow', 'Brown',
                                                                            'Black', 'Auburn', 'Red / Orange', 'White',
                                                                            'No Hair', 'Blond', 'Green', 'Red', 'Brown / White'])                                                   
            case '12':
                determinar_cuantos_heroes_tienen_cada_tipo_de_inteligencia(lista_personajes, ['inteligencia'], ['No tiene', 'average',
                                                                            'good', 'high'])
            case '13':
                listar_todos_los_heroes_agrupados_por_color_de_ojos(lista_personajes, "color_ojos", "nombre")
            case '14':
                listar_todos_los_heroes_agrupados_por_color_de_pelo(lista_personajes, "color_pelo", "nombre")
            case '15':
                listar_todos_los_heroes_agrupados_por_tipo_de_inteligencia(lista_personajes, "inteligencia", "nombre")
            case '16':
                salir = salir_del_menu()
                if salir == 's':
                    break
        os.system("pause")

def salir_del_menu():
    while True:
        salir = input("Confirma salida?[s/n]")
        if salir.isalpha():
            if not (salir != 's' and salir != 'n'):
                break
            else:
                print(
                    "Solo puede seleccionar 's' para salir o 'n' para volver al menu principal")
        else:
            print("No se pueden ingresar numeros")
    return salir











