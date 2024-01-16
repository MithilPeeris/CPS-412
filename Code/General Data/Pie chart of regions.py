import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')

count_asia = 0
count_australia = 0
count_africa = 0
count_north_amercia = 0
count_south_america = 0
count_europe = 0
count_antartica = 0



for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'Asia':
        count_asia += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'Australia':
        count_australia += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'Africa':
        count_africa += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'North America':
        count_north_amercia += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'South America':
        count_south_america += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'Europe':
        count_europe += 1
for j in range(len(df['Which continent do you belong to?'])):
    if df['Which continent do you belong to?'][j] == 'Antartica':
        count_antartica += 1

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
my_colors = ['indigo','turquoise','blue','palegreen','orange','red','yellow']
countries = ['count_asia','count_africa','count_australia','count_north_amercia','count_south_america','count_europe','count_antartica']
my_labels_first = {'count_asia':'Asia','count_africa':'Africa','count_australia':'Australia','count_north_amercia':'North America','count_south_america':'South America','count_europe':'Europe','count_antartica':'Antartica'}
my_labels = [my_labels_first[j] for j in countries if globals()[j] !=0]
sizes = [100/len(my_labels)]*len(my_labels)
patches, texts = plt.pie(sizes, colors=my_colors, startangle=90)
plt.legend(patches, my_labels, loc="best")
plt.pie([globals()[j] for j in countries if globals()[j] != 0],colors =  my_colors, autopct='%.1f%%',textprops={'color':"magenta", 'size':'large', 'fontweight' : 'bold'})
plt.title('Pie Chart of the Different Continents', color = 'Magenta', fontweight = 'bold')
plt.show()