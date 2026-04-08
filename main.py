import langchain_helper as lch
import streamlit as st

st.title("Pet Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Hamster", "Rabbit"))

if animal_type == "Cat":
    pet_color = st.sidebar.text_area(label="What color is your pet?", max_chars=15)
elif animal_type == "Dog":
    pet_color = st.sidebar.text_area(label="What color is your pet?", max_chars=15)
elif animal_type == "Hamster":
    pet_color = st.sidebar.text_area(label="What color is your pet?", max_chars=15)
elif animal_type == "Rabbit":
    pet_color = st.sidebar.text_area(label="What color is your pet?", max_chars=15)
    
if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response["pet_name"])