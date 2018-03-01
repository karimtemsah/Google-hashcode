import sys

from .io import input, output

# Import strategy list
from .strategy import __all__
# Import all strategies
from .strategy import *

class Simulation:

    def __init__(self, input_file, strategy):
        self.input_file = 'datasets/{}.in'.format(input_file)
        print('Running simulation!')
        print('Using strategy: {}'.format(strategy))
        print('Using dataset: {}'.format(self.input_file))
        print('')

        if strategy in __all__:
            self.strategy = eval(strategy)()
        else:
            print('Strategy does not exist!')
            sys.exit(-1)

    def run(self):
        # Read in the Input File
        input.read(self.input_file)
        
        # Run the Simulation
        self.strategy.run()
        output_data = 'Test'

        # Create the Output file
        output_file = '{}.out'.format(self.input_file[:-3])
        output.write(output_file, output_data)