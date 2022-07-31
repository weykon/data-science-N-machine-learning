
import pandas as pd
import numpy as np

# loc() : location based

# It has methods like scalar label, list of labels, slice object etc

# .iloc() : Interger based

# .ix() : Both integer and location based

df = pd.DataFrame(np.random.randn(4, 3),
                  index=['a', 'b', 'c', 'd'],
                  columns=['X', 'Y', 'Z'])
print(df.loc['c'] > 0)

df = pd.DataFrame(np.random.randn(8, 4), columns=['X', 'Y', 'Z', 'A'])
# Slicing through list of values
print(df)
print(df.iloc[[1, 2, 3], [1, 3]])

print(df.loc[1:4, :])
# print( df.loc[:, "x":"z"])   py2 fuck


# transform data frame
df = pd.DataFrame({"x":[120, 40, 3, None, None,34],
                   "y":[17, 12, None, 23, None,56],
                   "z":[200, 216, 101, None, 8,78],
                   "a":[114, 31, None, 12, 63,32]})

index_ = ['R1', 'R2', 'R3', 'R4', 'R5','R6']
df.index = index_
res = df.transform(func = ['log', 'exp'])

print(res)