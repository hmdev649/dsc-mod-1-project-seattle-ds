import psycopg2
import pandas as pd
import numpy as np
from tabula import read_pdf
pd.set_option('max_colwidth', 80)

def create_df():
    DBNAME ="opportunity_youth"
    conn=psycopg2.connect(dbname=DBNAME)
    df=pd.read_sql("""
SELECT  
        A.serialno, 
        A.puma, 
        A.pwgtp totalnumber,
        CASE WHEN A.sch ='1' AND (A.esr='3' OR A.esr='6') THEN 'Opportunity Youth'
             WHEN (A.esr ='1' or A.esr='2' OR A.esr='4' OR A.esr='5') AND A.schl < '16' THEN 'Working without Diploma'
             ELSE 'Not Opportunity Youth' 
             END AS youthtype,
        CASE WHEN A.agep BETWEEN 16 AND 18 THEN '16-18'
             WHEN A.agep BETWEEN 19 AND 21 THEN '19-21'
             WHEN A.agep BETWEEN 22 AND 24 THEN '22-24'
             END AS age,
        CASE WHEN A.sex = '1' THEN 'Male'
             WHEN A.sex = '2' THEN 'Female'
             ELSE 'Other'
             END AS sex,
        CASE WHEN A.schl BETWEEN '01' AND '15' THEN 'No Diploma'
             WHEN A.schl BETWEEN '16' AND '17' THEN 'HS Diploma or GED'
             WHEN A.schl BETWEEN '18' AND '19' THEN 'Some College, No Degree'
             ELSE 'Degree (Associate or Higher)'
             END as educationattainment,
        CASE WHEN a.rac1p = '1' AND HISP ='01' THEN 'White'
             WHEN a.rac1p = '2' AND HISP ='01' THEN 'Black/African American'                                                         
             WHEN (a.rac1p = '4' OR a.rac1p = '5' OR a.rac1p='3') AND HISP ='01' THEN 'American Indian\Alaska Native'
             WHEN a.rac1p = '6' AND HISP ='01' THEN 'Asian'
             WHEN a.rac1p = '7' AND HISP ='01' THEN 'Hawaiian and Other Pacific Islander'
             WHEN a.rac1p = '8' AND HISP ='01' THEN 'Some other Race alone'
             WHEN a.rac1p = '9' AND HISP ='01' THEN 'Two or More Races'
             ELSE 'Hispanic'
             END AS race,
        CASE WHEN a.rac1p = '1' AND HISP ='01' THEN 'White'
             WHEN a.rac1p = '2' AND HISP ='01' THEN 'Black/African American'                                                         
             WHEN a.rac1p in('3','4','5','6','7','8','9') AND HISP ='01' THEN 'Other Races'
             ELSE 'Hispanic'
             END AS race2
    
FROM  pums_2017 AS A
      
WHERE 
          puma BETWEEN '11610' AND '11615'
          AND agep BETWEEN 16 and 24
          AND rt = 'P'  

;
""", conn)
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
    opportunity_youth_2017=md.reindex(new_index2)
    return opportunity_youth_2017

def create_basetable_2016():
    df_2016 = read_pdf('https://roadmapproject.org/wp-content/uploads/2018/09/Opportunity-Youth-2016-Data-Brief-v2.pdf', 
              pages='9', output_format='DataFrame')
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
    race_2017.reset_index()
    race_2017.columns.rename('', inplace=True)
    race_2017=race_2017.drop(columns=['Not Opportunity Youth', 'Working without Diploma'])

    numa=(race_2017['Opportunity Youth']/race_2017['Opportunity Youth'][8]*100)
    race_2017.insert(0, '%oOpportunityYouth', numa)
    numb=race_2017['Total']/race_2017['Total'][8]*100
    race_2017.insert(2, '%oTotal', numb)
    race_2017.reindex(['Total', 'American Indian\Alaska Native','Hawaiian and Other Pacific Islander alone',
    'Black/African American', 'Hispanic', 'Some other Race alone','Two or More Races',
    'White','Asian'])
    return race_2017

def create_race2_2017(df):
    race2_2017 =pd.pivot_table(df,
               index=['race2'],
               values=['totalnumber'],
               columns=['youthtype'],
               aggfunc=np.sum,
               fill_value='',
               margins=True,
               margins_name='Total'
              )['totalnumber']
    race2_2017.reset_index()
    race2_2017.columns.rename('', inplace=True)
    race2_2017=race2_2017.drop(columns=['Not Opportunity Youth', 'Working without Diploma'])

    numa=(race2_2017['Opportunity Youth']/race2_2017['Opportunity Youth'][4]*100)
    race2_2017.insert(0, '%oOpportunityYouth', numa)
    numb=race2_2017['Total']/race2_2017['Total'][4]*100
    race2_2017.insert(2, '%oTotal', numb)
    race2_2017.round(0)
    race2_2017.reindex(['Total', 'Black or'])
    return race2_2017