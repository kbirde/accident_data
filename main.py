""" This is the main file to run all the other modules"""
import argparse
from map_donut import map_donut
from bar_plot import bar_plot
from codes import codes

# def main():
#     "Main function that gets users state id code input and uses it for plotting information"
    
#     # Get user input
#     print('----------------------------------------------------------')
#     user_input = int(input("Enter state code id: "))

#     # Call the map_donut function with user input
#     map_donut(user_input)

#     # Call the bar_plot function with user input
#     bar_plot(user_input)

# if __name__ == "__main__":
#     codes()
#     main()

def main(accident_file, input_state1, person_file, input_state2):
    "Main function that gets users state id code input and uses it for plotting information"

    # # Get user input
    # print('----------------------------------------------------------')
    # user_input = int(input("Enter state code id: "))

    # Call the map_donut function with user input
    map_donut(accident_file, input_state1)

    # Call the bar_plot function with user input
    bar_plot(person_file, input_state2)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Bar plot and Map / Donut chart generator"
        )
    parser.add_argument("accident_file", help="Path to ACCIDENT_YEAR.csv file")
    parser.add_argument("input_state1", help="State code ID ( Use: python3 codes.py)")
    parser.add_argument("person_file", help="Path to PERSON_YEAR.csv file")
    parser.add_argument("input_state2", help="State code ID ( Use: python3 codes.py)")
    args = parser.parse_args()

    main(args.accident_file, args.input_state1, args.person_file, args.input_state2)