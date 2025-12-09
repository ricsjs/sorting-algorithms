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


# exemplo de uso:
lista = [10, 7, 8, 9, 1, 5]
quick_sort(lista, 0, len(lista) - 1)
print(lista)
