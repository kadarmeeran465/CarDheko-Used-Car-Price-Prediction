# 🚗 Car Dekho - Used Car Price Prediction 

## Project Overview 📚
This project focuses on developing an interactive, predictive tool for determining the price of used cars based on various factors. Leveraging machine learning and the data from Car Dekho, we aim to create a robust model for accurate price prediction, deployed as a Streamlit application. This tool is designed to streamline the car pricing process for both customers and sales representatives, enhancing the car-buying and selling experience.

<div align="center">

[![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/stable/)
[![](https://img.shields.io/badge/Matplotlib-239120?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/ca2d143e-fa40-4d52-b9db-094739b77274" alt="image" style="width:60%; max-width:800px;">
</div>

---

## Skills and Techniques 🚀
- **Data Cleaning and Preprocessing**
- **Exploratory Data Analysis (EDA)**
- **Machine Learning Model Development**
- **Price Prediction Techniques**
- **Model Evaluation and Optimization**
- **Model Deployment with Streamlit**
- **Documentation and Reporting**

---

## Problem Statement 📝
**Objective:** Build an intuitive and accurate predictive tool that estimates the prices of used cars based on various features (e.g., make, model, year, fuel type, transmission type, and city). This tool is deployed as an interactive web application on Streamlit, enabling both customers and sales representatives to seamlessly predict car prices in real time.

**Project Scope:** Car Dheko’s historical dataset provides essential car features from different cities. The task is to process this data, build a machine learning model for price prediction, and deploy the model as a Streamlit web app.

---

## Business Use Cases 💼
![cardekho1](https://github.com/user-attachments/assets/8dfde5d5-f25b-40dd-82ef-9084577e189d)

- **Enhanced Customer Experience**: Offers customers easy access to realistic price estimates.
- **Sales Optimization**: Helps sales representatives set competitive prices based on accurate data.
- **Operational Efficiency**: Enables streamlined pricing processes, minimizing manual assessments.
- **Informed Decision-Making**: Provides insights for strategic planning based on predictive analysis.

---

## Approach 🔍
1. **Data Processing**:
   - **Concatenation**: Import and merge datasets from various cities into a unified format.
   - **Missing Value Treatment**: Handle missing values with imputation or by creating new categories.
   - **Data Standardization**: Ensure consistent formatting (e.g., converting "70 kms" to numerical).
   - **Categorical Encoding**: Apply One-Hot or Label Encoding for categorical variables.
   - **Feature Scaling**: Normalize numerical features as required.
   - **Outlier Removal**: Remove or cap outliers to maintain data quality.

2. **Exploratory Data Analysis (EDA)**:
   - **Descriptive Statistics**: Summarize key statistics for each variable.
   - **Data Visualization**: Use plots (scatter, box, histogram, etc.) to uncover trends.
   - **Feature Selection**: Identify influential features impacting price prediction.

   <img width="363" alt="image" src="https://github.com/user-attachments/assets/f6175ed8-b5ab-45a5-80df-5e9422f002d3">
   <img width="194" alt="image" src="https://github.com/user-attachments/assets/bb5a0e30-4d16-4a7b-96b9-e86509dcbaef">
   <img width="194" alt="image" src="https://github.com/user-attachments/assets/1d60230d-3fab-4682-a1cc-c27fb23f95b7">
   <img width="195" alt="image" src="https://github.com/user-attachments/assets/347df341-7c36-403b-8228-4cdb93d66add">
   <img width="193" alt="image" src="https://github.com/user-attachments/assets/eb570173-03f7-43a4-9e39-f3eb994d20b9">
   <img width="192" alt="image" src="https://github.com/user-attachments/assets/ddb6121d-dc28-4f53-877a-9e1957243c70">
   <img width="193" alt="image" src="https://github.com/user-attachments/assets/1c472080-2c57-439d-9ead-310a2986a9d7">
   <img width="291" alt="image" src="https://github.com/user-attachments/assets/78b43866-e627-4918-92ba-58135b20191b">
   <img width="206" alt="image" src="https://github.com/user-attachments/assets/701a7864-1936-47bc-bfb7-57132a6e1885">
   <img width="296" alt="image" src="https://github.com/user-attachments/assets/504a6f52-9310-429a-850c-98062af200f2">
   <img width="295" alt="image" src="https://github.com/user-attachments/assets/857f6a5b-d5e1-4ae0-874e-bb7ca2a65830">
   <img width="292" alt="image" src="https://github.com/user-attachments/assets/bf299f45-4104-4967-ab65-1cd77b2daf47">

   #### Skewness Visualization 📊
   To understand the distribution of car prices, we visualized the skewness before and after handling outliers:

   **Before Handling Outliers:**
   <img width="440" alt="image" src="https://github.com/user-attachments/assets/f1e8fb80-f894-4c29-b410-11b3f821b728">

   **After Handling Outliers:**
   <img width="443" alt="image" src="https://github.com/user-attachments/assets/94a93a4e-7049-424f-8288-f160aeff0df7">

   
4. **Model Development**:
   - **Train-Test Split**: Separate data into training and testing sets.
   - **Model Selection**: Choose suitable algorithms like Linear Regression, Random Forest, or Gradient Boosting.
   - **Hyperparameter Tuning**: Optimize model parameters for best performance.

5. **Model Evaluation**:
   - Use evaluation metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to assess model accuracy.

6. **Optimization**:
   - **Feature Engineering**: Create or refine features for enhanced prediction accuracy.
   - **Regularization**: Apply Lasso or Ridge to prevent model overfitting.

7. **Deployment**:
   - **Streamlit Application**: Build and deploy an interactive web app with user input options for real-time predictions.
   - **User Interface Design**: Ensure an intuitive, easy-to-navigate app layout.

---

## Project Evaluation Metrics 📏
- **Model Performance**: MAE, MSE, R-squared.
- **Data Quality**: Completeness and consistency of preprocessed data.
- **Application Usability**: User feedback and satisfaction from using the Streamlit app.
- **Documentation**: Clarity and comprehensiveness of project documentation.

---

## Data Set 📂
- **Sources**: Multiple Excel files from Car Dekho for different cities.
- **Features**: Includes car specifications like make, model, mileage, engine type, year, city, etc.
- **Preprocessing Steps**: Handled missing values, standardized formats, encoded categorical variables, and normalized numerical data.

---

## Project Deliverables 📝
- **Source Code**:
  - **Data Preprocessing Script**: For cleaning and structuring the data.
  - **EDA & Visualization**: In-depth exploration of data patterns.
  - **Model Training & Tuning Scripts**: Model training, evaluation, and hyperparameter tuning.
  - **Prediction Script**: Generates predictions for new car data.
  - **Streamlit Application**: Deployed interactive web application for price prediction.

---

## Streamlit Application 🌐
### Features
- **User Input Options**: Accepts details like make, model, fuel type, year, and city.
- **Instant Price Prediction**: Outputs a predicted price based on the input data.
- **Interactive Visualizations**: Displays historical pricing data, feature impacts, and more.

![cardekho](https://github.com/user-attachments/assets/d7e57a2c-12cc-440b-abba-f22562110be6)

---

## Video Demonstration 🎥
Watch how the Streamlit app works in this demonstration:

[![Streamlit App Demo](https://github.com/user-attachments/assets/d7e57a2c-12cc-440b-abba-f22562110be6)](https://www.dropbox.com/scl/fi/t1itw563cpeorb3rwbnna/CarDekho.mp4?rlkey=7a79kvvfkw57rjgqgkv6ms951&st=ay9shm5m&dl=1)

---

## Getting Started 💻
### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/car-dheko-price-prediction.git
   cd car-dheko-price-prediction
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
## 📬 Contact
If you have any questions or feedback, feel free to reach out!

[![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kadar-meeran465)
[![Gmail](https://img.shields.io/badge/gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:kadarmeeran465@gmail.com)

## Contributing 🤝
### Contributions are welcome! Feel free to open issues or submit pull requests.
