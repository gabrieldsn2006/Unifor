# Gabriel de Sousa Nobre - 2410399
# Lorenzo Barros Calheiros Pinheiro - 2410428

from Algebra_01 import *
LA = LinearAlgebra()
from Algebra_02 import Vector

# Matriz de Adjacência : A
# aij = 1 : se 'i' faz referencia à 'j'
# aij = 0 : se 'i' não faz referencia à 'j'
# CENTRO : site que mais faz referências
# AUTORIDADE : site que mais é referenciado por outros sites

def vetor_centro(matriz_adj):
    """
    matriz_adj: pode ser um array ou um objeto do tipo Matriz
    return: array do vetor centro
    """

    if not isinstance(matriz_adj, Matriz): A = Matriz(matriz_adj)
    else: A = Matriz(matriz_adj.array)

    h = list(sum(e) for e in A.array)
    
    return h

def vetor_autoridade(matriz_adj):
    """
    matriz_adj: pode ser um array ou um objeto do tipo Matriz
    return: array do vetor autoridade
    """

    A = Matriz(LA.transposta(matriz_adj))

    a = list(sum(e) for e in A.array)
    
    return a

def modulo(vetor):
    """
    vetor: array
    return: valor númerico do modulo de um vetor
    """
    return (sum(e**2 for e in vetor))**(1/2)

def normalizar(vetor):
    """
    vetor: array
    return: array do vetor normalizado ( divisão pelo modulo ou multi. pelo modulo**-1 ) 
    """
    # conversão array -> matriz coluna: Vector(vetor).mat
    return LA.produto_escalar(modulo(vetor)**-1, Vector(vetor).mat) # retorna o array de uma matriz coluna

def vk_centro(matriz_adj, k):
    """
    matriz_adj: pode ser um array ou um objeto do tipo Matriz
    k: número de iterações
    return: array do vetor centro ápos 'k' iterações
    """

    if not isinstance(matriz_adj, Matriz): A = Matriz(matriz_adj)
    else: A = Matriz(matriz_adj.array)

    At = Matriz(LA.transposta(A))
    
    p1 = Matriz(LA.produto(A, At))

    if k == 0: h = normalizar(vetor_centro(A))
    else: h = vk_centro(A, k-1)
    # conversão array -> matriz coluna:
    h = Vector(h).mat

    p2 = LA.produto(p1, h) # retornar o array de uma matriz coluna
    # conversão matriz coluna -> matriz linha -> array:
    p2 = LA.transposta(p2)[0] # primeira e única posição do array / primeira e única linha de uma matriz linha

    return normalizar(p2)

def vk_autoridade(matriz_adj, k):
    """
    matriz_adj: pode ser um array ou um objeto do tipo Matriz
    k: número de iterações
    return: array do vetor autoridade ápos 'k' iterações
    """

    if not isinstance(matriz_adj, Matriz): A = Matriz(matriz_adj)
    else: A = Matriz(matriz_adj.array)

    At = Matriz(LA.transposta(A))
    
    p1 = Matriz(LA.produto(At, A))

    if k == 0: a = normalizar(vetor_autoridade(A))
    else: a = vk_autoridade(A, k-1)
    # conversão array -> matriz coluna:
    a = Vector(a).mat

    p2 = LA.produto(p1, a) # teoricamente vair retornar o array de uma matriz coluna
    # conversão matriz coluna -> matriz linha -> array:
    p2 = LA.transposta(p2)[0] # primeira e única posição do array / primeira e única linha de uma matriz linha

    return normalizar(p2)


