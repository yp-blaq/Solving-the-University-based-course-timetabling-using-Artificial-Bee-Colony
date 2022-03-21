import initialize
import hardconstraints
import softconstraints
import timeit
import sys
import random


def solution():
    for c in initialize.courses:
        for r in initialize.rooms:
            # for d in range(initialize.header.days):
            #     for p in range(initialize.header.periods):
            # for v in initialize.timetable.values():
                    ccc = len(initialize.courses)-1
                    course = random.randint(0,ccc)
                    ccr = initialize.courses[course][2]              
                    cr = initialize.courses[course][5]
                    courseVal = initialize.courses[course][0]
                                    
                    rr = len(initialize.rooms)-1
                    room = random.randint(0,rr)                
                    rc = initialize.rooms[room][2]
                    roomVal = initialize.rooms[room][0]
                    
                    days = random.randint(0,initialize.header.days)
                    timeslot = random.randint(0,initialize.header.periods)
                    if hardconstraints.checkFeasibility(course=initialize.courses,timeslot=initialize.numberOfPeriods):
                        if rc == "NORM" or rc == "PRAC" and cr == "NORM" or cr == "PRAC":
                            if rc == cr:
                                    ass = str(courseVal)+"."+str(roomVal)+"."+str(days)+"."+str(timeslot)
                                    # print(ass)
                                    initialize.timetable.append(ass)
                                    # print(v)
                                    cost =softconstraints.totalTimetableCost()
                                    ccr -= 1
                                    if ccr == 0:
                                        del course
                                    print(ass)
                                    
    return cost


# print(solution())
file_path =r'C:\Users\Blaq\Documents\EJE_EMMANUEL\University_CB_CTT\project_code\solutions\initial_solution\initialsol1.txt'
sys.stdout= open(file_path, "w")
# print(initialize.header)
print(solution())
# print("Total Cost: ", softconstraints.totalTimetableCost())
# print(timetable)

stopTime = timeit.default_timer()
print("Time Taken: ",stopTime - initialize.starting_time)

sys.stdout.close()