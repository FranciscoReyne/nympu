import time
import random

# Crear cache con sumas precalculadas
range_value = 1000         # range_value
sum_cache = {(i, j): i + j for i in range(0, range_value+1) for j in range(0, range_value+1)}

def suma_caché(a, b):
    return sum_cache.get((a, b), a + b)

def suma_normal(a, b):
    return a + b

# Generar N_pares pares aleatorios
N_pares = 10              # N_pares pares aleatorios
pares = [(random.randint(-N_pares, N_pares), random.randint(-N_pares, N_pares)) for _ in range(N_pares)]

# Medir tiempo para suma normal
inicio_normal = time.perf_counter()
for a, b in pares:
    suma_normal(a, b)
fin_normal = time.perf_counter()
tiempo_normal = fin_normal - inicio_normal

# Medir tiempo para suma con caché
inicio_cache = time.perf_counter()
for a, b in pares:
    suma_caché(a, b)
fin_cache = time.perf_counter()
tiempo_cache = fin_cache - inicio_cache

print(f"Suma normal (N_pares pares): {tiempo_normal:.6f} segundos")
print(f"Suma con caché (N_pares pares): {tiempo_cache:.6f} segundos")
