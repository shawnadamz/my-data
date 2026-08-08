import pandas as pd
import numpy as np

#create a messy dataset imitating real-world data
raw_data = {
     "size_sqft": [1500, 2000, np.nan, 2400, 1800, 3200],#np.nan represents the missing values
     "Bedrooms": [3, np.nan, 4, 3, 2, np.nan],
     "prise_USD": [30000, 40000,45000, 52000, np.nan,60000]
 }
# convert this dictionary into a pandas dataFrame (a structured table)
df = pd.DataFrame(raw_data)
print("----ORIGINAL MESSY DATA----")
print(df)
print("\n")

      #FIX THE MISSING SIZES: Fill the missing Size values withe the AVERAGE(mean) size
mean_size = df["size_sqft"].mean()
df["size_sqft"] = df["size_sqft"].fillna(mean_size)

#FIX THE MISSING BEDROOMS: Fill missing bedrooms with the MOST COMMON value (mode)
#Since you cant easily have 3.2 bedrooms, we use the mode.
mode_bedrooms = df["Bedrooms"].mode()[0]
df["Bedrooms"] = df["Bedrooms"].fillna(mode_bedrooms)

#FIX MISSING PRICE: Drope the row entirely if the target price is missing
#(we cant predict prices if we don't know the true answer was!)
df = df.dropna(subset=["prise_USD"])

print("....CLEANED DATA READY FOR ML")
print(df)
print(df.columns.tolist())

