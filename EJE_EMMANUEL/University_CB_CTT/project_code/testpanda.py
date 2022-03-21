import initialize
import random
import hardconstraints
import softconstraints


ttables = []
for d in range(initialize.header.days):
    for t in range(initialize.header.periods):
        ttables.append([d,t])
# print(ttables)
assignments = []
def getCoursedifficulty():
    
    CURRICULAS_CONFLICTS_DIFFICULTY_FACTOR = 1;
    ROOMCOURSEMODE_DIFFICULTY_FACTOR = 1;
    COURSE_LECTURES_DIFFICULTY_FACTOR = 1;
    
    courses_difficulty = []
    for c in initialize.courses:
        # get number of curriculum the course belongs to?
        n_curricula = 0
        for cu in initialize.curricula:
            cur_course=[]
            if c[0] in cu:
                cur_course.append((cu[0],initialize.courses[::]))
                # print(cur_course)
                n_curricula += 1
                # print(n_curricula)
    
        # How many rooms is a course assigned too?
        n_rooms = 0
        for r in initialize.rooms:
            room_courses = []
            if r[2] == "NORM" or r[2] == "PRAC" and c[5] == "NORM" or c[5] == "PRAC":
                if r[2] == c[5]:
                    room_courses.append((c[0],r[0]))
                    # print(room_courses)
                    n_rooms += 1
                    # print(n_rooms)
        x = initialize.courses.index(c)
        # print(x)        
        # Compute the difficulty, based on the number of the course's associated constraints
        courses_difficulty.append((n_curricula * CURRICULAS_CONFLICTS_DIFFICULTY_FACTOR + 
                                 n_rooms * ROOMCOURSEMODE_DIFFICULTY_FACTOR) * max(1,c[2] * COURSE_LECTURES_DIFFICULTY_FACTOR))
        while(0):
            print("Course " +str(c[0])+ " has assignment difficulty = " +str(courses_difficulty[x]))
    return courses_difficulty    

def lec2diffTslot(c,r): 
    for v in ttables:
        for c in initialize.courses:
            for r in initialize.rooms:
                if (c,r) in v:
                    return True
                else:
                    if len(v)<5:
                        return True
                    else:
                        return False
# print(lec2diffTslot(initialize.courses,initialize.rooms))

def curriculumCompactness(c,r):
    # tt = ttables[day],[timeslot]
    for v in ttables:
        for c in initialize.courses:
            for r in initialize.rooms:
                for key,value in initialize.curriculaToCourses.items():
                    if c[0] in value:
                        if (c,r) in v:
                            return True
                        else:
                            if len(v)<5:
                                return True
                            else:
                                return False
                    else:
                        print("course does not exist")
# print(curriculumCompactness(c=initialize.courses,r=initialize.rooms))        

def course_room_mode(c,r):
    # tt = ttables[day],[timeslot]
    for c in initialize.courses:
        for r in initialize.rooms:
            if r[2] == "NORM" or r[2] == "PRAC" and c[5] == "NORM" or c[5] == "PRAC":
                if r[2] == c[5]:
                    continue
                for v in ttables:
                    if (c,r) in v:
                        return True
                    else:
                        if len(v)<5:
                            return True
                        else:
                            return False
                else:
                    return False
# print(course_room_mode(c=initialize.courses,r=initialize.rooms))        
 
def checkFeasibility(course,room):
    return (lec2diffTslot(course,room) and curriculumCompactness(course,room) and course_room_mode(course,room))
# print(checkFeasibility(course=initialize.courses,room=initialize.rooms))        
 
# print(ttables) 

def solution():
    
        for c in initialize.courses:
            cc = c[2]
            for r in initialize.rooms:
                for key,value in initialize.curriculaToCourses.items(): 
                    for v in ttables:
                        ccc = len(initialize.courses)-1
                        course = random.randint(0,ccc)
                        
                        cr = initialize.courses[course][5]
                        courseVal = initialize.courses[course][0]
                        
                        rr = len(initialize.rooms)-1
                        room = random.randint(0,rr)
                        
                        rc = initialize.rooms[room][2]
                        roomVal = initialize.rooms[room][0]
                        if rc == "NORM" or rc == "PRAC" and cr == "NORM" or cr == "PRAC":
                            if rc == cr:
                                # for key,value in initialize.curriculaToCourses.items(): 
                                    if courseVal in value:
                                        if courseVal in v:
                                            return True
                                        else:
                                            if courseVal not in v and len(v) < 8:
                                                ass = str(courseVal) +"."+ str(roomVal)
                                                v.append(ass)
                                                cc -= 1
                                                if cc == 0:
                                                    del c
                                                # print(softconstraints.totalTimetableCost())
                                                print(v)
                
print(solution())
          









# def solution(l,r,d,s):
#     # for c in initialize.courses:
#         # for r in initialize.rooms:
#     x = len(initialize.courses) - 1
#     c=initialize.courses[x][2] 
#     # print(c)   
#     assert(l>=0 and l<c and r>=0 and r<len(initialize.rooms) and d>=0 and d<initialize.header.days and s>=0 and s<initialize.header.periods)
#     ass =assignments[l] 
#     # print(ass)
# # print(solution())

# def sol():
#     # get courses difficulty
#     course_difficulty = getCoursedifficulty()
    
#     # assign a score to each lecture mostly based on courses difficulty
#     # but modified bby a random factor 'ranking_randomnes'
    
#     for e in initialize.courses:
#         x = initialize.courses.index(e)
#         # la = assignments[x]
#         ranking_randomness = random.normalvariate(1,0)
#         difficulty = course_difficulty[x] * ranking_randomness
#         # print(difficulty)
#         while(0):
#             print("Assignment difficulty of Lecture "+str(e)+", "+str(e[0])+ " =" +str(difficulty)+ " (base= " +str(course_difficulty[x])+" rand factor= " +str(ranking_randomness)+")")
    
#     assignments.sort(reverse=True)
    
#     n_assignments = 0
#     n_attempts = 0
    
#     for c in initialize.courses:
#         l = initialize.courses.index(c) -1
#         # la = assignments[initialize.courses[::]]
#         assigned = False
        
#         for r in initialize.rooms:
#             rr = initialize.rooms.index(r)
#             for d in range(initialize.header.days):
#                 for ts in range(initialize.header.days):
#                     while(0):
#                         print("Assignment attempt: Lecture "+str(l)+", "+str(c[0])+ " in room " +str(r[0])+ " on day " +str(d)+" slot " +str(ts))
#                     n_attempts += 1
#                     # print(n_attempts)
                    
#                     if hardconstraints.checkFeasibility(c,(r,ts)):
                    
#                         while(0):
#                             print("Assigned c= "+str(c[0])+ " to (r= "+str(r[0])+ ", day= "+str(d)+", period= "+str(ts))
#                     solution(l,rr,d,ts)
#                     n_assignments+=1
#                     break
                        
# print(sol())
    

# ttable = []
# # for d in range(initialize.header.days):
# #     for t in range(initialize.header.periods):
# #         for x in range(6):
# #             ttable.append([d,t,x])
# #             # print(ttable) 
    

# def lec2diffTslot(c,t):
#     t = ttable 
#     for c in initialize.courses:
#         # print(type(t))
#         return True if c[0] not in t else False
# # print(lec2diffTslot(c=initialize.courses,t=initialize.numberOfPeriods))

# def roomOccupancy(c,t):
#     t = ttable 
#     for r in initialize.rooms:
#         for c in initialize.courses:
#             return True if (c[0],r[0]) not in t else False 
# # print(roomOccupancy(c=initialize.courses,t=initialize.numberOfPeriods))

# def curriculumCompact(c,t):
#     t = ttable 
#     for cu in initialize.curricula:
#         for c in initialize.courses:
#             if c[0] in cu:
#                 return True if c[0] not in t else False
# # print(curriculumCompact(c=initialize.courses,t=initialize.numberOfPeriods))

# def roomcoursemode(c,t):
#     t = ttable 
#     for r in initialize.rooms:
#         for c in initialize.courses:
#             if r[2] == "NORM" or r[2] == "PRAC" and c[5] == "NORM" or c[5] == "PRAC":
#                 if r[2] == c[5]:
#                     return True if c[0] not in r[0] else False
# # print(roomcoursemode(c=initialize.courses,t=initialize.numberOfPeriods))

# def checkFeasibility(course,ts):
#     return (lec2diffTslot(course,ts) and roomOccupancy(course,ts) and curriculumCompact(course,ts) and roomcoursemode(course,ts))
# # print(checkFeasibility(course=initialize.courses,ts=initialize.numberOfPeriods))

# def sol():
    
#     TTable = []

#     for d in range(initialize.header.days):
#         for t in range(initialize.header.periods):
#             for c in initialize.courses:
#                 for r in initialize.rooms:
#                     # ass = str(c[0]) +"."+ str(r[0]) + "."+ str(d) +"."+ str(t)
#                     # cc = random.randint(0,(len(initialize.courses)-1))
#                     # c=initialize.courses[cc][0]
#                     # rr = random.randint(0,(len(initialize.rooms)-1))
#                     # r = initialize.rooms[rr][0]
#                     # t=random.randint(0,initialize.header.periods)
#                     # d = random.randint(0,initialize.header.days)
#                     ass = str(c[0]) +"."+ str(r[0]) + "."+ str(d) +"."+ str(t)
#                     TTable.append(ass)
#                     return TTable if checkFeasibility(course=c,ts=t) is True else False
#                         # cc=c[2]
                        # cc -= 1
                        # c[2] = cc
                        # # print(c[2])
                        # if c[2] == 0:
                        #     continue
                        # else:
                        #     ass = str(c[0]) +"."+ str(r[0]) + "."+ str(d) +"."+ str(t) 
                        #     print(ass)           
    
    # for c in range(len(initialize.courses)):
    #     table = []
    #     dd =  initialize.courses[c][2]
    #     dd -= 1
        
    #     initialize.courses[c][2] = dd
    #     if checkFeasibility(course=c,ts=initialize.header.periods):
    #         if initialize.courses[c][2] == 0:
    #             continue
    #         else:
    #             for d in range(initialize.header.days):
    #                 for t in range(initialize.header.periods):
    #                     for x in range(6):
    #                         # print("Run MF")
    #                         table.append([d,t,x])
    #                         if len(table[x]) < 6:
    #                             # print("Run MF")
    #                             for cr in initialize.courses:
    #                                 for r in initialize.rooms:
    #                                     ch = checkFeasibility(course=cr[0],ts=table[x])
    #                                     if ch:
    #                                         tx = [cr[0],r[0]]
    #                                         print(tx)
                                # if checkFeasibility(course=c,ts=initialize.header.periods):
                                #     # for c in initialize.courses:
                                #     #     for r in initialize.rooms:
                                #     #         tx = c[0],r[0],ttable[d][t][x]
                                #         print("Run MF")
    # for d in range(initialize.header.days):
    #     for t in range(initialize.header.periods):
    #         for x in range(6):
    #             # print("Run MF")
    #             if x < 6:
    #                 # print("Run MF")
    #                 for c in (initialize.courses):
    #                     for r in initialize.rooms:
    #                         dd = c[2]
    #                         dd -= 1
    #                         c[2] = dd
    #                         ch = checkFeasibility(course=c,ts=t)
    #                         print(ch)
    #                         # if checkFeasibility(course=c,ts=t):
    #                             # print("Run MF")
    #                         #     if c[2] == 0:
    #                         #         continue
    #                         #     else:
    #                         #         ass = ((c[0],r[0]))
    #                         #         ttable.append(ass)
    #                         # print(ttable)
                        
# print(sol())



# def sol():
    
#     timeTT = []
    
#     for d in range(initialize.header.days):
#         for t in range(initialize.numberOfPeriods):
#             for c in initialize.courses:
#                 tagCount = 0
#                 for r in initialize.rooms:
#                     if hardconstraints.coursefitTimeslot(course=c,ts=t):
#                         # ass = [str(c[0]) + "." + str(r[0]) + "." + str(t)]
#                         ass = str(c[0]) + "." + str(r[0]) + "." + str(t)
#                         # ass.append(tag)
#                         # print(ass)
#                         # for x in ass:
#                         #     if ass.count(x)>1 :
#                         #         tag += 1
#                         #         ass.append(tag)
#                         #         print(ass)
#                         if c[0] in ass:
#                             tagCount = tagCount + 1
#                             if tagCount == c[2]:
#                                 break
#                             # else:    
#                             print(ass)
#                             print(tagCount)

# # print(sol())

# def listTimeslot(course,listT = False):
#     if listT:
#         count = 0
#         t_list = []
#         for i in range(initialize.numberOfPeriods):
#             if hardconstraints.coursefitTimeslot(course,i):
#                 count += 1
#                 t_list.append(i)
#         return count,t_list
#     else:
#         count = 0
#         for i in range(initialize.numberOfPeriods):
#             if hardconstraints.coursefitTimeslot(course,i):
#                 count += 1
#         return count
    
# # print(listTimeslot(course=initialize.courses,listT=False))

# def availablePositions(course):
#     count = 0
#     for pos in initialize.emptyPosition:
#         if softconstraints.courseFitToPosition(course,pos):
#             count += 1
#     return count
# print(availablePositions(course=initialize.courses))
                        
                    
# # HARD CONSTRAINTS 3 :: ROOM OCCUPANCY :: Two lectures cannot take place in the same room in the same period.

# def roomOccupancy(ev,ts):
#     p = [t for t in range(initialize.numberOfPeriods)]
#     r = [rn for rn in initialize.rooms]
#     # assign = []
    # for x in (r):
    #     for ts in (p):
    #         for ev in initialize.courses:
    #             ass = str(ev[0]) + "."+ str(x[0]) +"."+ str(ts)
    #             # print(ass)
    #             # p.remove(ts)
    #             if x[0] == ass:
    #                 r.remove(x[0])
    #                 print(r)
    #                 p.remove(ts)
    #                 assign.append(ass)
    #             if ass in assign:
    #                 # assign.clear()
    #                 # print(bool(assign))
    #                 return True
                    
    #             # else:
    #                 # return False
    # return False
    # emptyPosition = []
    # for j in r:
    #     for i in range(initialize.numberOfPeriods):
    #         emptyPosition.append((i,j[0]))
    #         # print(emptyPosition)
    #         for c in initialize.courses:
    #             for x in emptyPosition:
    #                 ass = str(c[0]) + "." + str(x)
    #             #     emptyPosition.append(c[0])
    #                 print(ass)
    #                 # if c[0] in emptyPosition:
    #                 #     # emptyPosition += 1
    #                 #     continue
    #                 # else:
    #                 #     emptyPosition.append(c[0])
    #                 #     print(emptyPosition)
# print(roomOccupancy(ev=initialize.courses,ts=initialize.numberOfPeriods))





# tt = []
# def lec2DiffTslot():
#     violations = 0
#     violations_b = 0
#     # cl=[cc for cc in range(len(initialize.courses))]
#     # dl =[dd for dd in range(initialize.header.days)]
#     # tl=[tss for tss in range(initialize.header.periods)]
#     room_usage = []
    
#     for c in initialize.courses:
#         n = 0
#         for r in initialize.rooms:
#             f = room_usage
#             for d in range(initialize.header.days):
#                 for ts in range(initialize.header.periods):
#                     # room_usage.index([cl,dl,tl]) += initialize.timetable.index([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                     tt.append([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                     n += tt.index([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                     if r[0] in range(tt.index([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])):
#                         room_usage.append([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#         delta = c[2] - n
#         if delta > 0:
#             print("H1 [Lectures] violation: %d lectures assigned instead of %d for course '%s'", n,c[2],c[0])
#             violations += delta
#         if not len(f) <= 1:
#             print("H1 [Lectures] violation: %d rooms used for course '%s' at (day=%d, slot=%d)", f,c[0],d,ts)
#             violations_b += 1
#             print(room_usage)
#     return violations + violations_b

# # print(lec2DiffTslot())
# def lecture_violation():
#     return bool(lec2DiffTslot() == 0)
# # print(lecture_violation())

# def room_occupancy():
#     violations = 0
    
#     for r in initialize.rooms:
#         for d in range(initialize.header.days):
#             for ts in range(initialize.header.periods):
#                 n = 0
#                 for c in initialize.courses:
#                     tt.append([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                     n += tt.index([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                 if not n<= 1:
#                     print("H2 [RoomOccupancy] violation: %d courses in room '%s' at day=%d, slot=%d", n,r[0],d,ts)
#                     violations += 1
#     return violations

# def roomOccupancy():
#     return bool(room_occupancy() == 0)
# # print(roomOccupancy())

# def curricula_conflicts():
#     violations = 0
#     for cu in initialize.curricula:
#         cl = [x[1] for x in initialize.curricula ]
#         courses = cu[0],cl
#         for d in range(initialize.header.days):
#             for c in initialize.courses:
#                 for ts in range(initialize.header.periods):
#                     n = 0
                    
#                     for y in cl:
#                         for r in initialize.rooms:
#                             tt.append([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                             n += tt.index([cu[0],str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                     if not n <=1:
#                         print("H3 [Conflicts] violation: %d courses of curriculum '%s' scheduled at day=%d, slot=%d", n, cu[0],d,ts)
#                         violations += 1
#     return violations

# def curriculaConflicts():
#     return bool(curricula_conflicts() == 0)
# # print(curriculaConflicts())

# def room_course_mode():
#     violations = 0
    
#     for r in initialize.rooms:
#         n = 0
#         for d in range(initialize.header.days):
#             for ts in range(initialize.header.periods):
#                 for c in initialize.courses:
#                     if r[2] == "NORM" and c[5] == "NORM" or r[2] == "PRAC" and c[5] == "PRAC":
#                         tt.append([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#                         n += tt.index([str(c[0]) +"."+ str(r[0]) +"."+ str(d) +"."+ str(ts)])
#         if not n<=1:
#             print("H4 [Room and Course Mode] violations: %d rooms used for course '%s' at day=%d and slot=%d", n,c[0],d,ts)
#             violations += 1
#     return violations
# def roomCourseMode():
#     return bool(room_course_mode()==0)
# # print(roomCourseMode())

# def satisfyHardConstraints():
#     h1 = lecture_violation()
#     h2 = roomOccupancy()
#     h3 = curriculaConflicts()
#     h4 = roomCourseMode()
#     return bool(h1 and h2 and h3 and h4)
# # print(satisfyHardConstraints())
            

# def lec2DiffTImeslot(ev,ts):
#     p = [t for t in range(initialize.numberOfPeriods)]
#     # violations = 0
#     assign = []
#     # x = None
#     for ev in initialize.courses:
#         for r in (initialize.rooms):
#             for ts in (p):
#                 ass = [ev[0],r[0],ts]
#                 p.remove(ts)
#                 # print(p)
#                 assign.append(ass)
#                 if ass in assign:
#                     # print(assign)
#                     # assign.clear()
#                     return True
#                     # print(bool(assign))
                    
#                 # else:
#                     # return False
#     return False
                    
# # print(lec2DiffTImeslot(ev=initialize.courses,ts=initialize.numberOfPeriods))

# def curriculaconflicts(ev,ts):
#     p = [t for t in range(initialize.numberOfPeriods)]
#     assign = []
#     for cu in initialize.curricula:
#         for ev in initialize.courses:
#             for r in (initialize.rooms):
#                 for ts in (p):
#                     ass = [ev[0],r[0],ts]
#                     p.remove(ts)
#                     assign.append(ass)
#                     if ev[0] in cu: 
#                         if ass in assign:
#                             # print(assign)
#                             # print(bool(assign))
#                             # del ts
#                             # assign.clear()
#                             return True
                        
#                     # else:
#                         # return False
#     return False
# # print(curriculaconflicts(ev=initialize.courses,ts=initialize.numberOfPeriods))
# def roomOccupancy(ev,ts):
#     p = [t for t in range(initialize.numberOfPeriods)]
#     r = [rn for rn in initialize.rooms]
#     assign = []
#     for x in (r):
#         for ts in (p):
#             for ev in initialize.courses:
#                 ass = [ev[0],x[0],ts]
#                 # print(ass)
#                 p.remove(ts)
#                 # if x[0] in ass:
#                     # r.remove(x[0])
#                     # print(r)
#                 assign.append(ass)
#                 if ass in assign:
#                     # assign.clear()
#                     # print(bool(assign))
#                     return True
                    
#                 # else:
#                     # return False
#     return False
# # print(roomOccupancy(ev=initialize.courses,ts=initialize.numberOfPeriods))
# def course_room_mode(ev,ts):
    # p = [t for t in range(initialize.numberOfPeriods)]
    # r = initialize.rooms
    # assign = []
    # for x in (r):
    #     for ts in (p):
    #         for ev in (initialize.courses): 
    #             # assign = (ev[0],x[0],ts)
    #             if x[2] == "NORM" or x[2] == "PRAC" and ev[5] == "NORM" or ev[5] == "PRAC":
    #                 if x[2] == ev[5]:
    #                     print(x[0],ev[0])
    #                     ass = [ev[0],x[0],ts]
    #                     p.remove(ts)
    #                     assign.append(ass)
    #                     # print(assign)
    #                     if ass in assign:
    #                         # del ts
    #                         # print(bool(assign))
    #                         return True                      
    #                     # else:
    #                         # return (True, ts)
    # return False
# print(course_room_mode(ev=initialize.courses,ts=initialize.numberOfPeriods))
# def coursefitTimeslot(course,ts):
#     return ( lec2DiffTImeslot(course,ts) and curriculaconflicts(course,ts) and roomOccupancy(course,ts) and course_room_mode(course,ts))
# print(coursefitTimeslot(course=initialize.courses,ts=initialize.numberOfPeriods)) 
