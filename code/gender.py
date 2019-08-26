import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('../../raw/epi_labor_force_data_raw.csv')

"""
Going to grab the following splits of data:
`us_m`: All males in the US
`us_f`: All females in the US
`tenn_m`: All males in Tennessee
`tenn_f`: All females in Tennessee
"""

us_m = df.loc[(df.geo=='United States')&(df.categ=='Male')]
us_f = df.loc[(df.geo=='United States')&(df.categ=='Female')]
tenn_m = df.loc[(df.geo=='Tennessee')&(df.categ=='Male')]
tenn_f = df.loc[(df.geo=='Tennessee')&(df.categ=='Female')]

"""
Create a plot of labor force participation as a function of time (year).  
This may not be the most elegant solution, but the idea is to build up lists
of year and labor force participation by looping through each year's columns
"""

sns.set()
sns.set_style("white")
#sns.set_palette("BuGn_r")
#pal = sns.cubehelix_palette(4, start=2, rot=0, dark=0, light=0.75, reverse=True)
pal = sns.color_palette('YlGn',4)
sns.set_palette(pal)
fig, ax = plt.subplots(figsize=(8,4))
for category, name in zip([us_m, us_f, tenn_m, tenn_f], ['US Men', 'US Women', 'TN Men', 'TN Women']):
    year = list()
    participation = list()
    for i in np.arange(1979,2019,1):
        year.append(i)
        par = category['Nlf{}{}'.format(str(i)[2],str(i)[3])] / category['Npop{}{}'.format(str(i)[2],str(i)[3])]
        participation.append(par.values)
    ax.plot(year, participation, label=name)#, color=color_scheme(name))

plt.legend(loc=2,
        prop={'size': 10},
        bbox_to_anchor=(1.05,1),
        borderaxespad=0.0)
plt.xlabel('Year')
plt.ylabel('Labor Force Participation')
plt.grid(axis='y', alpha=0.3)

plt.savefig('lfp_by_gender.pdf',  bbox_inches='tight')
