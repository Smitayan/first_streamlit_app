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

def get_fruityvice_data(fruit):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  

streamlit.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information")
  else:
    returned_data = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(returned_data)

  #streamlit.write('The user entered ', fruit_choice)
except URLError as e:
  streamlit.error(e)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 

# write your own comment - what does this do?

streamlit.stop()
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_fruit_list = my_cur.fetchall()
streamlit.write("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_fruit_list)

#streamlit.text("What fruit would you like to add?")
fruit_to_add = streamlit.text_input('What fruit would you like to add?')
if fruit_to_add not in my_fruit_list:
  my_cur.execute("insert into fruit_load_list values(fruit_to_add)")

streamlit.write("Thanks for adding ",fruit_to_add)

