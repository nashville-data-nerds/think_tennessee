import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def color_scheme(name):
    """
    define color scheme for this figure
    """
    color = {'United States': 'green',
             'Tennessee': 'black'}

    return color[name]

df = pd.read_csv('../../raw/epi_labor_force_data_raw.csv')

"""
Going to grab data from the US as well as Tennessee
"""

us = df.loc[(df.geo == 'United States')&(df.categ=='All')]
tenn = df.loc[(df.geo == 'Tennessee')&(df.categ=='All')]

"""
Create a plot of the unemployment rate as a function of time (year).  
This may not be the most elegant solution, but the idea is to build up lists
of year and unemployment rate by looping through each year's columns
"""

sns.set()
sns.set_style("white")
pal = sns.color_palette('YlGn',2)
sns.set_palette(pal)
fig, ax = plt.subplots(figsize=(8,4))
for category, name in zip([us, tenn], ['United States', 'Tennessee']):
    year = list()
    unemployment = list()
    for i in np.arange(1979, 2019, 1):
        year.append(i)
        rate = category['Nunemp{}{}'.format(str(i)[2],str(i)[3])] / category['Nlf{}{}'.format(str(i)[2],str(i)[3])]
        unemployment.append(rate.values*100)
    ax.plot(year, unemployment, label=name)
plt.legend(loc=2,
        prop={'size': 10},
        bbox_to_anchor=(1.05,1),
        borderaxespad=0.0)
plt.ylim((0,14))
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(axis='y', alpha=0.3)

plt.savefig('unemployment.pdf', bbox_inches='tight')
