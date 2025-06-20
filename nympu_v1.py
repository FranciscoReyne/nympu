# v1

"""
Esta idea se asemeja a una técnica conocida como *memoization* o almacenamiento en caché de resultados previamente calculados.
Esto puede ser mucho más rápido si los datos ya calculados se consultan con alta frecuencia y si el conjunto de posibles sumas es limitado.
Si estás sumando solo números enteros dentro de un rango razonable (digamos, de -1000 a 1000), puedes generar todos los posibles resultados de suma y almacenarlos en un diccionario en memoria, como una tabla de búsqueda:
Este enfoque evita el costo de cómputo repetitivo cuando se trata de muchas consultas con entradas ya conocidas. 

**Eso sí, todo depende del tamaño del espacio de búsqueda**: 
Si los números son muy grandes o aleatorios, puede que el costo de almacenar y buscar sea igual o mayor que simplemente sumar.

"""


# Crear dataset de sumas posibles
sum_cache = {(i, j): i + j for i in range(-1000, 1001) for j in range(-1000, 1001)}Add commentMore actions

def suma_rapida(a, b):
    return sum_cache.get((a, b), a + b)  # En caso de no encontrar, calcula directamente





