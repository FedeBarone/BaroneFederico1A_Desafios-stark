def mostrar_superheroes(lista_superheroes:list)->None:
    print("+==================+=============================+=============+=======+=======+=======+=======================+=============+======+============+")
    print(f"|    Nombre        |          Identidad          |   Empresa   | Altura|  Peso |Genero |     Color de ojos     |Color de pelo|Fuerza|Inteligencia|")
    print("+==================+=============================+=============+=======+=======+=======+=======================+=============+======+============+")
    for heroe in lista_superheroes:
        mostrar_heroe_fila(heroe)
        print("==================================================================================================================================================")

def mostrar_heroe_fila(heroe:dict)->None:
    print(f"|{heroe['nombre']:^18s}|{heroe['identidad']:^29s}|{heroe['empresa']:^13s}|{float(heroe['altura']):^7.2f}"
          f"|{float(heroe['peso']):^7.2f}|{heroe['genero']:^7s}|{heroe['color_ojos']:^23s}|{heroe['color_pelo']:^13s}"
          f"|{int(heroe['fuerza']):^6d}|{heroe['inteligencia']:^12s}|")
    
def mostrar_heroe(heroe:dict)->None:
    print(f"""Nombre: {heroe['nombre']:^18s}
Identidad: {heroe['identidad']:^29s}
Empresa: {heroe['empresa']:^13s}
Altura: {float(heroe['altura']):^7.2f}
Peso: {float(heroe['peso']):^7.2f}
Genero: {heroe['genero']:^7s}
Color ojos: {heroe['color_ojos']:^23s}
Color pelo: {heroe['color_pelo']:^13s}
Fuerza: {int(heroe['fuerza']):^6d}
Inteligencia: {heroe['inteligencia']:^12s}""")
    
def mostrar_lista(lista:list, titulo:str)->None:
    print("+==================+")
    print(f"|      {titulo}      |")
    print("+==================+")
    for item in lista:
        print(f"|{item:18s}|")
        print("====================")

def mostrar_campos(lista, key, value, key_dos):
    for elemento in lista:
        if elemento[key] == value:
            print(elemento[key_dos], [elemento[key]])
    print("=====================================================")

def mostrar_listas(lista:list, lista_dos, titulo:str, titulo_dos:str)->None:
    print("+==================+")
    print(f"|      {titulo}         {titulo_dos}      |")
    print("+==================+")
    for i in range(len(lista)):
        print(f"|{lista[i]:18s}|{lista_dos[i]:18s}")
        print("====================")
