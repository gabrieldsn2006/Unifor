from random import randint

def sort(a):
    for x in range(0, len(a)-1):
        n_min = x
        for y in range(x+1, len(a)):
            if a[y] < a[n_min]: n_min = y
        if n_min != x:
            aux = a[x]
            a[x] = a[n_min]
            a[n_min] = aux

b = list()
for _ in range(10):
    b.append(randint(1, 10))

print(f'Lista antes do Sort: {b}')
sort(b)
print(f'Lista depois do Sort: {b}')