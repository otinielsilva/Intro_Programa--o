import matplotlib.pyplot as plt
x = list(range(-10, 11))
y = []

for n in x:
    y.append(n+2)
plt.title("f(x)=x+2")
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.show()