import random
import time
import statistics
import sys

sys.setrecursionlimit(300000)

def merge(v, s, m, e):
    p = s
    q = m + 1
    w = []

    for _ in range(e - s + 1):
        if (q > e) or (p <= m and v[p] < v[q]):
            w.append(v[p])
            p += 1
        else:
            w.append(v[q])
            q += 1

    for i in range(e - s + 1):
        v[s + i] = w[i]


def merge_sort(v, s, e):
    if s < e:
        m = (s + e) // 2
        merge_sort(v, s, m)
        merge_sort(v, m + 1, e)
        merge(v, s, m, e)


# -------------------------------
# Geradores de entrada
# -------------------------------
def melhor_caso(n):
    return list(range(n))

def caso_medio(n):
    return [random.randint(0, n) for _ in range(n)]

def pior_caso(n):
    return list(range(n, 0, -1))


# -------------------------------
# Teste de carga
# -------------------------------
def teste_carga(gerador, tamanho, repeticoes=5):
    tempos = []

    for _ in range(repeticoes):
        v = gerador(tamanho)

        inicio = time.perf_counter()
        merge_sort(v, 0, len(v) - 1)
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
tamanhos = [5000, 10000, 50000, 100000]

print("RESULTADOS – MERGE SORT\n")

for t in tamanhos:
    print(f"Tamanho do vetor: {t}\n")

    r_melhor = teste_carga(melhor_caso, t)
    r_medio = teste_carga(caso_medio, t)
    r_pior = teste_carga(pior_caso, t)

    print("Vetor ordenado:")
    print(f"  Tempo médio: {r_melhor['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_melhor['pior_tempo']:.6f} s\n")

    print("Vetor aleatório:")
    print(f"  Tempo médio: {r_medio['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_medio['pior_tempo']:.6f} s\n")

    print("Vetor inverso:")
    print(f"  Tempo médio: {r_pior['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_pior['pior_tempo']:.6f} s")

    print("-" * 45)

# RESULTADOS – MERGE SORT

# Tamanho do vetor: 5000

# Vetor ordenado:
#   Tempo médio: 0.011824 s
#   Pior tempo:  0.013236 s

# Vetor aleatório:
#   Tempo médio: 0.014186 s
#   Pior tempo:  0.017744 s

# Vetor inverso:
#   Tempo médio: 0.011305 s
#   Pior tempo:  0.012267 s
# ---------------------------------------------
# Tamanho do vetor: 10000

# Vetor ordenado:
#   Tempo médio: 0.025012 s
#   Pior tempo:  0.027820 s

# Vetor aleatório:
#   Tempo médio: 0.026156 s
#   Pior tempo:  0.026880 s

# Vetor inverso:
#   Tempo médio: 0.023634 s
#   Pior tempo:  0.024612 s
# ---------------------------------------------
# Tamanho do vetor: 50000

# Vetor ordenado:
#   Tempo médio: 0.141932 s
#   Pior tempo:  0.145563 s

# Vetor aleatório:
#   Tempo médio: 0.155727 s
#   Pior tempo:  0.161013 s

# Vetor inverso:
#   Tempo médio: 0.123677 s
#   Pior tempo:  0.139277 s
# ---------------------------------------------
# Tamanho do vetor: 100000

# Vetor ordenado:
#   Tempo médio: 0.205252 s
#   Pior tempo:  0.210122 s

# Vetor aleatório:
#   Tempo médio: 0.230788 s
#   Pior tempo:  0.240558 s

# Vetor inverso:
#   Tempo médio: 0.195375 s
#   Pior tempo:  0.196568 s
# ---------------------------------------------