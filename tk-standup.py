from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import ttk
import webbrowser
import datetime
from tinydb import TinyDB, Query
from PIL import Image, ImageTk
import os

"""
A GUI for the standup app.
"""
GITHUB_LINK = "https://github.com/kaipietila/solo-standup"
ENTRY_DB = TinyDB('entry_db.json')
LABEL_FONT = ("Verdana", 10)
ENTRY_FONT = ("Verdana", 8)
HEADER_FONT = ("Sans Serif", 16, 'bold')
LOGO_IMAGE = r"C:\Users\kai_p\OneDrive\Documents\GitHub\solo-standup\logo.png"


class Window(Frame):
    """
    Main window class
    """

    def __init__(self, master=None):
        Frame.__init__(self, master, height=300, background="white")
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

        quit_button = ttk.Button(self, text="I'm Done!", command=client_exit)
        quit_button.place(x=400, y=10)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=client_exit)
        menu.add_cascade(label="File", menu=file)

        options = Menu(menu)
        options.add_command(label="Empty db", command=lambda: self.popup("Are You Sure?"))
        menu.add_cascade(label="Options", menu=options)

        help_menubutton = Menu(menu)
        help_menubutton.add_command(label="About Me")
        help_menubutton.add_command(label="Github Link", command=open_github)
        menu.add_cascade(label="Help", menu=help_menubutton)

        input_text = Text(self.master, height=3, width=68, font=ENTRY_FONT)
        input_text.place(x=10, y=70)

        header = Label(self.master, text="The Raccoon Says Standup!", font=HEADER_FONT, bg="white")
        header.place(x=10, y=5)

        entry_button = ttk.Button(self, text="Save Entry", command=lambda: [self.create_entry(
            input_text.get(1.0, 'end -1c')), self.notify("Saved!")])
        entry_button.place(x=10, y=130)

        logo_image = Image.open(LOGO_IMAGE)
        logo_photo = ImageTk.PhotoImage(logo_image)
        img_label = Label(image=logo_photo, borderwidth=0)
        img_label.image = logo_photo
        img_label.place(x=155, y=130)

        label_input_text = Label(self.master, text="What are you going to code today?",
                                 font=LABEL_FONT, bg="white")
        label_input_text.place(x=10, y=40)

        query_button = ttk.Button(self.master, text="Show All", command=lambda:
        self.update_query(entry_text_box))
        query_button.pack()

        search_word = ttk.Entry(self.master)
        search_word.pack()

        search_button = ttk.Button(self.master, text="Search text", command=lambda:
        self.search_key_word(search_word.get(), entry_text_box))
        search_button.pack()

        search_date_button = ttk.Button(self.master, text="Search date", command=lambda:
        self.search_date(search_word.get(), entry_text_box))
        search_date_button.pack()

        search_latest_button = ttk.Button(self.master, text="Search latest", command=lambda:
        self.get_latest_entries(search_word.get(), entry_text_box))
        search_latest_button.pack()

        entry_text_box = tkst.ScrolledText(self.master, height=20, width=47, font=ENTRY_FONT)
        entry_text_box.pack(padx=10, pady=10, fill=BOTH, expand=True)

    def update_query(self, obj):
        """
        updating default query to view all entries
        :param obj:Textwidget
        :return:
        """
        obj.delete('1.0', END)
        all_entries = ENTRY_DB.all()
        for entry in all_entries:
            obj.insert(INSERT, entry)
            obj.insert(INSERT, "\n")

    def search_date(self, date, obj):
        """
        does not work yet!
        :param searchWordWord: date is the date user has entered
        :param obj:
        :return:
        """
        obj.delete("1.0", END)
        user = Query()
        results = ENTRY_DB.search(user.Date == date)
        for result in results:
            obj.insert(INSERT, result)
            obj.insert(INSERT, "\n")

    def search_key_word(self, word, obj):
        """
        does not work yet!!
        :param word:
        :param obj:
        :return:
        """
        obj.delete("1.0", END)
        self.update_query(obj)
        result_index= obj.search(word, 1.0, stopindex=END)
        while result_index:
            length = len(word)
            row, col = result_index.split('.')
            end = int(col) + length
            end = row + '.' + str(end)
            obj.tag_add('highlight', result_index, end)
            start = end
            result_index = obj.search(word, start, stopindex=END)
        obj.tag_config('highlight', background='white', foreground='red')

    def get_latest_entries(self, amount, obj):
        """
        To show the latest entries, as many as the user requests
        :return:
        returns the latest x amount of entries
        """
        obj.delete("1.0", END)

        def convert_to_int(amount):
            """
            takes in amount
            :param amount: string of a number
            :return: string of amount
            """
            if amount == '':
                return 0
            else:
                return int(amount)

        search_amt = convert_to_int(amount)
        db_len = len(ENTRY_DB)
        if search_amt == 1:
            latest_entry = ENTRY_DB.get(doc_id=db_len)
            obj.insert(INSERT, latest_entry)
        elif search_amt > 1:
            while (db_len - search_amt) != db_len:
                doc_pos = db_len - search_amt
                latest_entry = ENTRY_DB.get(doc_id=doc_pos)
                obj.insert(INSERT, latest_entry)
                obj.insert(INSERT, "\n")
                search_amt -= 1

    def create_entry(self, input_content):
        """
        Get the text from the text widget and insert it to the tinydb database
        """
        TODAYS_DATE = datetime.datetime.today()
        db_date = TODAYS_DATE.strftime('%d.%m.%Y')
        db_time = TODAYS_DATE.strftime("%H:%M")
        ENTRY_DB.insert({'Date': db_date, 'Time': db_time, 'Entry': input_content})

    def notify(self, msg):
        """
        A notification message, to notify user that something happened
        :param msg: whatever you want to display as notification
        :return:shows the messaage for 1 sec in the bottom right corner
        of the frame
        """
        notification = Label(self.master, text=msg, foreground="green")
        notification.pack(side=RIGHT)
        ROOT.after(1000, notification.destroy)

    def popup(self, msg):
        """
        A popup "are you sure?" window when emptying DB
        :param msg: the message to the user
        :return: Asks yes to proceed with emptying DB or no to not
        """
        popup = Toplevel()
        popup.title("!")

        def leavepop():
            """
            exits popup
            """
            popup.destroy()

        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)

        yes_button = Button(popup, text="Yes", command=lambda: [ENTRY_DB.purge(), leavepop()])
        yes_button.pack(side=RIGHT)
        no_button = Button(popup, text="No", command=lambda: leavepop())
        no_button.pack(side=LEFT)
        popup.mainloop()

def client_exit():
    """
    Basic exit from the window
    """
    exit()

def open_github():
    """
    Link to github
    :return: opens browser and opens the link
    """
    webbrowser.open(GITHUB_LINK, new=1, autoraise=1)
    return None


if __name__ == "__main__":
    """
    To run the program if main
    """
    ROOT = Tk()
    ROOT.geometry("500x800")
    ROOT.wm_iconbitmap(r"C:\Users\kai_p\OneDrive\Documents\GitHub\solo-standup\favicon.ico")
    APP = Window(ROOT)
    ROOT.mainloop()