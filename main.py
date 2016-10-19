import numpy as np
from math import sqrt
import random
import matplotlib.pyplot as plt
x = []
y = []
with open("input.txt") as f:
    for line in f:
        x.append(float(line.split(" ")[0]))
        y.append(float(line.split(" ")[1]))

N = len(x)

print "Enter the Degree of the Polynomial to be fit\n(It should be less than number of Data points available)\n"
n = int(input())

if n - 1 > N:
    print "N=",N,"<","n - 1=",n-1,"\nNot enough data points to generate ",n,"th degree polynomial.\n"
    exit()

def series_sum(x,t):
    s = 0
    for xi in x:
        s = s + xi**t
    return s
def series_sum_xy(x,y,t):
    s = 0
    for i in range(len(x)):
        s = s + y[i]*(x[i]**t)
    return s

M = np.array([[series_sum(x,i+j) for i in range(n+1)] for j in range(n+1)])

N = np.array([series_sum_xy(x,y,i) for i in range(n+1)])

coeffs =  np.linalg.solve(M, N)

s = ""
for i in range(len(coeffs)):
    s = s + str(coeffs[i]) + "\t"
s = s + "\n"
print "Coefficients of Polynomial\n",s

def get_prediction(coeffs, x):
    s = 0
    for i in range(len(coeffs)):
        s = s + (coeffs[i]*(x**i))
    return s

y_pred = [get_prediction(coeffs,x[i]) for i in range(len(x))]

S = 0
So = 0
for i in range(len(x)):
    S = S + (y[i] - y_pred[i])**2
    So = So + (y[i] - np.array(y).mean())**2

R = sqrt(1 - (S/So))

print "Coefficient of Determination",R

t = [random.random()*(max(x) - min(x)) + min(x) for i in range(1000)]
ty = [get_prediction(coeffs,t[i]) for i in range(1000)]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title("Polynomial Fit (Degree "+str(n)+")"+" vs True Values")
ax.set_ylabel("Y")
ax.set_xlabel("X")
ax.scatter(t,ty, s=30, c='b', marker="o", label='Estimated Value')
ax.scatter(x,y, s=30, c='r', marker="s", label='True Value')
# ax.scatter(x,y_pred, s=30, c='r', marker="o", label='Estimated Value')
plt.legend(loc='upper left')
plt.show()
fig.savefig("Plot.png")