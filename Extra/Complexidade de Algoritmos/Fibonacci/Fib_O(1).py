import math

def fib(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (1 - phi) ** n) / math.sqrt(5))

n = int(input('Termo da sequência que deseja encontrar: '))
print(f'Encontrado com apenas 1 execução, o {n}º termo da sequência é: {fib(n)}')