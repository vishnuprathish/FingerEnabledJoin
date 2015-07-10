import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def chartPlot(x1, x2, text1 = "test", text2 = "test"):
    red_patch = mpatches.Patch(color='red', label=text1)
    green_patch = mpatches.Patch(color='green', label=text2)
    plt.legend(handles=[red_patch, green_patch])
    plt.ylabel("Cost")
    plt.xlabel("Size(I) x Size(R)")
    plt.plot([a for a in range(0, len(x1))], x1, 'r')
    plt.plot([a for a in range(0, len(x2))], x2, 'g')
    plt.show()

def chartPlot3(x1, x2, y, text1 = "test", text2 = "test", title="test"):
    red_patch = mpatches.Patch(color='red', label=text1)
    green_patch = mpatches.Patch(color='green', label=text2)
    plt.legend(handles=[red_patch, green_patch], loc='best')
    plt.ylabel("Cost")
    plt.xlabel("Size(I) x Size(R)")
    plt.ylim(ymin = 0, ymax = 1000000)
    plt.plot(y, x1,'r')
    plt.plot(y, x2,'g')
    plt.savefig(title+".png")
    plt.show()

def plot4(x1, x2, x3, y):
    #red_patch = mpatches.Patch(color='red', label=text1)
    #green_patch = mpatches.Patch(color='red', label=text2)
    plt.ylabel("Cost")
    plt.xlabel("Size(I) x Size(R)")
    plt.plot(y, x1,'r')
    plt.plot(y, x2,'g')
    plt.plot(y, x3,'b')
    plt.show()

def plot5(x1, x2, x3, x4, y):
    #red_patch = mpatches.Patch(color='red', label=text1)
    #green_patch = mpatches.Patch(color='red', label=text2)
    plt.ylabel("Cost")
    plt.xlabel("Size(I) x Size(R)")
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