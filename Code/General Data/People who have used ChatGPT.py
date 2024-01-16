import pandas as ex
import matplotlib.pyplot as plt
import numpy as np
list_gender = []

count_male_18_23_yes = 0
count_male_24_30_yes = 0
count_male_30_yes = 0

count_female_18_23_yes = 0
count_female_24_30_yes = 0
count_female_30_yes = 0

count_non_binary_18_23_yes = 0
count_non_binary_24_30_yes = 0
count_non_binary_30_yes = 0

count_not_to_say_18_23_yes = 0
count_not_to_say_24_30_yes = 0
count_not_to_say_30_yes = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['How do you identify yourself?'])):
    list_gender.append([df['How do you identify yourself?'][j]])
for h in range(len(df['Select the age group you belong to.'])):
    list_gender[h].append(df['Select the age group you belong to.'][h])
for z in range(len(df['If yes, have you ever used ChatGPT?'])):
    list_gender[z].append(df['If yes, have you ever used ChatGPT?'][z])
for y in range(len(list_gender)):
    
    if list_gender[y][2] == 'Yes':
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '18-23':
            count_male_18_23_yes += 1
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '24-30':
            count_male_24_30_yes += 1
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '30+':
            count_male_30_yes += 1
        
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '18-23':
            count_female_18_23_yes += 1
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '24-30':
            count_female_24_30_yes += 1
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '30+':
            count_female_30_yes += 1
    
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '18-23':
            count_non_binary_18_23_yes += 1
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '24-30':
            count_non_binary_24_30_yes += 1
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '30+':
            count_non_binary_30_yes += 1

        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '18-23':
            count_not_to_say_18_23_yes += 1
        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '24-30':
            count_not_to_say_24_30_yes += 1
        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '30+':
            count_not_to_say_30_yes += 1

count_18_23_yes = np.array([count_male_18_23_yes, count_female_18_23_yes, count_non_binary_18_23_yes, count_not_to_say_18_23_yes])
count_24_30_yes =np.array([ count_male_24_30_yes, count_female_24_30_yes, count_non_binary_24_30_yes, count_not_to_say_24_30_yes])
count_30_yes = np.array([count_male_30_yes, count_female_30_yes, count_non_binary_30_yes, count_not_to_say_30_yes])

x_axis = ['Male','Female','Non-Binary','Prefer not to say']

plt.bar(x_axis, count_18_23_yes, color='turquoise')
plt.bar(x_axis, count_24_30_yes, bottom = count_18_23_yes, color='indigo')
plt.bar(x_axis, count_30_yes, bottom = count_18_23_yes + count_24_30_yes, color='palegreen')

plt.rcParams.update(plt.rcParamsDefault)
plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelsize'] = 'large'
plt.rcParams['axes.titlecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['figure.facecolor'] = 'black'
plt.rcParams['legend.labelcolor'] = 'white'
plt.rcParams['boxplot.boxprops.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.xlabel("Gender")
plt.ylabel("Number of People")
plt.legend(["Age between 18-23", "Age between 24-30", "Age 30+"])
plt.title("People who have used ChatGPT")
plt.show()


