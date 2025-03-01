import streamlit as st
import sklearn as sk
import pandas as pd

import pickle

st.title('Text Classification')

# Load the model
load_model = pickle.load(open('model.pickle', 'rb'))

# input data
news = st.text_area('Enter the news')

# Create a data frame
input_news = pd.DataFrame({
    'news': [news]
})

# Predict the news
if st.button('SUBMIT'):
    pred = load_model.predict(input_news['news'])
    st.success('THe news is submitted')
    st.write('The news category is: ', pred)
    st.balloons()