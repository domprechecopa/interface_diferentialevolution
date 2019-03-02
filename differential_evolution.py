# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:42:09 2019

@author: cleym
"""

# differential_evolution.py

import copy
import random
import time

from helpers.population import Population
from helpers.__init__ import get_best_point
from helpers.test_functions import Function
import matplotlib.pyplot as plt
from helpers.strategy import Strategy
#import seaborn as sns


class DifferentialEvolution(object):
    def __init__(self, num_iterations=10, CR=0.4, F=0.48, dim=2, population_size=10, print_status=False, visualize=False, func=None,upper_limit=10,lower_limit=-10,printar = None):
        if func == '':
            func = None
        self.printar = printar
        
        random.seed()
        self.print_status = print_status
        self.visualize = visualize
        self.num_iterations = num_iterations
        self.iteration = 0
        self.CR = CR
        self.F = F
        self.population_size = population_size
        self.func = Function(func=func)
        self.upper_limit = upper_limit
        self.lower_limit = lower_limit
        self.population = Population(dim=dim, num_points=self.population_size,upper_limit = self.upper_limit,lower_limit=self.lower_limit,  objective=self.func)
        self.strategy = Strategy(ppoints=self.population.points, cost = self.population.cost)
    def iterate(self):
        for ix in range(self.population.num_points):
            x = self.population.points[ix]
            [a, b, c, d, e] = random.sample(self.population.points, 5)
            while x == a or x == b or x == c or x == d:
                [a, b, c, d, e] = random.sample(self.population.points, 5)

            x1 = {'a' : a, 'b' : b, 'c' : c, 'd' : d, 'e' : e}
            y = copy.deepcopy(x)

            self.strategy.strategy(x, y, x1, self.CR,self.F)

            y.evaluate_point()
            if y.z < x.z:
                self.population.points[ix] = y
        self.iteration += 1

    def simulate(self, runner):
        all_vals = []
        avg_vals = []
        pnt = get_best_point(self.population.points)
        all_vals.append(pnt.z)
        avg_vals.append(self.population.get_average_objective())
        self.printar("Initial best value: " + str(pnt.z))
        while self.iteration < self.num_iterations:
            if self.print_status == True and self.iteration%50 == 0:
                pnt = get_best_point(self.population.points)
                self.printar ("{} {}".format(pnt.z, self.population.get_average_objective()))
            self.iterate()
            all_vals.append(get_best_point(self.population.points).z)
            avg_vals.append(self.population.get_average_objective())
            if self.visualize == True and self.iteration%2==0:
                self.population.get_visualization()
        # sns.figure(0)
        plt.figure()
        plt.plot(all_vals, 'r', label='Best')
        plt.plot(avg_vals, 'g', label='Average')
        plt.grid(True, linestyle='-.')
        plt.legend()
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        plt.title(self.func.func_name + ', ' + str(self.population.dim) + '-D')
        plt.savefig("graphics/graph_run_{}.jpeg".format(runner+1))
        
        pnt = get_best_point(self.population.points)
        self.printar("Final best value: " + str(pnt.z))
        return pnt.z





#if __name__ == '__main__':
#    number_of_runs = 1
#    val = 0
#    print_time = True
#
#    for i in range(number_of_runs):
#        start = time.clock()
#        de = DifferentialEvolution(num_iterations=500, dim=50, CR=0.4, F=0.48, population_size=75, print_status=False, func='rastrigin')
#        val += de.simulate()
#        if print_time:
#            print("")
#            print(time.clock() - start)
#
#    print(("Final average of all runs: "), (val / number_of_runs))