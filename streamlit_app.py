import streamlit as st
import requests

st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write("Choose the Fruits you want in your custom Smoothie!")

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

smoothiefroot_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)

