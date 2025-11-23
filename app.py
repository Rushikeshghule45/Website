import streamlit as st
import pandas as pd

st.title("Rhushi MOTORS")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different BIKES")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

with st.container():
 st.subheader("bajaj pulsar NS160")
 st.image("artifacts/images/Bajaj Pulsar NS160.jpg")
 st.subheader("KTM 390 DUKE")
 st.image("artifacts/images/KTM 390 DUKE.webp")
 st.subheader("R15")
 st.image("artifacts/images/R15.jpg")
 st.subheader("Royal Enfield")
 st.image("artifacts/images/Royal Enfield.jpg")


col1, col2, col3, col4 = st.columns([2, 2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.subheader("Bajaj Pulsar NS160")
col1.image("artifacts/images/Bajaj Pulsar NS160.jpg")
col2.subheader("KTM 390 DUKE")
col2.image("artifacts/images/KTM 390 DUKE.webp")
col3.subheader("R15")
col3.image("artifacts/images/R15.jpg")  
col4.subheader("Royal Enfield")
col4.image("artifacts/images/Royal Enfield.jpg") 
st.selectbox("Pick one", ["None","Bajaj pulsar NS160", "KTM 390 DUKE","R15","Royal Enfield"],placeholder="None")

price = st.slider("Enter Your Budget", min_value=50000, max_value=5000000,step=10000,value=100000)
st.write(f"Your Selected Budget is :- {price}")
st.text_input("Enter Your name")
st.text_input("Enter your Contact no")
st.text_input("Enter your Email Id")
st.text_area("Enter your full address",placeholder="thane")
if st.button("Submit"):
    st.switch_page('pages/feedback.py')