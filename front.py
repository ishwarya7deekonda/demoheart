import streamlit as st
import pandas as pd
import pickle

# Load the saved model
model = pickle.load(open('heart_model.pkl', 'rb'))

st.title(" Heart Disease Prediction App")
st.write("Enter patient data to predict the likelihood of heart disease.")

# Create input fields in a sidebar or grid
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=40)
    sex = st.selectbox("Sex (1=Male, 0=Female)", [1, 0])
    cp = st.selectbox("Chest Pain Type (0-3)", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", value=120)

with col2:
    chol = st.number_input("Serum Cholestoral in mg/dl", value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [0, 1])
    restecg = st.selectbox("Resting ECG Results (0-2)", [0, 1, 2])
    thalach = st.number_input("Maximum Heart Rate Achieved", value=150)

# Create a dataframe for the input
user_data = pd.DataFrame({
    'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
    'chol': [chol], 'fbs': [fbs], 'restecg': [restecg], 'thalach': [thalach],
    
    # Add other features used during training here...
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(user_data)
    
    if prediction[0] == 1:
        st.error("The model predicts a high risk of heart disease.")
    else:
        st.success("The model predicts a low risk of heart disease.")