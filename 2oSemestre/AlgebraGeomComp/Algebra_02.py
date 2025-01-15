import Algebra_01 as AL1
LA = AL1.LinearAlgebra()

def fat(n):
    if n == 0: return 1
    else: return n * fat(n-1)

def sen(x):
    y = 0
    signal = 1
    for i in range(1, 100, 2):
        y += signal*(x**i)/fat(i)
        signal *= -1
    return y

def cos(x):
    y = 0
    signal = 1
    for i in range(0, 100, 2):
        y += signal*(x**i)/(fat(i))
        signal *= -1
    return y

def pi():
    # encontrando PI com método de newton raphson em uma função Seno.
    x0 = 3
    for _ in range(99): 
        x1 = x0 - sen(x0)/cos(x0)
        x0 = x1
    return x1

def rad(theta):
    # convertendo theta em graus para radianos.
    return theta * (pi()/180)

class Vector:
    def __init__(self, array):
        self.dim = len(array)

        if not isinstance(array[0], list):
            # caso fornecido vetor como array
            self.array = array[:] # vetor (array)

            mat = list()
            for i, e in enumerate(array):
                mat.append(list())
                mat[i].append(e)
            self.mat = mat # representação matricial
        else:
            # caso fornecido vetor como representação matricial
            arr = list()
            for e in array:
                arr.append(e[0])
            self.array = arr # vetor (array)

            self.mat = array # representação matricial

class Tranformations:
    # Matrizes de Reflexão
    REF_2DX = ((1,  0), 
               (0, -1))
    
    REF_2DY = ((-1, 0), 
               (0,  1))
    
    REF_3DX = ((1,  0,  0),
               (0, -1,  0),
               (0,  0, -1))
    
    REF_3DY = ((-1, 0,  0),
               ( 0, 1,  0),
               ( 0, 0, -1))
    
    REF_3DZ = ((-1,  0, 0),
               ( 0, -1, 0),
               ( 0,  0, 1))
    
    # Métodos de Reflexão
    def reflection2DX(self, vector):
        return LA.produto(self.REF_2DX, vector.mat)
    
    def reflection2DY(self, vector):
        return LA.produto(self.REF_2DY, vector.mat)
    
    def  reflection3DX(self, vector):
        return LA.produto(self.REF_3DX, vector.mat)

    def  reflection3DY(self, vector):
        return LA.produto(self.REF_3DY, vector.mat)

    def  reflection3DZ(self, vector):
        return LA.produto(self.REF_3DZ, vector.mat)
    
    # Matrizes de Projeção
    PROJ_2DX = ((1, 0), 
                (0, 0))
    
    PROJ_2DY = ((0, 0), 
                (0, 1))
    
    PROJ_3DX = ((1, 0, 0),
                (0, 0, 0),
                (0, 0, 0))
    
    PROJ_3DY = ((0, 0, 0),
                (0, 1, 0),
                (0, 0, 0))
    
    PROJ_3DZ = ((0, 0, 0),
                (0, 0, 0),
                (0, 0, 1))
    
    # Métodos de Projeção
    def  projection2DX(self, vector):
        return LA.produto(self.PROJ_2DX, vector.mat)
    
    def  projection2DY(self, vector):
        return LA.produto(self.PROJ_2DY, vector.mat)
    
    def  projection3DX(self, vector):
        return LA.produto(self.PROJ_3DX, vector.mat)
    
    def  projection3DY(self, vector):
        return LA.produto(self.PROJ_3DY, vector.mat)
    
    def  projection3DZ(self, vector):
        return LA.produto(self.PROJ_3DZ, vector.mat)
    
    # Matrizes de Rotação
    def Rot(self, theta): # theta em graus
        theta = rad(theta) # convertendo theta em rad
        return ( ( cos(theta), sen(theta)), 
                 (-sen(theta), cos(theta)) )

    def Rot_X(self, theta):
        theta = rad(theta)
        return ( (1,          0,           0), 
                 (0, cos(theta), -sen(theta)), 
                 (0, sen(theta),  cos(theta)) )
    
    def Rot_Y(self, theta):
        theta = rad(theta)
        return ( (cos(theta),  0, sen(theta)), 
                 (0,           1,          0),
                 (-sen(theta), 0, cos(theta)) )
    
    def Rot_Z(self, theta):
        theta = rad(theta)
        return ( (cos(theta), -sen(theta), 0),
                 (sen(theta),  cos(theta), 0),
                 (0,                    0, 1) )
    
    # Métodos de Rotação
    def rotation2D(self, vector, angle):
        return (LA.produto(self.Rot(angle), vector.mat))
    
    def rotation3DX(self, vector, angle):
        return LA.produto(self.Rot_X(angle), vector.mat)
    
    def rotation3DY(self, vector, angle):
        return LA.produto(self.Rot_Y(angle), vector.mat)

    def rotation3DZ(self, vector, angle):
        return LA.produto(self.Rot_Z(angle), vector.mat)