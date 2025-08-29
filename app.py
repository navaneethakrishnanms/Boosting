import streamlit as st
import pandas as pd
import pickle

with open('xgb_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("California Housing Price Predictor")
st.write("Enter the values of the features to predict the median house value.")


feature_names = [
    'longitude', 'latitude', 'housing_median_age', 'median_income',
    'ocean_proximity_1H OCEAN', 'ocean_proximity_INLAND', 
    'ocean_proximity_ISLAND', 'ocean_proximity_NEAR BAY', 
    'ocean_proximity_NEAR OCEAN', 'rooms_per_household', 
    'bedrooms_per_room', 'population_per_household'
]


user_input = {}
for feature in feature_names:
    if 'ocean_proximity' in feature:
        user_input[feature] = st.radio(f"{feature}", options=[0, 1])
    else:
        user_input[feature] = st.number_input(f"Enter {feature} value:", value=0.0)

input_df = pd.DataFrame([user_input])


if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Median House Value: ${prediction[0]:,.2f}")
