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
    if isinstance(A, list) and isinstance(B, list): # produto de matrizes
        A = Matriz(A)
        B = Matriz(B)
        if A.nColunas != B.nLinhas: return None
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
    elif isinstance(A, (int, float)) or isinstance(B, (int, float)): # matriz * cte
        if isinstance(A, (int, float)):
            cte = A
            mat = Matriz(B)
        else:
            cte = B
            mat = Matriz(A)
        for i in range(mat.nLinhas):
            for j in range(mat.nColunas):
                mat.vetor[i][j] *= cte
        return mat.vetor

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
    
    if A.nLinhas == 1:
        return A.vetor[0][0]
    else:
        d = 0
        for x in range(A.nColunas):
            d += A.vetor[0][x] * laplace(A.vetor, 0, x)
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