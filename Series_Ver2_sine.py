
print('\n    Unit 3: Series Expansion\n')

import numpy as np
import math as mt
import matplotlib.pyplot as plt
from sympy import *
import sys

a=-3*np.pi; b=3*np.pi

x=np.linspace(a,b,200)
def ex(x,n):
    add = 0
    for k in range(n):
        add = add+ pow(-1,k)*pow(x,2*k+1)/(mt.factorial(2*k+1))
    plt.plot(x,add.T)#,lw=NN-n+1, ls= (0,(n+2,n,1,n)))
    plt.pause(0.2)
    return add

leg=[]
fn=[]
plt.ylim([-2.0,2.0])
while True:
    N = int(input(" Enter number of terms of a series to be evaluated: \n \
Enter 0 to exit programm:     "))
    #print(type(N))
    if N != 0: #type(N) is int:
        leg.append(f'for {N} terms') #leg.append(N)
        exp_s = ex(x,N)
        fn.append(exp_s[-1])
    else:
        plt.xlabel("X")
        plt.ylabel("Sine Series")
        plt.legend(leg)
        plt.title(r'$sin(x) = \sum_{k=0}^\infty (-1)^k\frac{x^{2k+1}}{(2k+1)!}$'\
          r'$= x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\ldots$')
        plt.pause(0.1)
        print("Exponential Series--\n"+"\n".join(f'value  {item} is {round(item2,4)}' for item, item2 in zip(leg,fn) ))
        print(" Exit Programm")
        exit(0) 
