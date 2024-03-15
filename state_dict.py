"""This module provides the state codes as a dictionary"""
import argparse
import pandas as pd

# Dictionary containing list of states and their code ID's as per the User's Manual
state_dict = {1:'Alabama',2: 'Alaska', 4: 'Arizona',5: 'Arkansas',6: 'California',8: 'Colorado',9: 'Connecticut',10: 'Delaware',
            11: 'District of Columbia',12: 'Florida',13: 'Georgia',15: 'Hawaii',16: 'Idaho',17: 'Illinois',18: 'Indiana',
            19: 'Iowa',20: 'Kansas',21: 'Kentucky',22: 'Louisiana',23: 'Maine',24: 'Maryland',25: 'Massachusetts',
            26: 'Michigan',27: 'Minnesota',28: 'Mississippi',29: 'Missouri',30: 'Montana',31: 'Nebraska',32: 'Nevada',
            33: 'New Hampshire',34: 'New Jersey',35: 'New Mexico',36: 'New York',37: 'North Carolina',38: 'North Dakota',
            39: 'Ohio',40: 'Oklahoma',41: 'Oregon',42: 'Pennsylvania',43: 'Puerto Rico',44: 'Rhode Island',45: 'South Carolina',
            46: 'South Dakota',47: 'Tennessee',48: 'Texas',49: 'Utah',50: 'Vermont',51: 'Virginia',52: 'Virgin Islands',
            53: 'Washington',54: 'West Virginia',55: 'Wisconsin',56: 'Wyoming'}

if __name__ == "__main__":
    # print('------------------------------------')    
    # print("This code contains the State code ids")
    # print('------------------------------------')

    parser = argparse.ArgumentParser(
        description="Contains the state code ids. This file is called & used by other modules."
        )
    args = parser.parse_args()