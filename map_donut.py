"""This module is for plotting US statewise accident location map & a Donut chart for accidents occurring on different days of the week """
import argparse
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from state_dict import state_dict

def map_donut(accident_file , input_state):
    """This function takes in user input and plots the map & donut chart"""

    # Assign the state_dictionary
    state_dict1 = state_dict

    # Setting up try block of statements that will work if existing state code is entered 
    try:

        # Assigning the state input from the user    
        get_state = state_dict1[int(input_state)]
        get_state_id = int(input_state)

        # Reading in 2010 ACCIDENT data, downselecting the rows related to the user's state choice & reducing the dataframe to 4 columns
        acc_data = pd.read_csv(accident_file, encoding='utf-8')
        state_data = acc_data[acc_data.STATE ==get_state_id]
        state_data = state_data.loc[:,['DAY_WEEK','HOUR','LATITUDE','LONGITUD']]
        state_accident_count = state_data.groupby(['DAY_WEEK']).count()
        state_accident_count_list = state_accident_count['HOUR'].tolist()

        # Setting up a subplot with 1 row and 2 columns, specifying that the first column is a scattergeo map and the second column is a pie chart
        fig = make_subplots(rows=1, cols=2,
                            column_widths=[0.6,0.4],
                            row_heights=[0.4],
                            specs=[[{"type": "scattergeo"}, {"type": "pie"}]])

    # Adding a Scattergeo trace with latitude, longitude, marker (w/ color), title & focusing map to USA region
        fig.add_trace(
            go.Scattergeo(lat=state_data["LATITUDE"],
                        lon=state_data["LONGITUD"],
                        mode="markers",
                        marker= dict(color='red'),
                        name='Accident Location',
                        locationmode = 'USA-states',)
        )

    # Updating Scattergeo to show the outline of US states with a black color
        fig.update_geos(showsubunits=True, subunitcolor="Black",fitbounds=False)

    # Creating a list of labels, adding a trace for pie/donut chart in row 1; column 2 position
        labels = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        fig.add_trace(go.Pie(labels=labels, values=state_accident_count_list, hole=.6),row=1, col=2)

    # Updating figure layout with different titles, NOTE: the main title dynamically updates the state name as selected by the user
        fig.update_layout(
            geo_scope='usa',
            height = 500,
            width = 900,
            title={
                'text': "<b> Accident Analysis for {} (2010)".format(get_state),
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            showlegend = True,
            annotations= [
                {
                    "font": {
                    "size": 15
                    },
                    "showarrow": False,
                    "text": 'Statewise Accident Location' ,
                    "x": 0.1,
                    "y": 1.0
                },
                {
                    "font": {
                    "size": 15
                    },
                    "showarrow": False,
                    "text": 'Weekday Accident Frequency' ,
                    "x": 0.97,
                    "y": 1.0
                }
            ]
        )

    # Plotting the figures
        map_donut_fig = fig.show()
        return map_donut_fig

    # Setting up except block of statements that will work if existing state code is NOT entered 
    except:
        print("State information is not available")

if __name__ == '__main__':

    # import sys
    # if len(sys.argv) != 2:
    #     print("Usage: python map_donut.py <integer_value>")
    #     sys.exit(1)
    # input_state = int(sys.argv[1])
    # map_donut(input_state)


    parser = argparse.ArgumentParser(
        description="Map & Donut chart generator"
        )
    parser.add_argument("accident_file", help="Path to ACCIDENT_YEAR.csv file")
    parser.add_argument("input_state", help="State code ID ( Use: python3 codes.py)")
    args = parser.parse_args()

    map_donut(args.accident_file, args.input_state)