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
             WHEN a.rac1p = '2' AND HISP ='01' THEN 'Black\African American'                                                         
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

FROM pums_2017 AS A

WHERE 
          puma BETWEEN '11610' AND '11615'
    AND agep BETWEEN 16 and 24
    AND rt = 'P'  

;