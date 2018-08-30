from tkinter import *
import webbrowser
from standups import *
import datetime
import time
from tinydb import TinyDB, Query

entry_db = TinyDB('entry_db.json')
"""
Creating a simple window to add out stand-up app to at some point
"""
github_link = "https://github.com/kaipietila/solo-standup"

LABEL_FONT= ("Verdana", 10)


class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        """
        The Start window, probably the only window in this app
        """
        self.master.title("Standup!")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="I'm Done!", command= self.client_exit)
        quitButton.place(x=300, y=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        options = Menu(menu)
        options.add_command(label="Empty db", command=lambda: self.popup("Are You Sure?"))
        menu.add_cascade(label="Options", menu=options)

        help = Menu(menu)
        help.add_command(label="About Me")
        help.add_command(label="Github Link", command=self.open_github)
        menu.add_cascade(label="Help", menu=help)

        inputText = Text(self.master, height=3, width= 40)
        inputText.place(x=10, y=70)

        entryButton = Button(self, text="Save Entry", command=lambda: [self.create_entry(inputText.get(1.0, 'end -1c')),
                                                                       self.notify("Saved!")])
        entryButton.place(x=10, y=130)

        labelInputText = Label(self.master, text="What are you going to code today?", font=LABEL_FONT)
        labelInputText.place(x=10, y=40)

    def create_entry(self, input_content):
        """
        Get the text from the text widget and insert it to the tinydb database
        """
        TODAYS_DATE = datetime.datetime.today()
        db_date = TODAYS_DATE.strftime('%d %b %Y %H:%M')
        entry_db.insert({'Date': db_date, 'Entry': input_content})

    def notify(self, msg):
        """
        A notification message, to notify user that something happened
        :param msg: whatever you want to display as notification
        :return:shows the messaage for 1 sec in the bottom right corner
        of the frame
        """
        notification = Label(self.master, text=msg, foreground="green")
        notification.pack(side=RIGHT)
        root.after(1000, notification.destroy)

    def popup(self, msg):
        """
        A popup "are you sure?" window when emptying DB
        :param msg: the message to the user
        :return: Asks yes to proceed with emptying DB or no to not
        """
        popup = Toplevel()
        popup.title("!")

        def leavepop():
            popup.destroy()

        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)

        yesButton = Button(popup, text="Yes", command=lambda:[entry_db.purge(), leavepop()])
        yesButton.pack(side=RIGHT)
        noButton = Button(popup, text="No", command=lambda: leavepop())
        noButton.pack(side=LEFT)
        popup.mainloop()

    def client_exit(self):
        exit()

    def open_github(self):
        """
        Link to github
        :return: opens browser and opens the link
        """
        webbrowser.open(github_link, new=1, autoraise=1)
        return None


if __name__ == "__main__":
    """
    To run the program if main
    """
    root = Tk()

    root.geometry("400x300")
    root.iconbitmap("favicon.ico")
    app = Window(root)

    root.mainloop()

