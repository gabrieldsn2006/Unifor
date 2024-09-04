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

sis = Matrix(sistema03)
print(f'Sistema de matriz aumentada: ')
sis.exibir()
print(f'Utilizando eliminação de Gauss: ')
gauss = Matrix(LA.gauss(sis))
gauss.exibir()
print(f'Solução: \n{LA.solve(sis)}')
print()

