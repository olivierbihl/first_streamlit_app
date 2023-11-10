import streamlit
import pandas

streamlit.title('My Parents new Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
