import streamlit as st
import pandas as pd
import pickle

load_model = pickle.load(open('covid_data.pickle', 'rb'))

st.title('COVID PREDICTION')

st.write('ENTER DATA BELOW: ')

Cough_symptoms = st.selectbox("Cough symptoms?", ["Yes", "No"])
Fever = st.selectbox("Fever?", ["Yes", "No"])
Sore_throat = st.selectbox("Sore throat?", ["Yes", "No"])
Shortness_of_breath = st.selectbox("Shortness of breath?", ["Yes", "No"])
Headache = st.selectbox("Headache?", ["Yes", "No"])
Known_contact = st.radio("Known contact?", ["Contact with confirmed", "Abroad", "Other"])

# Mapping Yes/No to 1/0 and Known_contact options to 1/0/2
symptom_mapping = {"Yes": 1, "No": 0, "Contact with confirmed": 1, "Abroad": 0, "Other": 2}

df = pd.DataFrame({
    'Cough_symptoms': [symptom_mapping[Cough_symptoms]],
    'Fever': [symptom_mapping[Fever]],
    'Sore_throat': [symptom_mapping[Sore_throat]],
    'Shortness_of_breath': [symptom_mapping[Shortness_of_breath]],
    'Headache': [symptom_mapping[Headache]],
    'Known_contact': [symptom_mapping[Known_contact]]
})

if st.button("SUBMIT: "):
    pred = load_model.predict(df)
    st.write("The data is submitted")
    st.write(df)
    st.write("The Predicted Result is = ", pred)
    st.write('Hence, The concluded result is: ')
    if pred == 1:
        st.write("' The person is COVID Positive '")
    else:
        st.write("' The person is COVID Negative '")