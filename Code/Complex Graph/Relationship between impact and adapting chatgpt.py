import pandas as np
import matplotlib.pyplot as plt

list_adapt = []

should_postitive = 0
should_negative = 0
should_not_sure = 0

should_not_postitive = 0
should_not_negative = 0
should_not_not_sure = 0

maybe_postitive = 0
maybe_negative = 0
maybe_not_sure = 0

df = np.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')

for j in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    list_adapt.append([df['Do you think universities should adapt ChatGPT as a part of educational system?'][j]])
for h in range(len(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"])):
    list_adapt[h].append(df["What kind of impact do you think ChatGPT will have on students' knowledge in the long run?"][h])
for g in range(len(df["If yes, have you ever used ChatGPT?"])):
    list_adapt[g].append(df["If yes, have you ever used ChatGPT?"][g])

for j in range(len(list_adapt)):
    if list_adapt[j][2] == 'Yes':
        if list_adapt[j][0] == 'Yes' and list_adapt[j][1] == 'Positive':
            should_postitive += 1
        if list_adapt[j][0] == 'Yes' and list_adapt[j][1] == 'Negative':
            should_negative += 1
        if list_adapt[j][0] == 'Yes' and list_adapt[j][1] == 'Not Sure':
            should_not_sure += 1
        
        if list_adapt[j][0] == 'No' and list_adapt[j][1] == 'Positive':
            should_not_postitive += 1
        if list_adapt[j][0] == 'No' and list_adapt[j][1] == 'Negative':
            should_not_negative += 1
        if list_adapt[j][0] == 'No' and list_adapt[j][1] == 'Not Sure':
            should_not_not_sure += 1
        
        if list_adapt[j][0] == 'Maybe' and list_adapt[j][1] == 'Positive':
            maybe_postitive += 1
        if list_adapt[j][0] == 'Maybe' and list_adapt[j][1] == 'Negative':
            maybe_negative += 1
        if list_adapt[j][0] == 'Maybe' and list_adapt[j][1] == 'Not Sure':
            maybe_not_sure += 1        
        
positive = np.array([should_postitive, should_not_postitive , maybe_postitive])
negative = np.array([should_negative, should_not_negative, maybe_negative])
not_sure = np.array([should_not_sure, should_not_not_sure, maybe_not_sure])
        

x_axis = ['Should Adapt','Should not Adapt','Not Sure']

plt.bar(x_axis, positive, color='turquoise', width = 0.6)
plt.bar(x_axis, negative, bottom = positive, color='indigo', width = 0.6)
plt.bar(x_axis, not_sure, bottom = positive + negative, color='palegreen', width = 0.6)

h1 = should_postitive
h2 = should_negative
h3 = should_not_sure
plt.text(0.0 ,h1 / 2., "%d" % h1, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 / 2., "%d" % h2, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")
plt.text(0.0 ,h1 + h2 + h3 / 2., "%d" % h3, ha="center", va="center", color="magenta", fontsize=16, fontweight="bold")

h4 = should_not_postitive
h5 = should_not_negative
h6 = should_not_not_sure
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
plt.xlabel("Should Universities Adapt ChaptGPT")
plt.ylabel("Number of People")
plt.legend(["Positive Impact", "Negative Impact", "Not Sure"])
plt.title("Relationship Between Adapting Chat GPT and the Impact on the Long Run", fontweight = 'bold', size = 'xx-large')
plt.show()


