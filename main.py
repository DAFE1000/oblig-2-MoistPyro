import matplotlib.pyplot as plt
import numpy as np
import math

def func(x: float) -> float:
    return math.exp(-1 * x / 4) * math.atan(x)

def derived(x: float) -> float:
    return math.atan(x) - 4/(x**2 + 1) #jeg ignorerer e^x leddet, siden det aldri er 0. (se utregning på papir)

def find_top():
    xs = np.linspace(0, 5, 50000)
    ys = [derived(x) for x in xs]
    temp = [(x, y) for (x, y) in enumerate(ys)]
    temp.sort(key=lambda a: abs(a[1])) #sorterer basert på absolut avstand fra 0.0
    i = temp[1][0] #finner indexen til tallet nermest 0.0
    return xs[i] #bruker indexen for å finne x-verdien


x_vals = np.linspace(0, 5, 50000)
y_vals = [func(x) for x in x_vals]

top_x = find_top()
top_y = func(top_x)

print(f"toppunkt: {top_x:.4f}, {top_y:.4f}")

plt.axis([0, 5, 0, 1])

plt.plot(x_vals, y_vals)
plt.plot(top_x, top_y, 'o')
plt.text(top_x+0.1, top_y+0.01, f"Toppunkt: {top_x:.4f}, {top_y:.4f}")

plt.grid(True, which='both') # bruk rutenett
# vis x og y aksen
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

plt.title("F(x)")
plt.savefig("plot.png")
plt.show()