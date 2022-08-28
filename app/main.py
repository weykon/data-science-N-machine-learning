#encoding: utf-8
import pandas as pd
print("Loading data from database")
# Read the csv file
df = pd.read_csv('./assets/kaggle_survey_2021_responses.csv')
# print the top 5 rows
df.memory_usage()
