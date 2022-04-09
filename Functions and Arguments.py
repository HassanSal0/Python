
#Importing libraries.
import matplotlib.pyplot as plt
import pandas as pd


#DataVisualization
fig, ax =plt.subplots()

ax.plot(x, y)
ax.set_xlabel('Time')
ax.set_ylabel('CO2')

plt.show()


#Plotting Time series data
#DateTimeIndex
climate_change.index



# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv', parse_dates=["date"], index_col="date")


#Plotting time-series with different variabls
#Using twin axes

ax2. = ax.twinx()

#Annotation data
ax2.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1) xytext = (pd.Timestamp('2008-10-06').-0.2), arrowprops={'arrowstyle':'->','color':'gray'})


ax.bar(medals.index,medals['Gold'])
