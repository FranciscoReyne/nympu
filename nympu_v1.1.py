Vamos a medir el rendimiento de dos formas de hacer una suma: una usando el método tradicional y otra usando una caché precargada. Aquí tienes un pequeño ejemplo con `timeit`:

```python
import timeit

# Crear cache con sumas precalculadas
sum_cache = {(i, j): i + j for i in range(-1000, 1001) for j in range(-1000, 1001)}

def suma_caché(a, b):
    return sum_cache.get((a, b), a + b)

def suma_normal(a, b):
    return a + b

# Prueba de rendimiento
veces = 1_000_000
resultado_normal = timeit.timeit('suma_normal(123, 456)', globals=globals(), number=veces)
resultado_cache = timeit.timeit('suma_caché(123, 456)', globals=globals(), number=veces)

print(f"Suma normal: {resultado_normal:.6f} segundos")
print(f"Suma con caché: {resultado_cache:.6f} segundos")
```

Este código prueba un millón de veces ambas funciones. Lo puedes ajustar a tu necesidad (por ejemplo, probar con otros números o aumentar el rango de la caché).

💡 **¿Qué esperar?**  
La función con caché puede ser más rápida si se repiten muchas veces las mismas sumas, pero para una suma tan simple como `a + b`, la diferencia puede ser muy pequeña o incluso nula en algunos casos. Sin embargo, esta técnica **cobra más valor** cuando el cálculo subyacente es más complejo (por ejemplo, funciones costosas o llamadas a APIs).
