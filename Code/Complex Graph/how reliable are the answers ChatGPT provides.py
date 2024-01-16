import pandas as ex
list_field_study = []
import matplotlib.pyplot as plt

def zero_or_one(n):
    return 1 if n == 0 else n

count_science_undergraduate = 0
count_engineering_undergraduate = 0
count_business_undergraduate = 0
count_medical_undergraduate = 0
count_arts_undergraduate = 0
count_finance_undergraduate = 0
count_politics_undergraduate = 0

count_science_diploma = 0
count_engineering_diploma = 0
count_business_diploma = 0
count_medical_diploma = 0
count_arts_diploma = 0
count_finance_diploma = 0
count_politics_diploma = 0

count_science_masters = 0
count_engineering_masters = 0
count_business_masters = 0
count_medical_masters = 0
count_arts_masters = 0
count_finance_masters = 0
count_politics_masters = 0

count_science_PhD = 0
count_engineering_PhD = 0
count_business_PhD = 0
count_medical_PhD = 0
count_arts_PhD = 0
count_finance_PhD = 0
count_politics_PhD = 0


count_science_undergraduate_reliability = 0
count_engineering_undergraduate_reliability = 0
count_business_undergraduate_reliability = 0
count_medical_undergraduate_reliability = 0
count_arts_undergraduate_reliability = 0
count_finance_undergraduate_reliability = 0
count_politics_undergraduate_reliability = 0

count_science_diploma_reliability = 0
count_engineering_diploma_reliability = 0
count_business_diploma_reliability = 0
count_medical_diploma_reliability = 0
count_arts_diploma_reliability = 0
count_finance_diploma_reliability = 0
count_politics_diploma_reliability = 0

count_science_masters_reliability = 0
count_engineering_masters_reliability = 0
count_business_masters_reliability = 0
count_medical_masters_reliability = 0
count_arts_masters_reliability = 0
count_finance_masters_reliability = 0
count_politics_masters_reliability = 0

count_science_PhD_reliability = 0
count_engineering_PhD_reliability = 0
count_business_PhD_reliability = 0
count_medical_PhD_reliability = 0
count_arts_PhD_reliability = 0
count_finance_PhD_reliability = 0
count_politics_PhD_reliability = 0

df = ex.read_excel(r'C:\D\Mithil\Studies\TMU\CPS 412\Assignment 1\ChatGPT.xlsx')
for j in range(len(df['What is your field of study?'])):
    list_field_study.append([df['What is your field of study?'][j]])
for h in range(len(df['Highest level of Education'])):
    list_field_study[h].append(df['Highest level of Education'][h])
for z in range(len(df['How reliable do you think the answers provided by ChatGPT are?'])):
    list_field_study[z].append(df['How reliable do you think the answers provided by ChatGPT are?'][z])
for g in range(len(df['If yes, have you ever used ChatGPT?'])):
    list_field_study[g].append(df['If yes, have you ever used ChatGPT?'][g])
    
for y in range(len(list_field_study)):
    if list_field_study[y][3] == 'Yes':
        if list_field_study[y][0] == 'Science':
            if list_field_study[y][1] == 'Undergraduate':
                count_science_undergraduate +=1
                count_science_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_science_diploma +=1
                count_science_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_science_masters +=1
                count_science_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_science_PhD +=1
                count_science_PhD_reliability += int(list_field_study[y][2])
            
        if list_field_study[y][0] == 'Engineering':
            if list_field_study[y][1] == 'Undergraduate':
                count_engineering_undergraduate +=1
                count_engineering_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_engineering_diploma +=1
                count_engineering_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_engineering_masters +=1
                count_engineering_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_engineering_PhD +=1
                count_engineering_PhD_reliability += int(list_field_study[y][2])
                
        if list_field_study[y][0] == 'Medical':
            if list_field_study[y][1] == 'Undergraduate':
                count_medical_undergraduate +=1
                count_medical_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_medical_diploma +=1
                count_medical_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_medical_masters +=1
                count_medical_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_medical_PhD +=1
                count_medical_PhD_reliability += int(list_field_study[y][2])
    
        if list_field_study[y][0] == 'Arts':
            if list_field_study[y][1] == 'Undergraduate':
                count_arts_undergraduate +=1
                count_arts_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_arts_diploma +=1
                count_arts_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_arts_masters +=1
                count_arts_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_arts_PhD +=1
                count_arts_PhD_reliability += int(list_field_study[y][2])
                
        if list_field_study[y][0] == 'Business':
            if list_field_study[y][1] == 'Undergraduate':
                count_business_undergraduate +=1
                count_business_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_business_diploma +=1
                count_business_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_business_masters +=1
                count_business_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_business_PhD +=1
                count_business_PhD_reliability += int(list_field_study[y][2])
        
        if list_field_study[y][0] == 'Finance':
            if list_field_study[y][1] == 'Undergraduate':
                count_finance_undergraduate +=1
                count_finance_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_finance_diploma +=1
                count_finance_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_finance_masters +=1
                count_finance_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_finance_PhD +=1
                count_finance_PhD_reliability += int(list_field_study[y][2])
                
        if list_field_study[y][0] == 'politics':
            if list_field_study[y][1] == 'Undergraduate':
                count_politics_undergraduate +=1
                count_politics_undergraduate_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Diploma':
                count_politics_diploma +=1
                count_politics_diploma_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Masters':
                count_politics_masters +=1
                count_politics_masters_reliability += int(list_field_study[y][2])
            if list_field_study[y][1] == 'Ph.D':
                count_politics_PhD +=1
                count_politics_PhD_reliability += int(list_field_study[y][2])

count_science_undergraduate = zero_or_one(count_science_undergraduate)
count_engineering_undergraduate = zero_or_one(count_engineering_undergraduate)
count_business_undergraduate = zero_or_one(count_business_undergraduate)
count_medical_undergraduate = zero_or_one(count_medical_undergraduate)
count_arts_undergraduate = zero_or_one(count_arts_undergraduate)
count_finance_undergraduate = zero_or_one(count_finance_undergraduate)
count_politics_undergraduate = zero_or_one(count_politics_undergraduate)

count_science_diploma = zero_or_one(count_science_diploma)
count_engineering_diploma = zero_or_one(count_engineering_diploma)
count_business_diploma = zero_or_one(count_business_diploma)
count_medical_diploma = zero_or_one(count_medical_diploma)
count_arts_diploma = zero_or_one(count_arts_diploma)
count_finance_diploma = zero_or_one(count_finance_diploma)
count_politics_diploma = zero_or_one(count_politics_diploma)

count_science_masters = zero_or_one(count_science_masters)
count_engineering_masters = zero_or_one(count_engineering_masters)
count_business_masters = zero_or_one(count_business_masters)
count_medical_masters = zero_or_one(count_medical_masters)
count_arts_masters = zero_or_one(count_arts_masters)
count_finance_masters = zero_or_one(count_finance_masters)
count_politics_masters = zero_or_one(count_politics_masters)

count_science_PhD = zero_or_one(count_science_PhD)
count_engineering_PhD = zero_or_one(count_engineering_PhD)
count_business_PhD = zero_or_one(count_business_PhD)
count_medical_PhD = zero_or_one(count_medical_PhD)
count_arts_PhD = zero_or_one(count_arts_PhD)
count_finance_PhD = zero_or_one(count_finance_PhD)
count_politics_PhD = zero_or_one(count_politics_PhD)


average_engineering_undergraduate_reliabilty = (count_engineering_undergraduate_reliability/count_engineering_undergraduate)
average_science_undergraduate_reliabilty = (count_science_undergraduate_reliability/count_science_undergraduate)
average_business_undergraduate_reliabilty = (count_business_undergraduate_reliability/count_business_undergraduate)
average_medical_undergraduate_reliabilty = (count_medical_undergraduate_reliability/count_medical_undergraduate)
average_arts_undergraduate_reliabilty = (count_arts_undergraduate_reliability/count_arts_undergraduate)
average_finance_undergraduate_reliabilty = (count_finance_undergraduate_reliability/count_finance_undergraduate)
average_politics_undergraduate_reliabilty = (count_politics_undergraduate_reliability/count_politics_undergraduate)

average_engineering_diploma_reliabilty = (count_engineering_diploma_reliability/count_engineering_diploma)
average_business_diploma_reliabilty = (count_business_diploma_reliability/count_business_diploma)
average_science_diploma_reliabilty = (count_science_diploma_reliability/count_science_diploma)
average_medical_diploma_reliabilty = (count_medical_diploma_reliability/count_medical_diploma)
average_arts_diploma_reliabilty = (count_arts_diploma_reliability/count_arts_diploma)
average_finance_diploma_reliabilty = (count_finance_diploma_reliability/count_finance_diploma)
average_politics_diploma_reliabilty = (count_politics_diploma_reliability/count_politics_diploma)

average_engineering_masters_reliabilty = (count_engineering_masters_reliability/count_engineering_masters)
average_business_masters_reliabilty = (count_business_masters_reliability/count_business_masters)
average_science_masters_reliabilty = (count_science_masters_reliability/count_science_masters)
average_medical_masters_reliabilty = (count_medical_masters_reliability/count_medical_masters)
average_arts_masters_reliabilty = (count_arts_masters_reliability/count_arts_masters)
average_finance_masters_reliabilty = (count_finance_masters_reliability/count_finance_masters)
average_politics_masters_reliabilty = (count_politics_masters_reliability/count_politics_masters)

average_engineering_PhD_reliabilty = (count_engineering_PhD_reliability/count_engineering_PhD)
average_business_PhD_reliabilty = (count_business_PhD_reliability/count_business_PhD)
average_science_PhD_reliabilty = (count_science_PhD_reliability/count_science_PhD)
average_medical_PhD_reliabilty = (count_medical_PhD_reliability/count_medical_PhD)
average_arts_PhD_reliabilty = (count_arts_PhD_reliability/count_arts_PhD)
average_finance_PhD_reliabilty = (count_finance_PhD_reliability/count_finance_PhD)
average_politics_PhD_reliabilty = (count_politics_PhD_reliability/count_politics_PhD)

science = [average_science_diploma_reliabilty,average_science_undergraduate_reliabilty,average_science_masters_reliabilty,average_science_PhD_reliabilty]
engineering = [average_engineering_diploma_reliabilty,average_engineering_undergraduate_reliabilty,average_engineering_masters_reliabilty,average_engineering_PhD_reliabilty]
arts = [average_arts_diploma_reliabilty,average_arts_undergraduate_reliabilty,average_arts_masters_reliabilty,average_arts_PhD_reliabilty]
medical = [average_medical_diploma_reliabilty,average_medical_undergraduate_reliabilty,average_medical_masters_reliabilty,average_medical_PhD_reliabilty]
finance = [average_finance_diploma_reliabilty,average_finance_undergraduate_reliabilty,average_finance_masters_reliabilty,average_finance_PhD_reliabilty]
business = [average_business_diploma_reliabilty,average_business_undergraduate_reliabilty,average_business_masters_reliabilty,average_business_PhD_reliabilty]
politics = [average_politics_diploma_reliabilty,average_politics_undergraduate_reliabilty,average_politics_masters_reliabilty,average_politics_PhD_reliabilty]

index = ['Diploma','Undergraduate','Masters','Ph.D']

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

df2 = ex.DataFrame({'Science':science,'Engineering':engineering,'Arts':arts,'Medical':medical,'Finance':finance,'Business':business,'Politics':politics},index = index)

ax = df2.plot.bar(rot=0, color={"Science": "palegreen", "Engineering": "turquoise", "Arts":"indigo", "Medical": "yellow", "Finance": "pink", "Business": "magenta", "Politics": "orange"})
ax.set_xlabel('Highest Level of Study')
ax.set_ylabel('Average Reliability of ChatGPT Answers')
ax.set_title('Reliability of ChatGPT Answers Across Various Levels of Education',fontweight = 'bold', size = 'xx-large')
plt.show()