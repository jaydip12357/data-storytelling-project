# data-storytelling-project

# Data Storytelling: The Untold Stories in Public Stroke Trial Data

## Project Overview  
In this project, we explore the **International Stroke Trial (IST)** dataset to uncover compelling stories about stroke outcomes, risk factors, and treatment effects. Our aim is not just to run analyses, but to communicate insights in a way that is engaging, clear, and accessible to a broader audience. We will highlight patterns, surprises, and caveats—especially around bias, missing data, and ethical concerns.

## Dataset Description & Citation

**Dataset**: International Stroke Trial (IST) database  
**Original publication**: Sandercock P. A. G., Niewada M., Członkowska A., et al. *The International Stroke Trial database*. Trials 2011. 
**Key facts**:  
- 19,435 patients with acute (ischemic) stroke, with ~99% follow-up completeness :contentReference 
- Variables recorded include baseline demographics, treatment assignment (aspirin / heparin / both / neither), 14-day outcomes, 6-month outcomes, comorbidities, and more :contentReference[oaicite:3]{index=3}  
- Data are anonymized: no direct identifiers; dates are converted to days since randomization; patient age is rounded :contentReference[oaicite:4]{index=4}  
- None of the patients in this trial received thrombolytic therapy, reflecting the era when the trial was done :contentReference[oaicite:5]{index=5}  

**Workflow (the following files can be found under scripts/)**
1) Run assess_data_structure.py to assess the data structure of the IST data.
2) Run report_descriptive_statistics.py to get descriptive stats on the IST data.
3) Run assess_data_quality.py to assess the data quality of the IST data.
4) Run clean_data.py to handle missing values in the IST data (resulting csv's should be stored under the data/cleaned folder) <-- Preprocessing Step 1.
5) Run transform_data.py to one-hot encode the categorical columns of the cleaned datasets (resulting csv's will be stored under data/transformed) <-- Preprocessing Step 2 and Feature Engineering.
6) Run variable_relationships.py to assess the importance of the variables in relation to whether patients remain alive/dead.
7) Run visualizations.py to get different graphs regarding the most important variables as determined in 6). The resulting visualizations have been stored as pngs under data/visualizations.


**Citation**:

> Sandercock, P. A. G., Niewada, M., Członkowska, A., & the International Stroke Trial Collaborative Group. (2011). *The International Stroke Trial database* (Version 2) [Dataset]. University of Edinburgh, Department of Clinical Neurosciences. https://doi.org/10.7488/ds/104 :contentReference[oaicite:6]{index=6}  
  

## Repository Structure

## Team Members
1. Ethan
2. Jaideep

