#!/usr/bin/env python3

"""
Dit script is voor week 1
"""

__author__ = 'L T Stein'
__date__ = '24-11-2022'
__version__ = 0.01

# IMPORTS
import sys


class Tentamen:
    """
    Class that prints exam information of a student
    """
    def __init__(self, student, vak, datum, cijfer):
        """
        Special constructor that receives class attributes
        :param student:
        :param vak:
        :param datum:
        :param cijfer:
        """
        self.student = student
        self.vak = vak
        self.datum = datum
        self.cijfer = cijfer

    def property(self):
        """
        Print exam info in format
        :return: fstring of exam information
        """
        return f"""
                 student : {self.student:^10}
                 vak     : {self.vak:^16}
                 datum   :{self.datum:^18}
                 cijfer  :{self.cijfer:^12}
                 """


def main():
    """
    call class and print properties
    """
    try:
        t = Tentamen('Luka', 'database02', '24-11-2022', 7.5)
        students = t.property()
        print(students)
    finally:
        print('Script finished')


if __name__ == '__main__':
    """
    Leave system after running script
    """
    sys.exit(main())