# Exploratory

This directory contains unpolished exploratory data analysis (EDA) notebooks.

Process and methods: 

    1. Created the basetable that contains the data needed for analysis in the sql. 
        * The total population is the serialno * pwgtp (the person weight)
        * puma values from 11610 to 11615 are used to identify south King County.
        * use esr for employee status.

    2. Created tables to update the report tables on page2 in the 2016 report. 
     https://roadmapproject.org/wp-content/uploads/2018/09/Opportunity-Youth-2016-Data-Brief-v2.pdf

    3. Installed tabula to extract the age table from the 2016 report. Created the race table for 2016 manually due to the tabula can only extract the age table. 

    4. Use seaborn to create visualizations. Reformed the data table as a format that could use sns.catplot to generate the charts for the need. 

    5. Create map by using geopanda package. The map shapefile was downloaded from https://bit.ly/31P8Iqu

    6. Wrote functions in Visual Studio, so that it is clean in the notebook when deliver the result to people.

    7. Update the environment.yml file. 


FIndings from comparing 2016 reports and current analysis:

    * Total sample size has dropped by 39%

    * The proportion of O.Y. to total youth population has slightly decreased

    * In the long run, the goal is for both O.Y. and youth working without diplomas to both decrease 

    * There are now proportionally fewer college-educated O.Y. across all age brackets
    
    * In terms of race: a). as a share of all American Indian/Alaska Native youth, higher percentage are now classified as OY. b). As a share of all OY, Hispanic youth are now a higher percentage. 

    
    
Recommendations:
    
    * Assess ROI of existing support programs and derive recommendations for greater efficiency

    * Highlight some individual success stories to the local business community to drive better hiring

    * Focus more on OY segments showing least improvement


References: 

    Seattle Region Partnership. 2016. “King County Opportunity Youth Overview: Demographics of opportunity youth and systemic barriers to employment”. Available at: https://bit.ly/2oRGz37.

    Yohalem, N., Cooley, S. 2016. “Opportunity Youth in the Road Map Project Region”. Community Center for Education Results. Available at: https://bit.ly/2P2XRF3.

    ACS 5-Year Estimates - Public Use Microdata Sample (2017). Available at https://bit.ly/37opwpi. 

    TIGER/Line Shapefile, 2017, 2010 state, Washington, 2010 Census Public Use Microdata Area (PUMA) State-based. Available at https://bit.ly/31P8Iqu.
    
    
Next steps: 

    * Data Freshness & Richness
    * Precisely duplicate sample set of 2016 report
    * Use PUMA Survey from 2014-2018
    * Include all intervening years in trend analysis
    * Additional EDA
    * Choropleth of O.Y. data by PUMA 
    * Available jobs for < 29 in South King County by PUMA:
    * Most popular industries for employment
    * Industries with the greatest shortage of workers
    * Expanded Scope
    * Track O.Y. pipeline over time
