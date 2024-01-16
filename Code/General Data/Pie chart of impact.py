import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
count_positive = 0
count_negative = 0
count_not_sure = 0

for j in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    if df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][j] == 'Positive':
        count_positive += 1
for j in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    if df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][j] == 'Negative':
        count_negative += 1
for j in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    if df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][j] == 'Not Sure':
        count_not_sure += 1

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
my_colors = ['indigo','palegreen','turquoise']
my_labels = ['Positive','Negative','Not Sure']
plt.pie([count_positive,count_negative,count_not_sure], labels = my_labels, colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('Impact of ChatGPT in the long run', color = 'Magenta', fontweight = 'bold')
plt.show()