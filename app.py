import streamlit as st
import helper
import requests, pickle
from io import BytesIO


url = "https://raw.githubusercontent.com/FriendUsername/RepoName/main/model.pkl"
response = requests.get(url)
model = pickle.load(BytesIO(response.content))
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






