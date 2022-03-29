'''
What is Seaborn?
- Python data visualization library
- Easily create the most common types of plots



Data Analytics
- Gather Data
- Transform and Clean
- Explore
- Analyze and Build Models
- Communicate Results

Advantages of Seaborn
- Easy to use
- works well with pandas data structures


'''


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp, y=phones)

# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()



# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()



#Using pandas with Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('masculinity.csv')
df.head()

sns.countplot( x = 'how_masculine' , data = df )
ply.show()


# Import Matplotlib, pandas, and Seaborn
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot( x ='Spiders', data = df)

# Display the plot
plt.show()
