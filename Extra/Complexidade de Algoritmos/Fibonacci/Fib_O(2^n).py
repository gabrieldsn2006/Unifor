calls = 0
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: global calls; calls += 2; return fib(n-1) + fib(n-2)

n = int(input('Termo da sequência que deseja encontrar: '))
fib_n = fib(n)
print(f'Encontrado com {calls} chamadas, o {n}º termo da sequência é: {fib_n}')