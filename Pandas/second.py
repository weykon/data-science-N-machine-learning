import pandas as pd
import numpy as np

# Creating a DataFrame
names = {"Names": ["Allen", "Rob", "Harold", "Amy"], "Age": [21, 11, 13, 15]}
# Creating a DataFrame using a Dictionary.
new_dic = pd.DataFrame(names)

print(new_dic["Age"])


# Assign Column name
var = [10, 30, 20, 89, 48, 40]
df = pd.DataFrame(var, columns=["Variables"])
print(df)

# Concept!

arr = np.random.randint(10, size=(5, 2))  # Numpy create DataFrame
print(arr)

new_arr = pd.DataFrame(arr, columns=["Var1", "Var2"])
print(new_arr)
print(new_arr.axes)
print(new_arr.shape)
print(new_arr.ndim)
print(new_arr.size)
print(new_arr.columns)
print(new_arr.index)
print(new_arr.values)
