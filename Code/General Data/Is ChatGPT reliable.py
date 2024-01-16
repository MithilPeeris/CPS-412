import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')

var1 = df['How reliable do you think the answers provided by ChatGPT are?']
plt.hist(var1, bins=4,color ='c')
plt.xlabel('Range of Ratings')
plt.ylabel('Number of People')
plt.title('How reliable do you think the answers provided by CHatGPT')
plt.show()