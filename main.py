import streamlit as st 
import pandas 
import mysql.connector 



def conexion_():
    connection = st.experimental_connection('connections.mysql', type='sql')
    cursor=''
    return cursor,connection

cur,con=conexion_()