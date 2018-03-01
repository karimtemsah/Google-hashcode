#!/usr/bin/env python3
"""Solver for the Google Hash Code 2018 Challenge.

Usage: main.py problem_statement [strategy]

The problem statement should exist in the datasets folder. Use the name of the
problem statement without the .in ending.
"""

import sys
from simulation import Simulation

# List of how many arguments are expected
# e.g. [1, 2] means that there may be 1 or 2 arguments
__numberOfArguments = [1, 2]

if __name__ == "__main__":
    # Check if number of arguments matches. +1 is needed for the filename
    if len(sys.argv) not in [i + 1 for i in __numberOfArguments]:
        print(__doc__)
        sys.exit(-1)

    input_file = sys.argv[1]

    try:
        strategy = sys.argv[2]
    except IndexError:
        strategy = 'BasicStrategy'

    simulation = Simulation(input_file, strategy)
    simulation.run()