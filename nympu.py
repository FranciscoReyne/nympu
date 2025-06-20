# Version 1.0.2

# Crear dataset de sumas posibles
sum_cache = {(i, j): i + j for i in range(-1000000000, 1000000001) for j in range(-1000000000, 1000000001)}

def suma_rapida(a, b):
    return sum_cache.get((a, b), a + b)  # En caso de no encontrar, calcula directamente
