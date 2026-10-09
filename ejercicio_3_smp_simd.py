import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def sumar_bloque_numpy(bloque):
    return int(np.sum(bloque, dtype=np.int64))


def ejercicio_integrador():
    print("EJERCICIO INTEGRADOR - SMP + SIMD")

    np.random.seed(2026)
    matriz = np.random.randint(0, 100, size=(10000, 10000), dtype=np.int32)

    inicio = time.perf_counter()
    suma_secuencial = int(np.sum(matriz, dtype=np.int64))
    tiempo_secuencial = time.perf_counter() - inicio

    bloques = []
    for fila in range(0, 10000, 1000):
        for columna in range(0, 10000, 1000):
            bloques.append(matriz[fila:fila + 1000, columna:columna + 1000])

    inicio = time.perf_counter()

    with ThreadPoolExecutor(max_workers=100) as executor:
        resultados = list(executor.map(sumar_bloque_numpy, bloques))

    suma_hibrida = sum(resultados)
    tiempo_hibrido = time.perf_counter() - inicio

    print(f"Suma secuencial : {suma_secuencial}")
    print(f"Suma SMP-SIMD   : {suma_hibrida}")
    print(f"Tiempo secuencial: {tiempo_secuencial:.6f} s")
    print(f"Tiempo SMP-SIMD  : {tiempo_hibrido:.6f} s")

    if tiempo_hibrido > 0:
        speedup = tiempo_secuencial / tiempo_hibrido
        print(f"Speedup          : {speedup:.4f}x")

    return tiempo_secuencial, tiempo_hibrido


if __name__ == "__main__":
    ejercicio_integrador()
