Customer Segmentation Using Machine Learning
📌 Project Overview

This project focuses on customer segmentation using Machine Learning and K-Means Clustering.

The main objective is to group customers into different segments based on their purchasing behavior, income, recency, and purchase activity. This can help businesses understand different types of customers and make better data-driven decisions.

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Joblib
Jupyter Notebook
📊 Features Used for Clustering

The K-Means model uses the following customer features:

Income
Recency
Total Spending
Number of Web Purchases
Number of Store Purchases
🤖 Machine Learning Model

The project uses K-Means Clustering, an unsupervised machine learning algorithm.

The customer data is first standardized using StandardScaler, and then customers are grouped into 6 clusters using K-Means.

📁 Project Structure
Customer-Segmentation-ML/
│
├── Analysis Model.ipynb
├── Customer Segmentation.csv
│
└── vid/
    ├── segmentation.py
    ├── Kmeans_model.pkl
    └── scaler.pkl
🚀 Streamlit Application

The project also includes a Streamlit web application where users can enter customer information and predict their customer segment.

The application provides:

Customer input form
Predicted cluster
Customer segment description
📈 Example Output

The application predicts a customer segment such as:

Cluster 4 – High web-purchase and high-spending customers

🎯 Learning Outcomes

Through this project, I practiced:

Data Cleaning
Exploratory Data Analysis (EDA)
Data Visualization
Feature Scaling
K-Means Clustering
Model Saving using Joblib
Building a Streamlit Application
Deploying a Machine Learning project structure on GitHub
👨‍💻 Author

Deepesh Rathore

B.Tech – Computer Science & Engineering (Data Science)
Oriental Institute of Science & Technology, Bhopal
