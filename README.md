# Obesity Level Prediction Based on Eating Habits and Physical Condition

## Description

This project aims to develop a machine learning model that predicts an individual's obesity level based on their eating habits, physical activity, lifestyle choices, and other relevant factors. The project involves data exploration, model building and evaluation, and deployment of a web application to make the prediction accessible to users.

## Tasks

1. Data Exploration and Preprocessing:

- Loading and understanding the dataset
- Handling missing values
- Encoding categorical variables
- Splitting data into training and testing sets

2. Model Building and Evaluation:

- Experimenting with different machine learning models
- Tuning hyperparameters to optimize performance
- Evaluating model accuracy, precision, recall, F1-score, and AUC-ROC
- Selecting the best-performing model

3. Web Application Development:

- Creating a user-friendly interface with **Streamlit**
- Handling user input
- Making predictions using the trained model
- Displaying prediction results in a clear and informative manner

## Technologies Used

- Python: Primary programming language
- Libraries: pandas, NumPy, matplotlib, seaborn, scikit-learn, pickle, Streamlit, XGBoost
- Jupyter Notebook: Environment for data exploration and model development
- Streamlit: Framework for building the web application

## Project Structure

- main.ipynb: Jupyter Notebook containing data exploration, model building, and evaluation code
- app.py: Python script for the Streamlit web application
- data/data.csv: The dataset used in the project
- final_model.pkl: Saved trained machine learning model

## Instructions to Run the Web Application

- Install required libraries: `pip install pandas numpy matplotlib seaborn scikit-learn xgboost pickle streamlit`
- Run the Streamlit app: `streamlit run app.py`
- Access the app in your web browser (usually at `http://localhost:8501`)
