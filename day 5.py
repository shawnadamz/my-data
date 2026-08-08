import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create email future data
# = Urgent Complaint, 0 = Normal Inquiry
email_data = {
    "exclamation_count": [0, 5, 1, 0, 4, 0, 6, 1, 3, 0],
    "caps_word_count": [1, 6, 0, 2, 5, 0, 7, 1, 4, 1],
    "is_urgent": [0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
}
df = pd.DataFrame(email_data)
x = df[["exclamation_count", "caps_word_count"]]
y = df["is_urgent"] # this my categorical target(0 or 1)

# split the data
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Initialize and train the LOGISTIC Regression Model
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

#Test the model`s prediction accuracy
prediction = classifier.predict(X_test)
final_accuracy = accuracy_score(y_test, prediction)

print("___CLASSIFICATION TRAINING COMPLETE___")
print(f"Model Accuracy Score on unseen Emails: {final_accuracy * 100:.1f}%")

# Test a brand new email!
# Imagine an email arrives with 4 exclamation marks and ALL-CAPS words
new_email = pd.DataFrame([[3, 0]], columns = ["exclamation_count", "caps_word_count"])
prediction = classifier.predict(new_email)

if prediction[0] == 1:
    print("\n !!! System Alert: This incoming email is classified as Urgent Complaint!!" )
else:
    print("\n @@ System Note: This incoming email is classified as Normal Inquiry. ")
