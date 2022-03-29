medals = pd.read_csv('medals_by_country_2016.csv',index_col = 0)
fig, ax = plt.subplots()

ax.bar(medals.index,medals['Gold'], label = 'Gold')
ax.bar(medals.index,medals['Silver'], bottom = medals['Gold'], label = 'Silver')
ax.bar(medals.index,medals['Bronze'], bottom = medals['Gold']+medals['Silver'], label = 'Bronze')


ax.set_xticklabels(medals.index,rotation = 90) #Rotating the la
ax.set_ylabel('Number of Medals')


ax.legend()
plt.show()


ax.hist(mens_rowing['Height'],label = 'Rowing',bins = 5)
ax.hist(mens_gymnastics['Height'], label = 'Gymnastics', bins = 5 ,histtype = 'step')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('# of observations')
ax.legend()
plt.show()


fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing['Weight'])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics['Weight'])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel('Weight (kg)')


# Set the y-axis label to "# of observations"
ax.set_ylabel('# of observations')


plt.show()












#Adding error bars to bar charts
fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr=mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics["Height"].mean(), yerr=mens_gymnastics["Height"].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()

#Adding error bars to plots
ax.errorbar(x,y,yerr)


#Adding boxplots
fig, ax = plt.subplots()

ax.boxplot([mens_rowing['Height'],mens_gymnastics['Height']])
ax.set_xticklabels(['Rowing','Gymnastics'])
ax.legend()
plt.show()



#Quantitative comparision: scatter plots
ax.scatter(climate_change['co2'],climate_change['relative_temp'])
ax.set_xlabel('CO2 (ppm)')

fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change["co2"], climate_change["relative_temp"], c=climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()
