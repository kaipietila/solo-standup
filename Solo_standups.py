'''
***SOLO STANDUP*** 
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
'''

import datetime
import sys
import time
import os

todays_date = datetime.datetime.today()
today_day = todays_date.day
today_month = todays_date.month
today_year = todays_date.year
today_hour = todays_date.hour
today_minute = todays_date.minute
'''
Setting up the date and time for the timestamp
'''
app_root = os.path.dirname(os.path.realpath(__file__)) 
'''
getting the path of the file to be able to create the .txt file in the right place
'''

class DailyEntry:
    '''
    Class for creating the User Entry
    '''
    def __init__(self, day, month, year, hour, minute):

        self.day = day
        self.month = month
        self.year = year
        self.entry = ''
        self.hour = hour
        self.minute = minute
    
    def prompt_for_entry(self):
        '''
        finc to ask the user for input. The astring is setup to be displayed in a nice flushing motion
        '''
        print(f"Date: {self.day}.{self.month}.{self.year}  Time: {self.hour}.{self.minute}")
        prompt_user = "What are you going to code this session? \n"
        for character in prompt_user:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        self.entry = input("> ")

    def save_to_file(self):
        '''
        Func to save the entry to the file and write the timestamp as string
        '''
        strdate = todays_date.strftime('%d %b %Y %H:%M\n') #formats the date as a string
        diary_file = open(app_root + "\diary_entries.txt", "a")
        diary_file.write(strdate)
        diary_file.write(self.entry)
        diary_file.write("\n\n")
        diary_file.close()
        print("#######################")

def print_entries():
    '''
    Func to print the entries written to the file. Basically just reading from the file the entries
    if the user does not wish to read the entries the program exits
    '''
    for entry in open(app_root + "\diary_entries.txt"):
        print(entry)
    input("Enter any key to move on and enter:")
    title_screen()

def run_diary():
    '''
    Main func to run the program
    '''
    todays_entry = DailyEntry(today_day,today_month,today_year,today_hour, today_minute)
    todays_entry.prompt_for_entry()
    todays_entry.save_to_file()
    title_screen()

def title_screen_selection():
    '''
    to select options to enter an entry or quit etc.
    '''
    while True:
        option = input("> ")
        if option.lower() == "w":
            run_diary()
        elif option.lower() == "p":
            print_entries()
        elif option.lower() == "q":
            sys.exit()
        else:
            print("Do not understand! Try again")
            continue

def title_screen():
    '''
    Prints the title screen and prompts the player for a choice
    '''
    print ("\n" * 100) #to clear the screen
    print("#########################")
    print("   So what's next?  ")
    print("#########################")
    print("To Write another entry enter 'w'")
    print("To Print entries enter 'p'")
    print("To Quit enter 'q'")
    title_screen_selection()
    


if __name__ == "__main__":
    '''
    To run the program if main
    '''
    run_diary()

