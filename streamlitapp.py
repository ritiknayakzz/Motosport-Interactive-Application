import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Motosport Data Science App')
st.write('An application for the data science team of Motosport')

df = pd.read_csv('cars.csv')
cols = list(df.columns)
if st.sidebar.checkbox('Show tutorials:'):
	st.title('Primal steps with pandas; Knowledge building')
	if st.sidebar.button('Read and view the data frame:'):
		st.write('type  "df = pd.read_csv("cars.csv")"  to read the data frame')
		st.write('print df to see the full data frame')
		st.write(df)
	if st.sidebar.button('Shape of the data frame'):
		st.write('type "df.shape" to see the shape of the data frame')
		st.write(df.shape)
		st.write('rows and columns')
	if st.sidebar.button('Describe the data'):
		st.write('To describe the data use;  "df.descibe()"  statement')
		st.write('It gives the following outcome')
		st.table(df.describe())
	option = st.sidebar.selectbox(
    	'Choose a column to view the frequency of values in it:',
     	df.columns)
	st.write('Type  "df["name of column"].value_counts()"  to view the frequency of the values in the data frame')
	'You selected:', df[option].value_counts()
#team_members = ['Sejal', 'Sahil', 'Akshit', 'Amrit', 'Eaman', 'Ajay Pal Singh Tuli', 'Ajay Jadeja', 'Tarun', 'Keshava', 'Ishaan', 'Mo hit']
#year = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

#df = pd.DataFrame({'team members':team_members,
#	'year':year})
#st.write(df)

#df = st.table({
 # 'first column': [1, 2, 3, 4],
  #'second column': [10, 20, 30, 40]
#})

#chart_data = pd.DataFrame(
 #    np.random.randn(20, 3),
  #   columns=['a', 'b', 'c'])

#st.line_chart(chart_data)
#st.line_chart(df['(kW)'])






