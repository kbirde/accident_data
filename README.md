# ACCIDENT DATA VISUALIZATION

# 1.0 INTRODUCTION:

The main objective of this project is to process & extract accident data from the US National Highway Traffic Safety Adminstration (NHTSA) and to generate two different chart visualizations. The first visualization displays the accident location in the US state that the user chooses and the annual average number of accidents that occurs on each day of the week in that state. The second visualization shows the effects of either wearing or not wearing seatbelts on the accident fatality rate.

# 2.0 DATASET:

 The original accident data is available for download for the years 1975 - 2021 at the following web address: https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/. For the purpose of this project, two sets of data (ACCIDENT & PERSON) were selected for the year <b>2010</b>. Each file is of the comma separated values (CSV) format and has several features. In this project only 4 features, i.e. DAY_WEEK, HOUR, LATITUDE & LONGITUDE from the ACCIDENT_2010.csv file and 2 features, i.e. RES_USE & DEATH_DA from the PERSON_2010.csv files have been downselected for plotting purposes. These CSV files are stored in a sub-directory called CSV_DATA. 

# 3.0 MODULE DESCRIPTION

The project consists of 5 different modules as outlined below:

1. state_dict.py: This module contains the state codes for each US state from which the user can select a state ID

2. code.py: This module calls in the state_dict.py and displays all the US state IDs from which the user can choose one

3. map_donut.py: After the user selects the US state ID by running code.py, this module plots the two visualizations in a new VS code tab when the user enters the aforementioned ID and the accident year they are interested in from the data stored in the CSV_DATA folder. In the event the user chooses an unavailable state ID, the try & except error block will capture this situation. This file can be run independently and the -h help option provides the syntax to run the code.

4. bar_plot.py: After the user selects the US state ID by running code.py, this module displays a bar chart with a pull down menu option when the user provides this state ID & the accident year as indicated in the map_donut module. The try & except error block will capture a situation that the user enters an invalid state ID. This file can also be run independently and the syntax is available via the -h help option.

5. main.py: This is the main module that can be run by the user to display the visualizations. The syntax to run this code can be obtained using the -h help option. If more modules are created for additional display charts, this main module should be able to integrate them.

# 4.0 USAGE:

Here are the complete steps to run this project:

1. Clone the project from https://github.com/kbirde/accident_data/

2. Install plotly package

    pip install plotly

3. Run the codes.py module to select your state ID:

    python3 codes.py

    Example: The code for MI can be noticed to be 26

4. (OPTIONAL) Run the map_donut.py module (arguments required are path to ACCIDENT_2010.csv file, state ID code, accident year of interest)

    python3 map_donut.py CSV_DATA/ACCIDENT_2010.csv 26 2010

5. (OPTIONAL) Run the bar_plot.py module (arguments required are path to PERSON_2010.csv file, state ID code, accident year of interest)

    python3 bar_plot.py CSV_DATA/PERSON_2010.csv 26 2010

6. Run the main.py module (arguments needed are path to ACCIDENT_2010.csv file, path to the PERSON_2010.csv file, state ID code, accident year of interest):

    python3 main.py CSV_DATA/ACCIDENT_2010.csv CSV_DATA/PERSON_2010.csv 26 2010

# 5.0 OUTPUT DESCRIPTION

The main.py will generate two different visualization pages in separate VS Code windows. The output desciption below is for the usage of state ID code 26 and the accident year 2010.

1. Map & Donut char plots:

This plot contains a map and a donut plot. 
    
The US map visualization indicates the location of the different accidents in the state of MI for the year 2010 (hovering the mouse over the state will provide the actual latitue and longitude locations).

The donut chart contains, for each day of the week, the average number of accidents that occurred on any particular day. We can notice that maximum number of accidents occurred over the weekend, indicative of possible DUI incidents (this could be correlated using additional data from different source in the FARS data set for future project work).

2. Bar plots:

This plot contains a bar plot with a pull down menu. By default, the effects of restraint for "All" scenarios are shown. Upon selecting the "Seatbelts Worn" option in the menu, the plot displays the effects of how restraints on fatality numbers. As expected, the number of fatalities go down with usage of seatbelts. When the user selects the "No Seatbelts" option, the effect of not wearing the restraints is displayed. This also corresponds to the expected result of higher fatalities occuring when driver do not wear their seatbelts.

# 6.0 FUTURE WORK

The modularity of the code allows us to add in other aspects that could be extracted from the FARS data set such as the effect of DUI driving, the occurance of accident types (frontal, side, rollover), etc. Each of these could be an independent module that can both be executed individually or called from the main.py module for a full report.

# 7.0 AUTHOR

Kiran Irde