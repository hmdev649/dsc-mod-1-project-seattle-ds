import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def pull_data():
    ty_2016 = pd.read_csv('../exploratory/total_youth_2016.csv').round(0)
    ty_2017 = pd.read_csv('../exploratory/total_youth_2017.csv').round(0)
    oy_2016 = pd.read_csv('../exploratory/opportunity_youth_2016.csv').round(0)
    oy_2017 = pd.read_csv('../exploratory/opportunity_youth_2017.csv').round(0)
    # race_2017 = pd.read_csv('../exploratory/race_2017.csv').round(0)
    # race2_2017 = pd.read_csv('../exploratory/race2_2017.csv').round(0)
    datafiles = {'ty_2016':ty_2016,
                 'ty_2017':ty_2017,
                 'oy_2016':oy_2016,
                 'oy_2017':oy_2017}

    return datafiles

def create_trend_bar_age(datafiles):
    ty_2016=datafiles['ty_2016'].rename(columns={'Unnamed: 0': 'youthtype'})
    ty_2016.set_index('youthtype', inplace=True)
    ty_2017=datafiles['ty_2017']
    ty_2017.set_index('youthtype', inplace=True)

    c_1620=pd.concat((ty_2016, ty_2017), axis=0, ignore_index=True)

    index_labels = {0: 'total youth',
                    1: 'opportunity youth',
                    2: 'working without diploma',
                    3: 'not opportunity youth',
                    4: 'total youth',
                    5: 'opportunity youth',
                    6: 'working without diploma',
                    7: 'not opportunity youth'}
    c_1620 = c_1620.rename(index=index_labels)

    c_1620['Year'] = ['2016', '2016', '2016','2016' ,'2020', '2020', '2020','2020']
    c_1620=c_1620.reset_index()

    for i, c in enumerate(c_1620):
        if 0<i<9:
            if i%2 == 1:
                data_bar=c_1620.loc[c_1620['index'] != 'total youth', ['index', c, 'Year']]
            else:
                data_bar=c_1620.loc[:, ['index', c, 'Year']]
            bar =sns.catplot(x='index', 
                             y=c, 
                             hue='Year', 
                             data=data_bar, 
                             kind='bar', 
                             height=6, 
                             aspect=3)
            bar.set_titles('Youth Type by Age')
            bar.set_xlabels('Youth Type')
            sns.set(font_scale = 1.5)
            plt.savefig(f'../../reports/figures/barchartage{i}.png')
    return bar

def create_trend_bar_degree(datafiles):
    oy_2016 = datafiles['oy_2016']
    oy_2017 = datafiles['oy_2017']
    oy_2016 = oy_2016.rename(columns={'Unnamed: 0':'educationattainment'})
    oy_1620 = pd.concat((oy_2016, oy_2017), axis=0)
    oy_1620['Year'] = ['2016', '2016', '2016','2016','2016','2020', '2020', '2020','2020','2020']
    
    for i, c in enumerate(oy_1620):
        if 0<i<9:
            if i%2 == 1:
                data_bar = oy_1620.loc[oy_1620['educationattainment'] !='Total', ['educationattainment', c, 'Year']]
            else:
                data_bar = oy_1620.loc[:, ['educationattainment', c, 'Year']]
            bar =sns.catplot(x='educationattainment', 
                             y=c, 
                             hue='Year', 
                             data=data_bar, 
                             kind='bar', 
                             height=6, 
                             aspect=3, 
                             ci=None, 
                             palette= 'RdBu', 
                             margin_titles=c)
            bar.set_titles(c)
            sns.set(font_scale=1.5) 
            plt.savefig(f'../../reports/figures/barchartdegree{i}.png')   
    return bar
 
def create_race_bar(race_2016,race_2017):
    race_1620 = pd.concat((race_2016, race_2017))
    year = []
    for i in range(18):
        if i<9:
            year.append('2016')
        else:
            year.append('2020')
    race_1620['Year'] = year
    
    race_1620 = race_1620.rename(columns={'Total': 'Total Population'})
    race_1620 = race_1620.reset_index()
   
    for i, c in enumerate(race_1620):
        if 0<i <5:
            if i == 3:
                data_bar = race_1620.loc[race_1620['index']!='Total', ['index', c, 'Year']]
            else:
                data_bar = race_1620.loc[:, ['index',  c, 'Year']]
            bar_race = sns.catplot(x=c, 
                                   y='index', 
                                   hue='Year', 
                                   data=data_bar, 
                                   kind ='bar', 
                                   aspect=3, 
                                   palette='Set2')
            sns.set(font_scale=1.5)
            bar_race.set_ylabels('Race')  
            plt.savefig(f'../../reports/figures/barchartrace{i}.png')
    return bar_race