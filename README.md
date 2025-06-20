# NymPu
Framework de idea de libreria python para hacer sumas más rapidas que con numpy.

Este código debería ejecutar sumas más rápido que NumPy en ciertos casos de operaciones.


# v1


Esta idea se asemeja a una técnica conocida como *memoization* o almacenamiento en caché de resultados previamente calculados.
Esto puede ser mucho más rápido si los datos ya calculados se consultan con alta frecuencia y si el conjunto de posibles sumas es limitado.
Si estás sumando solo números enteros dentro de un rango razonable (digamos, de -1000 a 1000), puedes generar todos los posibles resultados de suma y almacenarlos en un diccionario en memoria, como una tabla de búsqueda:
Este enfoque evita el costo de cómputo repetitivo cuando se trata de muchas consultas con entradas ya conocidas. 

**Eso sí, todo depende del tamaño del espacio de búsqueda**: 
Si los números son muy grandes o aleatorios, puede que el costo de almacenar y buscar sea igual o mayor que simplemente sumar.

---





