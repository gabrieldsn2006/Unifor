import { Matrix, Vector, LinearAlgebra } from './Algebra.js';
const LA = new LinearAlgebra();

var ex1x1 = [[1]]
var ex2x2 = [[1, 2],
             [4, 3]]
var ex3x3 = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
var ex4x4 = [[ 1,  2,  3, 4],
             [12, 13, 14, 5],
             [11, 16, 15, 6],
             [10,  9,  8, 7]]
var ex5x5 = [[ 1,  2,  3,  4, 5],
             [16, 17, 18, 19, 6],
             [15, 24, 25, 20, 7],
             [14, 23, 22, 21, 8],
             [13, 12, 11, 10, 9]]

// SPD:
var sistema01 = [[1,  1, 1, 3],
                 [2, -1, 3, 4],
                 [1,  2, 3, 6]]
// SPI:
var sistema02 = [[1, 1, 1, 3],
                 [2, 2, 2, 6]]
// SI:
var sistema03 = [[1, 1, 1, 3],
                 [2, 2, 2, 7]]

var vector01 = [1, 2, 3, 4]
var vector02 = [8, 6, 4, 2]

var sis = new Matrix(sistema01)
console.log("Sistema de Matriz aumentada: ")
sis.exibir()
console.log("Utilizando Eliminação de Gauss: ")
var gauss = new Matrix(LA.gauss(sis))
gauss.exibir()
console.log(`Solução: \n${LA.solve(sis)}`)

console.log("Exemplo de Matriz A: ")
var ex = new Matrix(ex2x2)
ex.exibir()
console.log("Transposta de A: ")
var transposta = new Matrix(LA.transpose(ex))
transposta.exibir()
console.log("Soma A + B (B = A nesse caso de teste): ")
var soma = new Matrix(LA.sum(ex, ex))
soma.exibir()
console.log("Produto entre Matrizes A * B (B = A nesse caso de teste): ")
var prod = new Matrix(LA.dot(ex, ex))
prod.exibir()
console.log("Produto Escalar cte * A (cte = 4 nesse caso de teste): ")
var prod_escalar = new Matrix(LA.times(4, new Matrix(ex)))
prod_escalar.exibir
console.log("Produto elemento a elemento de Matrizes A e B (B = A nesse caso de teste): ")
var prod_elem = new Matrix(LA.times(ex, ex))
prod_elem.exibir()
console.log("Considerando os vetores: ")
console.log(`u = ${vector01}`)
console.log(`v = ${vector02}`)
console.log("O produto elemento a elemento entre os vetores é: ")
console.log(`u * v = ${LA.times(Vector(1, vector01), Vector(1, vector02))}`)