Student Performance Predictor
1.) Overview

The Student Performance Predictor is a machine learning project that predicts a student’s marks based on study hours, attendance, and sleep duration. It demonstrates the application of supervised learning using Linear Regression.

2.) Objective

To analyze how different student habits affect academic performance and build a model that can estimate marks based on these factors.

3.) Technologies Used
Python
Pandas
scikit-learn
Project Structure
main.py          # Main Python script
README.md        # Project documentation

4.) Setup Instructions:

Step 1: Install Python
Make sure Python (3.x) is installed on your system.

Step 2: Install Required Libraries
Run the following command in terminal:
pip install pandas scikit-learn

Step 3: Run the Project
python main.py

5.) How to Use
Run the program
Enter the following inputs when prompted:
Study Hours
Attendance (%)
Sleep Hours
The model will output the predicted marks
Example :

Input:

Study Hours: 3  
Attendance: 94  
Sleep Hours: 5  

Output:

Predicted Marks: 68.04
Machine Learning Concept
Type: Supervised Learning
Algorithm: Linear Regression

The model learns the relationship between input features and marks, then predicts outcomes for new data.

Limitations
Uses a small dataset (for demonstration purposes)
Assumes a linear relationship between variables
Accuracy can improve with larger datasets
