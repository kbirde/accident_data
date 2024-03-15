"""This module plots a bar chart with a pull down menu from which user can plot results based on restraint usage """
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from state_dict import state_dict

def bar_plot(input_state):
    """This function takes user input and plots a pull down bar chart """

    # Assign the state_dictionary
    state_dict1 = state_dict

    # Setting up try block of statements that will work if existing state code is entered 
    try:
        
        # Assigning the state input from the user    
        get_state = state_dict1[int(input_state)]
        get_state_id = int(input_state)

        # Reading in PERSON related csv file
        person_data_2010 = pd.read_csv('CSV_DATA/PERSON_2010.csv', encoding='utf-8')

        # Selecting rows based on state entered by the user
        person_data_2010 = person_data_2010[person_data_2010.STATE ==get_state_id]

        # Reducing dataframe to 2 columns of interest
        person_data_2010 = person_data_2010.loc[:,["REST_USE",'DEATH_DA']]

        # Selecting rows with restraints used (code ==3) and dropping unavailable fatality information (code !=99)
        res_used_2010 = person_data_2010[(person_data_2010.REST_USE==3) & (person_data_2010.DEATH_DA!=99)]

        # Downselecting rows with restraints used and fatality (code !=88) and assigning total number via shape[0]
        fatal_res_used_2010 = res_used_2010[res_used_2010.DEATH_DA !=88].shape[0]
        fatal_res_used_2010_list = [fatal_res_used_2010]

        # Downselecting rows with restraints used and non-fatality (code ==88) and assigning total number via shape[0]
        non_fatal_res_used_2010 = res_used_2010[res_used_2010.DEATH_DA ==88].shape[0]
        non_fatal_res_used_2010_list = [non_fatal_res_used_2010]

        # Selecting rows with restraints NOT used (code ==7) and dropping unavailable fatality information (code !=99)
        res_not_used_2010 = person_data_2010[(person_data_2010.REST_USE==7) & (person_data_2010.DEATH_DA!=99)]

        # Downselecting rows with restraints NOT used and fatality (code !=88) and assigning total number via shape[0]
        fatal_res_not_used_2010 = res_not_used_2010[res_not_used_2010.DEATH_DA !=88].shape[0]
        fatal_res_not_used_2010_list = [fatal_res_not_used_2010]

        # Downselecting rows with restraints NOT used and non-fatality (code ==88) and assigning total number via shape[0]
        non_fatal_res_not_used_2010 = res_not_used_2010[res_not_used_2010.DEATH_DA ==88].shape[0]
        non_fatal_res_not_used_2010_list = [non_fatal_res_not_used_2010]

        # Creating year list
        year = ['2010']

        # Creating 4 traces for each combination of fatality/non-fatality data with & without seatbelts for 2010
        trace1 = go.Bar(
            x = year,
            y = non_fatal_res_used_2010_list,
            name='Non Fatal, w/ Seatbelts')

        trace2 = go.Bar(
            x = year,
            y = fatal_res_used_2010_list,
            name='Fatal, w/ Seatbelts')

        trace3 = go.Bar(
            x = year,
            y = non_fatal_res_not_used_2010_list,
            name='Non Fatal, w/o Seatbelts')

        trace4 = go.Bar(
            x = year,
            y = fatal_res_not_used_2010_list,
            name='Fatal, w/o Seatbelts')

        # Creating a list of traces
        data = [trace1, trace2, trace3, trace4]

        # Plotting the figure with the data list specified as the input
        fig1 = go.Figure(data=data)

        # Creating pull down menu buttons
        fig1.update_layout(
            updatemenus=[
                dict(
                    buttons=list([
                        dict(
                            label="All",
                            method="restyle",
                            args = [{'visible': [True, True, True, True]},
                                    {'type':'bar'}]
                        ),
                        dict(
                            label="Seatbelts Worn",
                            method="restyle",
                            args = [{'visible': [True, True, False, False]},
                                    {'type':'bar'}]
                        ),
                        dict(
                            label="No Seatbelts",
                            method="restyle",
                            args = [{'visible': [False, False, True,True]},
                                    {'type':'bar'}]
                        )
                    ]),
                    direction="down",
                    pad={"r": 10, "t": 10},
                    showactive=True,
                    x=0.0,
                    xanchor="left",
                    y=1.2,
                    yanchor="top"
                ),
            ]
        )

        # Specifying stacked bar char adding titles
        fig1.update_layout(barmode='stack',
            title={
                    'text': "<b> Effect of Restraints in {} (2010)".format(get_state),
                    'y':0.95,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
            xaxis_title="Year",
            yaxis_title="Occupant Injury",
            )
        
        # Plotting the figures
        bar_fig = fig1.show()

        return bar_fig

    # Setting up except block of statements that will work if existing state code is NOT entered 
    except:
        print("State information is not available")

if __name__ == '__main__':

    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 bar_plot.py <integer_value>")
        sys.exit(1)
    input_value = int(sys.argv[1])
    bar_plot(input_value)