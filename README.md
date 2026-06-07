
# Sistema de Gestión de Países

Trabajo Final Integrador – Programación I – UTN

## Estructura del proyecto:
- gestion_datos_paises.py
- informacion_paises.csv
- README.md
- Informe_trabajo_integrador.pdf

## Descripción:

Este programa permite administrar información de países almacenada en un archivo CSV.

El sistema carga los datos desde el archivo y ofrece distintas operaciones de consulta 
y actualización mediante un menú interactivo en consola.

Entre las funcionalidades disponibles se encuentran la incorporación de nuevos países, 
la actualización de datos existentes, la búsqueda y filtrado de información, 
el ordenamiento de registros y la generación de estadísticas generales.

## Funcionalidades

1- Agregar nuevos países al archivo.

2- Actualizar población y superficie de un país existente.

3- Buscar países por nombre (coincidencia exacta o parcial).

4- Filtrar países
	Filtrar países por continente.
	Filtrar países por rango de población.
	Filtrar países por rango de superficie.

5- Ordenar países
	Ordenar países por nombre.
	Ordenar países por población.
	Ordenar países por superficie.

6- Obtener estadísticas generales:
	País con mayor población.
	País con menor población.
	Promedio de población.
	Promedio de superficie.
	Cantidad de países por continente.

---------------------------------------------------------------------------------

## Instrucciones de uso

1- Ejecutar el archivo principal del programa.

2- Seleccionar una opción del menú.

3- Ingresar los datos solicitados.

El programa actualizará automáticamente el archivo CSV cuando corresponda.

## Ejemplos de uso

1- Agregar país

Entrada:

Nombre: Argentina
Población: 46000000
Superficie: 2780400 Km2
Continente: America

Salida:

País agregado correctamente.

3- Buscar país (coincidencia parcial o exacta)

Entrada:

Ingrese nombre: bar

Salida:

Nombre: Antigua & Barbuda | Población actual: 69108 | Superficie actual: 1147 Km2 | Continente: America

Nombre: Barbados | Población actual: 279912 | Superficie actual: 1116 Km2 | Continente: America

6- Estadísticas

Salida:

País con mayor población: [nombre del país]
País con menor población: [nombre del país]
Promedio de población: [valor]
Promedio de superficie: [valor] Km2

---------------------------------------------------------------------------------

## Fuente de datos:

El archivo CSV fue generado a partir de datasets públicos sobre países del mundo.

Adaptaciones realizadas:

Conservación únicamente de las columnas nombre, población, superficie y continente.
Conversión de superficie de millas cuadradas a kilómetros cuadrados (1 mi2 = 2,58999 km2).
Normalización de continentes a las categorías: Africa, America, Asia, Europa, Oceania y Antartida.

---------------------------------------------------------------------------------

## Requisitos

Python 3.10 o superior
Archivo informacion_paises.csv ubicado en la raíz del proyecto

---------------------------------------------------------------------------------

## Video explicativo

link: https://www.youtube.com/watch?v=C_BKAdEIrqw&t=1s

## Integrantes del proyecto:

Integrante 1:

Gualla, Mariano
- Desarrollo de funcionalidades
- Manejo del archivo CSV
- Validaciones 

Integrante 2:

Furfaro, Ivan
- Investigación 
- Pruebas del sistema
- Documentación

- Comision 21 
- Grupo 33
