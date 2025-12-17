# Relatório – Análise de Algoritmos de Ordenação

## Introdução

Os algoritmos de ordenação são fundamentais na Ciência da Computação, sendo amplamente utilizados em sistemas que necessitam organizar dados para otimizar buscas, comparações e análises. Neste relatório, são analisados cinco algoritmos de ordenação: Insertion Sort, Selection Sort, Merge Sort, Quick Sort e Counting Sort.
A avaliação considera tanto a análise teórica de complexidade quanto o desempenho prático, obtido por meio de testes de carga com diferentes tamanhos e configurações de entrada.

---

## Insertion Sort

### Descrição

O Insertion Sort é um algoritmo simples que constrói a lista ordenada gradualmente, inserindo cada elemento na posição correta em relação aos elementos já ordenados. Seu funcionamento é semelhante à forma como cartas são organizadas manualmente.

### Análise de Desempenho

* Apresenta ótimo desempenho quando o vetor está parcialmente ou totalmente ordenado.
* Torna-se ineficiente para grandes volumes de dados, devido ao crescimento quadrático do número de comparações e deslocamentos.

### Complexidade

| Caso           | Complexidade |
| -------------- | ------------ |
| Melhor caso    | O(n)         |
| Caso médio     | O(n²)        |
| Pior caso      | O(n²)        |
| Uso de memória | O(1)         |
| Estabilidade   | Estável      |

---

## Selection Sort

### Descrição

O Selection Sort funciona selecionando, a cada iteração, o menor elemento do vetor não ordenado e o posiciona na posição correta. Diferentemente do Insertion Sort, ele não se beneficia de entradas parcialmente ordenadas.

### Análise de Desempenho

* Realiza sempre o mesmo número de comparações, independentemente da entrada.
* Apresenta poucas trocas, porém muitas comparações, o que compromete seu desempenho.

### Complexidade

| Caso           | Complexidade |
| -------------- | ------------ |
| Melhor caso    | O(n²)        |
| Caso médio     | O(n²)        |
| Pior caso      | O(n²)        |
| Uso de memória | O(1)         |
| Estabilidade   | Não estável  |

---

## Merge Sort

### Descrição

O Merge Sort é um algoritmo baseado na técnica de divisão e conquista, que divide o vetor em partes menores, ordena cada uma recursivamente e, em seguida, as combina de forma ordenada.

### Análise de Desempenho

* Apresenta desempenho consistente, independentemente da ordem inicial dos dados.
* É altamente eficiente para grandes volumes de dados, porém requer memória auxiliar.

### Complexidade

| Caso           | Complexidade |
| -------------- | ------------ |
| Melhor caso    | O(n log n)   |
| Caso médio     | O(n log n)   |
| Pior caso      | O(n log n)   |
| Uso de memória | O(n)         |
| Estabilidade   | Estável      |

---

## Quick Sort

### Descrição

O Quick Sort também utiliza a estratégia de divisão e conquista, escolhendo um elemento pivô e reorganizando o vetor de forma que elementos menores fiquem à esquerda e maiores à direita do pivô.

### Análise de Desempenho

* Geralmente é o algoritmo mais rápido na prática.
* Seu desempenho depende fortemente da escolha do pivô.
* Pode apresentar degradação significativa no pior caso.

### Complexidade

| Caso           | Complexidade |
| -------------- | ------------ |
| Melhor caso    | O(n log n)   |
| Caso médio     | O(n log n)   |
| Pior caso      | O(n²)        |
| Uso de memória | O(log n)     |
| Estabilidade   | Não estável  |

---

## Counting Sort

### Descrição

O Counting Sort é um algoritmo não comparativo que ordena os elementos contando o número de ocorrências de cada valor. É eficiente quando os valores dos elementos pertencem a um intervalo pequeno.

### Análise de Desempenho

* Extremamente rápido para domínios de dados limitados.
* Não é aplicável a dados genéricos ou com grande variação de valores.

### Complexidade

| Caso           | Complexidade |
| -------------- | ------------ |
| Melhor caso    | O(n + k)     |
| Caso médio     | O(n + k)     |
| Pior caso      | O(n + k)     |
| Uso de memória | O(n + k)     |
| Estabilidade   | Estável      |

*(onde k representa o intervalo entre o menor e o maior valor)*

---

## Tabela Comparativa Geral de Complexidade

| Algoritmo      | Melhor Caso | Caso Médio | Pior Caso  | Memória  | Estável |
| -------------- | ----------- | ---------- | ---------- | -------- | ------- |
| Insertion Sort | O(n)        | O(n²)      | O(n²)      | O(1)     | Sim     |
| Selection Sort | O(n²)       | O(n²)      | O(n²)      | O(1)     | Não     |
| Merge Sort     | O(n log n)  | O(n log n) | O(n log n) | O(n)     | Sim     |
| Quick Sort     | O(n log n)  | O(n log n) | O(n²)      | O(log n) | Não     |
| Counting Sort  | O(n + k)    | O(n + k)   | O(n + k)   | O(n + k) | Sim     |

---

## Conclusão

Com base na análise teórica e nos testes experimentais, conclui-se que algoritmos simples, como Insertion Sort e Selection Sort, são adequados apenas para conjuntos pequenos ou situações específicas.
Algoritmos mais eficientes, como Merge Sort e Quick Sort, apresentam melhor escalabilidade, sendo mais indicados para grandes volumes de dados.
Por fim, o Counting Sort destaca-se pelo desempenho linear, desde que aplicado em cenários onde o domínio dos dados seja restrito.

---
