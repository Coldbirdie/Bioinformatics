#!/usr/bin/env python3

"""
Dit script is voor week 1
"""

__author__ = 'L T Stein'
__date__ = '24-11-2022'
__version__ = 0.02

# IMPORTS
import sys
import mysql.connector


class Connection:
    """
    Class that prints exam information of a student
    """

    def __init__(self, student=str):
        self.student = student
        self.con = None
        self.cursor = None
        self.names = []
        self.exams = set()

    def connector(self):
        """
        Method for connecting to database
        """
        try:
            self.con = mysql.connector.connect(option_files='lt.my.cnf')
            self.cursor = self.con.cursor()
        except mysql.connector.Error as error:
            print(f"Error connecting to MariaDB Platform: {error}")
            sys.exit(1)

    def fetch(self):
        """
        Create list consisting of student names
        """
        self.cursor.execute("SELECT naam FROM studenten")
        mystudents = self.cursor.fetchall()
        for x in mystudents:
            self.names.append("".join(x))
        return self.names

    def results(self):
        """
        Get results of exams made by student X, given as variable to function call
        """
        for name in self.names:
            if name == self.student:
                self.cursor.execute(f"select s.naam, c.naam, ex_datum, cijfer from examens e join cursussen c on"
                                    f" c.cur_id = e.cur_id join studenten s on s.stud_id = e.stud_id"
                                    f" where s.naam = '{name}';")
                myresult = self.cursor.fetchall()
                for exam in myresult:
                    self.exams.add(exam)
        return self.exams

    def close(self):
        """
        Close connection to sql database
        """
        self.con.close()

