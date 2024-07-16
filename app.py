#%%
import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv') # lendo os dados
st.header('Vehicles Dashboard', divider='rainbow')
check_button1 = st.checkbox('Criar um gráfico de dispesão') # criando uma caixa de seleção
check_button2 = st.checkbox('Criar um histograma')

if check_button1: #se a opção 1 for selecionada
    #escrever mensagem
    st.write('Criando um gráfico de dispersão')
    fig = px.scatter(car_data, x='price', y='model', labels={'price':'Price','model':'Model'}, title='Price per model')
    
    #exibindo um gráfico interativo
    st.plotly_chart(fig, use_container_width=True)

if check_button2: #se a opção 2 for selecionada
    #escrever mensagem
    st.write('Criando histograma')
    fig = px.histogram(car_data, x='condition', labels={'condition':'Car condition','count':'Frequency'}, title='Frequency of car condition')

    #exibindo um gráfico interativo
    st.plotly_chart(fig, use_container_width=True)

#%%
