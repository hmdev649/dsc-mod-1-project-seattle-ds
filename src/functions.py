import os
import sys
# -----------------------
from src.data import data_collection
# -----------------------
import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors

# -----------------------

# shape file data imported and saved as dataframe df
df = gp.read_file('tl_2017_53_puma10/tl_2017_53_puma10.shp')

# list comprehension with values 11610-11615 saved in list lst
# add column "s_kc" to dataframe df if value in list lst is in column "PUMACE10"
lst = [str(num) for num in range(11610, 11616)]
df["s_kc"] = df['PUMACE10'].isin(lst)

# ------------------------

# add column "kc" to dataframe df if "King" or "Seattle" is in columnn "NAMELSAD10"
df["kc"] = df['NAMELSAD10'].str.contains("King|Seattle")

# ------------------------

fig1, ax = plt.subplots(figsize=(20,10))
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["beige", "green"])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])

wa_patch = mpatches.Patch(color='beige', label='Washington State')
kc_patch = mpatches.Patch(color='green', label='King County')
ax.legend(handles=[wa_patch, kc_patch], loc='lower left', fontsize='xx-large')
ax.set_title('Washington State PUMAS', fontsize='xx-large')
df.plot(ax=ax, column='kc', edgecolor='black', cmap=cmap)

# ------------------------

fig1.savefig('1_wa_state.png', dpi=150, facecolor=None, edgecolor=None,
        orientation='landscape', papertype=None, format='png',
        transparent=False, bbox_inches=None, pad_inches=None, metadata=None)

# ------------------------

fig2, ax = plt.subplots(figsize=(20,10))
n_kc_patch = mpatches.Patch(color='beige', label='North King County')
s_kc_patch = mpatches.Patch(color='green', label='South King County')
ax.legend(handles=[n_kc_patch, s_kc_patch], loc='lower left', fontsize='xx-large')
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["beige", "green"])
ax.set_title('King County PUMAS', fontsize='xx-large')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
df[df['kc']==True].plot(ax=ax, column='s_kc', edgecolor='black', cmap=cmap)

# ------------------------

fig2.savefig('2_king_county.png', dpi=150, facecolor=None, edgecolor=None,
        orientation='landscape', papertype=None, format='png',
        transparent=False, bbox_inches=None, pad_inches=None, metadata=None)
# ------------------------

fig3, ax = plt.subplots(figsize=(20,10))
s_kc_patch = mpatches.Patch(color='green', label='South King County')
ax.legend(handles=[s_kc_patch], loc='lower left', fontsize='xx-large')
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["beige", "green"])
ax.set_title('South King County PUMAS', fontsize='xx-large')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xticks([])
ax.set_yticks([])
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
df[df['s_kc']==True].plot(ax=ax,column='s_kc', edgecolor='black', cmap=cmap)

# ------------------------

fig3.savefig('3_south_king_county.png', dpi=150, facecolor=None, edgecolor=None,
        orientation='landscape', papertype=None, format='png',
        transparent=False, bbox_inches=None, pad_inches=None, metadata=None)

# ------------------------