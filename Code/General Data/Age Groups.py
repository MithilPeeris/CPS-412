import pandas as ex
import matplotlib.pyplot as plt
df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
Age_group = df['Select the age group you belong to.']
Gender = df['How do you identify yourself?']
def age_groups():
    count_18_23 = 0
    count_24_30 = 0
    count_30 = 0
    for j in Age_group:
        if j == '18-23':
            count_18_23 += 1 
        elif j == '24-30':
            count_24_30 += 1
        elif j == '30+':
            count_30 += 1
    y_axis = [count_18_23,count_24_30,count_30]
    x_axis = ['18-23','24-30','30+']
    plt.bar(x_axis,y_axis,color = 'turquoise')
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
    plt.title('Age Groups')
    plt.xlabel('Age')
    plt.ylabel('Number of People')
    plt.show()
age_groups()
