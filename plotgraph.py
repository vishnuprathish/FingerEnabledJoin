import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as chart
from plotgraph import *

def chartPlot(x1, x2):
    plt.plot([a for a in range(0, len(x1))], x1,'r')
    plt.plot([a for a in range(0, len(x2))], x2,'g')
    plt.show()

def chartPlot3(x1, x2, y):
    plt.plot(y, x1,'r')
    plt.plot(y, x2,'g')
    plt.show()

def plot4(x1, x2, x3, y):
    plt.plot(y, x1,'r')
    plt.plot(y, x2,'g')
    plt.plot(y, x3,'b')
    plt.show()

def plot5(x1, x2, x3, x4, y):
    plt.plot(y, x1,'r')
    plt.plot(y, x2,'g')
    plt.plot(y, x3,'b')
    plt.plot(y, x4,'y')
    plt.show()    


x1 =[10000,20000,30400,40000,50000]
x2 =[10000,20000,30000,40000,50000]
x3 =[5000,15000,25000,35000,45000]
x4 =[2000,12000,22000,32000,42000]


#chartPlot(x1,x2)