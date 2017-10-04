import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
line = -1
x=1
charCount= []
wcharCount = []
input = raw_input('Search the wiki')
f = open('database', "r")
data = f.readlines()
for link in range(len(data)):
    data[link] = data[link][:-2]

for link in data:
    c = len(link)
    c = str(c)
    charCount.append(c)
    z = link.count(input)
    z = str(z)
    print(z)
    print(c)
    wcharCount.append(z)
print(wcharCount)
print(charCount)
plt.scatter(charCount, wcharCount, color = "b", marker = ".")
plt.xlabel("Total character count")
plt.ylabel('Total # of ' + input + "s in string")
plt.title("Matplotlib test")
plt.legend()
plt.show()