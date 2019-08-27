#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 08:16:46 2019

@author: cnorahs
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# CSV file name
input_csv = '../../data/raw/epi_jobs_raw.csv'

# Read in Pandas dataframe
df_all = pd.read_csv(input_csv, encoding='ISO-8859-1')

# Filter to get only year 2000 and 2019
df_tn = df_all[df_all['year'] == 2019]

# Filter to get only January, seasonal adjusted, and Tennessee numbers
df_tn = df_tn[(df_tn['month'] == 'January') & (df_tn['seasonal'] == 'S')][
        ['year',
         'super',
         'Tennessee']]

# Get values for Jan. 2019 for all sectors
list_delta = []
list_sectors = list(set(df_tn['super']))
for sector in list_sectors:
    n2019 = list(df_tn[(df_tn['super'] == sector) & (df_tn['year'] == 2019)]['Tennessee'])[0]
    list_delta.append(round(float(n2019), 1))

# Put into dataframe for plotting later
df = pd.DataFrame({
        'sector': list_sectors,
        'change_in_jobs': list_delta})
sectors_to_plot = ['Manufacturing',
                   'Construction & Mining',
                   'Wholesale Trade',
                   'Information',
                   'Education and Health Services',
                   'Leisure and Hospitality',
                   'Professional and Business Services',
                   'Trade Transportation and Utilities',
                   'Government',
                   'Retail Trade',
                   'Financial Activities',
                   'Other Services']
df = df[df['sector'].isin(sectors_to_plot)].sort_values(
        by='change_in_jobs',
        ascending=False)


# https://stackoverflow.com/questions/25550308/pyplot-bar-chart-of-positive-and-negative-values
# https://python-graph-gallery.com/4-add-title-and-axis-label/
# https://python-graph-gallery.com/3-control-color-of-barplots/
# https://stackoverflow.com/questions/30228069/how-to-display-the-value-of-the-bar-on-each-bar-with-pyplot-barh

x = range(len(df))
negative_data = [k if k < 0 else 0 for k in list(df['change_in_jobs'])]
positive_data = [k if k > 0 else 0 for k in list(df['change_in_jobs'])]
bars = list(df['sector'])
y_pos = np.arange(len(bars))
colors = list(sns.color_palette('cubehelix', len(sectors_to_plot)))
# random.shuffle(colors)

# Initiate figure
fig = plt.figure()
ax = plt.subplot(111)
ax.bar(x, positive_data, width=0.7, color=colors[::-1])
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
    ax.text(rect.get_x() + rect.get_width() / 2, height+5, label,
            ha='center', va='bottom', fontsize=8)

plt.savefig('job_sector_breakdowns.png',
            dpi=300,
            bbox_inches='tight')
