import pandas as pd
import numpy as np
from numpy.ma.core import size
from sklearn.linear_model import LinearRegression

#start with the cleaned dataset from yesterday
data = {
    "size_sqft": [1500, 200, 2180, 2400, 3200],
    "Bedrooms": [3,3,4,3,3],
    "price_usd": [30000, 40000, 45000, 52000, 60000]
}
df = pd.DataFrame(data)

# separate our data into feature (x) and target (y)
#we will use "size_sqft" to predict "price_USD"
x = df[["size_sqft","Bedrooms"]] # features must always be a 2D matrix/DataFrame
y = df["price_usd"] # target is a 1D vector/series

#Initialize the linear Regression Model
model = LinearRegression()

#Train the Model (this finds the optimal slope "m" and intercept "b"
model.fit(x, y)
print(".....MODEL TRAINING COMPLETE....")
print(f"calculated Slope (Weight): {model.coef_[0]:.2f}, Bedroom weight = {model.coef_[1]:.2f}")
print(f"calculated Intercept (Bias): {model.intercept_:.2f}")
print("\n" + "-"*40 + "\n")

# make a prediction on a brand-new house!
unknown_house_size = pd.DataFrame([[1000, 2]], columns=["size_sqft","Bedrooms"]) # A house size the model has never seen
predicted_price = model.predict(unknown_house_size)
print(f"Predicted Price for a 1000 sqft house with 1 bedrooms: ${predicted_price[0]:.2f}")
