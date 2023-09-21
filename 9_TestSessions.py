import streamlit as st
import pandas as pd

st.title("Lets Try out Session State & Callback Functions")

if 'number_of_rows' not in st.session_state:
    st.session_state['number_of_rows'] =10
    #st.session_state['type'] = 'Categorical'
    
df = pd.read_csv('C:\Tools\GUI-Apps\Streamlit-OpenAI\MOCK_DATA.csv', sep=';')

increment = st.button('Show MORE Columns')
if increment:
    st.session_state.number_of_rows += 1
    
    decrement = st.button('Show LESS Columns')
if increment:
    st.session_state.number_of_rows -= 1
    
st.table(df.head(st.session_state['number_of_rows']))