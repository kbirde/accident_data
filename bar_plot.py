"""This module plots a bar chart with a pull down menu from which user can
plot results based on restraint usage """
import argparse
import pandas as pd
import plotly.graph_objects as go
from state_dict import state_dict

def bar_plot(person_file , input_state, year):
    """This function takes user input and plots a pull down bar chart """

    state_dict1 = state_dict

    try:
        get_state_id = int(input_state)
        get_state = state_dict1[get_state_id]

        person_data = pd.read_csv(person_file, encoding='utf-8')
        person_data = person_data[person_data.STATE == get_state_id]
        person_data = person_data.loc[:,["REST_USE",'DEATH_DA']]

        res_used = person_data[(person_data.REST_USE==3) & (person_data.DEATH_DA!=99)]
        fatal_res_used = res_used[res_used.DEATH_DA !=88].shape[0]
        non_fatal_res_used = res_used[res_used.DEATH_DA ==88].shape[0]

        res_not_used = person_data[(person_data.REST_USE==7) & (person_data.DEATH_DA!=99)]
        fatal_res_not_used = res_not_used[res_not_used.DEATH_DA !=88].shape[0]
        non_fatal_res_not_used = res_not_used[res_not_used.DEATH_DA ==88].shape[0]

        year_list = [year]

        fig1 = go.Figure()

        fig1.add_trace(go.Bar(x=year_list, y=[non_fatal_res_used],
         name='Non Fatal, w/ Seatbelts'))
        fig1.add_trace(go.Bar(x=year_list, y=[fatal_res_used],
         name='Fatal, w/ Seatbelts'))
        fig1.add_trace(go.Bar(x=year_list, y=[non_fatal_res_not_used],
         name='Non Fatal, w/o Seatbelts'))
        fig1.add_trace(go.Bar(x=year_list, y=[fatal_res_not_used],
         name='Fatal, w/o Seatbelts'))

        fig1.update_layout(
            updatemenus=[
                {
                    'buttons': [
                        {'label': "All", 'method': "restyle",
                         'args': [{'visible': [True, True, True, True]}, {'type': 'bar'}]},
                        {'label': "Seatbelts Worn", 'method': "restyle",
                         'args': [{'visible': [True, True, False, False]}, {'type': 'bar'}]},
                        {'label': "No Seatbelts", 'method': "restyle",
                         'args': [{'visible': [False, False, True, True]}, {'type': 'bar'}]}
                    ],
                    'direction': "down",
                    'pad': {"r": 10, "t": 10},
                    'showactive': True,
                    'x': 0.0,
                    'xanchor': "left",
                    'y': 1.2,
                    'yanchor': "top"
                }
            ]
        )

        fig1.update_layout(barmode='stack',
            title={'text': f"<b> Effect of Restraints in {get_state} ({year})",
                   'y':0.95, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top'},
            xaxis_title="Year",
            yaxis_title="Occupant Injury",
        )

        return fig1.show()

    except KeyError:
        return print("State information is not available")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Bar plot with pull down menu generator")
    parser.add_argument("person_file", help="Path to PERSON_YEAR.csv file")
    parser.add_argument("input_state", help="State code ID ( Use: python3 codes.py)")
    parser.add_argument("year", help="Enter year of interest")
    args = parser.parse_args()

    bar_plot(args.person_file, args.input_state, args.year)
