import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree # dynamic tool to print out our tree structure

#let's build a classic dataset: Will customer buy item online?
#feature: Age, Is_Premium_member(1=yes, 0=No)
#target: Bought_Item (1=Yes,0=No)
market_data = {
    "age": [18, 45, 22, 54, 63, 25, 31, 49, 55, 20],
    "Is_premium_Member": [0, 1, 0, 1, 0, 1, 1, 0, 1,0 ],
    "Bought_Item": [0, 1, 0, 1, 1, 0, 1, 0, 1, 0,]
}
df = pd.DataFrame(market_data)

x = df[["age", "Is_premium_Member"]]
y = df["Bought_Item"]

#Train /test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)
#we set max_depth = 3 so the flow chat doesn't grow infinitely large
clf_tree = DecisionTreeClassifier(max_depth = 3, random_state = 42)
clf_tree.fit(x_train, y_train)

print ('### DECISION TREE COMPLETE ###')

#Test-based representation of how the algorithm splits the data
tree_rules = tree.export_text(clf_tree, feature_names=list(x.columns))
print("\n___ Under the Hood: The Algorithm's Logical Rules ____")
print(tree_rules)