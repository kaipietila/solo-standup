'''
An app to record some plans on what to code the this session. 
You can review your entries later via the app
'''

import datetime
import sys
import time
import os

# getting the time from datetime

todays_date = datetime.datetime.today()
today_day = todays_date.day
today_month = todays_date.month
today_year = todays_date.year

app_root = os.path.dirname(os.path.realpath(__file__))

class DailyEntry:
    #class for creating a single entry

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year
        self.entry = ''
    
    def prompt_for_entry(self):
        #asking the user for input
        print(f"Today is {self.day}.{self.month}.{self.year}")
        prompt_user = "What are you going to code this session? \n"
        for character in prompt_user:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
        self.entry = input("> ")

    def save_to_file(self):
        #saving to a file 
        strdate = todays_date.strftime('%d/%m/%Y\n') #formats the date as a string
        diary_file = open(app_root + "\diary_entries.txt", "a")
        diary_file.write(strdate)
        diary_file.write(self.entry)
        diary_file.write("\n\n")
        diary_file.close()
        print("ok, good luck!")

def print_entries():
    #if the user wishes to review old entries, he can print them out
    show_entries = "Do you want to read your previous entries? y/n\n"
    for character in show_entries:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    answer = input("> ")
    if answer.lower() == "y":
        for entry in open(app_root + "\diary_entries.txt"):
            print(entry)
        
    else: 
        exit()

def run_diary():
    #main func to run the program
    todays_entry = DailyEntry(today_day,today_month,today_year)
    todays_entry.prompt_for_entry()
    todays_entry.save_to_file()
    print_entries()


if __name__ == "__main__":
    run_diary()

