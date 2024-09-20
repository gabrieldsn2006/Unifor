class Matriz:
    def __init__(self, array):
        self.nLinhas = len(array)
        self.nColunas = len(array[0])

        array_copy = list()
        for i in range(self.nLinhas):
            array_copy.append(array[i][:])
        self.array = array_copy 

        if self.nLinhas == self.nColunas: self.quadrado = True
        else: self.quadrado = False

    def get(self, i, j):
        return self.array[i][j]

    def set(self, i, j, a):
        self.array[i][j] = a

    def exibir(self):
        for i in range(self.nLinhas):
            print(self.array[i])

class LinearAlgebra:

    def transposta(self, a):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)
        t = list()
        for i in range(A.nColunas):
            t.append(list())
            for j in range(A.nLinhas):
                t[i].append(A.array[j][i])
        return t
    
    def tr(self, a):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        t = 0
        if A.quadrado:
            for i in range(A.nLinhas):
                t += A.array[i][i]
            return t
        else: return None
    
    def soma(self, a, b):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)
        if not isinstance(b, Matriz): B = Matriz(b)
        else: B = Matriz(b.array)

        if A.nLinhas != B.nLinhas or A.nColunas != B.nColunas: return None  

        s = list() 
        for i in range(A.nLinhas):
            s.append(list())
            for j in range(A.nColunas):
                s[i].append((A.array[i][j]) + (B.array[i][j]))
        return s
    
    def produto_escalar(self, cte, a):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array) 

        e = Matriz(A.array)
        for i in range(A.nLinhas):
            for j in range(A.nColunas):
                e.array[i][j] *= cte
        return e.array

    def produto(self, a, b):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)
        if not isinstance(b, Matriz): B = Matriz(b)
        else: B = Matriz(b.array)

        if A.nColunas != B.nLinhas: return None

        p = list() 
        for i in range(A.nLinhas):
            aux = list()
            for k in range(B.nColunas):
                product_sum = 0
                for j in range(A.nColunas):
                    product_sum += A.array[i][j] * B.array[j][k]
                aux.append(product_sum)
            p.append(aux)
        return p
    
    def trocar_linha(self, a, i1, i2):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        result = list()
        for i in range(A.nLinhas):
            if i != i1 and i != i2: result.append(A.array[i])
            if i == i1: result.append(A.array[i2])
            if i == i2: result.append(A.array[i1])
        return result
    
    def multi_linha(self, a, i, value):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        for j in range(A.nColunas):
            A.array[i][j] *= value
        return A.array
    
    def atribuir_linha(self, a, i1, i2, k):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        for j in range(A.nColunas):
            A.array[i1][j] -= k * A.array[i2][j]
        return A.array


    def gauss(self, a):
        if not isinstance(a, Matriz): sis = Matriz(a)
        else: sis = Matriz(a.array)

        linha_atual = 0

        for j in range(sis.nColunas - 1):

            pivot = sis.array[linha_atual][j]

            pivot_possivel = True
            if pivot == 0:
                pivot_possivel = False
                for i in range(linha_atual+1, sis.nLinhas):
                    if sis.array[i][j] != 0:
                        sis = Matriz(self.trocar_linha(sis, linha_atual, i))
                        pivot = sis.array[linha_atual][j]
                        pivot_possivel = True
                        break

            if pivot_possivel:
                sis = Matriz(self.multi_linha(sis, linha_atual, (1/pivot)))

                for i in range(sis.nLinhas):
                    if i != linha_atual:
                        k = sis.array[i][j]
                        sis = Matriz(self.atribuir_linha(sis, i, linha_atual, k))
                linha_atual += 1

        return sis.array

    def tipo_de_solucao(self, a):
        if not isinstance(a, Matriz): sis = Matriz(a)
        else: sis = Matriz(a.array)

        if sis.nLinhas < sis.nColunas-1: return 'SPI'

        num = -1

        for i in range(sis.nLinhas):
            zeros = 0
            for e in sis.array[i]:
                if e == 0: zeros += 1
            if zeros == sis.nColunas:
                if num < 1: num = 1
            elif zeros == sis.nColunas-1 and sis.array[i][sis.nColunas-1] != 0:
                if num < 2: num = 2
            else:
                if num < 0: num = 0

        if num == 0: return 'SPD'
        if num == 1: return 'SPI'
        if num == 2: return 'SI'

    def solucao(self, a):
        sis = Matriz(self.gauss(a))

        tipo = self.tipo_de_solucao(sis.array)

        if tipo == "SPD":
            s = list()
            for i in range(sis.nLinhas):
                s.append(float(f'{sis.array[i][sis.nColunas - 1]:.1f}'))
            return s
        else: return tipo

    def det(self, a):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        if not A.quadrado: return None

        if A.nLinhas == 1: return A.array[0][0]
        else:
            d = 0
            for j in range(A.nColunas):
                d += A.array[0][j] * self.cofator(A, 0, j)
            return d

    def cofator(self, a, i, j):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        mat = list()
        ajuste = 0
        for x in range(A.nLinhas):
            if x != i:
                mat.append(list())
                for y in range(A.nColunas):
                    if y != j:
                        mat[x-ajuste].append(A.array[x][y])
            else: ajuste = 1

        return ((-1)**(i+j)) * self.det(mat)

    def inversa(self, A):
        return self.produto((1 / self.det(A)), self.transposta(self.matriz_cofatores(A)))

    def matriz_cofatores(self, a):
        if not isinstance(a, Matriz): A = Matriz(a)
        else: A = Matriz(a.array)

        if A.nLinhas == 1: return A.array[0][0]
        else:
            mat = list()
            for i in range(A.nLinhas):
                mat.append(list())
                for j in range(A.nColunas):
                    mat[i].append(self.cofator(A, i, j))
            return mat
