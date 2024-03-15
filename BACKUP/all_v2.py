import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

# # Print the state ID codes
# print("The image shows the state ID that you can choose from:")
# image_path = 'MISC/state_code.PNG'

# # Open the image file
# img = Image.open(image_path)

# # Display the image
# img.show()

# Reading in the state input from the user    
input_state = input("Enter the STATE you are interested in : ")

# Dictionary containing list of states and their code ID's as per the User's Manual
state_dict = {1:'Alabama',2: 'Alaska', 4: 'Arizona',5: 'Arkansas',6: 'California',8: 'Colorado',9: 'Connecticut',10: 'Delaware',
             11: 'District of Columbia',12: 'Florida',13: 'Georgia',15: 'Hawaii',16: 'Idaho',17: 'Illinois',18: 'Indiana',
             19: 'Iowa',20: 'Kansas',21: 'Kentucky',22: 'Louisiana',23: 'Maine',24: 'Maryland',25: 'Massachusetts',
             26: 'Michigan',27: 'Minnesota',28: 'Mississippi',29: 'Missouri',30: 'Montana',31: 'Nebraska',32: 'Nevada',
             33: 'New Hampshire',34: 'New Jersey',35: 'New Mexico',36: 'New York',37: 'North Carolina',38: 'North Dakota',
             39: 'Ohio',40: 'Oklahoma',41: 'Oregon',42: 'Pennsylvania',43: 'Puerto Rico',44: 'Rhode Island',45: 'South Carolina',
             46: 'South Dakota',47: 'Tennessee',48: 'Texas',49: 'Utah',50: 'Vermont',51: 'Virginia',52: 'Virgin Islands',
             53: 'Washington',54: 'West Virginia',55: 'Wisconsin',56: 'Wyoming'}

# Setting up try block of statements that will work if existing state code is entered 
try:

    # Assigning the state input from the user    
    get_state = state_dict[int(input_state)]
    get_state_id = int(input_state)

    # Reading in 2010 ACCIDENT data, downselecting the rows related to the user's state choice & reducing the dataframe to 4 columns
    data_2010 = pd.read_csv('CSV_DATA/ACCIDENT_2010.csv', encoding='utf-8')
    state_data_2010 = data_2010[data_2010.STATE ==get_state_id]
    state_data_2010= state_data_2010.loc[:,['DAY_WEEK','HOUR','LATITUDE','LONGITUD']]
    state_accident_count = state_data_2010.groupby(['DAY_WEEK']).count()
    state_accident_count_list = state_accident_count['HOUR'].tolist()

    # Setting up a subplot with 1 row and 2 columns, specifying that the first column is a scattergeo map and the second column is a pie chart
    fig = make_subplots(rows=1, cols=2,
                        column_widths=[0.6,0.4],
                        row_heights=[0.4],
                        specs=[[{"type": "scattergeo"}, {"type": "pie"}]])

    # Adding a Scattergeo trace with latitude, longitude, marker (w/ color), title & focusing map to USA region
    fig.add_trace(
        go.Scattergeo(lat=state_data_2010["LATITUDE"],
                        lon=state_data_2010["LONGITUD"],
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
    fig.show()

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

    # Printing Fatality with seatbelts, Non-fatality with seatbelts, Fatality without seatbelts & Non-fatality without seatbelts
    print(fatal_res_used_2010,non_fatal_res_used_2010,fatal_res_not_used_2010,non_fatal_res_not_used_2010)

    # Creating 4 traces for each combination of fatality/non-fatality data with & without seatbelts for 2010 - 2018
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
    fig = go.Figure(data=data)

    # Creating pull down menu buttons
    fig.update_layout(
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
    fig.update_layout(barmode='stack',
        title={
                'text': "<b> Effect of Restraints in {} (2010)".format(get_state),
                'y':0.95,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
        xaxis_title="Year",
        yaxis_title="Occupant Injury",
        )

    fig.show()

# Setting up except block of statements that will work if existing state code is NOT entered 
except:
    print("State information is not available")