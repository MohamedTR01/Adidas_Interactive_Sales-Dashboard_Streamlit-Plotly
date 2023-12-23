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
    page_title='Adidas | Home',
    page_icon=logo,
    layout='wide'
)
# Data Source :
qr_datasource = qrcode.make("https://www.kaggle.com/datasets/heemalichaudhari/adidas-sales-dataset/data")

col_logos_1,col_logos_2,col_logos_3 = st.columns([1,8,1])
with col_logos_2:
    st.markdown("""
            <style>
                .logos {
                    background-color: white;
                    height: 170px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    border-radius: 0 0 5px 5px;
                }
                
            </style>
            <div class="logos">
              <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/Fsjest.jpg" title="Fsjest" alt="Fsjest" width="150" height="150" />
              <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/Master%20DSEF.png" title="DSEF" alt="DSEF" width="400" height="150"/>
              <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/UAE.png" title="UAE" **alt="UAE" width="150" height="150" /> 
            </div>
    """,unsafe_allow_html=True)

st.markdown("""
            
            <div align="center" >

            # <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Adidas%20logo/Adidas.png" alt="Adidas Logo" width=100/> Adidas Interactive Sales Dashboard<center><h5 class="title-test">2020 and 2021</h5></center>
            

            </div>
            """,unsafe_allow_html=True)

st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container():
    col_img0, col_img1, col_img2 = st.columns([1,8,1])
    with col_img1:
        # st.image('https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Adidas%20logo/Adidas-Transforms-Customer-Insights-with-Salesforce.jpg')
        st.markdown("""
        <center><img src='https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Adidas%20logo/Adidas-Transforms-Customer-Insights-with-Salesforce.jpg' /></center>
        """,unsafe_allow_html=True)
with st.container():
    
    col_team0, col_team1, col_team2, col_team3 = st.columns([1,4,4,1])
    with col_team1:
        st.markdown("""
                <style>
                    .centered-header {
                        text-align: center;
                    }
                </style>
            """, unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Realized by :</h2>', unsafe_allow_html=True)
        team = pd.DataFrame({'Name':['TRIBAK MOHAMMED']})
        fig = ff.create_table(team, height_constant=30, colorscale=[[0, '#02365e'],[.5, '#ffffff'],[1, '#ffffff']])
        fig.update_layout(font=dict(size=20))
        st.plotly_chart(fig, use_container_width=True)  

    # with col_team2:
    #     st.markdown("""
    #             <style>
    #                 .centered-header {
    #                     text-align: center;
    #                 }
    #             </style>
    #         """, unsafe_allow_html=True)
    #     st.markdown('<h2 class="centered-header">Proposed by</h2>', unsafe_allow_html=True)
    #     team = pd.DataFrame({'':[]})
    #     fig = ff.create_table(team, height_constant=30, colorscale=[[0, '#02365e'],[.5, '#b3cce3'],[1, '#b3cce3']])
    #     fig.update_layout(font=dict(size=30))
    #     st.plotly_chart(fig, use_container_width=True)


st.markdown("""---""")
with st.container():
    st.markdown("""
    <h2>Data Source</h2>
    """,unsafe_allow_html=True)
    # Convert PilImage to bytes
    img_bytes_1 = BytesIO()
    qr_datasource.save(img_bytes_1, format='PNG')  # Assuming PNG format, change accordingly
    datasource_col0,datasource_col1,datasource_col2,datasource_col3,datasource_col4 = st.columns(5)
    with datasource_col1:
        # Display the QR code in Streamlit
        st.image(img_bytes_1, caption='Data Source QR Code')




st.markdown("""---""")
st.subheader('Tools')
tool1,tool2,tool3,tool4,tool5,tool6,tool7,tool8,tool9= st.columns(9)
st.markdown("""
        <style>
            .image {
                background-color: transparent;
                border: none;  /* Remove the button border */
                background-color: white;
                width: 100px;
                height: 100px;
                border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .image img {
                position:relative
                padding:5px;
            }
            .image:hover {
                background-color: #999999;
            }
   
        </style>
    """, unsafe_allow_html=True)
with tool1:
        st.markdown("""
                    <div class="image">
                    <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/python/python-original-wordmark.svg" alt="" with=80 height=80>
                    </div>
                    
                    """, unsafe_allow_html=True)
with tool2:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/vscode/vscode-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool3:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/git/git-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool4:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/docker/docker-plain-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool5:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/numpy/numpy-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool6:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/pandas/pandas-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool7:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/github/github-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool8:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/elghallali/my-images/aff6e3ea2f3f31483187856b7c9d412852c9205c/streamlit-logo-primary-colormark-darktext.svg" alt="" with=80 height=60>
                 </div>
                 """, unsafe_allow_html=True)
with tool9:
        st.markdown("""
                 <div class="image">
                 <img src="https://camo.githubusercontent.com/20db5efd6873b071b1c72818028df47ce86c511d7560e789c34ba1811593c3eb/68747470733a2f2f73746f72652d696d616765732e732d6d6963726f736f66742e636f6d2f696d6167652f617070732e33363836382e62666230653265652d626539652d346337332d383037662d6530613762383035623162652e37313261666635642d353830302d343765302d393762652d3538643137616461336662382e61343638343565362d636539342d343463662d383932622d353436333763366663663036" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
        

# st.markdown(
#     f"""
#     <style>
#     table {{
#         transform: scale(1.5); /* Zoom de 1.5 fois la taille normale */
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
