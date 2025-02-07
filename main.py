import numpy as np
import pandas as pd
import streamlit as st

st.title("Welcome to My Interactive Python Page")
st.write("Python Requires Practice, but it's also fun when you make things interactive!")

st.sidebar.header("Interactive Controls")

num_points = st.sidebar.slider("Select the number of points for the chart", 10, 100, 20)

columns = ['A', 'B', 'C']
selected_columns = st.sidebar.multiselect("Select columns to display in the chart", columns, default=columns)

if st.sidebar.button("Regenerate Random Data"):
    st.experimental_rerun()

data = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': ['a', 'b', 'c', 'd']
})
st.write("Below is the table for static data:")
st.write(data)

chart_data = pd.DataFrame(np.random.randn(num_points, 3), columns=['A', 'B', 'C'])

filtered_chart_data = chart_data[selected_columns]

st.write("Below is the table for dynamic chart data:")
st.write(filtered_chart_data)

st.write("Line Chart of Selected Columns:")
st.line_chart(filtered_chart_data)

st.subheader("Interactive Text Input")
user_input = st.text_input("Enter something interesting:")
if user_input:
    st.write(f"You entered: **{user_input}**")

if st.checkbox("Show Raw Data"):
    st.write("Raw Data:")
    st.write(chart_data)

st.subheader("Generate a Random Matrix")
if st.button("Generate Random Matrix"):
    random_matrix = np.random.randint(1, 10, size=(5, 5))  # Generates a 5x5 matrix with random integers
    st.write("Randomly Generated Matrix:")
    st.write(random_matrix)

matrix_size = st.slider("Select the size of the random matrix", 2, 10, 5)
if st.button("Generate Matrix with Custom Size"):
    custom_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    st.write(f"Randomly Generated {matrix_size}x{matrix_size} Matrix:")
    st.write(custom_matrix)