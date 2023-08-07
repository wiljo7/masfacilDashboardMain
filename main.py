import streamlit as st 
import pandas 
import mysq.connector 



def conexion_():
    connection = st.experimental_connection('mysql', type='sql')
    cursor=''
    return cursor,connection

cur,con=conexion_()