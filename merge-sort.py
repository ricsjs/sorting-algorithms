def merge(v, s, m, e):
    p = s
    q = m + 1
    w = []  # vetor aux

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


# exemplo de uso:
lista = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista, 0, len(lista) - 1)
print(lista)
