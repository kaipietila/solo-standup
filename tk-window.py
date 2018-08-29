from tkinter import *
import webbrowser
from standups import *
import datetime
from tinydb import TinyDB, Query

entry_db = TinyDB('entry_db.json')
"""
Creating a simple window to add out stand-up app to at some point
"""
github_link = "https://github.com/kaipietila/solo-standup"


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()


    def init_window(self):
        self.master.title("Standup!")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Get to Work!", command= self.client_exit)
        quitButton.place(x=300, y=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        options = Menu(menu)
        options.add_command(label="Empty db", command=lambda: self.purgeDb)
        menu.add_cascade(label="Options", menu=options)

        help = Menu(menu)
        help.add_command(label="About Me")
        help.add_command(label="Github Link", command=self.open_github)
        menu.add_cascade(label="Help", menu=help)

        inputText = Text(self.master, height=1, width= 40)
        inputText.place(x=10, y=50)

        entryButton = Button(self, text="Save Entry", command=lambda: self.create_entry(inputText.get(1.0, 'end -1c')))
        entryButton.place(x=10, y=75)

    def create_entry(self, input_content):
        """
        Get the text from the text widget and insert it to the tinydb database
        """
        TODAYS_DATE = datetime.datetime.today()
        db_date = TODAYS_DATE.strftime('%d %b %Y %H:%M')
        entry_db.insert({'Date': db_date, 'Entry': input_content})

    def purgeDb(self):
        popup = Toplevel(self.master)
        popup.title("Clearing Database")

        purge_message = Label(popup, text="Are you sure?")
        purge_message.pack()

        yesButton = Button(popup, text="Yes", command=lambda:[entry_db.purge(), self.client_exit()])
        yesButton.pack()


    def client_exit(self):
        exit()

    def open_github(self):
        github_link = "https://github.com/kaipietila/solo-standup"
        webbrowser.open(github_link, new=1, autoraise=1)
        return None

    def result_window(self):
        pass


if __name__ == "__main__":
    """
    To run the program if main
    """
    root = Tk()

    root.geometry("400x300")

    app = Window(root)

    root.mainloop()

