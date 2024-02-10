import streamlit as st

temp = True;

st.text("Welcome to my app!")

st.write("Hello World")

temp

numPeople = st.number_input("Number of People", min_value=0)


activities = st.text_input('List Some Activities to Do')



st.write('Currently, ', numPeople, ' people are attending')
