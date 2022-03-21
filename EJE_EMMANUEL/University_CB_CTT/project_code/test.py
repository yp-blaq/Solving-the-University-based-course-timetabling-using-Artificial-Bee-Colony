# import initialize
# import random

# timetable = []
# for d in range(initialize.header.days):
#     for t in range(initialize.header.periods):
#         timetable.append([d,t])

# # print(timetable)

# def lec2diffTslot(c):
#     for v in timetable:
#         for x in c:
#             if x[0] in v:
#                 return True
#             else:
#                 if x[0] not in v:
#                     return True
#                 else:
#                     return False
# # print(lec2diffTslot(c=initialize.courses))

# def curriculumCompactness(c):
#     for key,value in initialize.curriculaToCourses.items():
#         for x in c:
#             if x[0] in value:
#                 for v in timetable:
#                     if x[0] in v:
#                         return True
#                     else:
#                         if x[0] not in v:
#                             return True
#                         else:
#                             return False
# # print(curriculumCompactness(c=initialize.courses))

# def course_room_mode(c):
#     for r in initialize.rooms:
#         for x in c:
#             if r[2] == "NORM" or  "PRAC" and x[5] == "NORM" or "PRAC":
#                 if r[2] == x[5]:
#                     for v in timetable:
#                         if x[0] in v:
#                             return True
#                         else:
#                             if x[0] not in v:
#                                 return True
#                             else:
#                                 return False
# # print(course_room_mode(c=initialize.courses))


# def checkFeasibility(course):
#     return lec2diffTslot(c=course) and curriculumCompactness(c=course) and course_room_mode(c=course)
# # print(checkFeasibility(course=initialize.courses))

# def sol():
#     for v in timetable:
#         ccc = len(initialize.courses)-1
#         course = random.randint(0,ccc)
#         ccr = initialize.courses[course][2]              
#         # cr = initialize.courses[course][5]
#         courseVal = initialize.courses[course][0]
                        
#         rr = len(initialize.rooms)-1
#         room = random.randint(0,rr)                
#         # rc = initialize.rooms[room][2]
#         roomVal = initialize.rooms[room][0]
        
#         checkFeasibility(initialize.courses)
#         print(courseVal,roomVal)
        
        
# print(sol())


# # def lec2diffTslot(c):
# #     tt = timetable[(i[0],j)]
# #     for c in initialize.courses:
# #         if c in tt:
# #             return True
# #         else:
# #             if len(tt)< 5:
# #                 return True
# #             else:
# #                 return False
# # # print(lec2diffTslot(c=initialize.courses))

# # def curriculumCompactness(c):
# #     tt = timetable[(i[0],j)]
# #     for keys,value in initialize.curriculaToCourses.items():
# #         # print(value)
# #         for c in initialize.courses:
# #             if c[0] in value:
# #                 # print(c[0],keys)
# #                 if c in tt:
# #                     return True
# #                 else:
# #                     if len(tt)<5:
# #                         return True
# #                     else:
# #                         return False
# #             else:
# #                 print("course does not exist")
# # # print(curriculumCompactness(c=initialize.courses))

# # def course_room_mode(c):
# #     tt =timetable[(i[0],j)]
# #     for r in initialize.rooms:
# #         for c in initialize.courses:
# #             if r[2] == "NORM" or  "PRAC" and c[5] == "NORM" or "PRAC":
# #                 if r[2] == c[5]:
# #                     # print(c[0],r[0])
# #                     # for r[2] in c[5]:
# #                     #     print(r[0],c) 
# #                     if c[0] in tt:
# #                         return True
# #                     else:
# #                         if len(tt)<5:
# #                             return True
# #                         else:
# #                             return False
# #             # else:
# #             #     return False
# # # print(course_room_mode(c=initialize.courses))        

# # def checkFeasibility(c):
# #     return (lec2diffTslot(c) and curriculumCompactness(c) and course_room_mode(c))
# # # print(checkFeasibility(c=initialize.courses))      
 
# # # print(timetable)

# # def sol():
    
# #     for key,value in timetable.items():
# #         for course in initialize.courses:
# #             # cc = course[2]
# #             if lec2diffTslot(course) and curriculumCompactness(course) and course_room_mode(course):
# #                 # print(course)
# #                 value.append(course)
# #                 print(timetable)
# #                 # print(course[0])
    
# # # print(sol())
# # # print(initialize.timetable_data) 

import initialize
import os
# import construct

# initialSolution = []
# os.chdir(r'C:\Users\Blaq\Documents\EJE_EMMANUEL\University_CB_CTT\project_code\solutions\initial_solution')

# with open('initialsol1.txt','r')as f:
#     for line in f:
#         line = line[:-1] 
#         initialSolution.append(line) 
# f.close()


class FoodSource(object):
    trials = 0

    """docstring for FoodSource"""
    def __init__(self, initial_solution, initial_fitness):
        super(FoodSource, self).__init__()

        self.solution = initial_solution
        self.fitness = initial_fitness

    def __repr__(self):
        return f'<FoodSource s:{self.solution} f:{self.fitness} />'


class ABC(object):
    
    food_sources = []
    
    def __init__(self,npopulation,nruns,fn_eval,trials_limit = 50,employed_bees_percent = 0.5, fn_lb = [-5,-5],fn_ub=[5,5]):
        super(ABC, self).__init__()
        self.npopulation = npopulation
        self.nruns = nruns
        self.fn_eval = fn_eval
        self.trials_limit = trials_limit
        self.fn_lb = list(fn_lb)
        self.fn_ub = list(fn_ub)

        self.employed_bees = round(npopulation * employed_bees_percent)
        self.onlooker_bees = npopulation - self.employed_bees
        
    def optimize(self):
        self.initialize()
        print(self.food_sources)
        
        for nrun in range(1,self.nruns+1):
            self.employed_bees_stage()
            self.onlooker_bees_stage()
            self.scout_bees_stage()
            
        print(self.food_sources)
        best_fs = self.best_source()
        return best_fs.solution
    
    def initialize(self):
        self.food_sources = [self.create_foodsource() for i in range(self.employed_bees)]
        
    def employed_bees_stage(self):
        for i in range(self.employed_bees):
            food_source = self.food_sources[i]
            new_solution = self.generate_solution(i)
            best_solution = self.best_solution(food_source.solution, new_solution)
            
            self.set_solution(food_source,best_solution)
            
    def onlooker_bees_stage(self):
        for i in range(self.onlooker_bees):
            probabilities = [self.probability(fs) for fs in self.food_sources]
            selected_index = self.selection(range(len(self.food_sources)), probabilities)
            selected_source = self.food_sources[selected_index]
            new_solution = self.generate_solution(selected_index)
            best_solution = self.best_solution(selected_source.solution, new_solution)
            
            self.set_solution(selected_source, best_solution)

    def scout_bees_stage(self):
        for i in range(self.employed_bees):
            food_source = self.food_sources[i]

            if food_source.trials > self.trials_limit:
                food_source = self.create_foodsource()


    def generate_solution(self, current_solution_index):
        solution = self.food_sources[current_solution_index].solution
        k_source_index = self.random_solution_excluding([current_solution_index])
        k_solution = self.food_sources[k_source_index].solution
        d = random.randint(0, len(self.fn_lb) - 1)
        r = random.uniform(-1, 1)

        new_solution = np.copy(solution)
        new_solution[d] = solution[d] + r * (solution[d] - k_solution[d])

        return np.around(new_solution, decimals=4)

    def random_solution_excluding(self, excluded_index):
        available_indexes = set(range(self.employed_bees))
        exclude_set = set(excluded_index)
        diff = available_indexes - exclude_set
        selected = random.choice(list(diff))

        return selected

    def best_solution(self, current_solution, new_solution):
        if self.fitness(new_solution) > self.fitness(current_solution):
            return new_solution
        else:
            return current_solution

    def probability(self, solution_fitness):
        fitness_sum = sum([fs.fitness for fs in self.food_sources])
        probability = solution_fitness.fitness / fitness_sum

        return probability

    def fitness(self, solution):
        result = self.fn_eval(solution)

        if result >= 0:
            fitness = 1 / (1 + result)
        else:
            fitness = abs(result)

        return fitness

    def selection(self, solutions, weights):
        return random.choices(solutions, weights)[0]

    def set_solution(self, food_source, new_solution):
        if np.array_equal(new_solution, food_source.solution):
            food_source.trials += 1
        else:
            food_source.solution = new_solution
            food_source.trials = 0

    def best_source(self):
        best = max(self.food_sources, key=attrgetter('fitness'))

        return best

    def create_foodsource(self):
        solution = self.candidate_solution(self.fn_lb, self.fn_ub)
        fitness = self.fitness(solution)

        return FoodSource(solution, fitness)

    def candidate_solution(self, lb, ub):
        r = random.random()
        solution = lb + (ub - lb) * r

        return np.around(solution, decimals=4)

