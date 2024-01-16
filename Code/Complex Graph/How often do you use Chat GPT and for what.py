import pandas as np
import matplotlib.pyplot as plt

list_use = []
list_other = []

daily_self = 0
daily_assignment = 0
daily_summarizing = 0
daily_explore = 0
daily_other = 0

weekly_self = 0
weekly_assignment = 0
weekly_summarizing = 0
weekly_explore = 0
weekly_other = 0

monthly_self = 0
monthly_assignment = 0
monthly_summarizing = 0
monthly_explore = 0
monthly_other = 0

df = np.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')

for j in range(len(df['How often do you use ChatGPT?'])):
    list_use.append([df['How often do you use ChatGPT?'][j]])
for h in range(len(df["What did you use ChatGPT for?"])):
    list_use[h].append(df["What did you use ChatGPT for?"][h])
for z in range(len(df['If yes, have you ever used ChatGPT?'])):
    list_use[z].append(df["If yes, have you ever used ChatGPT?"][z])

for h in range(len(list_use)):
    if list_use[h][2] == 'Yes':
        if list_use[h][0] == 'Daily':
            if 'Self study ( Understanding Concepts, extra practice, etc.)' in list_use[h][1]:
                daily_self += 1
                list_use[h][1] = list_use[h][1].replace('Self study ( Understanding Concepts, extra practice, etc.)','')
            if 'To explore the concepts of ChatGPT' in list_use[h][1]:
                daily_explore += 1
                list_use[h][1] = list_use[h][1].replace('To explore the concepts of ChatGPT','')            
            if 'Aid in assignment' in list_use[h][1]:
                daily_assignment += 1
                list_use[h][1] = list_use[h][1].replace('Aid in assignment','')
            if 'Summarizing tool' in list_use[h][1]:
                daily_summarizing += 1
                list_use[h][1] = list_use[h][1].replace('Summarizing tool','')
            if len(list_use[h][1]) > 0:
                list_other.append(list_use[h][1])
 
        if list_use[h][0] == 'Weekly':
            if 'Self study ( Understanding Concepts, extra practice, etc.)' in list_use[h][1]:
                weekly_self += 1
                list_use[h][1] = list_use[h][1].replace('Self study ( Understanding Concepts, extra practice, etc.)','')
            if 'To explore the concepts of ChatGPT' in list_use[h][1]:
                weekly_explore += 1
                list_use[h][1] = list_use[h][1].replace('To explore the concepts of ChatGPT','')            
            if 'Aid in assignment' in list_use[h][1]:
                weekly_assignment += 1
                list_use[h][1] = list_use[h][1].replace('Aid in assignment','')
            if 'Summarizing tool' in list_use[h][1]:
                weekly_summarizing += 1
                list_use[h][1] = list_use[h][1].replace('Summarizing tool','')
            if len(list_use[h][1]) > 0:
                list_other.append(list_use[h][1])           
        
        if list_use[h][0] == 'Monthly':
            if 'Self study ( Understanding Concepts, extra practice, etc.)' in list_use[h][1]:
                monthly_self += 1
                list_use[h][1] = list_use[h][1].replace('Self study ( Understanding Concepts, extra practice, etc.)','')
            if 'To explore the concepts of ChatGPT' in list_use[h][1]:
                monthly_explore += 1
                list_use[h][1] = list_use[h][1].replace('To explore the concepts of ChatGPT','')            
            if 'Aid in assignment' in list_use[h][1]:
                monthly_assignment += 1
                list_use[h][1] = list_use[h][1].replace('Aid in assignment','')
            if 'Summarizing tool' in list_use[h][1]:
                monthly_summarizing += 1
                list_use[h][1] = list_use[h][1].replace('Summarizing tool','')
            if len(list_use[h][1]) > 0:
                list_other.append(list_use[h][1])

for j in range(len(list_other)):
    while ',' in list_other[j]:
        list_other[j] = list_other[j].replace(', ','')

new_list_other = list_other[:]
new_list_other = list(set(new_list_other))
new_list_other = list(filter(None, new_list_other))

for z in range(len(list_use)):
    for j in new_list_other:
        if type(list_use[z][1]) == str:
            if j in list_use[z][1]:
                if list_use[z][0] == "Daily":
                    daily_other += 1
                if list_use[z][0] == "Weekly":
                    weekly_other += 1
                if list_use[z][0] == "Monthly":
                    monthly_other += 1

assignment = np.array([daily_assignment, weekly_assignment , monthly_assignment,])
selfstudy = np.array([daily_self, weekly_self, monthly_self])
Summarizing = np.array([daily_summarizing, weekly_summarizing, monthly_summarizing])
explore = np.array([daily_explore, weekly_explore, monthly_explore])
other = np.array([daily_other, weekly_other, monthly_other])

x_axis = ['Daily','Weekly','Monthly']

plt.bar(x_axis, selfstudy, color='turquoise', width = 0.6)
plt.bar(x_axis, assignment, bottom = selfstudy, color='indigo', width = 0.6)
plt.bar(x_axis, Summarizing, bottom = selfstudy + assignment, color='palegreen', width = 0.6)
plt.bar(x_axis, explore, bottom = selfstudy + assignment + Summarizing, color='pink', width = 0.6)
plt.bar(x_axis, other, bottom = explore + selfstudy + assignment + Summarizing, color='yellow', width = 0.6)

h1 = daily_self
h2 = daily_assignment
h3 = daily_summarizing
h4 = daily_explore
h5 = daily_other
plt.text(0.0 ,h1 / 2., "%d" % h1, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 + h3 / 2., "%d" % h3, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 + h3 + h4 / 2., "%d" % h4, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 + h3 + h4 + h5/ 2., "%d" % h5, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

h6 = weekly_self
h7 = weekly_assignment
h8 = weekly_summarizing
h9 = weekly_explore
h10 = weekly_other
plt.text(1 ,h6 / 2., "%d" % h6, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h6 + h7 / 2., "%d" % h7, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h6 + h7 + h8 / 2., "%d" % h8, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h6 + h7 + h8 + h9 / 2., "%d" % h9, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h6 + h7 + h8 + h9 + h10/ 2., "%d" % h10, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

h11 = monthly_self
h12 = monthly_assignment
h13 = monthly_summarizing
h14 = monthly_explore
h15 = monthly_other
plt.text(2 ,h11 / 2., "%d" % h11, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h11 + h12 / 2., "%d" % h12, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h11 + h12 + h13 / 2., "%d" % h13, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h11 + h12 + h13 + h14 / 2., "%d" % h14, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h11 + h12 + h13 + h14 + h15 / 2., "%d" % h15, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

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
plt.xlabel("How often fo you use ChatGPT")
plt.ylabel("Number of People")
plt.legend(["Aid in Assignment", "Self Study", "Summarizing Tool", "To Explore"])
plt.title("Relationship Between Frequency and the Ways ChatGPT is used", fontweight = 'bold', x = 0.5, y = 1.05)
plt.show()


