# importing all modeules 
import os
import timeit


# penalty weights according to the UD specification by (De Cesco, Di Gaspero, Schaerf, 2012)
# UD2 (= ITC-2) specs: 1-5-2-1
RoomCapacityPenalty = 1
MinWorkingDays = 5
IsolatedLectures = 2
RoomStability = 1

starting_time = timeit.default_timer()

# loading the dataset file
timetable_data = []
os.chdir(r'C:\Users\Blaq\Documents\EJE_EMMANUEL\University_CB_CTT\project_code\datasets')
with open('100lvl.txt') as TTdata:
    for line in TTdata:
        line = line[:-1]    #taking after every last character in a line as a new line
        timetable_data.append(line) # then appending them to the empty timetable data list
TTdata.close()

# print(timetable_data)

# this function is used to prepare the data by splitting the raw list into sections
# and the section strings into list
def prepare_data(section_name):
    """
    prepares the raw data for the algo:
    splits the raw list into sections,
    splits the section string into a list,
    turns number strings into integers
    """
    if section_name == "HEADER":
        start = 0
    else:
        start = timetable_data.index(section_name) + 1 # don't include the section name in the list
    stop = timetable_data.index("", start)
    tmp_section = timetable_data[start:stop]
    section = []
    for i in tmp_section:
        part = i.split()
        part2 = []
        for element in part:
            try:
                e = int(element)
            except:
                e = element
            finally:
                part2.append(e)
        section.append(part2)
    return section
        
# Header
# Section "HEADER:"
# used to read the first 8 lines of the dataset
header1 = prepare_data("HEADER")


class Header:
    def __init__(self, header):
        self.name = header[0][1].lower()
        self.courses = header[1][1]
        self.rooms = header[2][1]
        self.days = header[3][1]
        self.periods = header[4][1]
        self.curricula = header[5][1]
        
        

    def __repr__(self):
        return "<Name: {}, courses: {}, rooms: {}, days {}>".format(self.name, self.courses, self.rooms, self.days)


header = Header(header1)
# print(header)

# list of courses
# section "COURSES:"
# <courseID> <creditload> <#lectures> <minworkingdays> <#students> <coursemode>
# course mode is used to specify if the course is a pratical course or a normal course
courses1 = prepare_data("COURSES:")

class Course:
    def __init__(self,course):
        self.id = course[0]
        self.creditload = course[1]
        self.num_lectures = course[2]
        self.minworkingdays = course[3]
        self.num_students = course[4]
        self.mode = course[5]
        
        def __repr__(self):
            return "<ID: {}, credit load: {}, lectures: {}, working days: {}, students: {}, Course Mode: {}>".format(self.id, self.creditload,self.num_lectures,
                                                                                                self.minworkingdays,self.num_students, self.mode)

courses = courses1.copy()
# print(len(courses))

# Generating event of each course
class Event:
    def __init__(self, course):
        self.id = course[0]
        self.minworkingdays = course[3] 
        self.num_students = course[4]
        self.mode = course[5]
        
    def __repr__(self):
        return "<{}>".format(self.id)
    
events = [Event(c) for c in courses1 for i in range(c[2])]
# print(len(events))


# list of Rooms
# Section "ROOMS:"
# <RoomID> <Capacity> <Mode>
rooms1 = prepare_data("ROOMS:")

class Room:
    def __init__(self, room):
        self.id = room[0]
        self.capacity = room[1]
        self.mode = room[2] #mode contains either the room is used for lectures or pratical
        
    def __repr__(self):
        return "<ID: {}, Capacity: {}, Mode: {}>".format(self.id, self.capacity, self.mode)

rooms = rooms1.copy()


# list of Curricula
# Section "CURRICULA:"
# <CurriculaID> <#Courses> <CoursesID> ... <CoursesID>
curricula1 = prepare_data("CURRICULA:")

class Curriculum:
    def __init__(self, curricula):
        self.id = curricula[0]
        self.num_courses = curricula[1]
        self.courses = curricula[2:]
        
    def __repr__(self):
        return "<ID: {}, num_courses: {}, courses: {}>".format(self.id, self.num_courses, self.courses)
    
curricula = curricula1.copy()
# curricula = [Curriculum(c) for c in curricula1]
# print(curricula)

# assigned = [[] for _ in range(header.periods)]
# ttable = [assigned for _ in range(header.days)]
numberOfPeriods = header.days * header.periods
numberOfRooms = len(rooms)
# print(numberOfPeriods)

# mapping a timeslot to a day and dayPeriod
mapTimeslotToDayAndPeriod = {}
for i in range(numberOfPeriods):
    mapTimeslotToDayAndPeriod[i] = (i // header.periods, i % header.periods)
# print(mapTimeslotToDayAndPeriod)

def convertTimeslotToDayPeriod(timeslot):
    """
    returns the day and dayPeriod of a timeslot
    """
    for key,value in mapTimeslotToDayAndPeriod.items():
        if timeslot == key:
            day, period = mapTimeslotToDayAndPeriod[timeslot]
            return str(day) + "." + str(period)
# print(convertTimeslotToDayPeriod(41))


timetable = []
# var = []
# for j in range(numberOfPeriods):
#     for i in (rooms):
#         timetable[(i[0],j)] = var
        
# print(timetable)
# emptyPosition = []
# for i in range(numberOfRooms):
#     for j in range(numberOfPeriods):
#         emptyPosition.append((i,j))
#         # timetable[(i,j)] = ()
# # print(timetable)

# forbiddenPosition = []
# unplacedEvents = []

days = []
day = []
for ts in range(numberOfPeriods):
    day.append(ts)
    if ts % header.periods == header.periods - 1:
        days.append(day)
        day = []
        
# curricula to courses.... mapping of curriculum to the courses in the curriculum
curriculaToCourses = {}
for cu in curricula:
    curriculaToCourses[cu[0]] = cu[2:]
# print(curriculaToCourses.values())
    
# mapping of the courses to all curricula containing the course
coursesToCurricula = {}
for course in courses:
    coursesToCurricula[course[0]] = []
    for cu, cuList in curriculaToCourses.items():
        if course[0] in cuList:
            coursesToCurricula[course[0]].append(cu)
# print(coursesToCurricula)
            
# mapping of room mode to course mode
roomModeToCourseMode = {}
# mode1 = "NORM"
# mode2 = "PRAC"
for rmode in rooms:
    roomModeToCourseMode[rmode[0]] = rmode[2] 
        # if rmode[2] == mode1 and cmode[5] == mode1:
        #     roomModeToCourseMode[rmode[2]] = cmode[5]
        # elif rmode[2] == mode2 and cmode[5] == mode2:
        #     roomModeToCourseMode[rmode[2]] = cmode[5]
            
# print(roomModeToCourseMode)          

# mapping of course mode to room mode
courseModeToRoomMode = {}
for m in courses:
    courseModeToRoomMode[m[5]] = []
    for rmode, rmodeList in roomModeToCourseMode.items():
        if m[5] in rmodeList:
            courseModeToRoomMode[m[5]].append(rmode)
# print(courseModeToRoomMode)   

# Map the course_name to its index in "courses" i.e basically mapping the course_name(courseid) to index values of an array
#where they are 90 courses, the index ranges from 0-89
courseNameToIndex = {}
for i, course in enumerate(courses):
    courseNameToIndex[course[0]] = i

def getCourseFromCourseName(courseName):
    """
    returns the course given by the course name
    """
    return courses[courseNameToIndex[courseName]]

