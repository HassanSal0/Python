fig, ax =plt.subplots()

ax.plot(x, y)
ax.set_xlabel('Time')
ax.set_ylabel('CO2')


sixties = climate_change['1960-01-01':'1969-12-31']


#Exercise

import pandas as pd

climate_change = pd.read_csv('climate_change.csv', parse_dates=['date'],index_col='date')


import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# Add the time-series for "relative_temp" to the plot
climate_change.index
ax.plot(climate_change.index,climate_change['relative_temp'])

# Set the x-axis label
ax.set_xlabel('Time')

# Set the y-axis label
ax.set_ylabel('Relative temperature (Celsius)')

# Show the figure
plt.show()


import matplotlib.pyplot as plt

# Use plt.subplots to create fig and ax
fig, ax = plt.subplots()

# Create variable seventies with data from "1970-01-01" to "1979-12-31"
seventies = climate_change["1970-01-01":"1979-12-31"]

# Add the time-series for "co2" data from seventies to the plot
ax.plot(seventies.index, seventies["co2"])

# Show the figure
plt.show()



#Plotting time-series with different variabls
#Using twin axes

ax2 = ax.twinx()

#Coloring the ticks
ax.tick_params('y', color = 'blue' )




def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color = color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel)
    axes.tick_params('y',colors =color)


fig, ax = plot.subplots()
plot_timeseries = (ax, climate_change.index, climate_change['co2'], 'blue', 'Time', 'CO2')



import matplotlib.pyplot as plt

# Initalize a Figure and Axes
fig, ax = plt.subplots()

# Plot the CO2 variable in blue
ax.plot(climate_change.index, climate_change['co2'], color='blue')

# Create a twin Axes that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature in red
ax2.plot(climate_change.index, climate_change['relative_temp'], color='red')

plt.show()




#Annotations time series data
ax2.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1) xytext = (pd.Timestamp('2008-10-06').-0.2))
#Adding arrows to annotation
ax2.annotate('>1 degree', xy = (pd.Timestamp('2015-10-06'),1) xytext = (pd.Timestamp('2008-10-06').-0.2), arrowprops={'arrowstyle':'->','color':'gray'})


fig, ax = plt.subplots()

# Plot the CO2 levels time-series in blue
plot_timeseries(ax, climate_change.index, climate_change["co2"], 'blue', "Time (years)", "CO2 levels")

# Create an Axes object that shares the x-axis
ax2 = ax.twinx()

# Plot the relative temperature data in red
plot_timeseries(ax2, climate_change.index, climate_change['relative_temp'], 'red', "Time (years)", "Relative temp (Celsius)")

# Annotate the point with relative temperature >1 degree
ax2.annotate(">1 degree", xy=(pd.Timestamp('2015-10-06'), 1), xytext=(pd.Timestamp('2008-10-06'), -0.2), arrowprops={'arrowstyle':'->', 'color':'gray'})

plt.show()
