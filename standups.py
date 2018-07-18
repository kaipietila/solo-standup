"""
***SOLO STANDUPS***
by Kai Pietilä

A program to record some plans on what to code the this session. 
You can review your entries later via the program

Name comes from when you at a comapny perform standups with your squad to see
what needs to be done etc each morning. 
Created this to have some nice log to follow my own coding and to keep some record for
myself.

Still needed features for full intended funtionality: 
- Add TinyDB to be able to use the entries for more stuff, search etc. To be able 
  to show an amount of entries on command.
"""

import datetime
import sys
import time
import os
from tinydb import TinyDB, Query

"""
Setting up the date and time for the timestamp
"""
todays_date = datetime.datetime.today()
today_day = todays_date.day
today_month = todays_date.month
today_year = todays_date.year
today_hour = todays_date.hour
today_minute = todays_date.minute
"""
Creating the TinyDB for later use
"""
entry_db = TinyDB('entry_db.json')

class DailyEntry:
    """
    Class for creating the User Entry
    """

    def __init__(self, day, month, year, hour, minute):

        self.day = day
        self.month = month
        self.year = year
        self.entry = ''
        self.hour = hour
        self.minute = minute
    
    def prompt_for_entry(self):
        """
        func to ask the user for input. The astring is setup to be
        displayed in a nice flushing motion
        """
        print(f"Date: {self.day}.{self.month}.{self.year}  Time: {self.hour}.{self.minute}")
        prompt_user = "What are you going to code this session? \n"
        for character in prompt_user:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        self.entry = input("> ")


def print_entries(db):
    """
    Func to print the entries written to the database. Basically just reading from the database the entries
    if the user does not wish to read the entries the program exits
    """
    for entry in db:
        print(entry)
    input("Enter any key and enter to get to title screen")
    title_screen()


def print_db(db):
    """
    To print the db to the user.
    """
    for entry in db:
        print(entry)


def run_diary():
    """
    Main func to run the program always runs on startup
    """
    todays_entry = DailyEntry(today_day, today_month, today_year, today_hour, today_minute)
    todays_entry.prompt_for_entry()
    dbdate = todays_date.strftime('%d %b %Y %H:%M')
    entry_db.insert({'date': dbdate, 'entry': todays_entry.entry})
    title_screen()


def title_screen_selection():
    """
    to select options to enter an entry or quit etc.
    """
    while True:
        option = input("> ")
        if option.lower() == "w":
            run_diary()
        elif option.lower() == "p":
            print_entries(entry_db)
        elif option.lower() == "q":
            sys.exit()
        else:
            print("Do not understand! Try again")
            continue


def title_screen():
    """
    Prints the title screen and prompts the player for a choice
    """
    print("\n" * 100)  # to clear the screen
    print("#########################")
    print("   So what's next?  ")
    print("#########################")
    print("To Write another entry enter 'w'")
    print("To Print entries enter 'p'")
    print("To Quit enter 'q'")
    title_screen_selection()
    

if __name__ == "__main__":
    """
    To run the program if main
    """
    run_diary()

