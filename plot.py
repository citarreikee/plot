import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

filename = 'ni_task_20200424173713_oven.txt'
X = []
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        value = list(map(float,line.split(',')))
        X += value
        
X1 =  X[:2000] 
# print(X)

  
plt.plot(X1)
plt.show()
