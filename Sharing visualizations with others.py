#Preparing your figures to share with others
import matplotlib.pyplot as plt


plt.style.use('ggplot') #Setting the style
fig, ax = plt.subplots()

ax.plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])
ax.plot(austin_weather['MONTH'],austin_weather['MLY-TAVG-NORMAL'])

ax.set_xlabel('Time (months)')
ax.set_ylabel('Average temperature (Fahrenheit degrees)')



plt.show()


plt.style.use('default')



# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()



# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()




#Sharing your visualizations with others
fig.savefig('Gold_medal.png',quality = 60, dpi = 300)

fig.set_size_inches([5,3])

ls #Check what files have been created


#Why automate?
#1 Easy and speed
#2 Flexibility
#3 Robustness
#4 Reproducable




fig, ax = plt.subplots()

#Getting unique values of a column
sports = summer_2016_medals['Sport'].unique()
for sport in sports:
    sport_df = summer_2016_medals[summer_2016_medals['Sport'] == sport ]
    ax.bar(sport,, sport_df['Height'].mean(), yerr = sport_df().std())
ax.set_ylabel('Height (cm)')
ax.set_xticklabels(sports, rotation = 90)
plt.show()



# Extract the "Sport" column
sports_column = summer_2016_medals['Sport']

# Find the unique values of the "Sport" column
sports = summer_2016_medals['Sport'].unique()

# Print out the unique sports values
print(sports)

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals["Sport"] == sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df["Weight"].mean(), yerr=sport_df["Weight"].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig("sports_weights.png")
