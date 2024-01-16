import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')

count_diploma = 0
count_undergraduate = 0
count_masters = 0
count_phd = 0


for j in range(len(df['Highest level of Education'])):
    if df['Highest level of Education'][j] == 'Diploma':
        count_diploma += 1
for j in range(len(df['Highest level of Education'])):
    if df['Highest level of Education'][j] == 'Undergraduate':
        count_undergraduate += 1
for j in range(len(df['Highest level of Education'])):
    if df['Highest level of Education'][j] == 'Masters':
        count_masters += 1
for j in range(len(df['Highest level of Education'])):
    if df['Highest level of Education'][j] == 'Ph.D':
        count_phd += 1

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
my_colors = ['turquoise','indigo','blue','palegreen','orange','red','yellow']
countries = ['count_diploma','count_undergraduate','count_masters','count_phd']
my_labels_first = {'count_diploma':'Diploma','count_undergraduate':'Undergraduate','count_masters':'Masters','count_phd':'Ph.D'}
my_labels = [my_labels_first[j] for j in countries if globals()[j] !=0]
sizes = [100/len(my_labels)]*len(my_labels)
patches, texts = plt.pie(sizes, colors=my_colors, startangle=90)
plt.legend(patches, my_labels, loc="best")
plt.pie([globals()[j] for j in countries if globals()[j] != 0],colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('Highest Level of Education', color = 'Magenta', fontweight = 'bold')
plt.show()