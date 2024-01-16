import pandas as ex
import matplotlib.pyplot as plt
import numpy as np
list_impact = []

count_yes_positive_yes = 0
count_yes_negative_yes = 0
count_yes_not_sure_yes = 0

count_no_positive_yes = 0
count_no_negative_yes = 0
count_no_not_sure_yes = 0

count_maybe_positive_yes = 0
count_maybe_negative_yes = 0
count_maybe_not_sure_yes = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['Do you think use of ChatGPT should be considered plagiarism?'])):
    list_impact.append([df['Do you think use of ChatGPT should be considered plagiarism?'][j]])
for h in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    list_impact[h].append(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][h])
for z in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    list_impact[z].append(df['Do you think universities should adapt ChatGPT as a part of educational system?'][z])
    
for y in range(len(list_impact)):
    
    if list_impact[y][2] == 'Yes':
        if list_impact[y][0] == 'Yes' and list_impact[y][1] == 'Positive':
            count_yes_positive_yes += 1
        if list_impact[y][0] == 'Yes' and list_impact[y][1] == 'Negative':
            count_yes_negative_yes += 1
        if list_impact[y][0] == 'Yes' and list_impact[y][1] == 'Not Sure':
            count_yes_not_sure_yes += 1
        
        if list_impact[y][0] == 'No' and list_impact[y][1] == 'Positive':
            count_no_positive_yes += 1
        if list_impact[y][0] == 'No' and list_impact[y][1] == 'Negative':
            count_no_negative_yes += 1
        if list_impact[y][0] == 'No' and list_impact[y][1] == 'Not Sure':
            count_no_not_sure_yes += 1
    
        if list_impact[y][0] == 'Maybe' and list_impact[y][1] == 'Positive':
            count_maybe_positive_yes += 1
        if list_impact[y][0] == 'Maybe' and list_impact[y][1] == 'Negative':
            count_maybe_negative_yes += 1
        if list_impact[y][0] == 'Maybe' and list_impact[y][1] == 'Not Sure':
            count_maybe_not_sure_yes += 1

count_positive_yes = np.array([count_yes_positive_yes, count_no_positive_yes, count_maybe_positive_yes])
count_negative_yes =np.array([ count_yes_negative_yes, count_no_negative_yes, count_maybe_negative_yes])
count_not_sure_yes = np.array([count_yes_not_sure_yes, count_no_not_sure_yes, count_maybe_not_sure_yes])

x_axis = ['Yes','No','Maybe']

ax = plt.bar(x_axis, count_positive_yes, color = 'turquoise')
ax = plt.bar(x_axis, count_negative_yes, bottom = count_positive_yes, color = 'indigo')
ax = plt.bar(x_axis, count_not_sure_yes, bottom = count_positive_yes + count_negative_yes, color = 'palegreen')
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
print(plt.rcParams.keys())
plt.xlabel("Plagarism")
plt.ylabel("Number of People")
plt.legend(["Positive Impact", "Negative Impact", "Not Sure"])
plt.title("Universities should adapt ChatGPT", fontweight = 'bold')
plt.show()


