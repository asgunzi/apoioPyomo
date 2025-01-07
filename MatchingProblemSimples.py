# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:07:12 2025

@author: asgunzi
"""

from pyomo.environ import *


#Valores
arrMatch = [[107, 91, 101],[111, 108, 83],[127, 74, 33]]


nrows = len(arrMatch)
# Exibir as primeiras linhas do DataFrame


arrProib = [[0,0,0],[0,0,0],[1, 0,0]]


#Cria o modelo de matching
model = ConcreteModel()


#Cria sets
rows = range(nrows)
cols = range(nrows)

# Define the decision variables
model.x = Var(rows, cols, within=Binary)


# Define the objective function
def value_rule(model):
    return sum(arrMatch[i][j] * model.x[i,j] for i in rows for j in cols)

model.obj = Objective(rule=value_rule, sense=maximize)


# Define the constraint
#Proibicoes
def proibidos_rule(model,i,j):
    return model.x[i,j] <= (1-arrProib[i][j])
model.proibidos = Constraint(rows, cols, rule=proibidos_rule)

#Máximo por linha
def maxRow_rule(model, i):
    return sum(model.x[i,j] for j in cols) <= 1
model.maxRow= Constraint(rows, rule=maxRow_rule)


#Máximo por coluna
def maxCol_rule(model, j):
    return sum(model.x[i,j] for i in rows) <= 1
model.maxCol= Constraint(cols, rule=maxCol_rule)


solver=SolverFactory('cbc.exe', executable='C:\\CBC\\cbc.exe')

solver.solve(model,tee = True)

# Display the results
print("Display")
model.display() 


print("-----")

obj_value = value(model.obj)
print(f"The objective function value is: {obj_value}")

output =[]
for j in cols:
    for i in rows:
        if value(model.x[i,j]) ==1:
            output.append([i, j])
print("Matches: ", output)