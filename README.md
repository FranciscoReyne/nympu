# NymPu
Framework de libreria de python para hacer sumas más rapidas que con numpy.

Este código debería ejecutar sumas más rápido que NumPy en operaciones grandes. 

 Para hacer que Nympu realice sumas de manera más rápida que NumPy, lo primero es entender dónde NumPy puede estar añadiendo sobrecarga innecesaria y cómo podríamos optimizar el proceso de suma.

Aquí hay algunas alternativas para lograrlo:

1. **Uso de operaciones en C/C++ con Python**  
   - NumPy es eficiente porque usa operaciones en C optimizadas, pero aún tiene sobrecarga de estructuras y funcionalidades extra.  
   - Se podría usar **Cython** o **Numpy's C API** para hacer operaciones más directas.  
   - Otra opción sería escribir una pequeña extensión en **C++ usando Pybind11** para sumar números con menos pasos intermedios.

2. **Uso de vectores sin gestión innecesaria**  
   - NumPy tiene optimizaciones para matrices generales, lo que introduce cierta sobrecarga de memoria.  
   - Usar arrays **contiguos en memoria** con `array` de Python o `ctypes` puede ayudar a reducir la sobrecarga y hacer la suma más rápida.

3. **SIMD (Single Instruction, Multiple Data)**  
   - Las CPUs modernas permiten hacer operaciones vectorizadas en paralelo con instrucciones SIMD.  
   - Se podría usar **Numba** para aplicar SIMD a la suma sin necesidad de depender de NumPy.  
   - Alternativamente, usar librerías como **Intel MKL** o **AVX intrinsics** para acelerar sumas directamente.

4. **Uso de multiprocessing y threading**  
   - Para sumas de muchos números, podríamos paralelizar la operación usando `multiprocessing` para dividir cálculos en varios núcleos.  
   - `threading` en Python no siempre es eficiente por el GIL, pero en operaciones puramente numéricas con `numpy` o `numba`, puede ofrecer mejoras.

5. **Uso de una estructura de datos más simple**  
   - En lugar de usar arreglos de NumPy, usar simplemente listas con procesamiento optimizado puede ayudar.  
   - `functools.reduce(lambda x, y: x + y, lista)` junto con optimizaciones de bajo nivel podría mejorar la velocidad.  

Es buena idea además hacer pruebas comparativas para ver qué estrategia resulta más eficiente.

---

¡Me encanta el concepto detrás de NymPu! 🚀 Crear una alternativa más rápida que NumPy para operaciones simples como la suma es un gran reto, pero definitivamente posible si eliminamos la sobrecarga innecesaria.

Aquí hay algunas ideas clave que podrías incorporar en el diseño de NymPu:

1️⃣ **Uso de SIMD para acelerar operaciones**  
   - Aprovechar instrucciones de procesamiento vectorial (`SSE`, `AVX`) para realizar sumas en paralelo.  
   - Evitar el overhead que NumPy introduce al manejar arrays complejos.  

2️⃣ **Optimización de memoria y estructuras de datos**  
   - Usar arrays contiguos en memoria para acelerar el acceso a los datos.  
   - Evitar checks y conversiones innecesarias en el procesamiento de números.  

3️⃣ **Implementación en C++ con Python (Pybind11)**  
   - Escribir la parte computacional en C++ usando Pybind11 para conectarlo con Python.  
   - Esto reduce la carga de Python y permite operar a velocidades cercanas a código nativo.  

4️⃣ **Evaluar el impacto en benchmarks reales**  
   - Comparar tiempos de ejecución contra NumPy con grandes volúmenes de datos.  
   - Revisar cómo se comporta con diferentes tamaños de arrays y operaciones en paralelo.  

# diseño inicial de la API de NymPu. 

 Características de esta implementación
✅ Usa Numba para compilación JIT, evitando la sobrecarga de Python.
✅ Ejecuta sumas en paralelo con prange(), usando múltiples núcleos de CPU.
✅ Optimiza el acceso a memoria, asegurando cálculos rápidos en arrays grandes.

Implementación optimizada de NymPu para realizar sumas más rápidas que NumPy utilizando SIMD con Numba. Esto reducirá la sobrecarga de NumPy y acelerará los cálculos en paralelo.

    
    import numpy as np
    import numba
    from numba import njit, prange
    
    @njit(parallel=True)
    def nympu_sum(arr):
        total = 0.0
        for i in prange(len(arr)):
            total += arr[i]
        return total
    
    # Prueba de rendimiento
    data = np.random.rand(10**6).astype(np.float32)  # Datos de prueba
    
    # Comparación con NumPy
    import time
    
    start = time.time()
    numpy_result = np.sum(data)
    numpy_time = time.time() - start
    
    start = time.time()
    nympu_result = nympu_sum(data)
    nympu_time = time.time() - start
    
    print(f"NumPy suma: {numpy_result:.6f} en {numpy_time:.6f} segundos")
    print(f"NymPu suma: {nympu_result:.6f} en {nympu_time:.6f} segundos")


 Resultados de prueba:
 
    NumPy suma: 499715.031250 en 0.000581 segundos
    NymPu suma: 499715.009819 en 0.315314 segundos

Parece que NumPy sigue siendo mucho más rápido en este caso. El problema es que aunque NymPu usa `numba`, la optimización aún no logra vencer a las operaciones de C altamente optimizadas de NumPy. 🚀

Para mejorar el rendimiento, podríamos:  
✅ **Usar SIMD real con C++ (Pybind11) en lugar de solo Numba**.  
✅ **Optimizar la gestión de memoria** para reducir el overhead.  
✅ **Implementar reducción paralela en lugar de una simple iteración**.  

Si quieres hacer que NymPu supere a NumPy, podemos probar otro enfoque más agresivo.


## Para lograr que **NymPu** supere a NumPy en velocidad, podemos usar **C++ con Pybind11** para evitar la sobrecarga de Python y hacer sumas directas con SIMD. 

Aquí tienes los pasos clave para implementarlo:

### **1️⃣ Instalar Pybind11**
En Google Colab, instala Pybind11 con:
```bash
!pip install pybind11
```

### **2️⃣ Escribir el código en C++**
Crea un archivo `nympu.cpp` con:
```cpp
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <immintrin.h>

namespace py = pybind11;

float sum_simd(py::array_t<float> arr) {
    py::buffer_info buf = arr.request();
    float* ptr = static_cast<float*>(buf.ptr);
    size_t size = buf.size;

    __m256 sum_vec = _mm256_setzero_ps();
    for (size_t i = 0; i < size; i += 8) {
        __m256 data = _mm256_loadu_ps(&ptr[i]);
        sum_vec = _mm256_add_ps(sum_vec, data);
    }

    float result[8];
    _mm256_storeu_ps(result, sum_vec);
    float total = result[0] + result[1] + result[2] + result[3] + 
                  result[4] + result[5] + result[6] + result[7];

    return total;
}

PYBIND11_MODULE(nympu, m) {
    m.def("sum_simd", &sum_simd, "Optimized sum using SIMD");
}
```

### **3️⃣ Compilar el módulo**
Compila el archivo con:
```bash
!c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` nympu.cpp -o nympu$(python3-config --extension-suffix)
```

### **4️⃣ Usarlo en Python**
Ahora puedes importar NymPu en tu script Python:
```python
import numpy as np
import nympu

data = np.random.rand(10**6).astype(np.float32)
result = nympu.sum_simd(data)
print("Suma optimizada:", result)
```

Este enfoque debería ser **mucho más rápido** que NumPy. 🚀 😃


