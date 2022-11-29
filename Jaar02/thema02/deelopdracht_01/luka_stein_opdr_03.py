#!/usr/env/bin/ python3

"""
Script that print names of students and shows the results of a specicified student
"""

__author__ = 'L T Stein'
__date__ = 28-11-2022
__version__ = 0.03

# IMPORTS
import sys
from opdracht_01 import Tentamen
from opdracht_02 import Connection

# var : 'Luka', 'database02', '24-11-2022', 7.5
def call_class():
    """
    Call class and return names property
    """
    # Class object Connection
    c = Connection(sys.argv[1])
    c.connector()
    names = c.fetch()
    exams = c.results()
    c.close()
    return names, exams

def students(names):
    """
    Print student names in format
    """
    print("Students:")
    for id, name in enumerate(names):
        print(f"{id:^5}{name}")

def rapport(exams):
    """
    Print exams made by student specified through argv
    """
    for col_tup in exams:
        # Class object tentamen
        t = Tentamen(*col_tup)
        format_st_ex = t.property()
        print(f"\n{format_st_ex}")

def main():
    """
    Call functions and finish script
    """
    try:
        names, exams = call_class()
        students(names)
        rapport(exams)
    finally:
        print('Script finished')

if __name__ == '__main__':
    """
    Exit system after running script
    """
    sys.exit(main())
