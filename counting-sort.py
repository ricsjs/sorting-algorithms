import random
import time
import statistics

def counting_sort(v):
    n = len(v)

    s = min(v)
    b = max(v)

    size_c = b - s + 1
    c = [0] * size_c

    for i in range(n):
        c[v[i] - s] += 1

    for i in range(1, size_c):
        c[i] += c[i - 1]

    w = [0] * n

    for i in range(n - 1, -1, -1):
        d = v[i] - s
        w[c[d] - 1] = v[i]
        c[d] -= 1

    for i in range(n):
        v[i] = w[i]

    return v


# -------------------------------
# Função de teste de carga
# -------------------------------
def teste_carga(tamanho, repeticoes=10, intervalo=10000):
    tempos = []

    for _ in range(repeticoes):
        v = [random.randint(0, intervalo) for _ in range(tamanho)]

        inicio = time.perf_counter()
        counting_sort(v)
        fim = time.perf_counter()

        tempos.append(fim - inicio)

    return {
        "tamanho": tamanho,
        "tempo_medio": statistics.mean(tempos),
        "pior_caso": max(tempos),
        "melhor_caso": min(tempos)
    }


# -------------------------------
# Execução dos testes
# -------------------------------
tamanhos = [1000, 5000, 10000, 50000, 100000]
resultados = []

for t in tamanhos:
    resultado = teste_carga(t)
    resultados.append(resultado)

# -------------------------------
# Relatório
# -------------------------------
print("RESULTADOS DO TESTE DE CARGA - COUNTING SORT\n")
for r in resultados:
    print(f"Tamanho do vetor: {r['tamanho']}")
    print(f"Tempo médio: {r['tempo_medio']:.6f} segundos")
    print(f"Pior caso:   {r['pior_caso']:.6f} segundos")
    print(f"Melhor caso: {r['melhor_caso']:.6f} segundos")
    print("-" * 40)

# RESULTADOS DO TESTE DE CARGA - COUNTING SORT

# Tamanho do vetor: 1000
# Tempo médio: 0.001242 segundos
# Pior caso:   0.001473 segundos
# Melhor caso: 0.001151 segundos
# ----------------------------------------
# Tamanho do vetor: 5000
# Tempo médio: 0.002407 segundos
# Pior caso:   0.002609 segundos
# Melhor caso: 0.002317 segundos
# ----------------------------------------
# Tamanho do vetor: 10000
# Tempo médio: 0.004392 segundos
# Pior caso:   0.006247 segundos
# Melhor caso: 0.003899 segundos
# ----------------------------------------
# Tamanho do vetor: 50000
# Tempo médio: 0.017475 segundos
# Pior caso:   0.020179 segundos
# Melhor caso: 0.016210 segundos
# ----------------------------------------
# Tamanho do vetor: 100000
# Tempo médio: 0.032368 segundos
# Pior caso:   0.038332 segundos
# Melhor caso: 0.026031 segundos
# ----------------------------------------