import pandas as pd
import numpy as np

s = pd.Series([100, 290, 40, 199, 76])
print(s)
print(type(s))
print("axes", s.axes)
print("size", s.size)
print("ndim", s.ndim)  # definition it is 1 for series objects.
print("values", s.values)
# s  :: axes ->  axis labels
# s  :: dtype -> DataType
# s  :: ndim -> number of dimensions of the underlying data


s1 = pd.Series([1, 2, 4, 5, 6], index=[
               "First", "Zero", "Second", "Third", "Fourth"])
print(s1)

print(s1.sort_index())

# Create Series with Dictionaries
ages = {'Andrew': 31, "Kate": 45, "Matthew": 26, "Helen": 19}
new_ages = pd.Series(ages)
print(new_ages)

# create series using numpy
n_one = np.array([1,2,3,4])
pd.Series(n_one)

# concat
s1 = pd.Series([2,3,55,2,6,44])
s2 = pd.Series([42,32,34,2,1,4,42])
pd.concat([s1,s2])

# rust look like this
l = pd.Series([11,12,13,14,15,16])
l[0:3]

