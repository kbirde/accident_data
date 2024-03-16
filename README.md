# ACCIDENT DATA VISUALIZATION

# 1.0 INTRODUCTION:

The main objective of this project is to process & extract accident data from the US National Highway Traffic Safety Adminstration (NHTSA) and to generate two different chart visualizations. The first visualization displays the accident location in the US state that the user chooses and the second visualization displays the annual average number of accidents that occurs on each day of the week in that state.

# 2.0 DATASET:

 The original accident data is available for download for the years 1975 - 2021 at the following web address: https://www.nhtsa.gov/file-downloads?p=nhtsa/downloads/FARS/. For the purpose of this project, two sets of data (ACCIDENT & PERSON) were selected for the year 2010. Each file is of the comma separated values (CSV) format and has several features. In this project only 4 features (DAY_WEEK, HOUR, LATITUDE & LONGITUDE) have been downselected for plotting purposes. These CSV files are stored in a sub-directory called CSV_DATA. 

# 3.0 MODULE DESCRIPTION

The project consists of 4 different modules as outlined below:

a) state_dict.py: This module contains the state codes for each US state from which the user can select a state ID

b) code.py: This module calls in the state_dict.py and displays all the US state IDs from which the user can choose one

c) map_donut.py: After the user selects the US state ID, this module plots the two visualizations in a new VS code tab when the user enters the aforementioned ID and the accident year they are interested in from the data stored in the CSV_DATA folder. In the event the user chooses an unavilable state ID, the try & except error block will capture this situation. This file can be run independently and the help option provides the syntax to run the code.

d) main.py: This is the main module that can be run by the user to display the visualizations. If more modules are created for additional display charts, this main module should be able to integrate them.

# 4.0 USAGE:

Here are the steps to run this project:

1) Clone the project from https://github.com/kbirde/accident_data/

2) Install plotly package

    pip instll plotly

3) Run the codes.py module to select your state ID:

    python3 codes.py

    Example: The code for MI can be noticed to be 26

4) Run the main.py module (arguments needed are path to CSV file, state ID code, accident year of interest):

    python3 main.py CSV_DATA/ACCIDENT_2010.csv 26 2010

# 5.0 OUTPUT DESCRIPTION

    Both the visualization plots will appear in a new window. 
    
    The first visualization indicates the location of the different accidents in the state of MI for the year 2010 (hovering the mouse over the state will provide the actual latitue and longitude locations).

    The second visualization shows a donut chart that contains, for each day of the week, the average number of accidents that occurred on any particular day. We can notice that maximum number of accidents occurred over the weekend, indicative of possible DUI incidents (this could be correlated using additional data from different source in the FARS data set for future project work).

# 6.0 AUTHOR:
    Kiran Irde