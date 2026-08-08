import pandas as pd
# introduction to a new tool that automatically splits our data randomly
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# an expanded dataset (10 houses) so we have enough data to split
data = {
    "size_sqft": [ 1500, 2000, 2180, 2400, 3200, 1200, 2800, 1900, 2500, 3100],
    "Bedrooms": [3, 3, 4, 3, 3, 2, 4, 3, 3, 4],
    "price_USD": [ 70000, 40000, 45000,52000, 60000,95000,56000,98000, 51000,59000]
}
df = pd.DataFrame(data)

x = df[["size_sqft","Bedrooms"]]
y = df[["price_USD"]]

# split the data: Hold back 20% of the data for testing
#random_state = 42 is just a seed to ensure the random split is identical every time run it
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# train the model ONLY using the training data pile
model = LinearRegression()
model.fit(x_train, y_train)
print(".....TRAINING COMPLETE ON 80% OF DATA....")

#EXAM TIME: Calculate the accuracy score using the unseen testing pile!
accuracy_score = model.score(x_test, y_test)

print (f"Model Final Exam Score (R-squared): {accuracy_score:.4f}")
print(f"This means our model explains {accuracy_score*100:.1f}% of the price variations!")