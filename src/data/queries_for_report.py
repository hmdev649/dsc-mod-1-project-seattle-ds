import psycopg2
import pandas as pd
import numpy as np
from tabula import read_pdf
pd.set_option('max_colwidth', 80)

from src.data import sql_utils

def create_df():
    DBNAME ="opportunity_youth"
    conn=psycopg2.connect(dbname=DBNAME)
    df=sql_utils.sql_script_to_df(conn, "13_opportunity_youth_df.sql")
    return df 

def create_total_youth_2017(df):
    nd =pd.pivot_table(df,
               index=['youthtype'],
               values=['totalnumber'],
               columns=['age'],
               aggfunc=np.sum,
               fill_value='',
               margins=True,
               margins_name='Total'
              )['totalnumber']
    nd.reset_index()
    nd.columns.rename('', inplace=True)
    for i, c in enumerate(nd):
        newc=(nd[c]/nd[c]['Total'])*100
        nd.insert(i*2, '%'+ str(c), newc)
    new_index1=['Total', 'Opportunity Youth', 'Working without Diploma', 'Not Opportunity Youth']
    total_youth_2017=nd.reindex(new_index1)
    for i in total_youth_2017:
        total_youth_2017[i]=total_youth_2017[i].astype('int')
    return total_youth_2017

def create_opportunity_youth_2017(df):
    df_oy =df[df['youthtype']=='Opportunity Youth']
    import numpy as np
    md =pd.pivot_table(df_oy,
                index=['educationattainment'],
                values=['totalnumber'],
                columns=['age'],
                aggfunc=np.sum,
                fill_value=0,
                margins=True,
                margins_name='Total'
                )['totalnumber']
    md.reset_index()
    md.columns.rename('', inplace=True)

    for i, c in enumerate(md):
        mewc=(md[c]/md[c]['Total'])*100
        md.insert(i*2, '%'+str(c), mewc)

    new_index2=pd.Index(['Total', 'No Diploma', 'HS Diploma or GED', 'Some College, No Degree', 'Degree (Associate or Higher)'], 
                    name='educationattainment')
    opportunity_youth_2017 = md.reindex(new_index2)
    for i in opportunity_youth_2017:
        opportunity_youth_2017[i]=opportunity_youth_2017[i].astype('int')
    return opportunity_youth_2017

def create_basetable_2016():
    df_2016 = read_pdf('https://roadmapproject.org/wp-content/uploads/2018/09/Opportunity-Youth-2016-Data-Brief-v2.pdf', 
              pages='9', multiple_tables=True, output_format='DataFrame')
    df_2016=df_2016[0]
    df_2016.columns =['16-18', '19-21', '22-24', 'Total']
    return df_2016

def create_total_youth_2016(df_2016):
    total_2016=df_2016[0:3]
    total_2016=total_2016.rename(index={0: 'Opportunity Youth', 1: 'Working without Diploma', 2:'Not Opportunity Youth'})
    
    for i in total_2016:    
        total_2016[i]=total_2016[i].str.replace(',','').astype('float')
    total_2016.loc['Total']=total_2016.sum(axis=0)

    total_2016=total_2016.reindex(['Total', 'Opportunity Youth', 'Working without Diploma', 'Not Opportunity Youth'])

    for i, c in enumerate(total_2016):
        num=(total_2016[c]/total_2016[c]['Total'])*100
        total_2016.insert(i*2, '%'+str(c), num)
        for i in total_2016:
            total_2016[i]=total_2016[i].astype('int')
    return total_2016

def create_opportunity_youth_2016(df_2016):
    oy_2016=df_2016[6:10]
    oy_2016=oy_2016.rename(index={6:'No Diploma', 7: 'HS Diploma or GED', 8: 'Some College, No Degree', 9:'Degree (Associate or Higher)'})

    for i in oy_2016:    
        oy_2016[i]=oy_2016[i].str.replace(',','').astype('float')
    oy_2016.loc['Total']=oy_2016.sum(axis=0)
    oy_2016=oy_2016.reindex(['Total', 'No Diploma', 'HS Diploma or GED', 'Some College, No Degree', 'Degree (Associate or Higher)'])

    for i, c in enumerate(oy_2016):
        num=(oy_2016[c]/oy_2016[c]['Total'])*100
        oy_2016.insert(i*2, '%'+str(c), num)
        for i in oy_2016:
            oy_2016[i]=oy_2016[i].astype('int')
    return oy_2016
    
def create_race_2017(df):
    race_2017 =pd.pivot_table(df,
               index=['race'],
               values=['totalnumber'],
               columns=['youthtype'],
               aggfunc=np.sum,
               fill_value='',
               margins=True,
               margins_name='Total'
              )['totalnumber']
    #race_2017.reset_index()
    race_2017.columns.rename('', inplace=True)
    race_2017=race_2017.drop(columns=['Not Opportunity Youth', 'Working without Diploma'])

    numa=race_2017['Opportunity Youth']/race_2017['Opportunity Youth'][8]*100
    race_2017.insert(0, 'Proportion of OY %', numa)
    numb=race_2017['Opportunity Youth']/race_2017['Total']*100
    race_2017.insert(2, 'Rate of OY %', numb)
    for i in race_2017:
        race_2017[i]=race_2017[i].astype('int')
    race_2017=race_2017.reindex(['Total', 'American Indian\Alaska Native','Hawaiian and Other Pacific Islander',
    'Black\African American', 'Hispanic', 'Some other Race alone','Two or More Races',
    'White','Asian'])
    race_2017=race_2017[['Rate of OY %', 'Total', 'Proportion of OY %', 'Opportunity Youth']]
    race_2017.reset_index()
    return race_2017

def create_race_2016():
    race_2016_index=['Total', 'American Indian\Alaska Native','Hawaiian and Other Pacific Islander',
    'Black\African American', 'Hispanic', 'Some other Race alone','Two or More Races',
    'White','Asian']
    race_2016_total=[139735, 1242, 1884, 14339, 11490, 6473, 12368, 69050, 22889]
    race_2016_oy=[18817, 387, 439, 2791, 2008, 1112, 1534, 8547, 1999]

    race_2016 = pd.DataFrame(list(zip(race_2016_total, race_2016_oy)), index=race_2016_index,
                columns =['Total', 'Opportunity Youth']) 
    race_2016['Rate of OY %']=race_2016['Opportunity Youth']/race_2016['Total']*100
    race_2016['Proportion of OY %']=race_2016['Opportunity Youth']/race_2016['Opportunity Youth'][0]*100
    race_2016=race_2016[['Rate of OY %', 'Total', 'Proportion of OY %', 'Opportunity Youth']]
    for i in race_2016:
            race_2016[i]=race_2016[i].astype('int')
    return race_2016

def create_race2_2017(df):
    race2_2017 =pd.pivot_table(df,
               index=['youthtype'],
               values=['totalnumber'],
               columns=['race2'],
               aggfunc=np.sum,
               fill_value='',
               margins=True,
               margins_name='Total'
              )['totalnumber']
    race2_2017.reset_index()
    race2_2017.columns.rename('', inplace=True)
    for i, c in enumerate(race2_2017):
        num=(race2_2017[c]/race2_2017[c]['Total'])*100
        race2_2017.insert(i*2, '%'+str(c), num)
        for i in race2_2017:
            race2_2017[i]=race2_2017[i].astype('int')
        race2_2017.reindex(['Total', 'Opportunity Youth','Working without Diploma','Not Opportunity Youth'])
    return race2_2017

    
