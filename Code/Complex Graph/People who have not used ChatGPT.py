import pandas as ex
import matplotlib.pyplot as plt
import numpy as np
list_gender = []

count_male_18_23_no = 0
count_male_24_30_no = 0
count_male_30_no = 0

count_female_18_23_no = 0
count_female_24_30_no = 0
count_female_30_no = 0

count_non_binary_18_23_no = 0
count_non_binary_24_30_no = 0
count_non_binary_30_no = 0

count_not_to_say_18_23_no = 0
count_not_to_say_24_30_no = 0
count_not_to_say_30_no = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['How do you identify yourself?'])):
    list_gender.append([df['How do you identify yourself?'][j]])
for h in range(len(df['Select the age group you belong to.'])):
    list_gender[h].append(df['Select the age group you belong to.'][h])
for z in range(len(df['Have you ever used ChatGPT?'])):
    list_gender[z].append(df['Have you ever used ChatGPT?'][z])
for y in range(len(list_gender)):

    if list_gender[y][2] == 'No':
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '18-23':
            count_male_18_23_no += 1
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '24-30':
            count_male_24_30_no += 1
        if list_gender[y][0] == 'Male' and list_gender[y][1] == '30+':
            count_male_30_no += 1
        
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '18-23':
            count_female_18_23_no += 1
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '24-30':
            count_female_24_30_no += 1
        if list_gender[y][0] == 'Female' and list_gender[y][1] == '30+':
            count_female_30_no += 1
    
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '18-23':
            count_non_binary_18_23_no += 1
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '24-30':
            count_non_binary_24_30_no += 1
        if list_gender[y][0] == 'Non-Binary' and list_gender[y][1] == '30+':
            count_non_binary_30_no += 1

        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '18-23':
            count_not_to_say_18_23_no += 1
        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '24-30':
            count_not_to_say_24_30_no += 1
        if list_gender[y][0] == 'Prefer not to respond' and list_gender[y][1] == '30+':
            count_not_to_say_30_no += 1

count_18_23_no = np.array([count_male_18_23_no, count_female_18_23_no, count_non_binary_18_23_no, count_not_to_say_18_23_no])
count_24_30_no =np.array([ count_male_24_30_no, count_female_24_30_no, count_non_binary_24_30_no, count_not_to_say_24_30_no])
count_30_no = np.array([count_male_30_no, count_female_30_no, count_non_binary_30_no, count_not_to_say_30_no])

x_axis_new = ['Male','Female','Non-Binary','Prefer not to say']
plt.bar(x_axis_new, count_18_23_no, color='turquoise')
plt.bar(x_axis_new, count_24_30_no, bottom = count_18_23_no, color='indigo')
plt.bar(x_axis_new, count_30_no, bottom = count_18_23_no + count_24_30_no, color='palegreen')
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
plt.title("People who have not used ChatGPT")
plt.show()
