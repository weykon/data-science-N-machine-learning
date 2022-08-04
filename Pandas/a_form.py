#encoding: utf-8

import pandas as pd
import numpy as np

dfc = pd.DataFrame({"Name": ["Josh", "Rachel", "Tim", "Kate", "Zach", "Andrew"], "Age": [
                   11, 13, 16, 12, 14, 18], "工资": [10000, 23000, 18000, 3900000, 19000, 24000]})
print(dfc)

print(dfc.Age)

print(dfc.Age[3])

# assign a value to a specific row
dfc.iloc[2] = ["Ron", 15, 185]
print(dfc)

# assign custom indexes
roll_no = [112890, 39080, 18878, 38788, 9070, 50830]
dfc["Roll Number"] = roll_no

# 根据卷号设置索引
# Setting the Index on the Basis of Roll Number
dfc.set_index("Roll Number", inplace=True)
print(dfc.loc[39080])

# sorting indexes
dfc = pd.DataFrame({"Name": ["Josh", "Rachel", "Tim", "Kate", "Zach", "Andrew"], "Age": [
                   11, 13, 16, 12, 14, 18], "Salary": [10000, 23000, 18000, 3900000, 19000, 24000]}, index=[1, 89, 39, 36, 78, 54])
dfc.sort_index(inplace=True)
print(dfc)

# filtering in DataFrame
employees = pd.DataFrame({"Name": ["Josh", "Mike", "Julia", "Sergio"],
                          "Department": ["IT", "Human Resources", "Finance", "Supply Chain"], "Income": [4800, 5200, 6600, 5700], "Age": [24, 28, 33, 41]})
print(employees)
print(employees["Department"] == "IT")
print(employees.loc[employees["Department"] == "IT", "Name"])  # interest
print(employees[employees["Income"] > 5500])
print(employees[(employees["Age"] > 30) | (employees["Department"] == "HR")]
      )

# a filter use ~(Tilde) sign
print(employees[~(employees["Age"] < 35)])

print(employees.filter(items=["Department", "Name", "Income"]))
print(employees.append({"Name": "Romeo", "Age": 26,
      "Department": "IT", "Income": 5500}, ignore_index=True))

# remove row - "drop"
print(employees.drop(employees[employees["Age"] > 30].index))

