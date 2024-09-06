from Algebra import Matrix, Vector, LinearAlgebra
LA = LinearAlgebra()

ex1x1 = [[1]]
ex2x2 = [[1, 2],
         [4, 3]]
ex3x3 = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
ex4x4 = [[ 1,  2,  3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10,  9,  8, 7]]
ex5x5 = [[ 1,  2,  3,  4, 5],
         [16, 17, 18, 19, 6],
         [15, 24, 25, 20, 7],
         [14, 23, 22, 21, 8],
         [13, 12, 11, 10, 9]]

# SPD:
sistema01 = [[1,  1, 1, 3],
             [2, -1, 3, 4],
             [1,  2, 3, 6]]
# SPI:
sistema02 = [[1, 1, 1, 3],
             [2, 2, 2, 6]]
# SI:
sistema03 = [[1, 1, 1, 3],
             [2, 2, 2, 7]]

sis = Matrix(sistema02)
print(f'Sistema de matriz aumentada: ')
sis.exibir()
print(f'Utilizando eliminação de Gauss: ')
gauss = Matrix(LA.gauss(sis))
gauss.exibir()
print(f'Solução: \n{LA.solve(sis)}')

print(f'Exemplo de Matriz A: ')
ex = Matrix(ex2x2)
ex.exibir()
print(f'Transposta de A: ')
transposta = Matrix(LA.transpose(ex))
transposta.exibir()
print(f'Soma A + B (B = A nesse caso de teste): ')
soma = Matrix(LA.sum(ex, ex))
soma.exibir()
print(f'Produto entre matrizes A * B (B = A nesse caso de teste): ')
prod = Matrix(LA.dot(ex, ex))
prod.exibir()
print(f'Produto Escalar A * cte (cte = 4 nesse caso de teste): ')
prod_escalar = Matrix(LA.times(4, ex))
prod_escalar.exibir()
