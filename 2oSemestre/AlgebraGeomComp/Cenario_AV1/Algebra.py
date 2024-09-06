class Matrix:
    # considerei desnecessário um Construtor receber 'rows' e 'cols' como argumentos
    def __init__(self, elements):
        self.rows = len(elements)
        self.cols = len(elements[0])

        elements_copy = list()
        for i in range(self.rows):
            elements_copy.append(elements[i][:])
        self.array = elements_copy  # cópia para garantir que nunhum objeto/array sejam linkados

        if self.rows == self.cols: self.quadrado = True
        else: self.quadrado = False

    def get(self, i, j):
        return self.array[i][j]

    def set(self, i, j, a):
        self.array[i][j] = a

    def exibir(self):  # método para facilitar exibição da matriz
        for i in range(self.rows):
            print(self.array[i])


class Vector:
    def __init__(self, dim, elements):
        self.dim = dim
        self.elements = elements[:]

    def get(self, i):
        return self.elements[i]

    def set(self, i, value):
        self.elements[i] = value


class LinearAlgebra:
    def transpose(self, A):  # retorna a transposta de uma matriz
        if not isinstance(A, Matrix): A = Matrix(A)
        t = list()  # 't' é minha variável de retorno
        for i in range(A.cols):
            t.append(list())
            for j in range(A.rows):
                t[i].append(A.array[j][i])
        return t

    def sum(self, A, B):  # retorna a soma entre duas matrizes
        if not isinstance(A, Matrix): A = Matrix(A)
        if not isinstance(B, Matrix): B = Matrix(B)

        if A.rows != B.rows or A.cols != B.cols: return None  # caso as A e B não sejam de mesma ordem

        s = list()  # 's' é minha variável de retorno
        for i in range(A.rows):
            s.append(list())
            for j in range(A.cols):
                s[i].append((A.array[i][j]) + (B.array[i][j]))
        return s

    def times(self, A, B):
        # não sei se interpretei corretamente o que estava no pdf então resolvi fazer todas as opções mesmo

        # esse método pode retornar uma Matriz resultante do produto de uma Matriz por Escalar (Matriz * Cte)
        # ou retornar uma Matriz resultante do produto de elemento a elemento entre duas matrizes (Matriz, Matriz)
        # ou retornar o vetor resultante do produto de elemento a elemento de dois vetores (u * v)

        # produto termo a termo (Matrix)
        if isinstance(A, Matrix) and isinstance(B, Matrix):
            if A.rows != B.rows or A.cols != B.cols: return None  # caso as A e B não sejam de mesma ordem
            t = list()  # 't' é minha variável de retorno
            for i in range(A.rows):
                t.append(list())
                for j in range(A.cols):
                    t.append((A.array[i][j]) * (B.array[i][j]))
            return t

        # produto (Vector)
        # considerando apenas vetores de 1 dimensão como estudamos até então
        elif isinstance(A, Vector) and isinstance(B, Vector):
            if len(A.elements) != len(B.elements): return None  # caso os vetores tenham tamanhos diferentes
            t = list()  # 't' é minha variável de retorno
            for i in range(len(A.elements)):
                t.append(A.elements[i] * B.elements[i])
            return t

        # produto (Escalar * Matrix)
        elif isinstance(A, (int, float)) and isinstance(B, Matrix):
            cte = A
            t = B.array[:]  # 't' é minha variável de retorno
            for i in range(B.rows):
                for j in range(B.cols):
                    t[i][j] *= cte
            return t

    def dot(self, A, B):  # esse método retorna Matriz resultante do Produto entre Matrizes
        if not isinstance(A, Matrix): A = Matrix(A)
        if not isinstance(B, Matrix): B = Matrix(B)

        if A.cols != B.rows: return None  # condição para realizar produto entre matrizes

        d = list()  # 'd' é minha variável de retorno
        for i in range(A.rows):
            aux = list()
            for k in range(B.cols):
                product_sum = 0
                for j in range(A.cols):
                    product_sum += A.array[i][j] * B.array[j][k]
                aux.append(product_sum)
            d.append(aux)
        return d

    def solve(self, A):  # retorna a solução de um sistema
        if not isinstance(A, Matrix): sis = Matrix(A)
        else: sis = Matrix(A.array)

        gauss_result = self.gauss(sis.array)
        if isinstance(gauss_result, list): gauss_result = Matrix(gauss_result)
        else: return gauss_result

        solution = list()
        for i in range(gauss_result.rows):  # separando a solução que é apenas a última coluna da matriz
            solution.append(float(f'{gauss_result.array[i][gauss_result.cols - 1]:.1f}'))
        return solution

    def gauss(self, A):  # retorna a matriz aumentada de um sistema após eliminação de Gauss
        if not isinstance(A, Matrix): sis = Matrix(A)
        else: sis = Matrix(A.array)

        for i in range(sis.rows):

            if sis.array[i][i] == 0 and i == sis.rows - 1:  # caso o último elemento a ser pivoteado seja 0
                return self.solution_type(sis.array[i])  # SPI/SI

            elif sis.array[i][i] == 0:  # verificar se posso trocar linhas
                boolean_aux = True
                for x in range(i + 1, sis.rows):
                    if sis.array[x][i] != 0:
                        sis.array = self.switch_lines(sis, i, x)  # troca
                        boolean_aux = False
                if boolean_aux: return self.solution_type(sis.array[i])  # SPI/SI

            pivot = sis.array[i][i]  # capturando o divisor para o pivoteamento
            for j in range(sis.cols):  # pivoteamento
                if pivot != 0: sis.array[i][j] = sis.array[i][j] / pivot

            aux = list()
            for pos in range(sis.rows):  # capturando a coluna referente a linha "i" do elemento pivoteado pivoteada
                aux.append(sis.array[pos][i])

            for ii in range(sis.rows):  # atribuindo valores para as outras linhas
                if ii != i:
                    for jj in range(sis.cols): sis.array[ii][jj] -= aux[ii] * sis.array[i][jj]

        return sis.array

    def switch_lines(self, A, i1, i2):  # troca de linhas
        if not isinstance(A, Matrix): A = Matrix(A)

        result = list()
        for i in range(A.rows):
            result.append(list())
            if i != i1 and i != i2: result[i].append(A.array[i])
            if i == i1: result[i].append(A.array[i2])
            if i == i2: result[i].append(A.array[i1])
        return result

    def solution_type(self, array):  # retorna o tipo de solução para um sistema
        cont = 0
        for e in array:
            if e == 0: cont += 1
        if cont == len(array):
            return 'SPI'  # ex.: 0x + 0y + 0z = 0
        elif cont == len(array) - 1 and array[len(array) - 1] != 0:
            return 'SI'  # ex.: 0x + 0y + 0z = -1
        # else: return 'SPD' # se de fato fosse um sistema possível determinado essa função nem seria chamada

# também fiz um método para calcular determinante e inversa
# o codigo completo pode ser acessado nesse link:
# https://github.com/gabrieldsn2006/Unifor/blob/main/2oSemestre/AlgebraGeomComp/AlgebraGeomComp.py
