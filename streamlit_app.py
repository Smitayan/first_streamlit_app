import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_fruit_list = my_cur.fetchall()
streamlit.write("The fruit load list contains:", type(my_fruit_list))
#streamlit.text(my_data_row)
streamlit.dataframe(my_fruit_list)

#streamlit.text("What fruit would you like to add?")
fruit_to_add = streamlit.text_input('What fruit would you like to add?')
streamlit.write("Thanks for adding ",fruit_to_add)

