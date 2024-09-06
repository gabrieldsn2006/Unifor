export class Matrix {
    constructor(vetor) {
        // considerei desnecessário um Construtor receber 'rows' e 'cols' como argumentos
        this.rows = vetor.length
        this.cols = vetor[0].length

        var copy = new Array()
        for (var i = 0; i < this.rows; i++) {
            copy.push(new Array())
            for (var j = 0; j < this.cols; j++) {
                copy[i].push(vetor[i][j])
            }
        }
        this.array = copy // cópia para garantir que nunhum objeto/array sejam linkados

        if (this.rows == this.cols) this.quadrado = true
        else this.quadrado = false
    }
    get(i, j) {
        return this.array[i][j]
    }
    set(i, j, a) {
        this.array[i][j] = a
    }
    exibir() {  // método para facilitar exibição da matriz
        for (var i = 0; i < this.rows; i++) {
            console.log(this.array[i])
        }
    }
}

export class Vector {
    constructor(dim, elem) {
        this.dimensions = dim

        var copy = new Array()
        for (var i = 0; i < elem.length; i++)
            copy.push(elem[i])
        this.elements = copy
    }
    get(i) {
        return this.elements[i]
    }
    set(i, value) {
        this.elements = value
    }
}

export class LinearAlgebra {
    transpose(a) {  // retorna a transposta de uma matriz
        if (a instanceof Array) var A = new Matrix(a)
        else var A = new Matrix(a.array)
        var t = new Array()
        for (var i = 0; i < A.rows; i++) {
            t.push(new Array())
            for (var j = 0; j < A.cols; j++) {
                t[i].push(A.vetor[j][i])
            }
        }
        return t
    }
    sum(a, b) {  // retorna a soma entre duas matrizes
        if (a instanceof Array) var A = new Matrix(a)
        else var A = new Matrix(a.array)
        if (b instanceof Array) var B = new Matrix(b)
        else var B = new Matrix(b.array)

        if (A.rows != B.rows || A.cols != B.cols) return undefined  // caso as A e B não sejam de mesma ordem

        var s = new Array()  //'s' é minha variável de retorno
        for (var i = 0; i < A.rows; i++) {
            s.push(new Array())
            for (var j = 0; j < A.cols; j++) {
                s[i].push(A.vetor[i][j] + B.vetor[i][j])
            }
        }
        return s
    }

    times(A, B) {
        /*
        não sei se interpretei corretamente o que estava no pdf então resolvi fazer todas as opções mesmo.
        esse método pode retornar uma Matriz resultante do produto de uma Matriz por Escalar (Matriz * Cte).
        ou retornar uma Matriz resultante do produto de elemento a elemento entre duas matrizes (Matriz, Matriz).
        ou retornar o vetor resultante do produto de elemento a elemento de dois vetores (u * v).
        */

        // produto termo a termo (Matrix)
        if (A instanceof Matrix && B instanceof Matrix) {
            if (A.rows != B.rows || A.cols != B.cols) return undefined  // caso as A e B não sejam de mesma ordem
            var t = new Array()  // 't' é minha variável de retorno
            for (var i = 0; i < A.rows; i++) {
                t.push(new Array())
                for (var j = 0; j < A.cols; j++) {
                    t[i].push(A.array[i][j] * B.array[i][j])
                }
            }
            return t
        }

        // produto (Vector)
        // considerando apenas vetores de 1 dimensão como estudamos até então
        else if (A instanceof Vector && B instanceof Vector) {
            if (A.elements.length != B.elements.length) return undefined  // caso os vetores tenham tamanhos diferentes
            var t = new Array()  // 't' é minha variável de retorno
            for (var i = 0; i < A.elements.length; i++) {
                t.push(A.elements[i] * B.elements[i])
            }
            return t
        }

        // produto (Escalar * Matrix)
        else if (A instanceof Number && B instanceof Matrix) {
            var cte = A
            var t = new Matrix(B.array)  // 't' é minha variável de retorno
            for (var i = 0; i < B.rows; i++) {
                for (var j = 0; j < B.cols; j++) {
                    t.array[i][j] *= cte
                }
            }
            return t.array
        }
    }

    dot(a, b) {  //esse método retorna Matriz resultante do Produto entre Matrizes
        if (a instanceof Array) var A = Matrix(a)
        else if (a instanceof Matrix) var A = new Matrix(a.array)
        if (b instanceof Array) B = Matrix(b)
        else if (b instanceof Matrix) var B = new Matrix(b.array)
        
        if (A.cols != B.cols) return undefined  // condição para realizar produto entre matrizes

        var d = new Array()  // 'd' é minha variável de retorno
        for (var i = 0; i < A.rows; i++) {
            var aux = new Array()
            for (var k = 0; k < B.cols; k++) {
                var product_sum = 0
                for (var j = 0; j < A.cols; j++) {
                    product_sum += A.array[i][j] * B.array[j][k]
                }
                aux.push(product_sum)
            }
            d.append(aux)
        }
        return d
    }

    solve(A) {  // retorna a solução de um sistema
        if (A instanceof Array) var sis = new Matrix(A)
        else var sis = new Matrix(A.array)
        
        var gauss_result = this.gauss(sis)
        if (gauss_result instanceof Array) gauss_result = new Matrix(gauss_result)
        else return gauss_result

        var solution = new Array()
        for (var i = 0; i < gauss_result.rows; i++) {  //separando a solução que é apenas a última coluna da matriz
            solution.push((gauss_result.array[i][gauss_result.cols-1]).toFixed(1))
        }
        return solution
    }

    gauss(A) {  // retorna a matriz aumentada de um sistema após eliminação de Gauss
        if (A instanceof Array) var sis = new Matrix(A)
        else if (A instanceof Matrix) var sis = new Matrix(A.array)

        for (var i = 0; i < sis.rows; i++) {
            // caso o último elemento a ser pivoteado seja 0
            if (sis.array[i][i] == 0 && i == sis.rows - 1) return this.solution_type(sis.array[i])
            
            // verificar se posso trocar linhas
            else if (sis.array[i][i] == 0) {
                var boolean_aux = true
                for (var x = i+1; x < sis.rows; x++) {
                    if (sis.array[x][i] != 0) {
                        sis.array = this.switch_lines(sis, i, x)  // troca
                        boolean_aux = false
                    }
                }
                if (boolean_aux) return this.solution_type(sis.array[i])  // SPI/SI
            }

            var pivot = sis.array[i][i]  // capturando o divisor para o pivoteamento
            for (var j = 0; j < sis.cols; j++) {  // pivoteamento
                sis.array[i][j] = sis.array[i][j] / pivot
            }

            var aux = new Array()
            for (var pos = 0; pos < sis.rows; pos++) {  // capturando a coluna do elemento pivoteado
                aux.push(sis.array[pos][i])
            }

            for (var ii = 0; ii < sis.rows; ii++) {  // atribuindo valores para as outras linhas
                if (ii != i) {
                    for (var jj = 0; jj < sis.cols; jj++) {
                        sis.array[ii][jj] -= aux[ii] * sis[i][jj]
                    }
                }
            }
        }
        return sis.array
    }

    switch_lines(a, i1, i2) {  // troca de linhas
        if (a instanceof Array) var A = new Matrix(a)
        else if (a instanceof Matrix) var A = new Matrix(a.array)
        var result = new Array()
        for (var i = 0; i < A.rows; i++) {
            result.push(new Array())
            if (i != i1 && i != i2) result[i].push(A.array[i])
            if (i == i1) result[i].push(A.array[i2])
            if (i == i2) result[i].push(A.array[i1])
        }
        return result
    }

    solution_type(array) {  // retorna o tipo de solução para um sistema
        var cont = 0
        for (var i = 0; i < array.length; i++) {
            if (array[i] == 0) cont++
        }
        if (cont == array.length) return 'SPI'  // ex.: 0x + 0y + 0z = 0
        else if (cont == array.length - 1 && array[array.length - 1] != 0) return 'SI'  // ex.: 0x + 0y + 0z = -1
        // else return 'SPD'  // se de fato fosse um sistema possível determinado essa função nem seria chamada
    }
}