# student-performance-prediction
Usage
Run the Streamlit App
To start the app, run the following command in your terminal:

bash
Copy code
streamlit run main.py
This will start a Streamlit server, and you can view the app in your browser. The app will prompt you for the number of hours studied and the maximum marks, and it will predict the score based on the provided input.

Input Fields:
Hours Studied: Enter the number of hours a student has studied. The valid range is from 0.0 to 10.0 hours.
Maximum Marks: Enter the maximum marks available for the exam. This can be set between 1 and 1000.
Output:
Once the user inputs the values and presses the "Predict Score" button, the app will display the predicted score along with the maximum marks.

Model Explanation
Polynomial Regression
The model is built using polynomial regression and Ridge regression:

Polynomial Transformation: This transformation is used to capture the non-linear relationship between the number of hours studied and the predicted score.
Ridge Regression: Ridge regression is applied to prevent overfitting by adding a regularization term to the loss function. This helps in making more accurate predictions on unseen data.
The model was trained using a dataset of student hours and scores and is saved as ridge_model.pkl along with the polynomial transformer polynomial_transformer.pkl.

How it works:
The number of hours entered by the user is transformed using the same polynomial transformation used during training.
The transformed data is passed to the trained Ridge regression model to predict the score.
The predicted score is then adjusted according to the maximum marks and displayed to the user.