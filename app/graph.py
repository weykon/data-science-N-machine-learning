# Age of survey participants
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
#encoding: utf-8
import pandas as pd
print("Loading data from database")
# Read the csv file
df = pd.read_csv('./assets/kaggle_survey_2021_responses.csv')
# print the top 5 rows
df.memory_usage()
df.columns = df.iloc[0]
df = df[1:]
df.columns= [c.replace(' ','_') for c in df.columns]
df.columns = df.columns.str.rstrip()

figure(figsize=(8,6),dpi=100)
age_index=df['What_is_your_age_(#_years)?'].value_counts().index
age_values = df['What_is_your_age_(#_years)?'].value_counts().values
sns.barplot(x=age_index,y=age_values,palette ='Set3',edgecolor='black',linewidth=0.8)
plt.xlabel('Age in years')
plt.ylabel('No of people')
plt.title('Age of people participated in the survey')
plt.xticks(rotation =90)
plt.show()