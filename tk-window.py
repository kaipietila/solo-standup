from tkinter import *
import tkinter.scrolledtext as tkst
import webbrowser
from standups import *
import datetime
from tinydb import TinyDB, Query
from PIL import Image, ImageTk

entry_db = TinyDB('entry_db.json')
"""
Creating a simple window to add out stand-up app to at some point
"""
github_link = "https://github.com/kaipietila/solo-standup"

LABEL_FONT= ("Verdana", 10)
ENTRY_FONT= ("Verdana", 8)

LOGO_IMAGE = "logo.png"

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master, height= 300, background="white")
        self.master = master
        self.init_window()

    def init_window(self):
        """
        The initial window, probably the only window in this app as everything can be and should
        be made simple in one frame
        """
        self.master.title("Standup!")
        self.pack(fill=BOTH, expand=1)
        self.master.config(background="white")

        quitButton = Button(self, text="I'm Done!", command= self.client_exit)
        quitButton.place(x=400, y=10)

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

        inputText = Text(self.master, height=3, width=68, font=ENTRY_FONT)
        inputText.place(x=10, y=70)

        entryButton = Button(self, text="Save Entry", command=lambda: [self.create_entry(inputText.get(1.0, 'end -1c')),
                                                                       self.notify("Saved!")])
        entryButton.place(x=10, y=130)

        logo_image = Image.open("logo.png")
        logo_photo = ImageTk.PhotoImage(logo_image)
        imgLabel = Label(image=logo_photo, borderwidth=0)
        imgLabel.image = logo_photo
        imgLabel.place(x=155, y=130)

        labelInputText = Label(self.master, text="What are you going to code today?", font=LABEL_FONT, bg="white")
        labelInputText.place(x=10, y=40)

        queryButton = Button(self.master, text="Update", command=lambda :self.updateQuery(entryTextBox))
        queryButton.pack()

        searchWord = Entry(self.master)
        searchWord.pack()
        searchWordWord = searchWord.get()
        searchButton = Button(self.master, text="Search", command= lambda : self.searchKeyWord(searchWordWord,
                                                                                               entryTextBox))
        searchButton.pack()

        entryTextBox = tkst.ScrolledText(self.master, height=20, width=47, font=ENTRY_FONT)
        entryTextBox.pack(padx=10, pady=10, fill=BOTH, expand=True)


    def updateQuery(self, obj):
        obj.delete('1.0', END)
        allEntries=entry_db.all()
        for entry in allEntries:
            obj.insert(INSERT, entry)
            obj.insert(INSERT, "\n")

    def searchKeyWord(self, word, obj):
        """
        does not work yet!!
        :param word:
        :param obj:
        :return:
        """
        resultIndex= obj.search(word, 1.0)
        print(resultIndex)


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

    root.geometry("500x700")
    root.iconbitmap("favicon.ico")
    app = Window(root)

    root.mainloop()

