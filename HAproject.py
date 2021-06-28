#To load the needed libraries:
import numpy as np
from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import requests
from io import StringIO
import plotly.graph_objs as go
import chart_studio.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
plotly.offline.init_notebook_mode(connected=True)
from PIL import Image
from typing import List, Optional
import spacy
from spacy import displacy
import streamlit.components.v1 as components

#To load the datasets:
orig_url1='https://drive.google.com/file/d/1hFAZ9po4NxaaGkNyLzF5SGbN6cswzopt/view?usp=sharing'
file_id1 = orig_url1.split('/')[-2]
dwn_url1='https://drive.google.com/uc?export=download&id=' + file_id1
url1 = requests.get(dwn_url1).text
csv_raw1 = StringIO(url1)
ages_data = pd.read_csv(csv_raw1)

orig_url2='https://drive.google.com/file/d/1uLne-d4jrJKPyUrlpKULSmLc4HPWeeMS/view?usp=sharing'
file_id2 = orig_url2.split('/')[-2]
dwn_url2='https://drive.google.com/uc?export=download&id=' + file_id2
url2 = requests.get(dwn_url2).text
csv_raw2 = StringIO(url2)
new_ages_data = pd.read_csv(csv_raw2)


orig_url3='https://drive.google.com/file/d/17yoGyNQnbS6jxMLmy3XBFOBNjUgCUpYa/view?usp=sharing'
file_id3 = orig_url3.split('/')[-2]
dwn_url3='https://drive.google.com/uc?export=download&id=' + file_id3
url3 = requests.get(dwn_url3).text
csv_raw3 = StringIO(url3)
new_deaths_data = pd.read_csv(csv_raw3)


#To setup the page layout:
st.set_page_config(page_title="MSBA 385 Project", 
                   page_icon=":virus:")

st.title('Healthcare Analytics Web App')
st.markdown("by Riwa Al Hakeem | June 2021")
st.sidebar.title("Navigator")
pressed= st.sidebar.radio("Navigate", ["🏠 Home" ,"🌎 Data Exploration: Worldwide","🏴 Data Exploration: Countries","💉 Healthcare Indices","🎯 90-90-90 Treatment Target"])

     
st.write("")
#___________________________________________________________________________________________________________________________________________
if "🏠 Home" in pressed:
    st.markdown(f"<h1 style='text-align:center; font-family:arial;' >{'<b>About</b>'} </h1>", unsafe_allow_html=True)
    components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    url4 = 'https://drive.google.com/file/d/1SYEh6A8T0EPUmot3Ah58zOn4qIDF_giA/view?usp=sharing'
    image4 = 'https://drive.google.com/uc?export=download&id='+url4.split('/')[-2]
    st.image(image4, use_column_width=None,clamp=True)
    st.markdown(f"<h2 style='text-align:left; font-family:arial;' >{'<b>Welcome! </b>'} </h2>", unsafe_allow_html=True)
    st.write("This Streamlit Web App is an exploration tool intended to allow users to explore HIV statitics worldwide from UNAIDS database that was collected from 2010 till 2020.")
    st.write("This dashboard answers different healthcare-related question regarding the HIV including its trends and patterns, distribution across gender, age and geographic mapping of HIV cases across countries.")
    st.markdown('#')
    st.write("""
    Dataset Source UNAIDS. (2021, June 15). https://www.unaids.org/en""")
#___________________________________________________________________________________________________________________________________________
#loading the icons needed
url = 'https://drive.google.com/file/d/1CbuqumRB7kXNwisXyg3jJIynKsHUW9uz/view?usp=sharing'
image = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
url1= 'https://drive.google.com/file/d/1T5tfShNp-RuOv_vt1RQxouWZaOx7-Zr3/view?usp=sharing'
image1 = 'https://drive.google.com/uc?export=download&id='+url1.split('/')[-2]
url2= "https://drive.google.com/file/d/1VSdBQ-Oa79_X-LSIgtyM9o4ICauooIZi/view?usp=sharing"
image2 = 'https://drive.google.com/uc?export=download&id='+url2.split('/')[-2]
url3= "https://drive.google.com/file/d/1vFj2ALmqsoPBm4N6kLR8xa6CxQ-y0jd_/view?usp=sharing"
image3 = 'https://drive.google.com/uc?export=download&id='+url3.split('/')[-2]

#To load the dataset:
orig_urls='https://drive.google.com/file/d/1DgQ8ovQbVflrgXxNfwGeRMtBV5BSkmYd/view?usp=sharing'
file_ids = orig_urls.split('/')[-2]
dwn_urls='https://drive.google.com/uc?export=download&id=' + file_ids
urls = requests.get(dwn_urls).text
csv_raws = StringIO(urls)
new_data = pd.read_csv(csv_raws)


st.write("")
if "🌎 Data Exploration: Worldwide" in pressed:
    my_page = st.sidebar.radio('Filter by', ['Gender', 'Age'])
    st.markdown(f"<h1 style='text-align:center; color: offblack;' >HIV by Numbers in 2020 </h1>", unsafe_allow_html=True)
    components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    cases_number= new_data.iloc[0]['HIV cases']
    new_cases=new_data.iloc[0]['New HIV cases']
    death_cases=new_data.iloc[0]['HIV-related Deaths']
    treatment_percent=new_data.iloc[0]['Treatment']
    female_number=new_data.iloc[0]['Female Adults']
    male_number=new_data.iloc[0]['Male Adults']
    female_newcases=new_data.iloc[0]['New Female cases']
    male_newcases=new_data.iloc[0]['New Male cases']
    female_death_cases=new_data.iloc[0]['Female Deaths']
    male_death_cases=new_data.iloc[0]['Male Deaths']
    children_number=ages_data.iloc[0]['Children 0-14']
    Adsocelent_number=ages_data.iloc[0]['Adsocelent 10-19']
    youngadults_number=ages_data.iloc[0]['Young Adults 15-24']
    adults_number=ages_data.iloc[0]['Adults 15-49']
    oldadults_number=ages_data.iloc[0]['Adults 50+']
    new_children_number=new_ages_data.iloc[0]['Children 0-14']
    new_Adsocelent_number=new_ages_data.iloc[0]['Adsocelent 10-19']
    new_youngadults_number=new_ages_data.iloc[0]['Adults 15-24']
    new_adults_number=new_ages_data.iloc[0]['Adults 15-49']
    new_oldadults_number=new_ages_data.iloc[0]['Adults 50+']
    death_children_number=new_deaths_data.iloc[0]['Children 0-14']
    death_Adsocelent_number=new_deaths_data.iloc[0]['Adsocelent 10-19']
    death_youngadults_number=new_deaths_data.iloc[0]['Adults 15-24']
    death_adults_number=new_deaths_data.iloc[0]['Adults 15-49']
    

    if my_page == 'Gender':
        col1, col2= st.beta_columns(2)
        selected_status= st.sidebar.selectbox('Filter by gender:', options=['Both genders','Females', 'Males'])
        with col1:
            st.image(image, use_column_width=None,clamp=True)
            if 'Both genders' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{cases_number} </h3>", unsafe_allow_html=True)
                st.write("People living with HIV in 2020")
            if 'Females' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{female_number}</h3>", unsafe_allow_html=True)
                st.write("Females living with HIV in 2020")
            if 'Males' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{male_number} </h3>", unsafe_allow_html=True)
                st.write("Males living with HIV in 2020") 
                
        with col2:
            st.image(image1, use_column_width=None,clamp=True)
            if 'Both genders' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_cases}</h3>", unsafe_allow_html=True)
                st.write("People newly infected with HIV in 2020")
            if 'Females' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{female_newcases} </h3>", unsafe_allow_html=True)
                st.write("Females newly infected with HIV in 2020")
            if 'Males' in selected_status:
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{male_newcases} </h3>", unsafe_allow_html=True)
                st.write("Males newly infected with HIV in 2020")
            
        st.write("")
        col3, col4= st.beta_columns(2)
        with col3:
                st.image(image2, use_column_width=None,clamp=True)
                if 'Both genders' in selected_status:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_cases} </h3>", unsafe_allow_html=True)
                    st.write("People died of HIV-related causes in 2020")
                if 'Females' in selected_status:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{female_death_cases} </h3>", unsafe_allow_html=True)
                    st.write("Females died of HIV-related causes in 2020")
                if 'Males' in selected_status:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{male_death_cases} </h3>", unsafe_allow_html=True)
                    st.write("Males died of HIV-related causes in 2020")
        with col4:
                st.image(image3, use_column_width=None,clamp=True)
                st.markdown(f"<h3 style='text-align:left; color: offblack;' >{treatment_percent} </h3>", unsafe_allow_html=True)
                st.write("% of people living with HIV received antiretroviral therapy (ART) in 2020")

                      
    if my_page == 'Age': 
            select =st.sidebar.selectbox('Filter by Age:',options=['All ages','Children 0-14','Adolescent 10-19','Young Adults 15-24', 'Adults 15-49','Adults 50+'])
            with col1:
                st.image(image, use_column_width=None,clamp=True)
                if 'All ages' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{cases_number}</h3>", unsafe_allow_html=True)
                    st.write("People living with HIV in 2020")
                if 'Children 0-14' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{children_number} </h3>", unsafe_allow_html=True)
                    st.write("Children 0-14 living with HIV in 2020")
                if 'Adolescent 10-19' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{Adsocelent_number} </h3>", unsafe_allow_html=True)
                    st.write("'Adolescent 10-19 living with HIV in 2020")
                if 'Young Adults 15-24' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{youngadults_number} </h3>", unsafe_allow_html=True)
                    st.write("Young Adults 15-24 living with HIV in 2020")
                if 'Adults 15-49' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{adults_number} </h3>", unsafe_allow_html=True)
                    st.write("Adults 15-49 living with HIV in 2020")
                if 'Adults 50+' in select:
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{oldadults_number} </h3>", unsafe_allow_html=True)
                    st.write("Adults 50+ living with HIV in 2020")   

            with col2:
                    st.image(image1, use_column_width=None,clamp=True)
                    if 'All ages' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{cases_number} </h3>", unsafe_allow_html=True)
                        st.write("People newly infected with HIV in 2020")
                    if 'Children 0-14' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_children_number} </h3>", unsafe_allow_html=True)
                        st.write("Children 0-14 newly infected with HIV in 2020")
                    if 'Adolescent 10-19' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_Adsocelent_number} </h3>", unsafe_allow_html=True)
                        st.write("'Adolescent 10-19 newly infected with HIV in 2020")
                    if 'Young Adults 15-24' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_youngadults_number} </h3>", unsafe_allow_html=True)
                        st.write("Young Adults 15-24 newly infected with HIV in 2020")
                    if 'Adults 15-49' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_adults_number} </h3>", unsafe_allow_html=True)
                        st.write("Adults 15-49 newly infected with HIV in 2020")
                    if 'Adults 50+' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{new_oldadults_number} </h3>", unsafe_allow_html=True)
                        st.write("Adults 50+ newly infected with HIV in 2020") 

            with col3:
                    st.image(image2, use_column_width=None,clamp=True) 
                    if 'All ages' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_cases} </h3>", unsafe_allow_html=True)
                        st.write("People died of HIV-related causes in 2020")
                    if 'Children 0-14' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_children_number} </h3>", unsafe_allow_html=True)
                        st.write("Children 0-14 died of HIV-related causes in 2020")
                    if 'Adolescent 10-19' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_Adsocelent_number} </h3>", unsafe_allow_html=True)
                        st.write("'Adolescent 10-19 died of HIV-related causes in 2020")
                    if 'Young Adults 15-24' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_youngadults_number} </h3>", unsafe_allow_html=True)
                        st.write("Young Adults 15-24 died of HIV-related causes in 2020")
                    if 'Adults 15-49' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_adults_number} </h3>", unsafe_allow_html=True)
                        st.write("Adults 15-49 died of HIV-related causes in 2020")
                    if 'Adults 50+' in select:
                        st.markdown(f"<h3 style='text-align:left; color: offblack;' >{death_oldadults_number} </h3>", unsafe_allow_html=True)
                        st.write("Adults 50+ died of HIV-related causes in 2020")   

            with col4:
                    st.image(image3, use_column_width=None,clamp=True)
                    st.markdown(f"<h3 style='text-align:left; color: offblack;' >{treatment_percent} </h3>", unsafe_allow_html=True)
                    st.write("% of people living with HIV received antiretroviral therapy (ART) in 2020")
            components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
#___________________________________________________________________________________________________________________________________________ 
orig_url14='https://drive.google.com/file/d/1K4SaNANI144JuNnzcfMqchrhq9M8ZoIs/view?usp=sharing'
file_id14 = orig_url14.split('/')[-2]
dwn_url14='https://drive.google.com/uc?export=download&id=' + file_id14
url14 = requests.get(dwn_url14).text
csv_raw14 = StringIO(url14)
df = pd.read_csv(csv_raw14)

orig_url15='https://drive.google.com/file/d/1K4SaNANI144JuNnzcfMqchrhq9M8ZoIs/view?usp=sharing'
file_id15 = orig_url15.split('/')[-2]
dwn_url15='https://drive.google.com/uc?export=download&id=' + file_id15
url15 = requests.get(dwn_url15).text
csv_raw15 = StringIO(url15)
df1 = pd.read_csv(csv_raw15)

orig_url16='https://drive.google.com/file/d/1K4SaNANI144JuNnzcfMqchrhq9M8ZoIs/view?usp=sharing'
file_id16 = orig_url16.split('/')[-2]
dwn_url16='https://drive.google.com/uc?export=download&id=' + file_id16
url16 = requests.get(dwn_url16).text
csv_raw16 = StringIO(url16)
df2 = pd.read_csv(csv_raw16)

orig_url17='https://drive.google.com/file/d/1K4SaNANI144JuNnzcfMqchrhq9M8ZoIs/view?usp=sharing'
file_id17 = orig_url17.split('/')[-2]
dwn_url17='https://drive.google.com/uc?export=download&id=' + file_id17
url17 = requests.get(dwn_url17).text
csv_raw17 = StringIO(url17)
data = pd.read_csv(csv_raw17)


if "🏴 Data Exploration: Countries" in pressed:
    st.markdown(f"<h1 style='text-align:center; color: offblack;' >HIV by Numbers in 2020 </h1>", unsafe_allow_html=True)
    components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    if st.button( "🔍 Show Data"):
        st.subheader('Raw data')
        st.write(df)

    choice = ['Cases 2020','New Cases 2020', 'Total Deaths 2020']
    choice_selected = st.selectbox("Select Choice", choice)
    if "Total Deaths 2020" in choice_selected:
        df2 = df2.groupby(by=['Country'], as_index=False)['Total Deaths 2020'].sum()
        layout2 = dict(geo=dict(showframe=False, projection={'type': 'natural earth'}),width=900,
        height=500)
        data2 = go.Choropleth(locations=df2['Country'], locationmode='country names', z=df2['Total Deaths 2020'], colorscale='matter',colorbar={'title': 'HIV-related deaths'})
        fig2 = go.Figure(data=data2, layout=layout2)
        st.plotly_chart(fig2)

    if "Cases 2020" in choice_selected:
        df1 = df1.groupby(by=['Country'], as_index=False)['Cases 2020'].sum()
        layout1 = dict(geo=dict(showframe=False, projection={'type': 'natural earth'}),width=900,
        height=500)
        data1 = go.Choropleth(locations=df1['Country'], locationmode='country names', z=df1['Cases 2020'], colorscale='matter',colorbar=             {'title': 'Cases of HIV'})
        fig1 = go.Figure(data=data1, layout=layout1)
        st.plotly_chart(fig1)

    if "New Cases 2020" in choice_selected:
        df = df.groupby(by=['Country'], as_index=False)['New Cases 2020'].sum()
        layout = dict(geo=dict(showframe=False, projection={'type': 'natural earth'}),width=900,
        height=500)
        data = go.Choropleth(locations=df['Country'], locationmode='country names', z=df['New Cases 2020'], colorscale='matter',                     colorbar={'title': 'New Cases of HIV'})
        fig = go.Figure(data=data, layout=layout)
        st.plotly_chart(fig)

#-------------------------------------------------------------------------------------------------------------------------------------------
orig_urlk='https://drive.google.com/file/d/1bQzEcD-8oJq0ddTFVSpqd2P2ajSpJr42/view?usp=sharing'
file_idk = orig_urlk.split('/')[-2]
dwn_urlk='https://drive.google.com/uc?export=download&id=' + file_idk
urlk= requests.get(dwn_urlk).text
csv_rawk= StringIO(urlk)
inc_data = pd.read_csv(csv_rawk)

 
orig_urlp='https://drive.google.com/file/d/1kPecOXWIQPHnpRT-eeEAT39Cj7D_Be5A/view?usp=sharing'
file_idp = orig_urlp.split('/')[-2]
dwn_urlp='https://drive.google.com/uc?export=download&id=' + file_idp
urlp= requests.get(dwn_urlp).text
csv_rawp= StringIO(urlp)
pre_data = pd.read_csv(csv_rawp)

    
orig_urlm='https://drive.google.com/file/d/1r1sW8UPpN3R039BNlN_N_8eO3FEob-2Y/view?usp=sharing'
file_idm = orig_urlm.split('/')[-2]
dwn_urlm='https://drive.google.com/uc?export=download&id=' + file_idm
urlm= requests.get(dwn_urlm).text
csv_rawm= StringIO(urlm)
mor_data = pd.read_csv(csv_rawm)

if "💉 Healthcare Indices" in pressed:  
    st.markdown(f"<h1 style='text-align:center; font-family:arial;' >{'<b>Healthcare Indices</b>'} </h1>", unsafe_allow_html=True)
    components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    selected_age= st.selectbox('Filter by age group:', options=['Adults 15+','Young People 15-24', 'Adults 15-49'])
    col1, col2,col3 = st.beta_columns(3)
    with col1:
        if 'Adults 15+' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' > 0.6% in 2020 </h2>", unsafe_allow_html=True)
        if 'Young People 15-24' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' > 0.3% in 2020 </h2>", unsafe_allow_html=True)
        if 'Adults 15-49' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' >0.7% in 2020 </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Prevalence</b>'} </h3>", unsafe_allow_html=True)
        components.html("""<hr style="height:3px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)


    with col2:
        st.markdown(f"<h2 style='text-align:center; color: offblack;' > 0.09 in 2020 </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Mortality</b>'} </h3>", unsafe_allow_html=True)
        components.html("""<hr style="height:3px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)

    with col3:
        if 'Adults 15+' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' > 0.27 in 2020 </h2>", unsafe_allow_html=True)
        if 'Young People 15-24' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' > 0.39 in 2020 </h2>", unsafe_allow_html=True)
        if 'Adults 15-49' in selected_age:
                    st.markdown(f"<h2 style='text-align:center; color: offblack;' >0.37  in 2020 </h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center; font-family:arial;' >{'<b>Incidence</b>'} </h3>", unsafe_allow_html=True)
        components.html("""<hr style="height:3px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    
    if st.button( "📈 Show Trend lines"):
        st.subheader('HIV Trend from 2010-2020')
        selected_ratio= st.selectbox('Filter by index:', options=['Incidence','Prevalence', 'Mortality'])

        if "Incidence" in selected_ratio:
            fig = px.line(inc_data, x="Year", y="Ratio",color='Age Groups')
            fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            st.plotly_chart(fig)
        if "Prevalence" in selected_ratio:
            figp= px.line(pre_data, x="Year", y="Ratio",color='Age Groups')
            figp.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
             })
            st.plotly_chart(figp)
        if "Mortality" in selected_ratio:
            figm = px.line(mor_data, x="Year", y="Ratio",color="Age Groups")
            figm.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
            st.plotly_chart(figm)




#___________________________________________________________________________________________________________________________________________

orig_url8='https://drive.google.com/file/d/1ngdgiYMlbqPbf9Q4BQN3y3NnRju7xi8R/view?usp=sharing'
file_id8 = orig_url8.split('/')[-2]
dwn_url8='https://drive.google.com/uc?export=download&id=' + file_id8
url8 = requests.get(dwn_url8).text
csv_raw8 = StringIO(url8)
treat_data = pd.read_csv(csv_raw8)


orig_url9='https://drive.google.com/file/d/1THAy6m6_pnnG4g26H-wAc3caZKSQ3Zd2/view?usp=sharing'
file_id9 = orig_url9.split('/')[-2]
dwn_url9='https://drive.google.com/uc?export=download&id=' + file_id9
url9 = requests.get(dwn_url9).text
csv_raw9 = StringIO(url9)
treat_data1= pd.read_csv(csv_raw9)

orig_url7='https://drive.google.com/file/d/1oFEKzeF_xBLQ6cW_5FqmNgT9axmrCw5W/view?usp=sharing'
file_id7 = orig_url7.split('/')[-2]
dwn_url7='https://drive.google.com/uc?export=download&id=' + file_id7
url7 = requests.get(dwn_url7).text
csv_raw7 = StringIO(url7)
treat_data2 = pd.read_csv(csv_raw7)


if "🎯 90-90-90 Treatment Target" in pressed:
    st.sidebar.info("""
    
                    To drive progress to end the chapter of the AIDS epidemic, a new target of HIV treatment was set:
                   -  By 2020, 90% of all people living with HIV should know their HIV status.
                   -  By 2020, 90% of all people with diagnosed HIV infection should receive sustained antiretroviral therapy.
                   -  By 2020, 90% of all people receiving antiretroviral therapy should have viral suppression.
                    """)
    st.markdown(f"<h1 style='text-align:center; font-family:arial;' >{'<b>Progress Towards 90-90-90 Target</b>'} </h1>",                         unsafe_allow_html=True)
    components.html("""<hr style="height:5px;border:none;color:#ec1c24;background-color:#ec1c24;" /> """,height=45)
    selected_group= st.selectbox('Select:', options=['All Ages', 'Female Adults (15+)','Male Adults (15+)'],)
     
    if 'Female Adults (15+)' in selected_group:
        st.subheader("90-90-90 Target in Female Adults")
        fig = px.bar(treat_data, x=treat_data['Selected Regions'], y= treat_data['For The Year 2020'],width=500, height=500)
        fig.update_traces(marker_color='#F90000')
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig)

    if 'Male Adults (15+)' in selected_group:
        st.subheader("90-90-90 Target in Male Adults")
        fig = px.bar(treat_data1, x=treat_data1['Selected Regions'], y= treat_data1['For The Year 2020'],width=500, height=500)
        fig.update_traces(marker_color='#F90000')
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig)

    if 'All Ages' in selected_group:
        st.subheader("90-90-90 Target in All Ages")
        fig = px.bar(treat_data2, x=treat_data2['Selected Regions'], y= treat_data2['For The Year 2020'],width=500, height=500)
        fig.update_traces(marker_color='#F90000')
        fig.update_layout({
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            })
        st.plotly_chart(fig)
        if st.button( "⚠️ Show Target Gap"):
            st.subheader('90-90-90 Target Gap in Regions')
            selected_gap= st.selectbox('Filter by region:', options=['Asia and Pacific','Caribbean', 'Eastern Europe and Central Asia','East and Southern Africa','Latin America','Middle East and North Africa','West and Central Africa','Western & Central Europe and North America','Global'])

            if 'Asia and Pacific' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-75)}% left to reach the target in Asia and Pacific region.</b> </h3>",unsafe_allow_html=True)

            if 'Eastern Europe and Central Asia' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-70)}% left to reach the target in Eastern Europe and Central Asia region.</b></h3>",unsafe_allow_html=True)

            if 'Caribbean' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-77)}% left to reach the target in Caribbean region.</b></h3>",unsafe_allow_html=True)


            if 'East and Southern Africa' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-68)}% left to reach the target in East and Southern Africa region.</b></h3>",unsafe_allow_html=True)

            if 'Latin America' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-77)}% left to reach the target in Latin America region.</b> </h3>",unsafe_allow_html=True)

            if 'Middle East and North Africa' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-52)}% left to reach the target in Middle East and North Africa region.</b></h3>",unsafe_allow_html=True)


            if 'West and Central Africa' in selected_gap:
                 st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-68)}% left to reach the target in West and Central Africa region.</b> </h3>",unsafe_allow_html=True)

            if 'Western & Central Europe and North America' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-88)}% left to reach the target in Western & Central Europe and North America region.</b> </h3>",unsafe_allow_html=True)

            if 'Global' in selected_gap:
                st.markdown(f"<h3 style='text-align:left; font-family:arial;' ><b>There is {(90-81)}% left to reach the target in worldwide.</b></h3>",unsafe_allow_html=True)



#___________________________________________________________________________________________________________________________________________
    
    
        
