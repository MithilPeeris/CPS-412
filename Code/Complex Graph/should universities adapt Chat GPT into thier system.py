import pandas as ex
import matplotlib.pyplot as plt

universities_should_adapt = 0
universities_should_not_adapt = 0
maybe_universities_should_adapt = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['Do you think universities should adapt ChatGPT as a part of educational system?'])):
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'Yes':
        universities_should_adapt += 1
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'No':
        universities_should_not_adapt += 1
    if df['Do you think universities should adapt ChatGPT as a part of educational system?'][j] == 'Maybe':
        maybe_universities_should_adapt += 1

y_axis = [universities_should_adapt,universities_should_not_adapt,maybe_universities_should_adapt]
x_axis = ['Yes','No','Maybe']

plt.bar(x_axis, y_axis, color = 'turquoise')
plt.xlabel("Plagarism")
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
plt.title("Do you think universities should adapt ChatGPT as a part of educational system?", fontweight = 'bold')
plt.show()


