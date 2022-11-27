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
    def __init__(self):
        pass

    def connector(self):
        """
        Method enables password authentication to login into the database.
        If authentication goes wrong an error will be returned and the user has to retry
        inserting its loging information into the database.
        """
        if self.args.password:
            password = getpass()
            # Connect to MariaDB Platform
            try:
                self.conn = mysql.connector.connect(
                    user=self.args.us,
                    host="mariadb.bin.bioinf.nl",
                    database=self.args.db,
                    password=password
                )
            except mysql.connector.Error as error:
                print(f"Error connecting to MariaDB Platform: {error}")
                sys.exit(1)

    def get_connection(self):
        """
        Method returns connection to become available in other classes
        """
        return self.conn

def main():
    """
    call class and print properties
    """



if __name__ == '__main__':
    """
    Leave system after running script
    """