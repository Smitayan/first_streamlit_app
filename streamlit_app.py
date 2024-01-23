import streamlit
import pandas as pd
import requests

file_path='https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt'
fruits_df = pd.read_csv(file_path)
fruits_df = fruits_df.set_index('Fruit')
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu:")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale,Spinach & Rocket smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑 🍞 Avocado Toast")
streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
fruits_selected=streamlit.multiselect("Pick some fruits:",list(fruits_df.index))
fruits_selected_data=fruits_df.loc[fruits_selected]
streamlit.dataframe(fruits_selected_data)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
