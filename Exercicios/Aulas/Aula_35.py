#Plotando Gráficos em Python

import matplotlib.pyplot as plt
x = [1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,3,4,5]
y = []
for n in x:
    y.append(n*n)
plt.title("Aula 35")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x,y)
plt.show()