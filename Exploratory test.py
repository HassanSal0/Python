'''
1. You have collected data on the age for each of 100 shoppers in your store. Calculate the mean age and the standard deviation for the shoppers. The age is stored as a numpy array.
'''
import numpy as np

average_age = np.mean(age)
spread_age = np.std(age)

print(average_age)
print(spread_age.round(2))







'''
2. Two of the columns in the heart DataFrame have very long names. Rename the columns using the provided dictionary.
'''
import pandas as pd

column_names = {
	'slope_of_peak_exercise_st_segment': 'slope',
	'fasting_blood_sugar_gt_120_mg_per_dl': 'fbs'
}

heart_clean = heart.rename(columns=column_names)
print(heart_clean.head())







'''
3. Add the height column to the df DataFrame shown below.
     species    name  weight
0       lion   Sally     121
1      tiger   Henry     228
2       lion    Tony     177
3      tiger    Lucy     165
'''
height = [70, 100, 80, 85]

df['height']= height

print(df.head())





'''
4. Subset the Pandas DataFrame df to return all rows with a weight greater than 175.
     species   name  weight
0       lion  Sally     121
1      tiger  Henry     228
2       lion   Tony     177
3      tiger   Lucy     165

'''
print(df[df['weight'] > 175])





'''
5. The three columns in the stars DataFrame currently have very cumbersome names (Temperature (K), Luminosity(L/Lo), Radius(R/Ro)). Rename them using the provided list column_names.
'''
import pandas as pd

column_names = [
  'temperature',
  'luminosity',
  'radius'
]

stars.columns = column_names
print(stars.head())




'''
6. Calculate the variance and standard deviation of the array x.
'''
x = np.array([2.2, 0.9, 4.4, 6.7, 2.8, 3.2, 1.1, 3.5])
x_var = np.var(x)
x_stdev = np.std(x)
print('Variance: {:4.2f}'.format(x_var))
print('Std Deviation: {:4.2f}'.format(x_stdev))




'''
7.You work for a second hand car sales company, and they want to know the relationship between the age and the value so that they can estimate the best price to sell their cars at. Create a plot to show the relationship, identifying the miles per gallon (mpg) by changing the size of each point. The valuation data is previewed below.
    age emissions   mpg  value
0    15       low  23.1   3047
1     8       low  10.4  15428
2     4      high  15.4  24973
3    10      high  31.0   4638
4     1       low  30.2  19303

'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.scatterplot(x = "age", y = "value", size = "mpg", data = valuation)

plt.show()





'''
8. You have access to a large DataFrame employee, but your manager has requested an anonymized subset, containing only the employee_id and salary of each employee.

Create a DataFrame private_employee containing only these two columns.

    employee_id   first_name  gender  salary
0          1ex5        Linda  female    3400
1          73fd        Steve    male    5000
2          ei10        Henry    male   12400
3          b45e         Sara  female    7600
'''
private_employee = employee[['employee_id', 'salary']]

print(private_employee)





'''
9. The steam data represents the average temperature (temp) and the average steam usage (usage) of a steam driven turbine per month. Create a scatterplot of usage vs temp.
'''
import matplotlib.pyplot as plt
import seaborn as sns


ax = sns.scatterplot(data=steam,
                    x="temp",
                    y="usage")

plt.show()




'''
10. You are investigating the impact of age on the valuation of cars to better understand prices that should be offered to customers for second hand cars. You want to visualize both the individual distributions as well as the relationship between the two variables on a single graphic.
'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.jointplot(x = 'age', y = 'value', data = valuation)

plt.show()




'''
11.  Calculate the inter-quartile range of the age of 100 customers who have recently bought products from your website.
'''
import pandas as pd
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)

print(Q3 - Q1)




'''
12. Visualize changes in the variable order over time (day) stored in the Pandas DataFrame df.

>>df
    day  order
0     0     10
1     1     11
2     2     14
3     3      7
4     4      5
5     5     16
'''
import matplotlib.pyplot as plt
import seaborn as sns

sns.lineplot(x = 'day', y = 'order', data=df)

plt.xticks(rotation = 45)
plt.show()

'''
13. The food DataFrame contains nutritional information about six menu items from a restaurant. Print the row index of the data.
'''
print(food.index)


'''
14. The chess DataFrame contains information about the top female chess players around the world. Determine how many missing values are in each column of the DataFrame.
'''
print(chess.isna().sum())

'''
15. Human resources want to conduct a review of the performance rating and salary of employees.

Print the summary statistics of these two numeric columns contained in the employee DataFrame shown below.
'''

print(employee.describe())


'''
16. Calculate the inter-quartile Range for the pH numpy array.

'''
from scipy import stats
IQR = stats.iqr(pH)
print(IQR)

'''
17. Select the three rows having the smallest values in the population column.
                population  GDP
Brics           210354000   186818
Russia          146780720   1657290
India           1387297452  2718732
China           1433783686  13368073
South Africa    58558270    368135
'''
print(df.nsmallest(3, 'population'))

'''
18.  Create a swarm plot of value as a function of measurement. Use the color to indicate the species. The data is contained in the iris DataFrame.
'''
import matplotlib.pyplot as plt
import seaborn as sns

ax = sns.swarmplot(x="measurement",
                   y="value",
                   hue="species",
                   data=iris)

plt.show()


'''
19. For each profession with the same sex in the DataFrame df, calculate the mean weight and height.

     profession        sex      name    weight_kg   height_cm
0       teacher     female      Ann          70         175
1        doctor       male    Henry          75         170
2        doctor     female     Tony          60         168
3        doctor     female      Mia          40         150
4       manager     female     Lucy          55         155
'''
import numpy as np

print(df.groupby(['profession', 'sex'])[['weight_kg', 'height_cm']].mean())



'''
20. Calculate the correlation coefficient cc for the luminosity and radius of stars. lum (luminosity) and rad (radius) have been extracted from a DataFrame df, and are available as two separate NumPy arrays.
rad = df['Radius(R/Ro)'].values
lum = df['Luminosity(L/Lo)'].values
'''
import numpy as np

cc = np.corrcoef(lum, rad)[0, 1]
print(round(cc, 3))


'''
21. The employee DataFrame is previewed below, and contains basic information on employees in a company. The start_date of each employee is currently set as the index.

Sort the DataFrame such that employees who have worked at the company the longest are displayed first.

                first_name      gender      salary
start_date
2018-06-05           Henry        male       12400
2018-04-24           Linda      female        3400
2018-06-26            Sara      female        7600
2018-05-15           Steve        male        5000
'''
employee_sorted = employee.sort_index()

print(employee_sorted)
