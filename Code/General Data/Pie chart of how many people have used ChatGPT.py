import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
count_yes = 0
count_no = 0

for j in range(len(df['If yes, have you ever used ChatGPT?'])):
    if df['If yes, have you ever used ChatGPT?'][j] == 'Yes':
        count_yes += 1
for j in range(len(df['If yes, have you ever used ChatGPT?'])):
    if df['If yes, have you ever used ChatGPT?'][j] == 'No':
        count_no += 1

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelsize'] = 'xx-large'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
plt.rcParams['boxplot.boxprops.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['xtick.labelsize'] = 'larger'
plt.rcParams['legend.fontsize'] = 'larger'
my_colors = ['indigo','palegreen']
my_labels = ['Yes','No']
plt.pie([count_yes,count_no], labels = my_labels, colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('People who have used ChatGPT', color = 'Magenta', fontweight = 'bold', size = 'xx-large')
plt.show()