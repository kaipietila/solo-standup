"""
***SOLO STANDUPS***
by Kai Pietilä

A program to record some plans on what to code the this session. 
You can review your entries later via the program

Name comes from when you at a company perform stand ups with your squad to see
what needs to be done etc each morning. 
Created this to have some nice log to follow my own coding and to keep some record for
myself.

Still needed features for full intended functionality:
- Add TinyDB query functionality and prettier printing
"""

import datetime
import sys
import time
from tinydb import TinyDB, Query

"""
Setting up the date and time for the timestamp
"""
TODAYS_DATE = datetime.datetime.today()
TODAY_DAY = TODAYS_DATE.day
TODAY_MONTH = TODAYS_DATE.month
TODAY_YEAR = TODAYS_DATE.year
TODAY_HOUR = TODAYS_DATE.hour
TODAY_MINUTE = TODAYS_DATE.minute
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
        func to ask the user for input. The string is setup to be
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


def query_keyword():
    """
    search the db with a keyword
    """
    pass


def query_history():
    """
    to search a seleceted amount of entries
    :return:
    prints out a selected amount of entires to the user
    """
    pass



def run_diary():
    """
    Main func to run the program always runs on startup
    """
    todays_entry = DailyEntry(TODAY_DAY, TODAY_MONTH, TODAY_YEAR, TODAY_HOUR, TODAY_MINUTE)
    todays_entry.prompt_for_entry()
    db_date = TODAYS_DATE.strftime('%d %b %Y %H:%M')
    entry_db.insert({'date': db_date, 'entry': todays_entry.entry})
    title_screen()


def advanced_options():
    print("\n" * 100)  # to clear the screen
    print(" "*30+"So what advanced thing are you doing?  ")
    print(" "*30+"BEWARE THESE THINGS CANT DE UNDONE!")
    print(" "*30+"To erase all entries enter 'erase'")
    print(" "*30+"To get back to title screen enter 'quit'")
    print("\n" * 10)
    advanced_options_selections()


def advanced_options_selections():
    """
    defining input for advanced options menu
    """
    while True:
        option_2 = input("> ")
        if option_2.lower() == "erase":
            entry_db.purge()
            print("You erased them all. Now go make new ones!")
            time.sleep(2)
            title_screen()
        elif option_2.lower() == "quit":
            title_screen()
        else:
            print("Do not understand! Try again")
            continue


def query_options():
    """
    query options menu
    """
    print("\n" * 100)  # to clear the screen
    print(" "*30+"####QUERY OPTIONS####  ")
    print(" "*30+"To search by keyword enter 'k'")
    print(" "*30+"To search the history of entries enter 'h'")
    print(" "*30+"To see all entries in the current history enter 'p'")
    print(" " * 30 + "To quit enter 'k'")
    print("\n" * 10)
    query_options_selections()

def query_options_selections():
    """
    To execute the options given in the query options menu
    """
    while True:
        option = input("> ")
        if option.lower() == "k":
            query_keyword()
        elif option.lower() == "h":
            query_history()
        elif option.lower() == "p":
            print_entries(entry_db)
        elif option.lower() == "q":
            title_screen()
        else:
            print("Do not understand! Try again")
            continue


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
        elif option.lower() == 'a':
            advanced_options()
        elif option.lower() == "s":
            query_options()
        else:
            print("Do not understand! Try again")
            continue


def title_screen():
    """
    Prints the title screen and prompts the player for a choice
    """
    print("\n" * 100)       # to clear the screen
    print(" "*30+"   So what's next?  ")
    print(" "*100)
    print(" "*30+"To Write another entry enter 'w'")
    print(" "*30+"To Print entries enter 'p'")
    print(" "*30+"To Enter search mode enter 's'")
    print(" "*30+"To Enter advanced options enter 'a'")
    print(" "*30+"To Quit enter 'q'")
    print("\n"*10)
    title_screen_selection()
    

if __name__ == "__main__":
    """
    To run the program if main
    """
    run_diary()

