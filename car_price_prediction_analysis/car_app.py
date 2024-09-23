import pandas as pd
import streamlit as st
from joblib import load

rf_model = load('RFmodel.joblib')
car_df = pd.read_csv('csv_files_car_dheko/CarData_Cleaned_UsedCarPricePrediction.csv')

# Prediction function
def predict(data):
    data = pd.DataFrame(data, index=[0])
    prediction = rf_model.predict(data)
    return round(prediction[0], 2)  # Return price with two decimal places

# Displaying car details after prediction
def display_car_details(data, car_details):
    data_df = pd.DataFrame(data, index=[0])
    data_df['modelyear'] = data_df['modelyear'].astype(int)
    data_df['mileage'] = round(car_details.get('mileage', 0), 1)
    data_df['comfort_count'] = car_details.get('comfort_count', 0)
    data_df['top_features_count'] = car_details.get('top_features_count', 0)
    data_df['safety_count'] = car_details.get('safety_count', 0)
    data_df['displacement'] = car_details.get('displacement', 0)
    data_df['seats'] = car_details.get('seats', 0)

    st.write("Car Details:")
    st.dataframe(data_df.style.format({'modelyear': '{:d}', 'mileage': '{:.1f}'}, na_rep='0'))

st.image('cardekho.jpeg', width= 500)
st.sidebar.image('cardekho1.jpeg', width= 150)
st.sidebar.header("Input Car Specifications:")

body_type = st.sidebar.selectbox("Select body type:",options=car_df['body_type'].unique())
available_fuel_types = car_df[car_df['body_type'] == body_type]['fuel_type'].unique()
fuel_type = st.sidebar.selectbox("Select fuel type:",options=available_fuel_types)
available_brands = car_df[(car_df['body_type'] == body_type) & (car_df['fuel_type'] == fuel_type)]['brand'].unique()
brand = st.sidebar.selectbox("Select the brand:",options=available_brands)
filtered_models = car_df[(car_df['brand'] == brand) & (car_df['body_type'] == body_type) & (car_df['fuel_type'] == fuel_type)]['model'].unique()
model = st.sidebar.selectbox("Select the model:",options=filtered_models)
available_transmissions = car_df[(car_df['model'] == model)]['transmission'].unique()
transmission = st.sidebar.selectbox("Select transmission type:",options=available_transmissions)
km_driven = st.sidebar.number_input("Enter kilometers driven:",step=5000,min_value=0,format="%d")

owner_number = st.sidebar.selectbox("Enter number of previous owners:",options=[1, 2, 3, 4, 5])

model_year = st.sidebar.number_input("Enter the model year:",step=1,min_value=1900,max_value=2024,format="%d")

insurance_validity = st.sidebar.selectbox("Select insurance validity:",options=car_df['insurance_validity'].unique())

color = st.sidebar.selectbox("Select the car color:",options=car_df[car_df['model'] == model]['color'].unique())

city = st.sidebar.selectbox("Select the city:",options=car_df['city'].unique())

car_details = car_df[car_df['model'] == model].iloc[0].to_dict()

input_data = {
    'body_type': body_type,
    'km': km_driven,
    'transmission': transmission,
    'ownerno': owner_number,
    'brand': brand,
    'model': model,
    'modelyear': model_year,
    'insurance_validity': insurance_validity,
    'fuel_type': fuel_type,
    'color': color,
    'city': city,
    'comfort_count': car_details.get('comfort_count', 0),
    'top_features_count': car_details.get('top_features_count', 0),
    'safety_count': car_details.get('safety_count', 0),
    'displacement': car_details.get('displacement', 0),
    'mileage': car_details.get('mileage', 0),
    'seats': car_details.get('seats', 0)
}

st.header('Car Price Prediction')

if st.sidebar.button("Predict Price", type='primary'):
    result = predict(input_data)
    st.success(f"The predicted price of the car is {result} Lakhs")
    display_car_details(input_data, car_details)

# Additional Information
st.sidebar.header("Additional Information")
st.sidebar.markdown("""
- **Objective:** To predict the price of used cars based on various specifications.
- **Features:**
    - Dynamic filtering of options based on user input.
    - Predicts car prices using a trained Random Forest model.
    - Displays relevant car details after prediction.
""")