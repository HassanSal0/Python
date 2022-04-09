sns.set_style()
sns.set_palette()



 # Set the style to "whitegrid"
set_style('whitegrid')

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()


# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette('Purples')


# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()


# Change the color palette to "RdBu"
sns.set_style("whitegrid")
sns.set_palette("RdBu")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes",
                  "Often", "Always"]

sns.catplot(x="Parents Advice",
            data=survey_data,
            kind="count",
            order=category_order)

# Show plot
plt.show()


# Change the context to "notebook"
sns.set_context("paper")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "talk"
sns.set_context("notebook")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Change the context to "poster"
sns.set_context("talk")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(["#39A7D0", "#36ADA4"])

# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age",
            data=survey_data, kind="box")

# Show plot
plt.show()



#Creatubg informative visualizations
g = sns.scatterplot(x ='height', y = ' weight', data = data)
type(g)

#Facet Grid contains subplots

g = sns.catplot( x ='Region', y = 'Birthrate', data = gdp_data, kind = 'box')
g.fig.suptitle('New Title', y =1.03)



# Create scatter plot
g = sns.relplot(x="weight",
                y="horsepower",
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"
g.fig.suptitle('Car Weight vs. Horsepower')

# Show plot
plt.show()


#Adding a title to AxesSubplot

g.set_title( 'This is {col_name}') # for various subplots
g.set(xlabel = 'New X Label', y = 'New Y label' ) # for setting axes titls

plt.xticks(rotation = 90)




# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean",
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels
g.set(xlabel = 'Car Model Year', ylabel = 'Average MPG')


# Show plot
plt.show()


# Create point plot
sns.catplot(x="origin",
            y="acceleration",
            data=mpg,
            kind="point",
            join=False,
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation = 90)


# Show plot
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt


plt.show()

#Relational plots - Scatter and line
sns.relplot(x = 'name', y = ' name', data = data , kind ='scatter')

#Categorical plots - Bar, count , box, point
sns.catplot(x = 'col_name', y ='col_name', data = pandas_df, kind = 'bar')











#Exercise

# Set palette to "Blues"
sns.set_palette('Blues')

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data,
                kind="box", hue='Interested in Pets')

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle('Age of Those Interested in Pets vs. Not')

# Show plot
plt.show()


# Set the figure style to "dark"
sns.set_style('dark')

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno",
                data=survey_data, kind="bar",
                col = 'Gender')

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence",
       ylabel="% Who Like Techno")

# Show plot
plt.show()
