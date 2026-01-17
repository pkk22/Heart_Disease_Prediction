# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 20:17:57 2026

@author: Priya Kumari
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 16 20:17:57 2026

@author: Priya Kumari
"""
import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Priya Kumari/Desktop/Machine Learning/trained_model.sav', 'rb'))


# creating a function for Prediction

def heartDisease_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 1):
        return 'The person has heart disease'
    else:
        return 'The person is healthy'
    
    
def main():
    # giving a title
    st.title('Heart Disease Prediction Web App')
    # getting the input data from the user
    #age = st.text_input('Your Age')
    #sex = st.text_input('Sex (1=M, 0=F)')
    #cp = st.text_input('Chest Pain type')
    #trestbps = st.text_input('Resting Blood Pressure')
    #chol = st.text_input('Serum Cholestoral')
    #fbs = st.text_input('Fasting Blood Sugar > 120')
    #restecg = st.text_input('Resting ECG results')
    #thalach = st.text_input('Max Heart Rate achieved')
    #exang = st.text_input('Exercise Induced Angina')
    #oldpeak = st.text_input('ST depression (oldpeak)')
    #slope = st.text_input('Slope of peak exercise ST')
    #ca = st.text_input('Major vessels (0-3)')
    #thal= st.text_input('thal: 0=normal; 1=fixed; 2=reversable')
    
    
    age = st.number_input("Age", min_value=1, max_value=120)

    sex = st.selectbox("Sex", ["Male", "Female"])
    sex = 1 if sex == "Male" else 0

    cp = st.selectbox(
        "Chest Pain Type",
        ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"]
    )
    cp_map = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }
    cp = cp_map[cp]

    trestbps = st.number_input("Resting Blood Pressure (mm Hg)")

    chol = st.number_input("Serum Cholesterol (mg/dl)")

    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["Yes", "No"])
    fbs = 1 if fbs == "Yes" else 0

    restecg = st.selectbox(
        "Resting ECG Results",
        ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"]
    )
    restecg_map = {
        "Normal": 0,
        "ST-T wave abnormality": 1,
        "Left ventricular hypertrophy": 2
    }
    restecg = restecg_map[restecg]

    thalach = st.number_input("Maximum Heart Rate Achieved")

    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    exang = 1 if exang == "Yes" else 0

    oldpeak = st.number_input("ST depression induced by exercise")

    slope = st.selectbox(
        "Slope of Peak Exercise ST Segment",
        ["Upsloping", "Flat", "Downsloping"]
    )
    slope_map = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }
    slope = slope_map[slope]

    ca = st.number_input("Number of Major Vessels (0–3)", min_value=0, max_value=3)

    thal = st.selectbox(
        "Thalassemia",
        ["Normal", "Fixed Defect", "Reversible Defect"]
    )
    thal_map = {
        "Normal": 1,
        "Fixed Defect": 2,
        "Reversible Defect": 3
    }
    thal = thal_map[thal]

    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        diagnosis = heartDisease_prediction([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis) 
    
if __name__== '__main__':
    main()

        
        
        
        
        
        
        
        
        