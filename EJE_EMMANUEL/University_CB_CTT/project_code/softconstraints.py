import initialize
import hardconstraints

# Soft Constraints: RoomCapacity : for each lecture the number of students that attend the course must be less than or
# equal too the number of seats in the room hosting the lecture

def roomCapacity(c,r):
    courseCap = []
    roomCap = []
    
    for c in initialize.courses:
        courseCap.append(c[4])
    for r in initialize.rooms:
        roomCap.append(r[1])
    return ((len(courseCap) - len(roomCap)) * initialize.RoomCapacityPenalty)
# print(roomCapacity(c=initialize.courses,r=initialize.rooms))

def courseFitsIntoPosition(course, position):
    room, ts = position
    return hardconstraints.checkFeasibility(course, ts) and roomCapacity(course, room) == 0


def roomCapacityTimeslot(event, timeslot):
    """
    returns the penalty of the RoomCapacity soft constraint for a single timeslot
    """
    penalty = 0
    for r in range(initialize.numberOfRooms):
        ev = initialize.timetable.keys()
        if ev is not None and ev == event:
            penalty += roomCapacity(event, r)

    return penalty
# print(roomCapacityTimeslot(initialize.courses,initialize.numberOfPeriods))


def roomCapacityAll():
    allMapping = {}
    for pos in initialize.timetable:
        ev = initialize.timetable
        # print(ev)
        
        if ev is not None:
            try:
                allMapping[tuple(ev)] += roomCapacity(ev,pos[0])
            except:
                allMapping[tuple(ev)] = roomCapacity(ev,pos[0])
                    
                
                
    penalty = 0
    for value in allMapping.values():
        penalty += value
    return penalty
# print(roomCapacityAll())


# Soft Constraints: Minimum Working Days: The lectures of each course must be spread into the given minimum number of days

def minWorkingDays(ev):
    for x in ev:
        event = x[3]
        # print(event)
    
    workingdays = 0
    for d in initialize.days:
        for ts in d:
            if hardconstraints.lec2diffTslot(ev,ts):
                workingdays += 1
                break

    return max(event - workingdays,0) * initialize.MinWorkingDays
# print(minWorkingDays(ev=initialize.courses))

# Soft Constraints: Curriculum Compactness: Lectures belonging to a curriculum should be adjacent to each
# other (i.e., in consecutive periods).

def curriculumCompactness(cur):
    allMapping = []
    # coursewithCurriculum = curriculaToCourses[cur.id]

    for cur in initialize.curriculaToCourses:
        coursewithCurriculum = initialize.curriculaToCourses[cur]
    
    for d in initialize.days:
        daily = []
        for ts in d:
            # checks if any course in the curriculum exists in the timeslot
            if any([hardconstraints.lec2diffTslot(initialize.getCourseFromCourseName(ev),ts) for ev in coursewithCurriculum]):
                    daily.append(True)
            else:
                daily.append(False)
        allMapping.append(daily)
        
    # we are returning violation penalty
    penalty = 0
    # checking for each day if an isolated lecture occurs
    for anyday in allMapping:
        for i, timeslotHasRelevantLecture in enumerate(anyday):
            if timeslotHasRelevantLecture:
                # account for first and last timeslot of the day
                if i == 0:
                    previousHasRelevantLecture = False
                else:
                    previousHasRelevantLecture = anyday[i - 1]
                try:
                    followingHasRelevantLecture = anyday[i + 1]
                except:
                    followingHasRelevantLecture =  False
                if not (previousHasRelevantLecture or followingHasRelevantLecture):
                    penalty += 1    
    return penalty * initialize.IsolatedLectures
# print(curriculumCompactness(cur=initialize.curricula))

# Soft Constraint: Room Stability: : All lectures of a course should be given in the same room.

def roomStability(event):
    penalty = 0
    assignedRooms = []
    
    for pos in initialize.timetable:
        ev = initialize.timetable
        if ev is not None and ev == event:
            room = pos[0]
            if room not in assignedRooms:
                assignedRooms.append(room)
                penalty += 1
                
    # substract 1 for the first room that has been used
    penalty -= 1
    
    return penalty * initialize.RoomStability
# print(roomStability(event=initialize.courses))

def totalTimetableCost():
    total_cost= roomCapacityAll()
    cost2 = minWorkingDays(initialize.courses)
    cost3 = roomStability(initialize.courses)
    cost4 = curriculumCompactness(initialize.curricula)
    total_cost += cost2 + cost3 + cost4
    # total_cost = roomCapacityAll()
    # for c in initialize.courses:
    #     # total_cost += minWorkingDays(c)
    #     print(minWorkingDays(ev=c))
    # #     total_cost += roomStability(c)
    # # for cu in initialize.curricula:
    # #     total_cost += curriculumCompactness(cu)
    
    return total_cost

# tc = totalTimetableCost()
# print("Total Cost: " +str(tc))

