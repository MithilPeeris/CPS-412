import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
count_yes = 0
count_no = 0
count_maybe = 0
list_recommend = []

for j in range(len(df['Would you recommend someone to use ChatGPT?'])):
    list_recommend.append([df['Would you recommend someone to use ChatGPT?'][j]])
for j in range(len(df['If yes, have you ever used ChatGPT?'])):
    list_recommend[j].append(df['If yes, have you ever used ChatGPT?'][j])

for j in range(len(list_recommend)):
    if list_recommend[j][1] == 'Yes':
        if list_recommend[j][0] == 'Yes':
             count_yes += 1
        if list_recommend[j][0] == 'No':
             count_no += 1
        if list_recommend[j][0] == 'Maybe':
             count_maybe += 1
        
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
my_colors = ['indigo','pink','palegreen']
my_labels = ['Yes','No','Maybe']
plt.pie([count_yes,count_no,count_maybe], labels = my_labels, colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('Will you recommend ChatGPT to someone ?', color = 'Magenta', fontweight = 'bold', size = 'xx-large')
plt.show()