import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
data={
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 6, 7],
    "attendance":  [50, 60, 65, 70, 75, 80, 85, 90, 55, 68, 82, 88],
    "sleep_hours": [5, 6, 6, 7, 7, 8, 8, 8, 5, 6, 7, 8],
    "marks":       [35, 40, 45, 55, 60, 65, 70, 80, 38, 50, 68, 75]
}
df=pd.DataFrame(data)
X=df[["study_hours", "attendance", "sleep_hours"]]
y=df["marks"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model=LinearRegression()
model.fit(X_train, y_train)
accuracy=model.score(X_test, y_test)
print(f"\nModel Accuracy (R-squared score): {accuracy:.2f}")
print("\nEnter the following details to predict marks for a new student:")
study_hours=float(input("  Enter study hours: "))
attendance=float(input("  Enter attendance (%): "))
sleep_hours=float(input("  Enter sleep hours: "))
input_data=pd.DataFrame(
    [[study_hours, attendance, sleep_hours]],
    columns=["study_hours", "attendance", "sleep_hours"]
)
prediction=model.predict(input_data)
print(f"\nBased on your input, the Predicted Marks are: {prediction[0]:.2f}")