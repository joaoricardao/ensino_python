#IMC
from matplotlib import pyplot as plt

altura=eval(input("Digite sua altura [em metros]: "))
peso=eval(input("Digite seu peso [em kilogramas]: "))
imc = ((peso)/(altura*altura))
print ("Seu IMC é:", (round(imc,2)), "kg/m2")

alturapadrao=list(range(150,180,2))
print (alturapadrao)

#Calcular a faixa padrão do IMC
pesopadrao=[]
for i in alturapadrao:
    pesopadrao.append(i*i*25/10000)
print (pesopadrao)

#Visualização da faixa padrao de IMC e do Valor de IMC calculado
plt.plot(pesopadrao, alturapadrao, marker='o')
plt.plot(peso, altura, marker='o')
plt.title("Índice de Massa Corpórea")
plt.xlabel("peso [kilogramas]")
plt.ylabel("altura [metros]")
plt.grid(True)
plt.show()
