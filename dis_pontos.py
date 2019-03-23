# Distância entre dois Pontos

from matplotlib import pyplot as plt

#xa = input("Digite a coordenada x do primeiro ponto: ")
#ya = input("Digite a coordenada y do primeiro ponto: ")
#xb = input("Digite a coordenada x do segundo ponto: ")
#yb = input("Digite a coordenada y do segundo ponto: ")

xa=2
ya=-3
xb=4
yb=5
x=[xa,xb]
y=[ya,yb]
# Isso:
print ((((xb-xa)**2)+((yb-ya)**2))**0.5)

# Ou isso:
dx=((xb-xa)**2)
dy=((yb-ya)**2)
d=((dx+dy))
resultado = d**(0.5)
print ("distância x: ", dx)
print ("distância y: ", dy)
print ("a diferença entre as distâncias x e y: ", d)
print ("o quadrado da diferença", round(resultado,2))


#visualização
plt.plot(x,y)
plt.title("Distância entre dois pontos")
plt.ylabel("Eixo Y")
plt.xlabel("Eixo X")
plt.grid(True)
plt.show()
