import matplotlib.pyplot as plt
x = list(range(0,41))
y1=[]
y2=[]
y3=[]
y4=[]

for n in x:
    y1.append(4*n+5)
    y2.append(3*n+5)
    y3.append(2*n+5)
    y4.append(n+5)
plt.plot(x,y1,label="4x+5")
plt.plot(x,y2,label="3x+5")
plt.plot(x,y3,label="2x+5")
plt.plot(x,y4,label="x+5")
plt.legend()
plt.show()