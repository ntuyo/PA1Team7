'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from dis import Instruction
from unicodedata import name
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
# eliminate courses with no students
schedule = schedule.enrolled(range(5, 1000))

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
        if command == 'quit':
            return
        elif command in ['h', 'help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r', 'reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5, 1000))
            continue
        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')
        elif command in ['s', 'subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])
        # course  -- filter by subject/coursenumber
        elif command in ['c', 'course']:

            # instructor -- filter by instructor email or lastname
        elif command in ['i', 'instructor']:

        instructor = input("enter instructor last name or email")

        if "@" in instructor:

                schedule = schedule.lastname([instructor])

        if "@" not in instructor:

                schedule = schedule.email([instructor])
                    # what should i return

        # title -- filter by phrase in the title
        elif command in ['t', 'title']:

            title = input("enter a title")

            schedule = schedule.title([title])

            # Create your own filter (each team member creates their own)
<<<<<<< Updated upstream
        elif command in ['', '']:
            
            Gabby = input("enter instructor last name or email")
            
            #TODO
            pass
        elif command in ['', '']:
            
            Ianna = input("enter instructor last name or email")
            
            #TODO
            pass
        elif command in ['', '']:
            
            Nazari = input("enter instructor last name or email")
            
            #TODO
            pass
        elif command in ['', '']:
            
            Tiffany = input("enter instructor last name or email")
            
            #TODO
            pass
=======
        # elif command in ['', '']:

        #     Gabby = input("enter")

        #     #TODO
        #     pass
        # elif command in ['', '']:

        #     Ianna = input("enter instructor ")

        #     #TODO
        #     pass
        # elif command in ['', '']:

        #     Nazari = input("enter instructor last ")

        #     #TODO
        #     pass
        # elif command in ['', '']:

        #     Tiffany = input("enter instructor last name")

        #     #TODO
        #     pass
>>>>>>> Stashed changes
        else:
            print('command', command, 'is not supported')
            continue

        print("courses has", len(schedule.courses), 'elements', end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)


def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'], course['coursenum'], course['section'],
          course['name'], course['term'], course['instructor'])


if __name__ == '__main__':
    topmenu()
