from random import randint

def search(vetor, x):
    for index, value in enumerate(vetor):
        if value == x: return index
    return None

a = list()
for _ in range(10):
    a.append(randint(1, 10))

pos = search(a, 1)
if pos == None: print(f'A lista {a} não apresenta o item "1".')
else: print(f'A lista {a} apresenta o item "1" na posição: {pos}.')