import random
import time
import statistics

def selection_sort(v):
    n = len(v)

    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if v[m] > v[j]:
                m = j
        v[m], v[i] = v[i], v[m]

    return v


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
        selection_sort(v)
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

print("RESULTADOS – SELECTION SORT\n")

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

# RESULTADOS – SELECTION SORT

# Tamanho do vetor: 500

# Vetor ordenado:
#   Tempo médio: 0.006030 s
#   Pior tempo:  0.007270 s

# Vetor aleatório:
#   Tempo médio: 0.005884 s
#   Pior tempo:  0.007386 s

# Vetor inverso:
#   Tempo médio: 0.004910 s
#   Pior tempo:  0.005217 s
# ---------------------------------------------
# Tamanho do vetor: 1000

# Vetor ordenado:
#   Tempo médio: 0.022298 s
#   Pior tempo:  0.024502 s

# Vetor aleatório:
#   Tempo médio: 0.020992 s
#   Pior tempo:  0.022204 s

# Vetor inverso:
#   Tempo médio: 0.020502 s
#   Pior tempo:  0.020708 s
# ---------------------------------------------
# Tamanho do vetor: 2000

# Vetor ordenado:
#   Tempo médio: 0.079922 s
#   Pior tempo:  0.083647 s

# Vetor aleatório:
#   Tempo médio: 0.081404 s
#   Pior tempo:  0.084051 s

# Vetor inverso:
#   Tempo médio: 0.082879 s
#   Pior tempo:  0.082998 s
# ---------------------------------------------
# Tamanho do vetor: 5000

# Vetor ordenado:
#   Tempo médio: 0.485535 s
#   Pior tempo:  0.500473 s

# Vetor aleatório:
#   Tempo médio: 0.356142 s
#   Pior tempo:  0.372383 s

# Vetor inverso:
#   Tempo médio: 0.359511 s
#   Pior tempo:  0.361624 s
# ---------------------------------------------