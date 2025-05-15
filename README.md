# Flight-Price-Prediction
This project aims to develop a machine learning model capable of accurately predicting flight ticket prices based on various features such as airline, source, destination, departure and arrival times, duration, and number of stops.

### Dataset
The dataset utilized for this project is sourced from Kaggle, containing comprehensive information on flight details and prices. Key features include:
Airline: Name of the airline
Date of Journey: Date of the flight
Source: Departure city
Destination: Arrival city
Route: Flight path
Dep_Time: Departure time
Arrival_Time: Arrival time
Duration: Total duration of the flight
Total_Stops: Number of stops
Additional_Info: Additional information
Price: Ticket price (Target variable)

### Technologies Used
Programming Language: Python 3.8.5

**Libraries:**
Data Manipulation: pandas, numpy
Visualization: matplotlib, seaborn
Machine Learning: scikit-learn, RandomForestRegressor
Web Framework: Streamlit
Model Serialization: pickle

**Tools:**
Jupyter Notebook for exploratory data analysis and model development
Streamlit for deploying the model as a web application

### Project Highlights
**Feature Engineering:** Extracted and transformed features such as journey day and month, departure and arrival hours and minutes, and duration in minutes to enhance model performance.

**Model Selection:**  The Random Forest Regressor yielded the best performance with an R² score of 0.82.

**Hyperparameter Tuning:** Utilized GridSearchCV to fine-tune model parameters for optimal performance.

**Web Application:** Developed a user-friendly web interface using Streamlit, allowing users to input flight details and receive predicted prices in real-time.

### Results
The final model demonstrates strong predictive capabilities, achieving an R² score of 0.82 on the test dataset. This indicates that the model can explain 82% of the variance in flight prices based on the input features.
