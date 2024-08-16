from random import randint

def search(vetor, x):
    pos_inicial = 0
    pos_final = len(vetor) - 1
    while pos_inicial <= pos_final:
        meio = (pos_final - pos_inicial) // 2
        if vetor[meio] == x: 
            return meio
        elif vetor[meio] > x:
            pos_final = meio - 1
        elif vetor[meio] < x:
            pos_inicial = meio + 1
    return None

a = list()
for _ in range(10):
    a.append(randint(1, 10))

pos = search(a, 1)
if pos == None: print(f'A lista {a} não apresenta o item "1".')
else: print(f'A lista {a} apresenta o item "1" na posição: {pos}.')