import os
import random
import numpy as np
import initialize
import softconstraints
# initialSolution = []
# os.chdir(r'C:\Users\Blaq\Documents\EJE_EMMANUEL\University_CB_CTT\project_code\solutions\initial_solution')

# with open('initialsol1.txt','r')as f:
#     for line in f:
#         line = line[:-1] 
#         initialSolution.append(line) 
# f.close()

# def read_file():
#     global initialSolution
#     sol = []
#     os.chdir(r'C:\Users\Blaq\Documents\EJE_EMMANUEL\University_CB_CTT\project_code\solutions\initial_solution')

#     with open('initialsol1.txt','r')as f:
#         for line in f:
#             line = line[:-1] 
#             sol.append(line) 
    
#     for x in sol:
#         initialSolution = x
#         # print(initialSolution)
# # print(read_file())

# def initialization():
#     """Random Initialization of food source"""
#     for 

# class ABC:
#     def __init__(self, objectiveFunc: softconstraints.totalTimetableCost, trial = 10, colonySize = 50, iter = 100):
#         self.cs = colonySize
#         self.objFunc = objectiveFunc
#         self.trial = trial
#         self.iteration = iter

n_population = 100
food_number = (n_population/2)
limit = 100

