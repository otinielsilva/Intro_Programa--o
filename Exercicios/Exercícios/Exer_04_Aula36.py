import matplotlib.pyplot as plt

meses=["Jan","Fav","Mar","Abr","Mai","Jun"]
vendas=[]
for x in meses:
    vendas.append(input("Digite o total de vendas do mês de {}: ".format(x)))
plt.title("Vendas Por Mês")
plt.xlabel("Meses")
plt.ylabel("Vendas")
plt.bar(meses,vendas)
plt.show()