import initialize
           
####################################
######## HARD CONSTRAINTS ##########
####################################

# H1: LECTURES: all lectures must be scheduled to different timeslot. if two lectures of a course are assigned to a timeslot 
# then it counts as a violation           
           
def lec2diffTslot(c,t):
    # for v in initialize.timetable:
        for x in c:
            for i in range(t):
                if (x[0],i) in initialize.timetable:
                # for val in initialize.timetable.values():
                    # if x[0] in val:
                        return True
                else:
                    if x[0] not in initialize.timetable:
                        return True
                    else:
                            return False
# print(lec2diffTslot(c=initialize.courses,t=initialize.numberOfPeriods))

# H2: Curricula: courses of a curricula should be assigned adjacent to each other.
def curriculumCompactness(c,t):
    for key,value in initialize.curriculaToCourses.items():
        for x in c:
            for i in range(t):
                if x[0] in value:
                    # for v in initialize.timetable:
                        # for val in initialize.timetable.values():
                            if (x[0],i) in initialize.timetable:
                                return True
                            else:
                                if (x[0],i) not in initialize.timetable:
                                    return True
                                else:
                                    return False
# print(curriculumCompactness(c=initialize.courses,t=initialize.numberOfPeriods))

# H3: Course,Room Mode
def course_room_mode(c,t):
    for r in initialize.rooms:
        for x in c:
            for i in range(t):
                if r[2] == "NORM" or  "PRAC" and x[5] == "NORM" or "PRAC":
                    if r[2] == x[5]:
                        # for v in initialize.timetable:
                            # for val in initialize.timetable.values():
                                if x[0] in initialize.timetable:
                                    return True
                                else:
                                    if x[0] not in initialize.timetable:
                                        return True
                                    else:
                                        return False
# print(course_room_mode(c=initialize.courses,t=initialize.numberOfPeriods))


def checkFeasibility(course,timeslot):
    return lec2diffTslot(c=course,t=timeslot) and curriculumCompactness(c=course,t=timeslot) and course_room_mode(c=course,t=timeslot)
# print(checkFeasibility(course=initialize.courses,timeslot=initialize.numberOfPeriods))
