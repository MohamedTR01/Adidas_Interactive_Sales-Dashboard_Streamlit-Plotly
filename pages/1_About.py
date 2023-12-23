import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
import qrcode
from io import BytesIO
import warnings


warnings.filterwarnings('ignore')

path_file = os.getcwd() + './Adidas.png'
logo = Image.open(path_file)
st.set_page_config(
    page_title='Adidas | About',
    page_icon=logo,
    layout='wide'
)
st.markdown("""
<h1>▶<b> About Dataset :</b></h1>
<i><h6>Adidas Sales in United States</h6></i>
""",unsafe_allow_html=True)

st.markdown("""
<div>
    <p>An Adidas sales dataset is a collection of data that includes information on the sales of Adidas products. This type of dataset may include details such as the number of units sold, the total sales revenue, the location of the sales, the type of product sold, and any other relevant information.

Adidas sales data can be useful for a variety of purposes, such as analyzing sales trends, identifying successful products or marketing campaigns, and developing strategies for future sales. It can also be used to compare Adidas sales to those of competitors, or to analyze the effectiveness of different marketing or sales channels.

There are a variety of sources that could potentially provide an Adidas sales dataset, including Adidas itself, market research firms, government agencies, or other organizations that track sales data. The specific data points included in an Adidas sales dataset may vary depending on the source and the purpose for which it is being used.</p>
</div>
""",unsafe_allow_html=True)

st.markdown("""

<h1><b>▶ Data Processing :</b></h1>

""",unsafe_allow_html=True)

st.write('We transformed and modified our data in Excel. Here are the results we obtained :')

st.subheader('Before :')

st.markdown("""

<center><img src='https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Adidas%20logo/Before.png' width="1000" height="700"/></center>

""",unsafe_allow_html=True)


st.subheader('After :')

st.markdown("""

<center><img src='https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Adidas%20logo/After.png' width="1000" height="700"/></center>

""",unsafe_allow_html=True)