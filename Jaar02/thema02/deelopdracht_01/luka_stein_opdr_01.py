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
            student : {self.student:5}
            vak : {self.vak}
            datum : {self.datum}
            cijfer : {self.cijfer:1}
            """
