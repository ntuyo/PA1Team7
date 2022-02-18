'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("/Users/nazarituyo/Desktop/Brandeis/GitHub/PA1Team7/pa01-team7/courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' email returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def title(self,phrase):
        return Schedule([course for course in self.courses if phrase in course['name']])

    def description(self,description):
        return Schedule([course for course in self.courses if description in course['description']])

    ##Create your own filter method
    ##isIndependent is the filter for part 6c
    def isIndependent(self):
        return Schedule([course for course in self.courses if course['independent_study'] == True])

    def sortedLetter(self,letter):
        return Schedule([course for course in self.courses if letter in course['name'][0] == letter])
        ## Tiffany method
        ## This method returns all the classes that start with the the letter that the user inputed

    def amountWaiting(self,size):
        return Schedule([course for course in self.courses if int(course['waiting']) < int(size)])
        ## Gabby method
        ## This method return the courses that have a waiting list less than the inputed size

    def capacity(self):
        return Schedule([course for course in self.courses if course['limit'] != None])
        ## Jimkelly method
        ## This method checks if the course has a capacity or not using limit

    def isRemote(self):
        return Schedule([course for course in self.courses if "remote" in course['details']])
        ## Nazari method
        ## this method checks if the course if remote by looking in the details section
   
    def checkStatus(self):
        ''' filters '''
        return Schedule([course for course in self.courses if course['status_text'] == 'Open'])
        ## Ianna Method
        ## this Method checks if the courses are open and returns them
        
    def sort(self,field):
        if field=='subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        else: 
            print("can't sort by "+str(field)+" yet")
            return self
 
