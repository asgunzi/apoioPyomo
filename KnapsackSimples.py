# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 05:17:26 2025

@author: ASGUNZI
"""

from pyomo.environ import *

# Define the data
values = {'hammer': 8, 'wrench': 3, 'screwdriver': 6, 'towel': 11}
weights = {'hammer': 5, 'wrench': 7, 'screwdriver': 4, 'towel': 3}
weight_limit = 14

# Create a concrete model
model = ConcreteModel()

# Define the set of items
model.ITEMS = Set(initialize=values.keys())

# Define the decision variables
model.x = Var(model.ITEMS, within=Binary)

# Define the objective function
def value_rule(model):
    return sum(values[i] * model.x[i] for i in model.ITEMS)
model.value = Objective(rule=value_rule, sense=maximize)

# Define the constraint
def weight_rule(model):
    return sum(weights[i] * model.x[i] for i in model.ITEMS) <= weight_limit
model.weight = Constraint(rule=weight_rule)

# Solve the problem
#solver = SolverFactory('glpk')
solver=SolverFactory('cbc.exe', executable='C:\\CBC\\cbc.exe')

solver.solve(model)

# Display the results
model.display()
