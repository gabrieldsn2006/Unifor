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

# SPD
sistema01 = [[1,  1, 1, 3],
             [2, -1, 3, 4],
             [1,  2, 3, 6]]

# SPI
sistema02 = [[1, 1, 1, 3],
             [2, 2, 2, 6]]

# SI
sistema03 = [[1, 1, 1, 3],
             [2, 2, 2, 7]]

print(LA.solve(sistema01))
print(LA.solve(sistema02))
print(LA.solve(sistema03))

ex3x3 = Matrix(ex3x3)
ex3x3.exibir()

ex3x3_transposto = Matrix(LA.transpose(ex3x3))
ex3x3_transposto.exibir()

# produto_escalar = Matrix(LA.times(ex2x2, 2))  # ordem dos argumentos não importa
produto_escalar = Matrix(LA.times(2, ex2x2))
produto_escalar.exibir()

produto_matrizes = LA.dot(ex2x2, ex3x3)  # None (não atende condição para produto de matrizes)
print(produto_matrizes)

a = [[1, 2, 3],
     [6, 5, 4]]

b = [[1, 2],
     [6, 3],
     [5, 4]]

produto_matrizes = Matrix(LA.dot(ex2x2, ex2x2))
produto_matrizes.exibir()

