    
""" 
    ===========================
    Trabajo práctico integrador
    Gestión de datos de países
    Programación 1 
    ===========================
"""

import csv

# ========================
# Declaración de funciones
# ========================

# Funciones de validación
# Validación de entradas (Acepta espacios)
def validar_letras(mensaje):
    """
    Recibe como Parámetros: palabra (str)
    acepta espacios, para nombres que lo requieran
    Retorna: str() validado.
    """
    while True:

        palabra = input(mensaje)
        # Recorre cada carácter, si alguno no es letra ni espacio, vuelve a pedir la entrada
        if not all(c.isalpha() or c.isspace() for c in palabra) or not palabra.strip():

            print("\nSolo se aceptan letras y espacios")

            continue  

        # No permite 2 o mas espacios consecutivos
        if "  " in palabra:

            print("\nNo se permiten espacios consecutivos")

            continue
        
        # Retorna el valor sin espacios delante ni detrás
        return palabra.strip()


# Validación de entradas
def validar_numero_int(mensaje):
    """
    Pide input str()
    permite ingresar 0
    Retorna int(validado)
    """
    while True:

        num = input(mensaje)

        # verifica que solo se ingresen dígitos
        if not num.isdigit():

            print("Solo se aceptan números enteros positivos")

            continue

        num = int(num)

        return num


def crear_archivo_si_no_existe():
    """
    Se ejecuta al iniciar el programa
    verifica que el archivo csv exista.
    si no existe, lo crea con sus encabezados correspondientes
    """
    try:
        # Modo "x": crea el archivo únicamente si no existe
        with open("informacion_paises.csv", "x", newline= "", encoding = "utf-8") as archivo:

             # Crear escritor CSV
            escritor = csv.writer(archivo)

            # Escribir la fila de encabezados
            escritor.writerow(["nombre", "población", "superficie_km2", "continente"])

    # Si el archivo ya existe, no realiza ninguna acción
    # Y el programa se ejecuta normalmente
    except FileExistsError:

        pass


# Menú iterativo
def menu():
    print("""
=== Gestión de Datos de Países ===
1 - Agregar país
2 - Actualizar datos de país
3 - Buscar país
4 - Filtrar por datos
5 - Ordenar país
6 - Estadísticas
0 - Salir\n""")


# detener ejecución para visualización
def pausar_ejecucion():
    """ Realiza una pausa, hasta que el usuario ingrese una tecla """
    input("\nPresione una tecla para continuar...")

# =================================
# Funciones especificas de programa
# =================================

# Abrir el archivo, construir lector
def leer_archivo():
    """
    Esta función es para evitar repetir el bloque
    with open() en cada función que necesite leer el archivo CSV.
    Retorna:
    filas (list): Lista de diccionarios con los datos de cada país.
    encabezados (list): Lista con los nombres de las columnas.
    En caso de error, retorna (None, None)
    """
    try:

        with open("informacion_paises.csv", "r", newline="", encoding="utf-8") as archivo:
            # las claves, las genera de los encabezados
            # Y lee el archivo como un diccionario clave:valor
            lector = csv.DictReader(archivo)
            # Convertir todo el contenido del lector en una lista
            filas = list(lector)
            # Detecta los encabezados de las columnas del .csv
            encabezados = lector.fieldnames

            return filas, encabezados
    
    # El archivo aún no fue creado o la ruta es incorrecta
    except FileNotFoundError:
        print("Error: El archivo no existe")
        return None, None

    # Captura cualquier otro error inesperado y muestra su tipo
    except Exception as e:
        print("Error inesperado: ", type(e).__name__)
        return None, None


def fila_vacia(filas):
    """
    Retorna:
    True: Si no hay datos disponibles.
    False: Si existen filas para procesar.
    """

    # Valida que la lista exista y contenga registros

    if filas is None or len(filas) == 0:

        print("\nError: Faltan datos en el archivo")

        return True

    return False
    

# =========================
# Funcionalidad 1: Agregar 
# =========================
""" El programa permite crear un archivo desde 0, ingresando manualmente
cada país con sus datos asociados, pero se recomienda utilizar el dataset informacion_paises.csv"""

def agregar_pais(continentes):
    """
    Permite agregar un país con sus datos
    los carga en el archivo csv en tipo str()
    validando todas las entradas
    """
    # Se abre el archivo.csv en modo append
    with open("informacion_paises.csv", "a", newline = "", encoding = "utf-8") as archivo:

        # Se crea el escritor
        escritor = csv.writer(archivo)

        print("=== Agregar País ===")
                
        while True:

            # Ingresar nombre del país

            nombre = validar_letras("Ingrese nombre del país: ")

            # Verifica si el país existe dentro del archivo
            if pais_existe(nombre):

                print("El país ya se encuentra registrado")

                continue

            break
        
        # Los compos población y superficie, se validan en tipo str()
        # para poder ser añadidos al archivo csv

        while True:

            # Ingresar población del país

            poblacion = validar_numero_int("Ingrese población del país: ")

            if poblacion <= 0:

                print("La población de un país, no puede ser igual o menor a 0")

                continue
            
            # Convertir a str para poder agregar al archivo csv
            poblacion = str(poblacion)

            break

        while True:

            # Ingresar superficie del país

            superficie = validar_numero_int("Ingrese superficie en Km2 del país: ")

            if superficie <= 0:

                print("La superficie de un país, no puede ser igual o menor a 0 Km2")

                continue
            
            # Convertir a str para poder agregar al archivo csv
            superficie = str(superficie)

            break
                
        while True:

            # Ingresar continente del país
            print()

            # Muestra la lista de continentes disponibles
            for continente in continentes:

                print(f"{continente}", end = " | " )
            
            print()

            continente = validar_letras("Ingrese continente donde se encuentra el país: ")

            # Verifica si la entrada se encuentra dentro de la lista de continentes
            if not continente.capitalize() in continentes:

                print("\nEl continente ingresado no es valido\nIngrese nuevamente")

                continue

            break
        
        # Ingresa los datos en 1 sola fila al final del archivo
        escritor.writerow([nombre.title(), poblacion, superficie, continente.capitalize()])

        # Muestra confirmación 
        print("\n=== Nuevo país guardado correctamente ===")


# Verificar si la entrada existe en la columna del archivo
def pais_existe(nombre):
    """
    Recibe: nombre (str)
    Retorna: True si el país ya existe en el CSV, False si no.
    """
    filas, _ = leer_archivo()

    if fila_vacia(filas):
        
        return False

    # Verificar si el valor es igual a la entrada
    for linea in filas:

        if linea["nombre"].title() == nombre.title():

            return True
    
    return False


# ===========================
# Funcionalidad 2: Actualizar
# ===========================

def actualizar_pais():
    """
    Permite actualizar los datos de
    población y superficie de un país.

    Reescribe por completo el archivo original.
    """

    filas, encabezados = leer_archivo()

    # Si las filas están vacías, detiene la ejecución
    if fila_vacia(filas):

        return
    
    print("=== Actualizar datos de país ===")

    buscar_nombre = validar_letras("Seleccione un país: ")

    encontrado = False

    for linea in filas:

        # Buscar coincidencia exacta
        if buscar_nombre.title() == linea["nombre"]:

            encontrado = True

            print(f"\nPaís encontrado: {linea['nombre']}")

            # ========================
            # Mostrar población actual
            # ========================

            poblacion = linea["población"] or ""

            if poblacion.isdigit():

                print(f"=== Población: {poblacion} Habitantes ===")

            else:

                print("=== Población: Dato no disponible ===")

                return

            # =====================
            # Actualizar población
            # =====================

            while True:

                nueva_poblacion = validar_numero_int("Nueva población: ")

                if nueva_poblacion <= 0:

                    print("La población no puede ser menor o igual a 0")

                    continue
                 
                # Para darle consistencia al formato csv se convierte a tipo str
                linea["población"] = str(nueva_poblacion)

                break

            # =========================
            # Mostrar superficie actual
            # =========================

            superficie = linea["superficie_km2"] or ""

            if superficie.isdigit():

                print(f"=== Superficie: {superficie} Km2 ===")

            else:

                print("=== Superficie: Dato no disponible ===")

                return

            # =====================
            # Actualizar superficie
            # =====================

            while True:

                nueva_superficie = validar_numero_int("Nueva superficie: ")

                if nueva_superficie <= 0:

                    print("La superficie no puede ser menor o igual a 0 Km2")

                    continue
                
                # Para darle consistencia al formato csv se convierte a tipo str
                linea["superficie_km2"] = str(nueva_superficie)

                break

            break

    # Si no se encontró el país
    if not encontrado:

        print("\n=== País no encontrado ===")

        return

    # Reescribir el archivo completo con los datos modificados
    with open("informacion_paises.csv", "w", newline="", encoding="utf-8") as archivo:

        escritor = csv.DictWriter(archivo, fieldnames = encabezados)

        # Escribir encabezado
        escritor.writeheader()

        # Volcar todas las filas, al archivo
        escritor.writerows(filas)

    print("\n=== Información del país actualizada correctamente ===")


# ====================================
# Funcionalidad 3: Búsqueda por nombre
# ====================================

def buscar_pais():
    """
    Busca países por nombre, permitiendo coincidencias parciales.

    Muestra la información almacenada del país.

    Si algún dato se encuentra vacío o es inválido
    dentro del archivo CSV, se mostrará como "Dato no disponible".
    """

    filas, _ = leer_archivo()

    if fila_vacia(filas):
        return

    print("=== Buscar país ===")

    buscar_nombre = validar_letras("Seleccione un país: ").strip()

    encontrado = False

    print()

    # Recorre cada país almacenado en el archivo
    for linea in filas:

        # Si el nombre es None, se reemplaza por cadena vacía
        nombre = linea["nombre"] or ""

        # Buscar por coincidencia parcial
        if buscar_nombre.lower() in nombre.lower():

            encontrado = True

            # Obtiene los datos del país
            # Si alguno es None, se reemplaza por cadena vacía
            poblacion = linea["población"] or ""

            superficie = linea["superficie_km2"] or ""
            
            continente = linea["continente"] or ""

            # Verifica que la población sea numérica
            if poblacion.isdigit():

                poblacion = int(poblacion)

            else:

                poblacion = "Dato no disponible"

            # Verifica que la superficie sea numérica
            if superficie.isdigit():

                superficie = int(superficie)

            else:

                superficie = "Dato no disponible"

            # Verifica que el continente no esté vacío
            if continente.strip():

                continente = continente

            else:

                continente = "Dato no disponible"

            print("=== País encontrado ===")

            # Mostrar información encontrada
            print(f"Nombre: {nombre} | "
                f"Población actual: {poblacion} Habitantes | "
                f"Superficie actual: {superficie} Km2 | "
                f"Continente: {continente}\n")

    # Si no se encontró ninguna coincidencia
    if not encontrado:

        print("País no encontrado")


# ==============================
# Funcionalidad 4: Filtrar datos
# ==============================

def filtrar_datos(continentes):
    """
    Permite filtrar los países registrados
    según distintos criterios de búsqueda.
    Continente, Rango de población, Rango de superficie.

    Muestra únicamente los países que
    cumplen con la condición seleccionada
    por el usuario."""

    while True:

        # Mostrar submenu 
        print("Filtrar países por:\n"\
            "1 - Continente\n"\
            "2 - Rango de población\n"\
            "3 - Rango de superficie\n"\
            "0 - Volver al menú")
            
        opcion = validar_numero_int("-> ")

        print()

        filas, _ = leer_archivo()

        if fila_vacia(filas):

            return

        match opcion:

            case 1:

                # ==============================
                # busca por columna 'continente'
                # ==============================

                print("=== Filtrar países por continente ===")

                while True:

                    for continente in continentes:

                        # Mostrar continentes disponibles
                        print(f"{continente}",end=" | " )
            
                    print()

                    continente = validar_letras("Ingrese continente: ")

                    print()

                    # Verificar si el continente existe
                    if not continente.capitalize() in continentes:

                        print("\nEl continente ingresado no es valido\nIngrese nuevamente")

                        continue

                    break

                # En una nueva lista, guarda cada elemento que pertenezca al continente declarado
                encontrados = []

                try:

                    for fila in filas:

                        if fila['continente'].capitalize() == continente.capitalize():

                            encontrados.append(fila)
                    
                    if not encontrados:

                        print("No hay países registrados en ese continente")
                
                except AttributeError:

                    print("\nError: Hay países sin continente registrado\n")
                
                except Exception as e:
                    
                    print("Ha ocurrido un error inesperado: ", type(e).__name__)
                
                # Solo mostrara el nombre de los países que pertenezcan al continente declarado

                print(f"Países en {continente.capitalize()}:")

                for linea in encontrados:

                    print(f"- {linea['nombre']}")

                break

            case 2:

                # ==============================
                # busca por columna 'población'
                # ==============================

                print("=== Filtran por rango de población ===")

                while True:

                    # Pide al usuario declarar rango mínimo y máximo de búsqueda
                    minimo = validar_numero_int("Rango mínimo: ")
                    maximo = validar_numero_int("Rango máximo: ")

                    if minimo > maximo:

                        print("El rango mínimo no puede ser mayor que el rango máximo")

                        continue

                    break

                print("-"*65)

                encontrados = []

                for fila in filas:
                    
                    # Guardar el valor de población, si no tiene lo guarda como vació
                    poblacion = fila['población'] or ""

                    # Si el valor no es numérico, lo ignora

                    if not poblacion.isdigit():

                        continue

                    if minimo <= int(poblacion) <= maximo:

                        encontrados.append(fila)

                if not encontrados:

                    print("No hay países en ese rango de población\n")

                else:
                    
                    # Mostrar resultados
                    for linea in encontrados:

                        print(f"{linea['nombre']} | Población: {linea['población']} Habitantes")
            
                print()

            case 3:

                # ===================================
                # busca por columna 'superficie_km2'
                # ===================================

                print("=== Filtran por rango de superficie ===")

                while True:

                    # Pide al usuario declarar rango mínimo y máximo de búsqueda
                    minimo = validar_numero_int("Rango mínimo: ")
                    maximo = validar_numero_int("Rango máximo: ")

                    if minimo > maximo:

                        print("El rango mínimo no puede ser mayor que el rango máximo")

                        continue

                    break

                print("-"*65)

                encontrados = []

                for fila in filas:

                    superficie = fila['superficie_km2'] or ""

                    if not superficie.isdigit():

                        continue

                    if minimo <= int(superficie) <= maximo:

                        encontrados.append(fila)

                if not encontrados:

                    print("No hay países en ese rango de superficie\n")
                
                else:

                    # Mostrar resultados
                    for linea in encontrados:

                        print(f"{linea['nombre']} | Superficie: {linea['superficie_km2']} Km2")
                
                print()

            case 0:

                break
            
            # Si se ingresa un rango invalido re vuelve a iterar el bucle
            case _:

                print("\n=== Opción Invalida ===")

                pausar_ejecucion()


# ==============================
# Funcionalidad 5: Ordenar datos
# ==============================


def ordenar_datos():
    """
    Permite ordenar los países almacenados en el archivo CSV.

    El usuario puede elegir ordenar los datos por:
    - Nombre.
    - Población (orden ascendente o descendente).
    - Superficie (orden ascendente o descendente).
    """
    while True:

        # Mostrar submenu
        print("Ordenar países por:\n"\
            "1 - Nombre\n"\
            "2 - Población\n"\
            "3 - Superficie\n"\
            "0 - Volver al menú")

        opcion = validar_numero_int("-> ")

        filas, _ = leer_archivo()

        if fila_vacia(filas):

            return

        match opcion:

            case 1:

                # ==================
                # Ordenar por nombre
                # ==================
                
                print("\n=== Países ordenados por nombre ===")

                filas_ordenadas = ordenamiento(filas, 'nombre',1)

                for fila in filas_ordenadas:

                    print(f"{fila['nombre']}")
                
                pausar_ejecucion()


            case 2:

                # =====================
                # Ordenar por población
                # =====================

                while True:

                    # El usuario puede elegir el tipo de orden en poblacion
                    print("--------------------")
                    print("1 - Orden ascendente\n" \
                        "2 - Orden descendente\n" \
                        "0 - Para volver al menú")
                    
                    opcion = validar_numero_int("-> ")

                    break

                print("\n=== Países ordenados por población ===")

                filas_ordenadas = ordenamiento(filas, 'población', opcion)

                for fila in filas_ordenadas:

                    print(f"{fila['nombre']} | Población: {fila['población']} Habitantes")

                pausar_ejecucion()


            case 3:

                # ======================
                # Ordenar por superficie
                # ======================

                while True:

                    # El usuario puede elegir el tipo de orden en superficie
                    print("--------------------")
                    print("1 - Orden ascendente\n" \
                        "2 - Orden descendente\n" \
                        "0 - Para volver al menú")
                    
                    opcion = validar_numero_int("-> ")

                    break
                    
                print("\n=== Países ordenados por superficie ===")

                filas_ordenadas = ordenamiento(filas, 'superficie_km2', opcion)

                for fila in filas_ordenadas:

                    print(f"{fila['nombre']} | Superficie: {fila['superficie_km2']} Km2")

                pausar_ejecucion()


            case 0:

                break


            # Si se ingresa un rango invalido se vuelve a iterar el bucle
            case _:
                
                print("\n=== Opción Invalida ===")

                pausar_ejecucion()


def ordenamiento(filas, columna, opcion):
    """
    Ordena una lista de diccionarios mediante
    el método burbuja según la columna indicada.
    """

    cantidad_elementos = len(filas)

    for i in range(cantidad_elementos - 1):

        hizo_intercambio = False

        for j in range(cantidad_elementos - 1 - i):
            
            # Se guardan los elementos que se compararan en cada iteración
            valor_actual = filas[j][columna]

            valor_siguiente = filas[j + 1][columna]

            # Si la columna es numérica
            if columna in ["población", "superficie_km2"]:

                # Si el valor no es numérico, lo ignora
                if not valor_actual.isdigit():

                    continue

                if not valor_siguiente.isdigit():

                    continue
                
                # Convertir a int para comparar
                valor_actual = int(valor_actual)
                valor_siguiente = int(valor_siguiente)

            # Comparación ascendente
            if opcion == 1:

                if valor_actual > valor_siguiente:

                    # Intercambia las posiciones de los elementos si se cumple la condición
                    filas[j], filas[j + 1] = filas[j + 1], filas[j]

                    hizo_intercambio = True
                    
            # Comparación descendente
            elif opcion == 2:
                
                if valor_actual < valor_siguiente:

                    filas[j], filas[j + 1] = filas[j + 1], filas[j]

                    hizo_intercambio = True

        if not hizo_intercambio:

            break

    return filas


# =============================
# Funcionalidad 6: Estadísticas
# =============================

def poblacion_minima_y_maxima():
    """
    Busca y muestra el país con mayor y menor población

    Ignora aquellos países que no tengan una población
    válida registrada.
    """

    filas, _ = leer_archivo()

    if fila_vacia(filas):

        return

    # Valores iniciales para las comparaciones
    pais_menor_poblacion = float("inf")
    pais_mayor_poblacion = float("-inf")

    nombre_pais_menor = ""
    nombre_pais_mayor = ""

    # Recorre cada país del archivo
    for fila in filas:

        # Si en la fila falta el valor de columna continente
        # lo ignora por falta de datos
        if not fila['continente']:

            continue

        # Si la población está vacía o contiene texto, ignora el registro
        if not (fila["población"] or "").isdigit():

            continue

        poblacion = int(fila["población"])

        # Buscar menor población
        if poblacion < pais_menor_poblacion:

            pais_menor_poblacion = poblacion

            nombre_pais_menor = fila["nombre"]

        # Buscar mayor población
        if poblacion > pais_mayor_poblacion:

            pais_mayor_poblacion = poblacion

            nombre_pais_mayor = fila["nombre"]

    # Verifica si encontró al menos un país válido
    if pais_menor_poblacion == float("inf"):

        print("No hay datos de población válidos")

        return

    print("\n=== Estadísticas ===")

    print("\nPaís con menor población:")

    print(f"{nombre_pais_menor} | Población: {pais_menor_poblacion} Habitantes")

    print("\nPaís con mayor población:")

    print(f"{nombre_pais_mayor} | Población: {pais_mayor_poblacion} Habitantes")


def promedio_poblacion_superficie():
    """
    Calcula y muestra el promedio mundial de población
    y superficie utilizando los datos válidos del archivo CSV.

    Ignora los países que tengan población o superficie
    vacías o inválidas.
    """

    filas, _ = leer_archivo()

    if fila_vacia(filas):

        return
    
    # ==========================
    # Promedio de población
    # ==========================

    # Va guardando los valores de población
    sumatoria_poblacion = 0

    # Se utiliza para dividir sumatoria_poblacion por la cantidad de países a promediar
    cantidad_paises = 0

    for fila in filas:

        # Si en la fila falta el valor de columna continente
        # lo ignora por falta de datos
        if not fila['continente']:

            continue

        # Si el valor es None, lo reemplaza por ""
        poblacion = fila["población"] or ""

        # Ignora datos vacíos o inválidos
        if not poblacion.isdigit():

            continue

        sumatoria_poblacion += int(poblacion)

        cantidad_paises += 1

    print("\n=== Promedio de población ===")

    if cantidad_paises > 0:

        # Calcular promedio
        print(f"Mundial: {sumatoria_poblacion // cantidad_paises} Habitantes")

    else:

        print("No hay datos de población válidos")

    # ==========================
    # Promedio de superficie
    # ==========================

    # Va guardando los valores de superficie
    sumatoria_superficie = 0

    # Se utiliza para dividir sumatoria_poblacion por la cantidad de países a promediar
    cantidad_paises = 0

    for fila in filas:

        # Si el valor es None, lo reemplaza por ""
        superficie = fila["superficie_km2"] or ""

        # Ignora datos vacíos o inválidos
        if not superficie.isdigit():

            continue

        sumatoria_superficie += int(superficie)

        cantidad_paises += 1

    print("\n=== Promedio de superficie ===")

    if cantidad_paises > 0:

        # Calcular promedio
        print(f"Mundial: {sumatoria_superficie // cantidad_paises} km2")

    else:

        print("No hay datos de superficie válidos")


def paises_por_continente(continentes):
    """
    Cuenta y muestra la cantidad de países registrados
    por cada continente.
    """
    filas, _ = leer_archivo()

    if fila_vacia(filas):

        return
    
    # Lista donde se almacenan los continentes encontrados
    lista_continentes = []

    # Guarda los continentes válidos
    for fila in filas:

        # Verificar que el valor se encuentre en continentes
        if fila['continente'] in continentes:

            lista_continentes.append(fila['continente'])

    # Recorre continentes sin repetir y cuenta ocurrencias
    print("\n=== Cantidad de países por continente ===")

    # Elimina los duplicados convirtiendo a set
    for continente in set(lista_continentes):
        
        # Muestra cantidad de países por cada continente
        print(f"{continente}: {lista_continentes.count(continente)}")


# ========================
#          Main
# ========================

def main():

    """
    Punto de entrada principal del programa.

    Inicializa los recursos necesarios,
    muestra el menú de opciones y dirige
    el flujo de ejecución hacia la
    funcionalidad seleccionada por el usuario.
    """

    crear_archivo_si_no_existe()

    continentes = ["Africa", "America", "Asia", "Europa", "Oceania", "Antartida"]

    while True:

        menu()   

        opcion = validar_numero_int("-> ")

        match opcion:

            case 1:
                
                agregar_pais(continentes)

                pausar_ejecucion()

            case 2:
                
                actualizar_pais()

                pausar_ejecucion()

            case 3:
                
                buscar_pais()

                pausar_ejecucion()
            
            case 4:
                
                filtrar_datos(continentes)

                pausar_ejecucion()

            case 5:
                
                ordenar_datos()

                pausar_ejecucion()

            case 6:
                
                poblacion_minima_y_maxima()

                promedio_poblacion_superficie()

                paises_por_continente(continentes)

                pausar_ejecucion()

            case 0:
                
                print("\n=== Programa finalizado ===\n")

                break
            
            case _:
                print("=== Opción inválida ===")

                pausar_ejecucion()

# Ejecuta main() solo si este archivo es el programa principal
if __name__=="__main__":
        main()