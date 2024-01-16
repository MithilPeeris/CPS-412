import pandas as ex
import matplotlib.pyplot as plt

Self_study = 0
Aid_in_assignment = 0
Summarizing_tool = 0
To_explore_the_concepts_of_ChatGPT = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['What did you use ChatGPT for?'])):
    if df['What did you use ChatGPT for?'][j] == 'Self study ( Understanding Concepts, extra practice, etc.)':
        Self_study += 1
    if df['What did you use ChatGPT for?'][j] == 'Aid in assignment':
        Aid_in_assignment += 1
    if df['What did you use ChatGPT for?'][j] == 'Summarizing tool':
        Summarizing_tool += 1
    if df['What did you use ChatGPT for?'][j] == 'To explore the concepts of ChatGPT':
        To_explore_the_concepts_of_ChatGPT += 1

y_axis = [Self_study,Aid_in_assignment,Summarizing_tool,To_explore_the_concepts_of_ChatGPT]
x_axis = ['Self study','Aid in assignment','Summarizing tool','To explore the concepts of ChatGPT']

plt.bar(x_axis, y_axis, color = 'turquoise')
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
plt.ylabel("Number of People")
plt.xlabel("Uses of ChatGPT")
plt.title('What did you use ChatGPT for?', fontweight = 'bold')
plt.show()
