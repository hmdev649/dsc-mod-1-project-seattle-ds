# South King County Opportunity Youth

by [Daihong Chen](https://github.com/Daihongchen), [Hamza Masood](https://github.com/hmdev649), and [Calvin Tirrell](https://github.com/calvintirrell)

This project offers an updated estimate of the number of Opportunity Youth in South King County using the 2017 5-year American Community Survey [(ACS)](https://www.census.gov/programs-surveys/acs/about.html) Public Use Microdata Survey [(PUMS)](https://www.census.gov/programs-surveys/acs/technical-documentation/pums.html).

## THIS REPOSITORY

### Setup Instructions

If you are missing required software (e.g. Anaconda, PostgreSQL), please run the following command in Bash:
```bash
# installs necessary requirements
# note: this may take anywhere from 10-20 minutes
sh src/requirements/install.sh
```

### `oy-env` conda Environment

This project relies on you using the [`environment.yml`](environment.yml) file to recreate the `oy-env` conda environment. To do so, please run the following commands *in your terminal*:

```bash
# create the oy-env conda environment
conda env create -f environment.yml

# activate the oy-env conda environment
conda activate oy-env

# if needed, make oy-env available to you as a kernel in jupyter
python -m ipykernel install --user --name oy-env --display-name "Python 3 (oy-env)"
```

Note that this may take 10 or more minutes depending on internet speed.

**Catalina Note:** You may need to modify the `prefix` at the very bottom of `environment.yml` if you are on macOS Catalina.  Run `conda env list` in your terminal to determine the appropriate path by looking at the paths of your existing conda environment(s).  Modify `environment.yml` then try running the installation commands listed above again.

### Data Download

To download the relevant data, run the following command *in Python*:

```
data_collection.download_data_and_load_into_sql()
```

Note that this may take 10 or more minutes depending on internet speed.

## PROCESS AND METHODS

1. Used a SQL query on the `pums_2017` table to create a "base" DataFrame that contains all of the data needed for analysis
    * The total population is the `serialno` * `pwgtp` (the person weight)
    * `puma` values from 11610 to 11615 are used to identify South King County
    * Use `esr` for employee status
2. Created tables to update the report tables on page 2 in the [2016 report](https://roadmapproject.org/wp-content/uploads/2018/09/Opportunity-Youth-2016-Data-Brief-v2.pdf)
3. Used the `tabula` library to extract the **age** table from the 2016 report PDF. Created the **race** table for 2016 manually because `tabula` can only extract the age table.
4. Used the `seaborn` library to create graph visualizations
    * Reshaped the data table as a format that could use `sns.catplot` to generate the charts
5. Used the `geopandas` library to create map visualizations.
    * The map shapefile was downloaded from https://bit.ly/31P8Iqu
6. Refactored the exploratory notebook code into functions (using Visual Studio), in order to deliver a [clean final notebook](/notebooks/report/oy_project_1.ipynb)
7. Updated the `environment.yml` file for reproducibility

## FINDINGS

From comparing 2016 reports and current analysis:

 * Total sample size has dropped by 39%
 * The proportion of O.Y. to total youth population has slightly decreased
 * In the long run, the goal is for both O.Y. and youth working without diplomas to both decrease
 * There are now proportionally fewer college-educated O.Y. across all age brackets
 * In terms of race: a). as a share of all American Indian/Alaska Native youth, higher percentage are now classified as OY. b). As a share of all OY, Hispanic youth are now a higher percentage.

## RECOMMENDATIONS

 * Assess ROI of existing support programs and derive recommendations for greater efficiency
 * Highlight some individual success stories to the local business community to drive better hiring
 * Focus more on OY segments showing least improvement


## REFERENCES

Seattle Region Partnership. 2016. “King County Opportunity Youth Overview: Demographics of opportunity youth and systemic barriers to employment”. Available at: https://bit.ly/2oRGz37.

Yohalem, N., Cooley, S. 2016. “Opportunity Youth in the Road Map Project Region”. Community Center for Education Results. Available at: https://bit.ly/2P2XRF3.

ACS 5-Year Estimates - Public Use Microdata Sample (2017). Available at https://bit.ly/37opwpi.

TIGER/Line Shapefile, 2017, 2010 state, Washington, 2010 Census Public Use Microdata Area (PUMA) State-based. Available at https://bit.ly/31P8Iqu.
    
    
## NEXT STEPS

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
