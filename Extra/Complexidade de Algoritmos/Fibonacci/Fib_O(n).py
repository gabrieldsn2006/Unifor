rep = 0
def fib(n):
    if n == 1: return 1
    elif n == 2: return 1
    else:
        a = 1
        b = 1
        global rep
        for _ in range(n-2):
            c = a + b
            a = b
            b = c
            rep += 1
        return c

n = int(input('Termo da sequência que deseja encontrar: '))
fib_n = fib(n)
print(f'Encontrado com {rep} repetições, o {n}º termo da sequência é: {fib_n}')