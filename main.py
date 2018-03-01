#!/usr/bin/env python3
"""Solver for the Google Hash Code 2018 Challenge.

Usage: main.py [strategy]
"""

import sys
import os
from simulation import Simulation

# List of how many arguments are expected
# e.g. [1, 2] means that there may be 1 or 2 arguments
__numberOfArguments = [0, 1]

if __name__ == "__main__":
    # Check if number of arguments matches. +1 is needed for the filename
    if len(sys.argv) not in [i + 1 for i in __numberOfArguments]:
        print(__doc__)
        sys.exit(-1)

    try:
        strategy = sys.argv[1]
    except IndexError:
        strategy = 'BasicStrategy'

    for input_file in os.listdir('datasets'):
        if input_file.endswith('in'):
            simulation = Simulation(input_file, strategy)
            simulation.run()