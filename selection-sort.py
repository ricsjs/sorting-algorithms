def selection_sort(v):
    n = len(v)
    
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if v[m] > v[j]:
                m = j
        v[m], v[i] = v[i], v[m]
    
    return v

# exemplo de uso
lista = [64, 25, 12, 22, 11]
ordenada = selection_sort(lista)
print(ordenada)
