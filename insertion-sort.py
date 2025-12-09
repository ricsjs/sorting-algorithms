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

# exemplo de uso
lista = [5, 2, 4, 6, 1, 3]
print(insertion_sort(lista))
