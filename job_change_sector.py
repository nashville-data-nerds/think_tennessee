#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:37:55 2019

@author: cnorahs
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# CSV file name
input_csv = 'epi_jobs_raw.csv'

# Read in Pandas dataframe
df_all = pd.read_csv(input_csv, encoding='ISO-8859-1')

# Filter to get only year 2000 and 2019
df_tn = df_all[(df_all['year'] == 2000) | (df_all['year'] == 2019)]

# Filter to get only January, seasonal adjusted, and Tennessee numbers
df_tn = df_tn[(df_tn['month'] == 'January') & (df_tn['seasonal'] == 'S')][
        ['year',
         'super',
         'Tennessee']]

# Get differences between Jan. 2019 and Jan. 2000 for all sectors
list_delta = []
list_sectors = list(set(df_tn['super']))
for sector in list_sectors:
    n2019 = list(df_tn[(df_tn['super'] == sector) & (df_tn['year'] == 2019)]['Tennessee'])[0]
    n2000 = list(df_tn[(df_tn['super'] == sector) & (df_tn['year'] == 2000)]['Tennessee'])[0]
    list_delta.append(round(float(n2019) - float(n2000), 1))

# Put into dataframe for plotting later
df = pd.DataFrame({
        'sector': list_sectors,
        'change_in_jobs': list_delta})
sectors_to_plot = ['Manufacturing',
                   'Wholesale Trade',
                   'Information',
                   'Education and Health Services',
                   'Leisure and Hospitality',
                   'Professional and Business Services',
                   'Trade Transportation and Utilities',
                   'Government',
                   'Retail Trade',
                   'Financial Activities']
df = df[df['sector'].isin(sectors_to_plot)].sort_values(by='change_in_jobs')


# https://stackoverflow.com/questions/25550308/pyplot-bar-chart-of-positive-and-negative-values
# https://python-graph-gallery.com/4-add-title-and-axis-label/
# https://python-graph-gallery.com/3-control-color-of-barplots/
# https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh

x = range(len(df))
negative_data = [k if k < 0 else 0 for k in list(df['change_in_jobs'])]
positive_data = [k if k > 0 else 0 for k in list(df['change_in_jobs'])]
bars = list(df['sector'])
y_pos = np.arange(len(bars))

# Initiate figure
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(x, negative_data, width=0.7, color='#0a3317')
ax.bar(x, positive_data, width=0.7, color='#22bd53')
rects = ax.patches

# Label x-axis
plt.xticks(y_pos, bars, rotation=45, ha='right')
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False)         # ticks along the top edge are off

# Make bars' labels as their heights
labels = [str(k) for k in list(df['change_in_jobs'])]
heights = list(df['change_in_jobs'])

# Actually writing the labels
for rect, label, height in zip(rects, labels, heights):
    if height > 0:
        ax.text(rect.get_x() + rect.get_width() / 2, height+5, label,
                ha='center', va='bottom')
    else:
        ax.text(rect.get_x() + rect.get_width() / 2, height-20, label,
                ha='center', va='bottom')

plt.savefig('job_change_sector.png',
            dpi=300,
            bbox_inches='tight')
