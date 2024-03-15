"""This module provides a list of state code ids to the user"""
import argparse
import pandas as pd
from state_dict import state_dict

def codes():
    """This function displays the state ids as a Dataframe table """

    # Assign the state_dictionary
    state_dict1 = state_dict

    # Create a Dataframe
    codes_df = pd.DataFrame(state_dict1.items(), columns=['State_Code', 'State_Name'])

    # Split the DataFrame into two parts
    df_part1 = codes_df.iloc[:27].reset_index(drop=True)
    df_part2 = codes_df.iloc[27:].reset_index(drop=True)

    # Concatenate the two parts horizontally
    df_combined = pd.concat([df_part1, df_part2], axis=1)

    # Fill NaN values with empty string
    df_combined = df_combined.fillna('')

    # return print(codes_df.to_string(index=False))
    return print(df_combined.to_string(index=False))

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Choose the state code to be entered:"
        )
    args = parser.parse_args()

    codes()    

