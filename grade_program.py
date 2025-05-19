#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: May 2025
# This program converts a number grade to a percentage using the calc_mark(level) function


def calc_mark(level):
    # This function converts a grade level to a percentage
    if level == "0":
        return 25
    elif level == "1-":
        return 51
    elif level == "1":
        return 55
    elif level == "1+":
        return 58
    elif level == "2-":
        return 61
    elif level == "2":
        return 65
    elif level == "2+":
        return 68
    elif level == "3-":
        return 71
    elif level == "3":
        return 75
    elif level == "3+":
        return 78
    elif level == "4-":
        return 83
    elif level == "4":
        return 91
    elif level == "4+":
        return 98
    else:
        return None


def main():
    # This function gets user input and validates it
    level = input("Enter the level (0-4+): ")

    # Calculate percentage
    percentage = calc_mark(level)

    # Output result
    if percentage is not None:
        print(f"The percentage for level {level} is {percentage}%.")
    else:
        print("Invalid level entered.")


if __name__ == "__main__":
    main()
