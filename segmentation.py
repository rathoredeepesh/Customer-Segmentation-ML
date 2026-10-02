import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="📊",
    layout="centered"
)

Kmeans = joblib.load(r"C:\Users\ratho\Desktop\Kmeans_model.pkl")
scaler = joblib.load(r"C:\Users\ratho\Desktop\scaler.pkl")

st.title("Customer Segmentation App")
st.write("Enter customer details to predict the segment.")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    income = st.number_input(
        "Income",
        min_value=0,
        max_value=200000,
        value=50000
    )

    total_spending = st.number_input(
        "Total Spending",
        min_value=0,
        max_value=5000,
        value=1000
    )

    num_web_purchase = st.number_input(
        "Number of Web Purchases",
        min_value=0,
        max_value=100,
        value=10
    )

with col2:
    num_store_purchase = st.number_input(
        "Number of Store Purchases",
        min_value=0,
        max_value=100,
        value=10
    )

    num_web_visits = st.number_input(
        "Web Visits per Month",
        min_value=0,
        max_value=50,
        value=3
    )

    recency = st.number_input(
        "Recency (Days Since Last Purchase)",
        min_value=0,
        max_value=365,
        value=30
    )
input_data = pd.DataFrame({

    "Income": [income],

    "Recency": [recency],

    "Total_Spending": [total_spending],

    "NumWebPurchases": [num_web_purchase],

    "NumStorePurchases": [num_store_purchase]

})

input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):

    cluster = Kmeans.predict(input_scaled)[0]

    cluster_descriptions = {
        0: "Low-income, low-spending customers",
        1: "High-income, high-spending active customers",
        2: "High-income, high-spending less-recent customers",
        3: "Low-income, low-spending less-recent customers",
        4: "High web-purchase and high-spending customers",
        5: "Possible high-income outlier with low spending"
    }

    st.success(f"🎯 Predicted Customer Segment: Cluster {cluster}")

    st.info(
        f"📌 Customer Profile: {cluster_descriptions[cluster]}"
    )