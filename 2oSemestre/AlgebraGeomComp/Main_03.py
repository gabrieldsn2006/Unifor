from Algebra_03 import *

def print_vetor(array):
     for i in range(0, len(array)):
          if i < len(array) -1: print(f'{array[i][0]:.5f}', end=', ')
          else: print(f'{array[i][0]:.5f}')

# exemplo de MATRIZ DE AJACÊNCIA

A = [[0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 1, 1, 1, 1, 0, 0, 1, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

a = vk_autoridade(A, 10)
print("VETOR AUTORIDADE ÁPOS ALGUMAS ITERAÇÕES: ")
print_vetor(a)
print(f'O {a.index(max(a))+1}º site é a AUTORIDADE')

print()

h = vk_centro(A, 10)
print("VETOR CENTRO ÁPOS ALGUMAS ITERAÇÕES: ")
print_vetor(h)
print(f'O {h.index(max(h))+1}º site é o CENTRO')
