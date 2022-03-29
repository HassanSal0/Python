import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])
ax.plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()


# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Call the show function to show the result
plt.show()


# Import the matplotlib.pyplot submodule and name it plt
import matplotlib.pyplot as plt

# Create a Figure and an Axes with plt.subplots
fig, ax = plt.subplots()

# Plot MLY-PRCP-NORMAL from seattle_weather against the MONTH
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'])

# Plot MLY-PRCP-NORMAL from austin_weather against MONTH
ax.plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# Call the show function
plt.show()


#Customizing your plots
#Customizing data appeareance
#Adding markers
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], marker = 'o') #circular markers
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], marker = 'v') #pointy markers

#Setting linestyle
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], marker = 'o',linestyle='--') #dashed line
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], marker = 'o',linestyle='None') #no line line

#Setting Color
ax.plot(seattle_weather["MONTH"], seattle_weather['MLY-PRCP-NORMAL'], marker = 'o',linestyle='--', color = 'r') #Red color line

#Setting the axies labels
ax.set_xlabel('Time (months)')
ax.set_ylabel('Average temperature')

#Setting title
ax.set_title('Weather in Seattle')




#small multiples with plt.subplots()
fig, ax = plt.subplots(3,2, sharey = True)
ax[0,0].plot()



# Create a Figure and an array of subplots with 2 rows and 2 columns
fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation
ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures
ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations
ax[1,0].plot(austin_weather['MONTH'],austin_weather ['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures
ax[1,1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()



# Create a figure and an array of axes: 2 rows, 1 column with shared y axis
fig, ax = plt.subplots(2, 1, sharey=True)

# Plot Seattle precipitation data in the top axes
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'], color = 'b')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-25PCTL'], color = 'b', linestyle = '--')
ax[0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-75PCTL'], color = 'b', linestyle = '--')

# Plot Austin precipitation data in the bottom axes
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'], color = 'r')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-25PCTL'], color = 'r', linestyle = '--')
ax[1].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-75PCTL'], color = 'r', linestyle = '--')

plt.show()
