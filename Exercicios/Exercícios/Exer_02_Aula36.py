import matplotlib.pyplot as plt
x = list(range(-10, 11))
y = []

for n in x:
    y.append((n**2)+(2*n)-1)
plt.title("f(x)=x^2+2*x-1")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y,".r",x,y,"-b")
plt.show()