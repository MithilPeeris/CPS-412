import pandas as ex
import matplotlib.pyplot as plt
df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
Gender = df['How do you identify yourself?']
def gender():
    count_male = 0
    count_female = 0
    count_transgender = 0
    count_non_binary = 0
    count_prefer_not_to_respond = 0
    for j in Gender:
        if j == 'Male':
            count_male += 1 
        elif j == 'Female':
            count_female += 1
        elif j == 'Non-Binary':
            count_non_binary += 1
        elif j == 'Transgender':
            count_transgender += 1
        elif j == 'Prefer not to respond':
            count_prefer_not_to_respond += 1
    y_axis = [count_female,count_male,count_transgender,count_non_binary,count_prefer_not_to_respond]
    x_axis = ['Female','Male','Transgender','Non-Binary','Perfer not to say']
    
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
    plt.title('Gender of Data')
    plt.xlabel('Gender')
    plt.ylabel('Number of People')
    plt.show()
gender()