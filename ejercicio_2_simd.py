import time

import matplotlib.pyplot as plt
import numpy as np


def multiplicacion_matrices_python(A, B):
    """
    Multiplicación de matrices con bucles tradicionales.
    Se usa el orden i-k-j para reducir accesos repetidos y
    hacer la implementación razonablemente eficiente en Python.
    """
    filas_a = len(A)
    comun = len(B)
    columnas_b = len(B[0])

    resultado = [
        [0.0 for _ in range(columnas_b)]
        for _ in range(filas_a)
    ]

    for i in range(filas_a):
        fila_a = A[i]
        fila_resultado = resultado[i]

        for k in range(comun):
            aik = fila_a[k]
            fila_b = B[k]

            for j in range(columnas_b):
                fila_resultado[j] += aik * fila_b[j]

    return resultado


def ejercicio_2():

    print("EJERCICIO 2 - ARQUITECTURA SIMD")

    np.random.seed(123)
    A_np = np.random.rand(1000, 1000)
    B_np = np.random.rand(1000, 1000)

    inicio = time.perf_counter()
    resultado_numpy = A_np @ B_np
    tiempo_numpy = time.perf_counter() - inicio

    A_py = A_np.tolist()
    B_py = B_np.tolist()

    inicio = time.perf_counter()
    resultado_python = multiplicacion_matrices_python(A_py, B_py)
    tiempo_python = time.perf_counter() - inicio

    resultado_python_np = np.array(resultado_python)
    error_maximo = np.max(np.abs(resultado_numpy - resultado_python_np))

    print(f"Tiempo NumPy       : {tiempo_numpy:.6f} s")
    print(f"Tiempo Python puro : {tiempo_python:.6f} s")

    if tiempo_numpy > 0:
        factor = tiempo_python / tiempo_numpy
        print(f"Python/NumPy       : {factor:.2f}x")

    print("\nComparación")
    print(f"{'Método':<20} {'Tiempo (s)':>15}")
    print("-" * 45)
    print(f"{'NumPy':<20} {tiempo_numpy:>15.6f}")
    print(f"{'Python tradicional':<20} {tiempo_python:>15.6f}")

    metodos = ["NumPy", "Python tradicional"]
    tiempos = [tiempo_numpy, tiempo_python]

    plt.figure(figsize=(8, 5))
    plt.bar(metodos, tiempos)
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación de tiempos - Multiplicación 1000x1000")
    plt.tight_layout()
    plt.savefig("comparacion_ejercicio_2.png", dpi=150)
    plt.show()

    return tiempo_numpy, tiempo_python


if __name__ == "__main__":
    ejercicio_2()
