import streamlit as st
import joblib
import pandas as pd

# Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Health Assessment"])

# Home Page
if app_mode == "Home":
    st.header("Remote Health Monitoring System")
    image_path = r"D:\target\ml\Health_monitoring_systems\doctor-interacts-with-virtual-interface-holding-icon-symbolizing-health-alongside-electro_1005794-11069.jpg"
    st.image(image_path, use_column_width=True)
    
    st.markdown("""
    Welcome to the Remote Health Monitoring System! ❤️‍🩹🧑‍⚕️💊🩺

    Our goal is to assist in diagnosing health conditions based on various health metrics. Using our SVM model, simply input your health data to receive a preliminary analysis, which may help in identifying underlying health issues.

    ### How It Works
    1. **Input Data:** Head to the **Health Assessment** page and fill in your health information through the provided fields.
    2. **Analysis:** Our SVM-based system processes the data to predict the likelihood of various health conditions.
    3. **Results:** Obtain personalized health insights and potential recommendations.

    ### Why Choose Our System?
    - **Accuracy:** Built using SVM models, this system ensures reliable predictions.
    - **User-Friendly Interface:** Just select your symptoms from dropdowns and enter basic health details.
    - **Quick and Efficient:** Receive insights within seconds, enabling prompt decision-making.
                
    ### Input Fields
    - **Dehydration:** Yes/No dropdown
    - **Medicine Overdose:** Yes/No dropdown
    - **Acidious:** Yes/No dropdown
    - **Cold:** Yes/No dropdown
    - **Cough:** Yes/No dropdown
    - **Temperature:** Numerical input
    - **Heart Rate:** Numerical input
    - **Pulse:** Numerical input
    - **BPSYS:** Systolic Blood Pressure (Numerical)
    - **BPDIA:** Diastolic Blood Pressure (Numerical)
    - **Respiratory Rate:** Numerical input
    - **Oxygen Saturation:** Numerical input (percentage)
    - **PH Level:** pH level of blood (Numerical)

    ### Getting Started
    Simply visit the **Health Assessment** section on the sidebar, fill in the details, and see your health report instantly.

    ### About Us
    Learn more about this project and the team behind it on the **About** page.
    """)

# About Page
elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About Dataset
    The dataset for the Remote Health Monitoring System contains health indicators that can be used to predict potential health conditions. The dataset has 20 columns and 4,286 entries, capturing various symptoms and measurements.

    This data includes both categorical fields (such as dehydration and cold symptoms) and numerical fields (such as temperature, heart rate, and blood pressure). 

    #### Data Cleaning and Preprocessing
    - **Duplicate Columns:** During preprocessing, we removed duplicate columns such as `Dehydration.1`, `Medicine Overdose.1`, `Acidious.1`, `Cold.1`, and `Cough.1`, as these duplicated the information found in `Dehydration`, `Medicine Overdose`, `Acidious`, `Cold`, and `Cough`.
    - **Label Encoding:** The column `Causes Respiratory Imbalance` contains text labels (e.g., "Chronic", "Severe", "Mild"), which were converted to numerical values using **LabelEncoder**. This encoding allows the SVM model to process these categorical values effectively, improving prediction accuracy.

    #### Content Summary
    1. **Symptom Indicators:** Boolean values indicating conditions like dehydration, medicine overdose, and respiratory imbalance.
    2. **Health Metrics:** Includes temperature, heart rate, pulse, blood pressure, respiratory rate, oxygen saturation, and pH levels.
    3. **Target Column:** A label indicating the type or severity of the illness, used by the model for classification.

    This cleaned and preprocessed data helps the SVM model make more accurate health predictions based on the provided health metrics.
    """)

# Health Assessment Page
elif app_mode == 'Health Assessment':
    model = joblib.load(r"D:\target\ml\Health_monitoring_systems\trained_remote_health_monitoring_system.joblib")
    st.header("Health Assessment")
    
    # User inputs
    Dehydration = st.selectbox("Do you face Dehydration?", ['Select your option', 'Yes', 'No'])
    Medicine_Overdose = st.selectbox("Have you taken Medicine Overdose?", ['Select your option', 'Yes', 'No'])
    Acidious = st.selectbox("Do you feel Acidious?", ['Select your option', 'Yes', 'No'])
    Cold = st.selectbox("Do you have Cold?", ['Select your option', 'Yes', 'No'])
    Cough = st.selectbox("Do you have Cough?", ['Select your option', 'Yes', 'No'])
    type_selection = st.selectbox("Select Type:", ['Select your option', 0, 1, 2, 3, 4, 5])
    
    Temperature = st.number_input("Enter Temperature (°C)")
    Heart_Rate = st.number_input("Enter Heart Rate (bpm)")
    Pulse = st.number_input("Enter Pulse (bpm)")
    BPSYS = st.number_input("Enter Systolic Blood Pressure (mmHg)")
    BPDIA = st.number_input("Enter Diastolic Blood Pressure (mmHg)")
    Respiratory_Rate = st.number_input("Enter Respiratory Rate (breaths/min)")
    Oxygen_Saturation = st.number_input("Enter Oxygen Saturation (%)")
    PH = st.number_input("Enter PH Level")
    
    # Validate input selections
    if (Dehydration != 'Select your option' and
        Medicine_Overdose != 'Select your option' and
        Acidious != 'Select your option' and
        Cold != 'Select your option' and
        Cough != 'Select your option' and
        type_selection != 'Select your option'):
        
        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'Dehydration': [1 if Dehydration == 'Yes' else 0],
            'Medicine Overdose': [1 if Medicine_Overdose == 'Yes' else 0],
            'Acidious': [1 if Acidious == 'Yes' else 0],
            'Cold': [1 if Cold == 'Yes' else 0],
            'Cough': [1 if Cough == 'Yes' else 0],
            'Type': [type_selection],  # Added Type column here
            'Temperature': [Temperature],
            'Heart Rate': [Heart_Rate],
            'Pulse': [Pulse],
            'BPSYS': [BPSYS],
            'BPDIA': [BPDIA],
            'Respiratory Rate': [Respiratory_Rate],
            'Oxygen Saturation': [Oxygen_Saturation],
            'PH': [PH],
        })
        
        # Debugging: Check the input DataFrame
        st.write("Input Data for Prediction:", input_data)
        
        # Make prediction
        prediction = model.predict(input_data)
      
        
        # Display the prediction based on the classifier's output
        if prediction[0] == 0:
            st.write('Prediction: Normal')
        elif prediction[0] == 1:
            st.write('Prediction: Mild')
        elif prediction[0] == 2:
            st.write('Prediction: Severe')
        elif prediction[0] == 3:
            st.write('Prediction: Chronic')
        else:
            st.write('Prediction: Other condition')  # Assuming you might want to handle other conditions
    
        st.snow()
    else:
        st.write("Please select all options.")
