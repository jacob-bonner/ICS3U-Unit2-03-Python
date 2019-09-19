#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program can calculate the circumference of a circle using TAU

import constants


# This function calculates the circumference of a circle using TAU
def main():

    # Input
    radius = int(input("Enter the radius of the circle here: "))

    # Process
    circumference = constants.TAU*radius

    # Output
    print("")
    print("The circumference is ", circumference, "cm")


if __name__ == "__main__":
    main()
