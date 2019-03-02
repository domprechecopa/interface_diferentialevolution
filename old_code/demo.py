# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:43:26 2019

@author: cleym
"""

# demo.py

from differential_evolution import DifferentialEvolution
import datetime

import numpy as np
from matplotlib import pyplot as plt

if __name__ == '__main__':
    number_of_runs = 5
    val = 0
    print_time = True

    for i in range(number_of_runs):
        start = datetime.datetime.now()
        de = DifferentialEvolution(num_iterations=200, dim=10, CR=0.4, F=0.48, population_size=75, print_status=False, func='ackley',upper_limit=5.12,lower_limit=-5.12)
        val += de.simulate()
        if print_time:
            print ("\nTime taken: ", datetime.datetime.now() - start)
    print ('-'*80)
    print ("\nFinal average of all runs:", val / number_of_runs)