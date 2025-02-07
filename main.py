import numpy as np
import pandas as pd
import streamlit as st


st.title("Welcome Its Python ")
st.write("Python Requires Practice")

data=pd.DataFrame({
    'c1':[1,2,3,4],
    'c2':['a','b','c','d']})


st.write("Before is the table for data")
st.write(data)


chart_data=pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
#sst.write(chart_data)
st.line_chart(chart_data)
