# CarDheko - Used Car Price Prediction
A machine learning project aimed at predicting the prices of used cars based on various features such as brand, model, year, mileage, fuel type, and more.
The project involves data preprocessing, feature engineering, model building, and deployment through a Streamlit web application for real-time price predictions.

## Features
- Data Preprocessing: Handling missing values, outliers, encoding categorical variables, and scaling numerical features.
- Model Building: Multiple regression models trained, with Random Forest Regressor chosen as the best-performing model after hyperparameter tuning.
- Streamlit App: Provides real-time price predictions based on user input.
## Technologies Used
- Python
- Streamlit: For application deployment.
- scikit-learn: For machine learning models.
- pandas, numpy: For data manipulation.
- joblib: For saving/loading the model pipeline.
## Model Performance
- Best Model: Random Forest Regressor
- R² Score: 0.996
- Mean Absolute Error: 0.0039 lakhs
## Streamlit Application
A user-friendly interface where users can input car details like body type, brand, model, fuel type, and mileage. The app predicts the car price and displays relevant car details.
