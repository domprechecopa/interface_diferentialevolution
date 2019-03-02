# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:40:58 2019

@author: cleym
"""

# helpers/population.py

import copy
import numpy as np
from matplotlib import pyplot as plt

from helpers.point import Point
from matplotlib import pyplot as plt

class Population:
    def __init__(self, dim=2, num_points=50, upper_limit=10, lower_limit=-10, init_generate=True, objective=None):
        self.points = []
        self.cost = []
        self.num_points = num_points
        self.init_generate = init_generate
        self.dim = dim
        self.range_upper_limit = upper_limit
        self.range_lower_limit = lower_limit
        self.objective = objective
        # If initial generation parameter is true, then generate collection
        if self.init_generate == True:
            for ix in range(num_points):
                new_point = Point(dim=dim, upper_limit=self.range_upper_limit,
                                  lower_limit=self.range_lower_limit, objective=self.objective)
                new_point.generate_random_point()
                self.cost.append(float(new_point.z))
                self.points.append(new_point)

    def get_average_objective(self):
        avg = 0.0

        for px in self.points:
            avg += px.z
        avg = avg/float(self.num_points)
        return avg