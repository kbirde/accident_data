""" This is the main file to run all the other modules"""
from map_donut import map_donut
from bar_plot import bar_plot
from codes import codes

def main():
    "Main function that gets users state id code input and uses it for plotting information"
    
    # Get user input
    print('----------------------------------------------------------')
    user_input = int(input("Enter state code id: "))

    # Call the map_donut function with user input
    map_donut(user_input)

    # Call the bar_plot function with user input
    bar_plot(user_input)

if __name__ == "__main__":
    codes()
    main()