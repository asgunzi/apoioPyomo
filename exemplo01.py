# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 05:53:00 2025

@author: ASGUNZI
"""

from pyomo.environ import *

model = ConcreteModel(name = "(H)")


A = ['Scoops', 'Peanuts']


h = {'Scoops': 1, 'Peanuts': 0.1}
d = {'Scoops': 5, 'Peanuts': 27}
c = {'Scoops': 3.14, 'Peanuts': 0.27}
b = 12
u  = {'Scoops': 100, 'Peanuts': 40.6}

def x_bounds(m, i):
    return (0, u[i])

model.x = Var(A, bounds= x_bounds)

def obj_rule(model):
    return sum(h[i]*(model.x[i] - (model.x[i]/d[i])) for i in A)
    
model.z = Objective(rule = obj_rule, sense = maximize)

model.budgetConst = Constraint(expr = sum(c[i]*model.x[i] for i in A) <= b)

#opt = SolverFactory('glpk')
opt = SolverFactory('cbc', executable = "C:\\CBC\\cbc.exe")

results = opt.solve(model)


model.display()
