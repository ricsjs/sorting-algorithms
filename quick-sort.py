import random
import time
import statistics
import sys

sys.setrecursionlimit(300000)

def partition(v, s, e):
    d = s - 1
    pivot = v[e]

    for i in range(s, e):
        if v[i] <= pivot:
            d += 1
            v[d], v[i] = v[i], v[d]

    v[d + 1], v[e] = v[e], v[d + 1]
    return d + 1


def quick_sort(v, s, e):
    if s < e:
        p = partition(v, s, e)
        quick_sort(v, s, p - 1)
        quick_sort(v, p + 1, e)


# -------------------------------
# Geradores de entrada
# -------------------------------
def melhor_caso(n):
    return [random.randint(0, n) for _ in range(n)]

def caso_medio(n):
    return [random.randint(0, n) for _ in range(n)]

def pior_caso(n):
    return list(range(n))


# -------------------------------
# Teste de carga
# -------------------------------
def teste_carga(gerador, tamanho, repeticoes=5):
    tempos = []

    for _ in range(repeticoes):
        v = gerador(tamanho)

        inicio = time.perf_counter()
        quick_sort(v, 0, len(v) - 1)
        fim = time.perf_counter()

        tempos.append(fim - inicio)

    return {
        "tamanho": tamanho,
        "tempo_medio": statistics.mean(tempos),
        "pior_tempo": max(tempos),
        "melhor_tempo": min(tempos)
    }


# -------------------------------
# Execução dos testes
# -------------------------------
tamanhos = [5000, 10000, 30000]

print("RESULTADOS – QUICK SORT\n")

for t in tamanhos:
    print(f"Tamanho do vetor: {t}\n")

    r_melhor = teste_carga(melhor_caso, t)
    r_medio = teste_carga(caso_medio, t)
    r_pior = teste_carga(pior_caso, t)

    print("Melhor caso (entrada aleatória):")
    print(f"  Tempo médio: {r_melhor['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_melhor['pior_tempo']:.6f} s\n")

    print("Caso médio (entrada aleatória):")
    print(f"  Tempo médio: {r_medio['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_medio['pior_tempo']:.6f} s\n")

    print("Pior caso (vetor ordenado):")
    print(f"  Tempo médio: {r_pior['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_pior['pior_tempo']:.6f} s")

    print("-" * 45)


# RESULTADOS – QUICK SORT

# Tamanho do vetor: 5000

# Melhor caso (entrada aleatória):
#   Tempo médio: 0.006060 s
#   Pior tempo:  0.006798 s

# Caso médio (entrada aleatória):
#   Tempo médio: 0.005894 s
#   Pior tempo:  0.007014 s

# Pior caso (vetor ordenado):
#   Tempo médio: 0.748855 s
#   Pior tempo:  0.756995 s
# ---------------------------------------------
# Tamanho do vetor: 10000

# Melhor caso (entrada aleatória):
#   Tempo médio: 0.010479 s
#   Pior tempo:  0.014240 s

# Caso médio (entrada aleatória):
#   Tempo médio: 0.009684 s
#   Pior tempo:  0.010442 s

# Pior caso (vetor ordenado):
#   Tempo médio: 3.033435 s
#   Pior tempo:  3.055557 s
# ---------------------------------------------
# Tamanho do vetor: 30000

# Melhor caso (entrada aleatória):
#   Tempo médio: 0.033155 s
#   Pior tempo:  0.037407 s

# Caso médio (entrada aleatória):
#   Tempo médio: 0.033371 s
#   Pior tempo:  0.034246 s

# Pior caso (vetor ordenado):
#   Tempo médio: 27.688466 s
#   Pior tempo:  27.754175 s
# ---------------------------------------------