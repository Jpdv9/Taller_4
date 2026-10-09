import time
from concurrent.futures import ThreadPoolExecutor

import numpy as np


def suma_secuencial_python(matriz):
    total = 0
    for fila in matriz:
        for valor in fila:
            total += int(valor)
    return total


def suma_bloque_python(datos):
    matriz, fila_inicio, fila_fin, col_inicio, col_fin = datos

    total = 0
    for i in range(fila_inicio, fila_fin):
        fila = matriz[i]
        for j in range(col_inicio, col_fin):
            total += int(fila[j])

    return total


def ejercicio_1():
    print("EJERCICIO 1 - ARQUITECTURA SMP")

    np.random.seed(42)
    matriz = np.random.randint(0, 100, size=(1000, 1000), dtype=np.int64)

    inicio = time.perf_counter()
    suma_secuencial = suma_secuencial_python(matriz)
    tiempo_secuencial = time.perf_counter() - inicio

    tareas = []
    for fila in range(0, 1000, 100):
        for columna in range(0, 1000, 100):
            tareas.append((matriz, fila, fila + 100, columna, columna + 100))

    inicio = time.perf_counter()

    with ThreadPoolExecutor(max_workers=100) as executor:
        resultados = list(executor.map(suma_bloque_python, tareas))

    suma_paralela = sum(resultados)
    tiempo_paralelo = time.perf_counter() - inicio

    print(f"Suma secuencial : {suma_secuencial}")
    print(f"Suma paralela   : {suma_paralela}")
    print(f"Tiempo secuencial: {tiempo_secuencial:.6f} s")
    print(f"Tiempo paralelo  : {tiempo_paralelo:.6f} s")

    if tiempo_paralelo > 0:
        speedup = tiempo_secuencial / tiempo_paralelo
        print(f"Speedup          : {speedup:.4f}x")

    return tiempo_secuencial, tiempo_paralelo


if __name__ == "__main__":
    ejercicio_1()
