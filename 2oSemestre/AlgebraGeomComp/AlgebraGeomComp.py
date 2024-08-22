class Matriz:
    def __init__(self, vetor):
        self.nLinhas = len(vetor)
        self.nColunas = len(vetor[0])
        self.vetor = vetor[:]
        self.quadrado = True if self.nLinhas == self.nColunas else False

def exibir(A):
    A = Matriz(A)
    print(f'Matriz : ')
    for i in range(A.nLinhas):
        print(A.vetor[i])

def transposta(A):
    A = Matriz(A)
    t = list()
    for i in range(A.nColunas):
        t.append(list())
        for j in range(A.nLinhas):
            t[i].append(A.vetor[j][i])
    return t

def tr(A): 
    A = Matriz(A)
    if A.quadrado:
        for i in range(A.nLinhas):
            tr += A.vetor[i][i]
        return tr
    else:
        return None

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
    A = Matriz(A)
    B = Matriz(B)
    P = list()
    
    for i in range(A.nLinhas):
        aux = list()
        for k in range(B.nColunas):
            sum = 0
            for j in range(A.nColunas):
                sum += A.vetor[i][j] * B.vetor[j][k]
            aux.append(sum)
        P.append(aux)
    return P

def sistema(*sis):
    nLinhas = len(sis) # nº de linhas da matriz
    nColunas = len(sis[0]) # nº de colunas da matriz

    for i in range(nLinhas):

        pivot = sis[i][i] # capturando o divisor para o pivoteamento
        for j in range(nColunas): # pivoteamento
            if sis[i][i] != 0:
                sis[i][j] = sis[i][j]/pivot

        aux = list()
        for pos in range(nLinhas): # capturando a coluna referente a linha "i" que foi pivoteada
            aux.append(sis[pos][i])

        for ii in range(nLinhas): # atribuindo valores para as outras linhas
            if ii != i:
                for jj in range(nColunas): sis[ii][jj] -= aux[ii]*sis[i][jj]

    solucao = list()
    for iii in range(nLinhas): # separando a solução que é apenas a ultima coluna da matriz
        solucao.append(float(f'{sis[iii][nColunas-1]:.1f}'))
    return solucao

def det(A):
    nLinhas = len(A) # nº de linhas da matriz
    nColunas = len(A[0]) # nº de colunas da matriz
    if nLinhas != nColunas: return None

    if nLinhas == 2:
        return (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
    else:
        r = 0
        for x in range(nColunas):
            r += A[0][x] * laplace(A, 0, x)
        return r

def laplace(A, i, j):
    mat = list()

    nLinhas = len(A)
    nColunas = len(A[0])

    for x in range(1, nLinhas):
        mat.append(list())
        for y in range(nColunas):
            if y != j:
                mat[x-1].append(A[x][y])

    return ((-1)**(i+j)) * det(mat)