import pandas as ex
import matplotlib.pyplot as plt

daily_usage = 0
weekly_usage = 0
monthly_usage = 0
never_used =0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['How often do you use ChatGPT?'])):
    if df['How often do you use ChatGPT?'][j] == 'Daily':
        daily_usage += 1
    if df['How often do you use ChatGPT?'][j] == 'Weekly':
        weekly_usage += 1
    if df['How often do you use ChatGPT?'][j] == 'Monthly':
        monthly_usage += 1
    if df['How often do you use ChatGPT?'][j] == 'Never':
        never_used += 1

y_axis = [daily_usage,weekly_usage,monthly_usage,never_used]
x_axis = ['Daily','Weekly','Monthly','Never']

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
plt.title("How often do you use ChatGPT?", fontweight = 'bold')
plt.show()