import joblib
import numpy as np
import streamlit as st

# Load the saved model and polynomial transformer
poly = joblib.load('polynomial_transformer.pkl')
ridge_model = joblib.load('ridge_model.pkl')

# Define the function to predict the score based on study hours
def predict_score(hours, max_marks):
    # Define the valid range for hours based on your training data
    min_hours = 0.0
    max_hours = 10.0  # Adjust this to the max hours in your dataset

    if hours < min_hours or hours > max_hours:
        return f"Please enter hours between {min_hours} and {max_hours}."

    # Transform the input using the same polynomial transformation used during training
    transformed_data = poly.transform(np.array([[hours]]))  # Reshaping hours input to 2D array
    # Predict the score using the Ridge model
    predicted_score = ridge_model.predict(transformed_data)[0]

    # Ensure the predicted score is a valid number
    if predicted_score is None:
        return "Prediction error. Please try again."


    # Round the score to the nearest integer
    return round(predicted_score)

# Streamlit web interface
def main():
    st.title("Student Performance Prediction")

    # Input for hours studied
    hours = st.number_input("Enter the number of hours studied(for 100 marks):", min_value=0.0, max_value=10.0, step=0.1)


    # Predict the score when the button is pressed
    if st.button("Predict Score"):
        if hours >= 0:  # Check if hours is valid
            predicted_score = predict_score(hours)
            if isinstance(predicted_score, str):  # If there's a message returned instead of a score
                st.write(predicted_score)
            else:
                # Display the rounded predicted score
                st.write(f"Predicted score for {hours} hours of study: {predicted_score} out of 100")
        else:
            st.write("Please enter a valid number of hours studied.")

if __name__ == "__main__":
    main()
