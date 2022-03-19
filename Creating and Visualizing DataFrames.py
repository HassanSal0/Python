import matplotlib.pyplot as plt

dogs_pack['height_cm'].hist()
plt.show()

dogs_pack['height_cm'].hist(bins=5)
plt.show()

#Bar Plots
avg_weight_by_breed = dogs_pack.groupby('breed')['weight_kg'].mean()
avg_weight_by_breed.plot(kind = 'bar',title = 'avg_weight_by_breed')
plt.show()

#Line plots
sully.plot(x = 'date',y = 'weight_kg', kind = 'line',rot = 45)
#scatter Plots
dogs_pack.plot(x='height_cm', y = 'weight_kg',kind = 'scatter')

#Layering Plots. Aplha is called to make them more transaparent
dogs_pack[dogs_pack['sex'] == 'F']['height_cm'].hist(alpha = .5)
dogs_pack[dogs_pack['sex'] == 'M']['height_cm'].hist(alpha = .5)
#Adding labeling to the two
plt.legend(['F','M'])
plt.show()



# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind = 'bar')

# Show the plot
plt.show()

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(kind = 'line')

# Show the plot
plt.show()

# Scatter plot of avg_price vs. nb_sold with title
avocados.plot(x="nb_sold", y="avg_price", kind="scatter", title="Number of avocados sold vs. average price")

# Show the plot
plt.show()



# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5, bins = 20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5,bins = 20)

# Add a legend
plt.legend(["conventional", "organic"])

# Show the plot
plt.show()





#Missing Values
dogs.isna()
dogs.isna().any()
dogs.isna().sum()
dogs.dropna()

dogs.fillna(0)


# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Check individual values for missing values
print(avocados_2016.isna())

# Check each column for missing values
print(avocados_2016.isna().any())

# Bar plot of missing values by variable
avocados_2016.isna().sum().plot(kind='bar')

# Show plot
plt.show()



# From previous step
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()

# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)

# Create histograms of the filled columns
avocados_filled[cols_with_missing].hist()

# Show the plot
plt.show()






#Creating DataFrames
list_of_dicts = [ {'name':'Ginger','breed':'Daschund','height_cm':22,'weight_kg':10,'date_of_birth':'2019-03-14'},{'name':'Scout','breed':'Dalmatian','height_cm':59,'weight_kg':25,'date_of_birth':'2019-05-09'}]
new_dogs = pd.DataFrame(list_of_dicts)

dict_of_lists = {'name':['Ginger','Scout'], 'breed':['Daschund','Dalmatian'] }
new_dogs = pd.DataFrame(list_of_dicts)



# From previous step
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())

# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()

# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values("bumps_per_10k", ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv("airline_totals_sorted.csv")
