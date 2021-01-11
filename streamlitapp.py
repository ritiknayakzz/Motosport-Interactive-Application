import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import pyplot as plt

st.title('Motosport Data Science App')
st.write('An application for the data science team of Motosport')

df = pd.read_csv('cars.csv')
cols = list(df.columns)

if st.sidebar.checkbox('Tutorial 1: Some operations using pandas'):
	
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

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

movies = ["Annie Hall", "Ben-Hur", "Cassablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

mentions = [500, 505]
year = [2013, 2014]

friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error = [x+y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]

st.set_option('deprecation.showPyplotGlobalUse', False)

if st.sidebar.checkbox('Tutorial 2: Introduction to matplotlib:'):
	
	st.title('A brief introduction to data visualization matplotlib')
	
	if st.sidebar.button('Making a simple plot:'):
		st.write('years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]')
		st.write('gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]')
		st.write('Create a line chart - years on x-axis, gdp, on y-axis')
		st.write('plt.plot(years, gdp, color="green", marker="o", linestyle="solid"')
		st.write('plt.title("Nominal GDP")')
		st.write('plt.ylabel("Billions of $")')
		st.write('plt.show()')
		(plt.plot(years, gdp, color="green", marker="o", linestyle="solid"))
		(plt.title("Nominal GDP"))
		(plt.ylabel("Billions of $"))
		#st.write(plt.show())
		st.set_option('deprecation.showPyplotGlobalUse', False)
		st.pyplot()
	
	if st.sidebar.button('Bar Chart:'):

		st.subheader('1. Sample Bar graph')

		st.write('movies = ["Annie Hall", "Ben-Hur", "Cassablanca", "Gandhi", "West Side Story"]')
		st.write('num_oscars = [5, 11, 3, 8, 10]')
		st.write("Bars are by default width 0.8, so we'll add 0.1 to the left coordinates so that each bar is centered")
		st.write('xs = [i + 0.1 for i, _ in enumerate(movies)]')
		st.write('plt.bar(xs, num_oscars)')
		st.write('plt.ylabel("# of academy awards")')
		st.write('plt.title("My favorite movies")')
		st.write('plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)')
		st.write('plt.show()')
		xs = [i + 0.1 for i, _ in enumerate(movies)]
		(plt.bar(xs, num_oscars))
		(plt.ylabel("# of academy awards"))
		(plt.title("My favorite movies"))
		(plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies))
		st.pyplot()

		st.subheader('2. Misleading Bar graph')

		st.write('mentions = [500, 505]')
		st.write('year = [2013, 2014]')
		st.write('plt.bar([2012.6, 2013.6], mentions, 0.8)')
		#st.write('plt.ticklabel_format(useOffset=False)')
		st.write('plt.ylabel("# times I heard someone say data science")')
		st.write('plt.axis([2012.5, 2014.5, 499, 506])')
		st.write('plt.title("Look at the HUGE increase")')
		st.write('plt.xticks(years)')
		st.write('plt.show()')
		(plt.bar([2012.6, 2013.6], mentions, 0.8))
		(plt.ylabel("# times I heard someone say data science"))
		(plt.axis([2012.5, 2014.5, 499, 506]))
		(plt.title("Look at the HUGE increase"))
		(plt.xticks(year))
		#st.write(plt.ticklabel_format(useOffset=False))
		st.pyplot()

		st.subheader('3. Correcting the graph')

		st.write("plt.axis([2012.5, 2014.5, 0, 550])")
		st.write("plt.title('Not so HUGE any more')")
		st.write("plt.show()")
		(plt.bar([2012.6, 2013.6], mentions, 0.8))
		(plt.ylabel("# times I heard someone say data science"))
		(plt.axis([2012.5, 2014.5, 0, 550]))
		(plt.title("Look at the HUGE increase"))
		(plt.xticks(year))
		(plt.title('Not so HUGE any more'))
		st.pyplot()

	if st.sidebar.button('Line Charts:'):
		st.write("variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]", 
			"bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]")
		st.write("total_error = [x+y for x, y in zip(variance, bias_squared)]")
		st.write("plt.plot(xs, variance, 'g-', label='variance')  -  green solid linestyle")
		st.write("plt.plot(xs, bias_squared, 'r-', label='bias^2')  -  red dot-dashed linestyle")
		st.write("plt.plot(xs, total_error, 'b:', label='total error'  -  blue dotted linestyle)")
		st.write("plt.legend(loc=9)")
		st.write("plt.xlabel('model complexity')")
		st.write("plt.title('The Bias-Variance Tradeoff')")
		st.write("plt.show()")
		(plt.plot(xs, variance, 'g-', label='variance'))
		(plt.plot(xs, bias_squared, 'r-', label='bias^2'))
		(plt.plot(xs, total_error, 'b:', label='total error'))
		(plt.legend(loc=9))
		(plt.xlabel('model complexity'))
		(plt.title('The Bias-Variance Tradeoff'))
		(plt.show())
		st.pyplot()

	#if sidebar.button('Scatterplots:'):

	#	st.subheader('1. Sample Scatterplot')

	#	st.write("friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]")
	#	st.write("minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]")
	#	st.write("labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']")







