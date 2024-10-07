def funcao(vetor, x):
    y = 0
    for i in range(len(vetor[0])):
        y += vetor[0][i]*(x**vetor[1][i])
    return y

def derivada(vetor, x):
    vetor_derivada = [[], []]
    for i in range(len(vetor[0])):
        vetor_derivada[1].append(vetor[1][i]-1)
        vetor_derivada[0].append(vetor[0][i]*vetor[1][i])
    return funcao(vetor_derivada, x)

def integral(vetor, a, b):
    vetor_integral = [[], []]
    for i in range(len(vetor[0])):
        vetor_integral[1].append(vetor[1][i]+1)
        if vetor[1][i] != -1:
            vetor_integral[0].append(vetor[0][i]/(vetor[1][i]+1))
        else:
            vetor_integral[0].append(vetor[0][i]) # !
    return funcao(vetor_integral, b) - funcao(vetor_integral, a)

def newton_raphson(vetor, x0):
    for _ in range(1000):
        x1 = x0 - (funcao(vetor, x0)/derivada(vetor, x0))
        x0 = x1
    return x1

# considerando que π pode ser encontrado usando o método de newton-raphson em uma função Seno
def pi():
    x0 = 3
    for _ in range(31): 
        x1 = x0 - sen(x0)/cos(x0)
        x0 = x1
    return x1

def fat(n):
    if n == 0: return 1
    else: return n * fat(n-1)

def sen(x):
    y = 0
    signal = 1
    for i in range(1, 100, 2):
        y += signal*(x**i)/fat(i)
        signal *= -1
    return y

def cos(x):
    y = 0
    signal = 1
    for i in range(0, 100, 2):
        y += signal*(x**i)/(fat(i))
        signal *= -1
    return y

# f(x) = 1x^5 - 5x^3 + 4x + 1/3
# [[coeficientes], [expoentes]]
f = [[1, -5, 4, 1/3], [5, 3, -1, 0]]

print(pi())
print(funcao(f, 1.5))
print(derivada(f, 1.5))
print(integral(f, -2, 2))
