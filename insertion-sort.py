import random
import time
import statistics

def insertion_sort(A):
    n = len(A)

    for j in range(1, n):
        k = A[j]
        i = j - 1

        while i >= 0 and A[i] > k:
            A[i + 1] = A[i]
            i -= 1

        A[i + 1] = k

    return A


# -------------------------------
# Funções para gerar cenários
# -------------------------------
def melhor_caso(n):
    return list(range(n))

def caso_medio(n):
    return [random.randint(0, n) for _ in range(n)]

def pior_caso(n):
    return list(range(n, 0, -1))


# -------------------------------
# Função de teste de carga
# -------------------------------
def teste_carga(gerador, tamanho, repeticoes=5):
    tempos = []

    for _ in range(repeticoes):
        A = gerador(tamanho)

        inicio = time.perf_counter()
        insertion_sort(A)
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
tamanhos = [500, 1000, 2000, 5000]

print("RESULTADOS – INSERTION SORT\n")

for t in tamanhos:
    print(f"Tamanho do vetor: {t}\n")

    r_melhor = teste_carga(melhor_caso, t)
    r_medio = teste_carga(caso_medio, t)
    r_pior = teste_carga(pior_caso, t)

    print("Melhor caso (vetor ordenado):")
    print(f"  Tempo médio: {r_melhor['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_melhor['pior_tempo']:.6f} s\n")

    print("Caso médio (vetor aleatório):")
    print(f"  Tempo médio: {r_medio['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_medio['pior_tempo']:.6f} s\n")

    print("Pior caso (vetor inverso):")
    print(f"  Tempo médio: {r_pior['tempo_medio']:.6f} s")
    print(f"  Pior tempo:  {r_pior['pior_tempo']:.6f} s")

    print("-" * 45)


# RESULTADOS – INSERTION SORT

# Tamanho do vetor: 500

# Melhor caso (vetor ordenado):
#   Tempo médio: 0.000048 s
#   Pior tempo:  0.000051 s

# Caso médio (vetor aleatório):
#   Tempo médio: 0.003724 s
#   Pior tempo:  0.004272 s

# Pior caso (vetor inverso):
#   Tempo médio: 0.007927 s
#   Pior tempo:  0.010023 s
# ---------------------------------------------
# Tamanho do vetor: 1000

# Melhor caso (vetor ordenado):
#   Tempo médio: 0.000088 s
#   Pior tempo:  0.000097 s

# Caso médio (vetor aleatório):
#   Tempo médio: 0.017158 s
#   Pior tempo:  0.020541 s

# Pior caso (vetor inverso):
#   Tempo médio: 0.028878 s
#   Pior tempo:  0.029540 s
# ---------------------------------------------
# Tamanho do vetor: 2000

# Melhor caso (vetor ordenado):
#   Tempo médio: 0.000147 s
#   Pior tempo:  0.000151 s

# Caso médio (vetor aleatório):
#   Tempo médio: 0.065226 s
#   Pior tempo:  0.073743 s

# Pior caso (vetor inverso):
#   Tempo médio: 0.130967 s
#   Pior tempo:  0.155778 s
# ---------------------------------------------
# Tamanho do vetor: 5000

# Melhor caso (vetor ordenado):
#   Tempo médio: 0.000534 s
#   Pior tempo:  0.000546 s

# Caso médio (vetor aleatório):
#   Tempo médio: 0.594124 s
#   Pior tempo:  0.605237 s

# Pior caso (vetor inverso):
#   Tempo médio: 1.120473 s
#   Pior tempo:  1.153191 s
# ---------------------------------------------