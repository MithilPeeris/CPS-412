import pandas as np
import matplotlib.pyplot as plt

list_plagarism = []

yes_postitive = 0
yes_negative = 0
yes_not_sure = 0

no_postitive = 0
no_negative = 0
no_not_sure = 0

maybe_postitive = 0
maybe_negative = 0
maybe_not_sure = 0

df = np.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['Do you think use of ChatGPT should be considered plagiarism?'])):
    list_plagarism.append([df['Do you think use of ChatGPT should be considered plagiarism?'][j]])
for h in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    list_plagarism[h].append(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][h])
for g in range(len(df['If yes, have you ever used ChatGPT?'])):
    list_plagarism[g].append(df['If yes, have you ever used ChatGPT?'][g])
    
    
for j in range(len(list_plagarism)):
    if list_plagarism[j][2] == 'Yes':
        if list_plagarism[j][0] == 'Yes' and list_plagarism[j][1] == 'Positive':
            yes_postitive += 1
        if list_plagarism[j][0] == 'Yes' and list_plagarism[j][1] == 'Negative':
            yes_negative += 1
        if list_plagarism[j][0] == 'Yes' and list_plagarism[j][1] == 'Not Sure':
            yes_not_sure += 1
        
        if list_plagarism[j][0] == 'No' and list_plagarism[j][1] == 'Positive':
            no_postitive += 1
        if list_plagarism[j][0] == 'No' and list_plagarism[j][1] == 'Negative':
            no_negative += 1
        if list_plagarism[j][0] == 'No' and list_plagarism[j][1] == 'Not Sure':
            no_not_sure += 1
        
        if list_plagarism[j][0] == 'Maybe' and list_plagarism[j][1] == 'Positive':
            maybe_postitive += 1
        if list_plagarism[j][0] == 'Maybe' and list_plagarism[j][1] == 'Negative':
            maybe_negative += 1
        if list_plagarism[j][0] == 'Maybe' and list_plagarism[j][1] == 'Not Sure':
            maybe_not_sure += 1   
     
        
positive = np.array([yes_postitive, no_postitive , maybe_postitive])
negative = np.array([yes_negative, no_negative, maybe_negative])
not_sure = np.array([yes_not_sure, no_not_sure, maybe_not_sure])
        

x_axis = ['Yes','No','maybe']

plt.bar(x_axis, positive, color='turquoise', width = 0.6)
plt.bar(x_axis, negative, bottom = positive, color='indigo', width = 0.6)
plt.bar(x_axis, not_sure, bottom = positive + negative, color='palegreen', width = 0.6)

h1 = yes_postitive
h2 = yes_negative
h3 = yes_not_sure
plt.text(0.0 ,h1 / 2., "%d" % h1, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 + h3 / 2., "%d" % h3, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

h4 = no_postitive
h5 = no_negative
h6 = no_not_sure
plt.text(1 ,h4 / 2., "%d" % h4, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h4 + h5 / 2., "%d" % h5, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(1 ,h4 + h5 + h6 / 2., "%d" % h6, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

h7 = maybe_postitive
h8 = maybe_negative
h9 = maybe_not_sure
plt.text(2,h7 / 2., "%d" % h7, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h7 + h8 / 2., "%d" % h8, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(2 ,h7 + h8 + h9 / 2., "%d" % h9, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

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
plt.xlabel("Is using ChatGPT Plagarism")
plt.ylabel("Number of People")
plt.legend(["Positive Impact", "Negative Impact", "Not Sure"])
plt.title("Relationship Between Plagarism and the Impact on the Long Run", fontweight = 'bold', size = 'xx-large')
plt.show()