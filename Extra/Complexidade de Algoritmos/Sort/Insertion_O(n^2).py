from random import randint

def sort(a):
    for x in range(1, len(a)):
        for y in range(x-1, -1, -1):
            if a[y] > a[y+1]:
                aux = a[y]
                a[y] = a[y+1]
                a[y+1] = aux
            else: break

b = list()
for _ in range(10):
    b.append(randint(1, 10))

print(f'Lista antes do Sort: {b}')
sort(b)
print(f'Lista depois do Sort: {b}')