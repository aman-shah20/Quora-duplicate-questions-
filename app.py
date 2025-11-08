import streamlit as st
import helper
import requests, pickle

url = "https://github.com/Abhavya-Singh02/Duplicate-Quora-Question_Pair/blob/main/model.pkl"
model = pickle.loads(requests.get(url).content)

# with gzip.open("model.pkl.gz", "rb") as f:
#     model = pickle.load(f)

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:

        st.header('Not Duplicate')





