import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
count_yes = 0
count_no = 0
count_maybe = 0

for j in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'Yes':
        count_yes += 1
for j in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'No':
        count_no += 1
for j in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'Maybe':
        count_maybe += 1

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
my_colors = ['indigo','palegreen','turquoise']
my_labels = ['Yes','No','Maybe']
plt.pie([count_yes,count_no,count_maybe], labels = my_labels, colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('Should Universities Adapt ChatGPT?', color = 'Magenta', fontweight = 'bold')
plt.show()