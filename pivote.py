# importing pandas
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana',
                               'Beans', 'Orange', 'Broccoli', 'Banana'],
                   'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit',
                                'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})
df
#Get the Total Sales of Each Product
pivot = df.pivot_table(index=['Product'],
                       values=['Amount'],
                       aggfunc='sum')
print(pivot)
# creating pivot table of total
pivot = df.pivot_table(index=['Category'],
                       values=['Amount'],
                       aggfunc='sum')
print(pivot)
#Get Total Sales by Category and Product Both
pivot = df.pivot_table(index=['Product', 'Category'],
                       values=['Amount'], aggfunc='sum')
print(pivot)
# Get the Mean, Median, Minimum Sale by Category
# 'mean', 'min'} will get median, mean and
# minimum of sales respectively
pivot = df.pivot_table(index=['Category'], values=['Amount'],
                       aggfunc={'median', 'mean', 'min'})
print(pivot)