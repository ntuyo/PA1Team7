'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        elif command in ['ti','title']:
            titleword= input("enter a title:")
            schedule = schedule.title(titleword).sort('subject')
        elif command in ['d','description']:
            description = input("enter a description:")
            schedule = schedule.description(description).sort('subject')
        elif command in ['c','courses']:
            course = input("enter a course:")
            schedule = schedule.subject([course]).sort('subject')
        elif command in ['i', 'instructor']:
            instructor = input("enter an instructor:")
            schedule = schedule.lastname([instructor]).sort('subject')
        elif command in ['in', 'independent']:
            schedule = schedule.isIndependent().sort('subject')
        elif command in ['l', 'letter']: ##tiffany filter
            letter = input("enter an Letter for a course:")
            ## this checks the first letter of a class 
            schedule = schedule.sortedLetter(letter).sort('subject') 
        elif command in ['cz', 'class size']: ## Gabby filter
            waiting = input("enter a class size:")
            ## this asked for class size
            schedule = schedule.amountWaiting(waiting).sort('subject')
        elif command in ['stat', 'status']: ## Ianna filter
            schedule = schedule.checkStatus().sort('subject')
            ## this ask for status of class
        elif command in ['cap', 'capacity']: ##jimkelly filter
            schedule = schedule.capacity().sort('subject')
            ## this checks the capacity 
        elif command in ['rem', 'remote']: ## Nazari filter
            schedule = schedule.isRemote().sort('subject')
            ## this checks if a class is remote or not
        
        
        
        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()

