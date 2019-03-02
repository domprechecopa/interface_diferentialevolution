# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:59:59 2019

@author: cleym
"""

from helpers.point import Point
from helpers.population import Population
from helpers.test_functions import Function


def get_best_point(points):
    best = sorted(points, key=lambda x:x.z)[0]
    return best


if __name__ == '__main__':
	pass