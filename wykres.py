# rysowanie funkcji x = f(x)
import matplotlib.pyplot as plt

x = [-5,-4,-3,0,1,2,3,4,5,6,7]
x = [ i for i in range(-300,300) ]
y = []

for i in x:
    w = 2*i - 5
    y.append(w)

print(x)
print(y)

# rysujemy
plt.plot(x,y)
plt.grid()
plt.show()
