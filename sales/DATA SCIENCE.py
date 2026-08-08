import pandas as pd
d = { "co1": [1,2,3,4,7],
  "co2": [4,5,6,9,5],
  "co3":[7,8,2,1,3]}
df = pd.DataFrame(data = d)
print(df)

count_R = df.shape[0]
count_C = df.shape[1]
print(count_R)
print(count_C)

A_max = max(df["co1"])
print(A_max)
import numpy as np
A_mean = np.mean(df["co1"])
print(A_mean)

super_sales = pd.read_csv("superstoreSales.csv", index_col = 0)
print(super_sales.head())

super_sales.dropna(axis = 0, how = "any", inplace = True)
print(super_sales)

print(super_sales.shape)
print(super_sales.info())
print(super_sales.describe())

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
print(super_sales.describe())

import matplotlib.pyplot as plt
super_sales.plot(x = "Sales", y = "Profit", kind = "scatter"),
plt.ylim(ymin = 0)
plt.xlim(xmin = 0)
plt.show()