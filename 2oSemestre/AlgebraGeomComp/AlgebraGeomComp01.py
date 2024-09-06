class Matriz:
    def __init__(self, vetor):
        self.nLinhas = len(vetor)
        self.nColunas = len(vetor[0])
        self.vetor = vetor[:]
        if self.nLinhas == self.nColunas: self.quadrado = True
        else: self.quadrado = False


def exibir(A):
    print(f'Matriz : ')
    for i in range(len(A)):
        print(A[i])


def transposta(A):
    A = Matriz(A)
    t = list()
    for i in range(A.nColunas):
        t.append(list())
        for j in range(A.nLinhas):
            t[i].append(A.vetor[j][i])
    return t


def tr(A):
    t = 0
    A = Matriz(A)
    if A.quadrado:
        for i in range(A.nLinhas):
            t += A.vetor[i][i]
        return t
    else: return None


def soma(A, B):
    A = Matriz(A)
    B = Matriz(B)
    S = list()
    for i in range(A.nLinhas):
        S.append(list())
        for j in range(A.nColunas):
            S[i].append((A.vetor[i][j]) + (B.vetor[i][j]))
    return S


def produto(A, B):
    if isinstance(A, list) and isinstance(B, list):  # produto de matrizes
        A = Matriz(A)
        B = Matriz(B)
        if A.nColunas != B.nLinhas: return None
        P = list()
        for i in range(A.nLinhas):
            aux = list()
            for k in range(B.nColunas):
                s = 0
                for j in range(A.nColunas):
                    s += A.vetor[i][j] * B.vetor[j][k]
                aux.append(s)
            P.append(aux)
        return P
    else:  # matriz * cte
        if isinstance(A, (int, float)) and isinstance(B, list):
            cte = A
            mat = Matriz(B)
        elif isinstance(A, list) and isinstance(B, (int, float)):
            cte = B
            mat = Matriz(A)
        else: return None  # pq alguem faria isso?
        for i in range(mat.nLinhas):
            for j in range(mat.nColunas):
                mat.vetor[i][j] *= cte
        return mat.vetor


def sistema(sis):
    sis = Matriz(sis)

    for i in range(sis.nLinhas):

        if sis.vetor[i][i] == 0 and i == sis.nLinhas - 1:  # caso o último elemento a ser pivoteado seja 0
            return tipo_de_solucao(sis.vetor[i])  # SPI/SI

        elif sis.vetor[i][i] == 0:  # verificar se posso trocar linhas
            # for I in range(i+1, sis.nLinhas):
            #     if sis.vetor[I][i] != 0: sis.vetor = troca(sis.vetor, i, I)  # troca
            # return tipo_de_solucao(sis.vetor[i])  # SPI/SI
            boolean_aux = True
            for x in range(i + 1, sis.nLinhas):
                if sis.array[x][i] != 0:
                    sis.array = troca(sis, i, x)  # troca
                    boolean_aux = False
            if boolean_aux: return tipo_de_solucao(sis.array[i])  # SPI/SI

        pivot = sis.vetor[i][i]  # capturando o divisor para o pivoteamento
        for j in range(sis.nColunas):  # pivoteamento
            if pivot != 0:
                sis.vetor[i][j] = sis.vetor[i][j] / pivot

        aux = list()
        for pos in range(sis.nLinhas):  # capturando a coluna referente a linha "i" do elemento pivoteado pivoteada
            aux.append(sis.vetor[pos][i])

        for ii in range(sis.nLinhas):  # atribuindo valores para as outras linhas
            if ii != i:
                for jj in range(sis.nColunas): sis.vetor[ii][jj] -= aux[ii] * sis.vetor[i][jj]

    solucao = list()
    for iii in range(sis.nLinhas):  # separando a solução que é apenas a última coluna da matriz
        solucao.append(float(f'{sis.vetor[iii][sis.nColunas - 1]:.1f}'))
    return solucao


def troca(A, i1, i2):
    A = Matriz(A)
    r = list()
    for i in range(A.nLinhas):
        r.append(list())
        if i != i1 and i != i2: r[i].append(A.vetor[i])
        if i == i1: r.append(A.vetor[i2])
        if i == i2: r.append(A.vetor[i1])
    return r


def tipo_de_solucao(vetor):
    cont = 0
    for e in vetor:
        if e == 0: cont += 1
    if cont == len(vetor): return 'SPI'  # 'sistema possível indeterminado'
    if cont == len(vetor) - 1 and vetor[len(vetor) - 1] != 0: return 'SI'  # sistema impossível'
    # return 'SPD' # se de fato fosse um sistema possível determinado essa função nem seria chamada


def det(A):
    A = Matriz(A)
    if not A.quadrado: return None

    if A.nLinhas == 1: return A.vetor[0][0]
    else:
        d = 0
        for j in range(A.nColunas):
            d += A.vetor[0][j] * laplace(A.vetor, 0, j)
        return d


def laplace(A, i, j):
    mat = list()
    A = Matriz(A)

    aux = 0
    for x in range(A.nLinhas):
        if x != i:
            mat.append(list())
            for y in range(A.nColunas):
                if y != j:
                    mat[x-aux].append(A.vetor[x][y])
        else: aux = 1

    return ((-1)**(i+j)) * det(mat)


def inversa(A):
    return produto((1/det(A)), transposta(cofator(A)))


def cofator(A):
    A = Matriz(A)
    if A.nLinhas == 1: return A.vetor[0][0]
    else:
        c = list()
        for i in range(A.nLinhas):
            c.append(list())
            for j in range(A.nColunas):
                c[i].append(laplace(A.vetor, i, j))
        return c
