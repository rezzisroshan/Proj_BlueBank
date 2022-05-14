import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_json('loan_data_json.json')

data.info()

# To filter out all the Purposes
data['purpose'].unique()

# To find out the minimyum and maximum values
data['int.rate'].describe()
data['fico'].describe()
data['dti'].describe()

# Finding exponent of Log annual income to get Annual income
Annual_Income = np.exp(data['log.annual.inc'])

data['Annual.Income']= Annual_Income

# List initialization for segregation based on Fico scores
category = []

# Segregation
for i in range(0,len(data['fico'])):
    if data['fico'][i] <=600:
        category.append("Poor")
    elif data['fico'][i] <=660 and data['fico'][i] > 600:
        category.append("Fair")
    elif data['fico'][i] <=780 and data['fico'][i] > 660:
        category.append("Good")
    elif data['fico'][i] > 780:
        category.append("Excellant")
    else:
        print('Unknown')

data['Fico.Category'] = category

# Method for segregation without For loop
data.loc[data['int.rate'] > 0.12, 'int.rate.type'] = 'High'
data.loc[data['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# Grouping for plot
ficocatgroup = data.groupby(['Fico.Category']).size()       
purposegroup = data.groupby(['purpose']).size()

# Plot
ficocatgroup.plot.bar()
plt.show()

purposegroup.plot.bar()
plt.show()

# For Scatter plot
ypoint= data['Annual.Income']
xpoint= data['dti']
plt.scatter(xpoint, ypoint)
plt.show()

#Export
data.to_csv('Blue_Bank.csv', index = True)
