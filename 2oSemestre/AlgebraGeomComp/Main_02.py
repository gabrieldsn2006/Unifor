import matplotlib.pyplot as plt
import Algebra_02 as AL2
TR = AL2.Tranformations()

def plot(arr):
    plt.plot(arr[0], arr[1], marker='o')
    plt.text(arr[0], arr[1], f'({arr[0]:.1f}, {arr[1]:.1f})\n', fontsize=12, ha='center', va='bottom')

myVector1 = AL2.Vector( [1, 1] )

myVector2 = AL2.Vector( TR.projection2DX(myVector1) )
myVector3 = AL2.Vector( TR.projection2DY(myVector1) )

myVector4 = AL2.Vector( TR.reflection2DX(myVector1) )
myVector5 = AL2.Vector( TR.reflection2DY(myVector1) )

myVector6 = AL2.Vector( TR.rotation2D(myVector1, 45) )
myVector7 = AL2.Vector( TR.rotation2D(myVector1, -45) )



plot(myVector1.array)
plot(myVector2.array)
plot(myVector3.array)
plot(myVector4.array)
plot(myVector5.array)
plot(myVector6.array)
plot(myVector7.array)



plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()