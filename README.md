# LOFAR Failure Analysis
Repository of LOFAR failure analysis tools for producing the bi-semester failure reports. 

### How to run
1) `git clone` the repository
2) `cd` to main folder 
3) In terminal: `jupyter notebook`
4) Open the template ipynb: `LOFARFailureAnalysis-Template.ipynb`
5) In the notebook window: `File` > `Make a copy...`
6) Rename the copy to something sensible, e.g. `LOFARFailureAnalysis-Cycle11Part2.ipynb`
7) Edit the initialisation values in cell 2 of the notebook, e.g. `csv_name = 'input/Cycle11-Part2.csv'`
8) In the notebook window: `Kernel` > `Restart & Run All`

This should generates all the resulting plots in the subfolder `results` (included but not filled). A test can be run with the notebook as it is to ensure it is functioning correctly. 

### Note about CSVs (WIP)
The file used for the report (e.g. `'input/Cycle11-Part2.csv'`) assumes that the contents contain the relevant failures for the given time period. Not yet done, but the notebook should be extended to include a start date + end date, to allow the input CSV file to contain all the data (given the new Google form way of collecting data), and then just select failures between the two dates. 
