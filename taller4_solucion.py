from ejercicio_1_smp import ejercicio_1
from ejercicio_2_simd import ejercicio_2
from ejercicio_3_smp_simd import ejercicio_integrador


def main():
    print("TALLER 4")

    t1_seq, t1_par = ejercicio_1()
    t2_np, t2_py = ejercicio_2()
    t3_seq, t3_hib = ejercicio_integrador()

    print("RESUMEN")
    print(f"Ejercicio 1 - Secuencial : {t1_seq:.6f} s")
    print(f"Ejercicio 1 - SMP        : {t1_par:.6f} s")
    print(f"Ejercicio 2 - NumPy      : {t2_np:.6f} s")
    print(f"Ejercicio 2 - Python     : {t2_py:.6f} s")
    print(f"Ejercicio 3 - Secuencial : {t3_seq:.6f} s")
    print(f"Ejercicio 3 - SMP-SIMD   : {t3_hib:.6f} s")


if __name__ == "__main__":
    main()
