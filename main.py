""" This is the main file to run all the other modules"""
import argparse
from map_donut import map_donut

def main(accident_file, input_state, year):
    "Main function that gets users state id code input and uses it for plotting information"

    # Call the map_donut function with user input
    map_donut(accident_file, input_state, year)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Bar plot and Map / Donut chart generator"
        )
    parser.add_argument("accident_file", help="Path to ACCIDENT_YEAR.csv file")
    parser.add_argument("input_state", help="State code ID ( Use: python3 codes.py)")
    parser.add_argument("year", help="Enter year of interest")
    args = parser.parse_args()

    main(args.accident_file, args.input_state, args.year)
