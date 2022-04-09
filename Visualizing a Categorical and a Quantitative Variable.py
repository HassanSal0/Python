'''
Categorical plots
- Involve a categorical variable
- Comparisons between groups
- Examples: count plots, bar plots

'''

import seaborn as sns
#Count plot syntax
sns.countplot( x = 'how_masculine', data = masculinity_data)

#To show the same in catplot()
sns.catplot(x = 'how_masculine', data = masculinity_data, kind = 'count', order = ['1','2','3'])
plt.show()

'''
Bar plots
Displays mean of quantitatve variable per category
Automatically shows 95% confidence interval
'''

sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'bar', ci = None)
plt.show()



# List of categories from lowest to highest
category_order = ["<2 hours",
                  "2 to 5 hours",
                  "5 to 10 hours",
                  ">10 hours"]

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order, ci = None)

# Show plot
plt.show()



'''
Box Plot
- Shows the distribution of quantitatve Data
- Box shows the 25th to 75th percentile
- line in middle represent the median
- outliers and skewness is showed in
- Facilitates Comparisons between groups

'''

g = sns.catplot(x ='time', y ='total_bill', kind ='box', data = tips, order = ['Dinner','Lunch'], sym = '', whis = 2 ) #1.5 is the default for IQR whis

g = sns.catplot(x ='time', y ='total_bill', kind ='box', data = tips, order = ['Dinner','Lunch'], sym = '', whis = [5,95] ) #Show the 5th and 95th percentiles

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours",
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(data = student_data, x = 'study_time', y = 'G3', order = study_time_order, kind = 'box')

# Show plot
plt.show()





# Create a box plot with subgroups and omit the outliers
sns.catplot(data = student_data, x ='internet', y = 'G3', kind ='box', sym ='', hue = 'location', ci = None)
# Show plot
plt.show()


# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])

# Show plot
plt.show()



'''
Point plots
points show mean of quantitatve variable


'''


# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2, join = False)

# Show plot
plt.show()



# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None, estimator = median)

# Show plot
plt.show()
