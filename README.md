Project Report
Student Performance Predictor Using Machine Learning

1. Introduction
In today’s academic environment, students often struggle to understand how their daily habits impact their performance. Factors such as study time, attendance, and sleep play a crucial role, but their combined effect is not always clear.

This project aims to address this problem by developing a simple machine learning model that predicts student marks based on these key factors. The project demonstrates how basic AI/ML techniques can be applied to solve real-world problems in the education domain.

2. Problem Statement
Students lack a clear understanding of how their study habits and lifestyle choices affect their academic performance. There is a need for a system that can analyze these factors and provide an estimated prediction of marks.

3. Objectives
To build a machine learning model that predicts student marks
To analyze the relationship between study hours, attendance, sleep, and performance
To demonstrate the application of supervised learning techniques
To gain practical experience in implementing ML models

4. Methodology
4.1 Data Collection

A small dataset was manually created containing the following features:
Study Hours
Attendance (%)
Sleep Hours
Marks (target variable)

4.2 Data Preprocessing
The dataset was structured using a DataFrame
Input features (X) and output variable (y) were separated
Data was split into training (80%) and testing (20%) sets

4.3 Model Selection
The project uses Linear Regression implemented with scikit-learn.
This algorithm was chosen because:
It is simple and suitable for small datasets
It models the relationship between input variables and output effectively
It is ideal for beginners in machine learning

4.4 Model Training
The model was trained using the training dataset. During this process, it learned the relationship between input features and marks.

4.5 Prediction
User inputs are taken at runtime, and the model predicts the expected marks based on learned patterns.

5. Results and Output
The model successfully predicts student marks based on given inputs.
Example:
Study Hours: 3
Attendance: 94%
Sleep Hours: 5
Predicted Marks: ~68
The model also provides an accuracy score (R² score), indicating how well it fits the data.

6. Key Concepts Used
Supervised Learning
Regression Analysis
Train-Test Split
Model Evaluation (Accuracy Score)

7. Challenges Faced
Creating a meaningful dataset manually
Understanding how to structure input data correctly
Handling warnings related to feature names in prediction
Ensuring proper model training and testing

8. Limitations
Small dataset reduces prediction accuracy
Assumes a linear relationship between variables
Does not consider other factors like IQ, stress, or teaching quality

9. Future Improvements
Use a larger and real-world dataset
Add more features (e.g., study method, screen time)
Build a graphical user interface (GUI)
Deploy as a web application

10. Conclusion
This project demonstrates how machine learning can be used to solve a practical problem in education. By applying Linear Regression, the model successfully predicts student performance based on simple inputs. The project provided valuable hands-on experience in data handling, model building, and prediction.

11. Learning Outcomes
Understanding of basic machine learning workflow
Practical implementation of Linear Regression
Experience with Python libraries like Pandas and scikit-learn
Improved problem-solving and analytical thinking
