print(8*"-=-")
print("Calculando Equação do 2º")
print(8*"-=-")
print("Equação do 2º -> ax^2+bx+c=0\n")
def cal_delta(a,b,c):
    delta = (val_b**2) - (4*val_a*val_c)
    return delta
val_a = float(input("Digite o valor de A: "))
val_b = float(input("Digite o valor de B: "))
val_c = float(input("Digite o valor de c: "))
print("\nO valor de delta é: {:.1f}".format(cal_delta(val_a,val_b,val_c)))

def bhaskara(a,b,c):
    if cal_delta(a,b,c) == 0:
        raiz_1 = (-val_b + cal_delta(a,b,c) **(1/2)) / (2*val_a)
        print("A equação possue uma raiz!\nx1=x2 -> {}".format(raiz_1))
    elif cal_delta(a,b,c) > 0:
        x_1 = (-val_b + cal_delta(a,b,c) ** (1/2)) / (2 * val_a)
        x_2 = (-val_b - cal_delta(a,b,c) ** (1/2)) / (2 * val_a)
        print("A equação possue duas raizes!\nX1->{:.2f}\nX2->{:.2f}".format(x_1, x_2))
    else:
        print("A equação não possue raizes reais!")
print(bhaskara(val_a,val_b,val_c))