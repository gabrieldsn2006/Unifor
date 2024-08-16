class Matriz:
    def __init__(self, vetor):
        self.nLinhas = len(vetor)
        self.nColunas = len(vetor[0])
        self.vetor = vetor[:]
        self.len = len(vetor)

        self.quadrado = False
        if self.nLinhas == self.nColunas:
            self.quadrado = True

        self.linhas = vetor[:]
        C = []
        tr = 0
        for i in range(self.nColunas):
            C.append([])
            for j in range(self.nLinhas):
                C[i].append(vetor[j][i])
                if i == j: tr += vetor[i][j]
        self.colunas = C
        self.tr = tr
        self.transposta = C
        
    def dados(self):
        if self.quadrado:
            print(f'Sua matriz possui {self.nLinhas} linhas e {self.nColunas} colunas e é quadrada.')
            print(f'O traço de sua matriz vale {self.tr}')
        else:
            print(f'Sua matriz possui {self.nLinhas} linhas e {self.nColunas} colunas.')

    def exibir(self):
        print(f'Matriz : ')
        for i in range(self.nLinhas):
            print(self.linhas[i]) 

def Soma(A, B):
    A = Matriz(A)
    B = Matriz(B)
    R = list()
    for i in range(A.nLinhas):
        R.append(list())
        for j in range(A.nColunas):
            R[i].append((A.vetor[i][j]) + (B.vetor[i][j]))
    return R

def Produto(A, B):
    A = Matriz(A)
    B = Matriz(B)
    R = list()
    
    for i in range(A.nLinhas):
        r = list()
        for k in range(B.nColunas):
            sum = 0
            for j in range(A.nColunas):
                sum += A.vetor[i][j] * B.vetor[j][k]
            r.append(sum)
        R.append(r)
    return R

def Sistema(*sis):
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
