import os
import sys
from src.data import data_collection
import numpy as np
import pandas as pd
import geopandas as gp
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.colors

# list of labels for map creation function
labels = ("Washington State", "King County", "North King County", "South King County")

# map creation
def map_creation(labels, title):
        fig, ax = plt.subplots(figsize=(20,10))
        colors = ["beige", "green"]
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", colors)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_xticks([])
        ax.set_yticks([])
        handles = []
        for index in range(len(labels)):
                patch = mpatches.Patch(color=colors[index], label=labels[index])
                handles.append(patch)
        ax.legend(handles=handles, loc="lower left", fontsize="xx-large")
        ax.set_title(title, fontsize="xx-large")
        return fig, ax, cmap

# save map
def save_map(fig, savename):
        fig.savefig(savename, dpi=150, facecolor=None, edgecolor=None,
        orientation='landscape', papertype=None, format='png',
        transparent=False, bbox_inches=None, pad_inches=None, metadata=None)