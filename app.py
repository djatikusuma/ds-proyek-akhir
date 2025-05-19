import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the model
model = joblib.load('model/model.joblib')

# Set page config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main > div {
        padding: 2rem;
        border-radius: 10px;
        background: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 100%;
        margin-top: 20px;
        background-color: #4CAF50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Title and description
st.title('🎓 Student Performance Predictor')
st.markdown('''
This application predicts whether a student will graduate or dropout based on various academic and personal factors.
Please fill in the following information to get a prediction.
''')

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader('Personal Information')
    marital_status = st.selectbox('Marital Status', options=[1, 2], format_func=lambda x: 'Single' if x == 1 else 'Married', index=0)
    age = st.number_input('Age at Enrollment', min_value=17, max_value=70, value=20)
    gender = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male', index=0)
    scholarship = st.selectbox('Scholarship Holder', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', index=1)
    international = st.selectbox('International Student', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', index=0)
    
    st.subheader('Financial Information')
    debtor = st.selectbox('Debtor', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', index=0)
    tuition_up_to_date = st.selectbox('Tuition Fees Up to Date', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes', index=1)

with col2:
    st.subheader('Academic Background')
    admission_grade = st.slider('Admission Grade', min_value=0.0, max_value=200.0, value=150.0)
    prev_qualification = st.selectbox('Previous Qualification', options=[1, 2, 3, 4], format_func=lambda x: f'Type {x}', index=0)
    prev_qualification_grade = st.slider('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=150.0)
    application_mode = st.number_input('Application Mode', min_value=1, max_value=50, value=1)
    course = st.number_input('Course Code', min_value=1, max_value=10000, value=9238)

# Create tabs for semester data
tab1, tab2 = st.tabs(['First Semester', 'Second Semester'])

with tab1:
    st.subheader('First Semester Performance')
    col3, col4 = st.columns(2)
    with col3:
        curricular_units_1st_credited = st.number_input('1st Semester Credited Units', min_value=0, max_value=20, value=6)
        curricular_units_1st_enrolled = st.number_input('1st Semester Enrolled Units', min_value=0, max_value=20, value=6)
        curricular_units_1st_evaluations = st.number_input('1st Semester Evaluations', min_value=0, max_value=20, value=6)
        curricular_units_1st_approved = st.number_input('1st Semester Approved Units', min_value=0, max_value=20, value=6)
        curricular_units_1st_grade = st.slider('1st Semester Grade', min_value=0.0, max_value=20.0, value=13.5)

with tab2:
    st.subheader('Second Semester Performance')
    col5, col6 = st.columns(2)
    with col5:
        curricular_units_2nd_credited = st.number_input('2nd Semester Credited Units', min_value=0, max_value=20, value=6)
        curricular_units_2nd_enrolled = st.number_input('2nd Semester Enrolled Units', min_value=0, max_value=20, value=6)
        curricular_units_2nd_evaluations = st.number_input('2nd Semester Evaluations', min_value=0, max_value=20, value=6)
        curricular_units_2nd_approved = st.number_input('2nd Semester Approved Units', min_value=0, max_value=20, value=6)
        curricular_units_2nd_grade = st.slider('2nd Semester Grade', min_value=0.0, max_value=20.0, value=13.5)

# Economic Indicators in an expander
with st.expander('Economic Indicators'):
    col7, col8, col9 = st.columns(3)
    with col7:
        unemployment_rate = st.slider('Unemployment Rate (%)', min_value=0.0, max_value=20.0, value=10.0)
    with col8:
        inflation_rate = st.slider('Inflation Rate (%)', min_value=-5.0, max_value=5.0, value=1.4)
    with col9:
        gdp = st.slider('GDP Growth Rate (%)', min_value=-5.0, max_value=5.0, value=1.74)

# Prediction button
if st.button('Predict Performance'):
    # Prepare input data with only the features used in training
    input_data = pd.DataFrame({
        'Application_mode': [application_mode],
        'Debtor': [debtor],
        'Tuition_fees_up_to_date': [tuition_up_to_date],
        'Gender': [gender],
        'Scholarship_holder': [scholarship],
        'Age_at_enrollment': [age],
        'Curricular_units_1st_sem_approved': [curricular_units_1st_approved],
        'Curricular_units_1st_sem_grade': [curricular_units_1st_grade],
        'Curricular_units_2nd_sem_approved': [curricular_units_2nd_approved],
        'Curricular_units_2nd_sem_grade': [curricular_units_2nd_grade]
    })
    
    # Ensure column order matches training data
    expected_columns = ['Application_mode', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
                       'Age_at_enrollment', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                       'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']
    input_data = input_data[expected_columns]
    
    # Make prediction
    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]
        
        # Display result with custom styling
        st.markdown('''
        <style>
        .prediction-box {
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
        }
        .graduate {
            background-color: #4CAF50;
            color: white;
        }
        .dropout {
            background-color: #f44336;
            color: white;
        }
        </style>
        ''', unsafe_allow_html=True)
        
        if prediction == 'Graduate':
            st.markdown(f'''
            <div class="prediction-box graduate">
                <h2>Prediction: Graduate</h2>
                <p>Probability: {probability[1]:.2%}</p>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="prediction-box dropout">
                <h2>Prediction: Dropout</h2>
                <p>Probability: {probability[0]:.2%}</p>
            </div>
            ''', unsafe_allow_html=True)
            
        # Additional recommendations
        st.subheader('Recommendations')
        if prediction == 'Graduate':
            st.success("The student shows strong potential for graduation. Continue with current academic strategies.")
        else:
            st.warning("Consider implementing the following interventions:")
            st.markdown("""- Schedule regular meetings with academic advisors
            - Join study groups or seek tutoring
            - Review and adjust study habits
            - Consider reducing course load if necessary""")
            
    except Exception as e:
        st.error(f'Error making prediction: {str(e)}')
        
        # Debug information
        st.expander("Debug Information").write({
            "Model expected features": "Check model.feature_names_ or similar attribute",
            "Input data features": list(input_data.columns)
        })

# Footer
st.markdown('''
---
<div style="text-align: center">
    <p>Created by Rangga Djatikusuma Lukman</p>
</div>
''', unsafe_allow_html=True)