class Matriz:
    def __init__(self, vetor):
        self.nLinhas = len(vetor)
        self.nColunas = len(vetor[0])
        self.vetor = vetor[:]
        if self.nLinhas == self.nColunas: self.quadrado = True 
        else: self.quadrado = False

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
    sis = Matriz(sis)

    for i in range(sis.nLinhas):

        pivot = sis.vetor[i][i] # capturando o divisor para o pivoteamento
        for j in range(sis.nColunas): # pivoteamento
            if sis.vetor[i][i] != 0:
                sis.vetor[i][j] = sis.vetor[i][j]/pivot

        aux = list()
        for pos in range(sis.nLinhas): # capturando a coluna referente a linha "i" que foi pivoteada
            aux.append(sis.vetor[pos][i])

        for ii in range(sis.nLinhas): # atribuindo valores para as outras linhas
            if ii != i:
                for jj in range(sis.nColunas): sis.vetor[ii][jj] -= aux[ii]*sis.vetor[i][jj]

    solucao = list()
    for iii in range(sis.nLinhas): # separando a solução que é apenas a ultima coluna da matriz
        solucao.append(float(f'{sis.vetor[iii][sis.nColunas-1]:.1f}'))
    return solucao

def det(A):
    A = Matriz(A)
    if A.quadrado == False: return None

    if A.nLinhas == 2:
        return (A.vetor[0][0] * A.vetor[1][1]) - (A.vetor[0][1] * A.vetor[1][0])
    else:
        r = 0
        for x in range(A.nColunas):
            r += A.vetor[0][x] * laplace(A.vetor, 0, x)
        return r

def laplace(A, i, j):
    mat = list()
    A = Matriz(A)

    for x in range(1, A.nLinhas):
        mat.append(list())
        for y in range(A.nColunas):
            if y != j:
                mat[x-1].append(A.vetor[x][y])

    return ((-1)**(i+j)) * det(mat)