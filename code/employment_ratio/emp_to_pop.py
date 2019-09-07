import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

"""
Create a plot of labor force participation and the unemployment to
population ratio in Tennessee as a function of time (year).
"""

sns.set()
sns.set_style("white")
pal = sns.color_palette('YlGn',2)
sns.set_palette(pal)
df = pd.read_csv('../../data/raw/epi_labor_force_data_raw.csv')
tenn = df.loc[(df.geo=='Tennessee')&(df.categ=='All')]

fig, ax = plt.subplots(figsize=(8,4))
year = list()
participation = list()
ratio_list = list()

# Loop through years 1979 to 2018 to grab the corresponding columns
for i in np.arange(1979, 2019, 1):
    year.append(i)
    lfp = tenn['Nlf{}{}'.format(str(i)[2],str(i)[3])] / tenn['Npop{}{}'.format(str(i)[2],str(i)[3])]
    ratio = tenn['Nemp{}{}'.format(str(i)[2],str(i)[3])] / tenn['Npop{}{}'.format(str(i)[2],str(i)[3])]

    participation.append(lfp.values)
    ratio_list.append(ratio.values)

ax.plot(year, participation, label='Labor Force Participation')
ax.plot(year, ratio_list, label='Employment to Population Ratio')
plt.legend(loc=2,
          prop={'size': 10},
          bbox_to_anchor=(1.05,1),
          borderaxespad=0.0)
plt.xlabel('Year')
# Set y tick labels to percent signs
ax.set_yticklabels(['{0:.0%}'.format(x) for x in ax.get_yticks()])
plt.grid(axis='y', alpha=0.3)

plt.savefig('employment_to_population.pdf', bbox_inches='tight')
