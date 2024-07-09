from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Treeview
import datetime

b1, b2, b3, b4, cur, con, e1, e2, e3, e4, e5, i, ps = None, None, None, None, None, None, None, None, None, None, None, None, None
window, win = None, None
com1d, com1m, com1y, com2d, com2m, com2y = None, None, None, None, None, None

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']
y = list(range(2020, 2040))
d = list(range(1, 32))
def quest():
    import tkinter as tk
    from tkinter import scrolledtext, messagebox
    import requests

    # Function to fetch answer from Wolfram Alpha API
    def get_answer(question):
        app_id = 'UKHHE9-GGJV3KG49R'  # Replace with your actual Wolfram Alpha App ID
        base_url = "http://api.wolframalpha.com/v1/result"
        params = {
            'appid': app_id,
            'i': question
        }
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    # Function to handle ask button click
    def ask_question():
        question = question_entry.get("1.0", tk.END).strip()
        if not question:
            messagebox.showwarning("Input Error", "Please enter a question.")
            return

        response = get_answer(question)
        response_text.insert(tk.END, f"Q: {question}\nA: {response}\n\n")
        question_entry.delete("1.0", tk.END)

    # Creating the main window
    root = tk.Tk()
    root.title("Question Answer Interface")
    root.geometry("600x400")

    # Creating the input field for questions
    question_label = tk.Label(root, text="Enter your question:")
    question_label.pack(pady=10)

    question_entry = tk.Text(root, height=3, width=70)
    question_entry.pack(pady=5)

    ask_button = tk.Button(root, text="Ask", command=ask_question)
    ask_button.pack(pady=10)

    # Creating a scrolled text box to display the responses
    response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    response_text.pack(pady=10)

    # Running the application
    root.mainloop()
def randomquest():
    import tkinter as tk
    from tkinter import scrolledtext, messagebox
    import requests

    # Function to fetch a trivia question
    def get_trivia_question():
        base_url = "https://opentdb.com/api.php"
        params = {
            'amount': 50,
            'type': 'multiple'
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            question = data['results'][0]['question']
            correct_answer = data['results'][0]['correct_answer']
            return f"{question}\nCorrect Answer: {correct_answer}"
        else:
            return "Error: Unable to get the question"

    # Function to handle ask button click
    def ask_question():
        response = get_trivia_question()
        response_text.insert(tk.END, f"Q: {response}\n\n")

    # Creating the main window
    root = tk.Tk()
    root.title("Trivia Question Interface")
    root.geometry("600x400")

    # Creating the input field for questions
    ask_button = tk.Button(root, text="Get Trivia Question", command=ask_question)
    ask_button.pack(pady=20)

    # Creating a scrolled text box to display the responses
    response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
    response_text.pack(pady=10)

    # Running the application
    root.mainloop()


class Book:
    def __init__(self, title, author, rating, summary, reviews, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.summary = summary
        self.reviews = reviews
        self.price = price


class BookVerseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Verse")

        # Dummy book data
        self.books = [


            Book(
                title="Book 1: Python Programming",
                author="Guido van Rossum",
                rating=4.3,
                summary='''Key Concepts and Structure Introduction to Python Basics

Overview of Python's syntax and fundamental programming constructs.
Understanding variables, data types, loops, and conditional statements.
Introduction to Python's standard library and commonly used modules.
Project-Based Learning

The book is divided into several chapters, each focusing on a specific project or problem to solve.
Each project is designed to be completed within 100 lines of code, fostering creativity and efficiency.
Sample Projects

Web Scraper: A basic web scraper using libraries like requests and BeautifulSoup to extract data from web pages.
Command-Line Tools: Building simple command-line utilities to automate repetitive tasks.
Data Analysis: Using pandas and matplotlib to perform basic data analysis and visualization.
APIs and Networking: Creating scripts to interact with APIs and handle network requests.
File Handling: Reading from and writing to files, including CSV and JSON formats.
Code Optimization

Techniques for writing concise and efficient Python code.
Tips for reducing code length without sacrificing readability or functionality.
Error Handling and Debugging

Implementing robust error handling using try-except blocks.
Debugging strategies to identify and fix issues in your code.
Best Practices

Writing clean and maintainable code.
Adhering to PEP 8 guidelines for Python code style.
Using version control systems like Git to manage code changes.
Advanced Topics

Introduction to object-oriented programming (OOP) concepts within the 100-line constraint.
Using Python's built-in libraries and third-party packages to extend functionality.
Conclusion and Next Steps

Encouragement to apply the learned skills to more complex projects.
Suggestions for further reading and advanced Python topics.
Learning Outcomes
Efficiency: Develop the ability to write concise, efficient, and effective Python code.
Problem-Solving: Enhance problem-solving skills by working on real-world projects.
Practical Skills: Gain practical experience with commonly used Python libraries and tools.
Code Quality: Learn to write clean, readable, and maintainable code''',
                reviews=["Great book!", "Highly recommended for beginners.", "Easy to follow examples."],
                price="$35.50"
            ),

            Book(
                title="Book 2: Java Programming",
                author="James Gosling",
                rating=4.5,
                summary=''' Java Programming Concepts
1. Syntax and Structure
Class: The fundamental building block in Java. It is a blueprint from which individual objects are created.
Method: A block of code within a class that performs a specific task.
Main Method: The entry point for any Java application, defined as public static void main(String[] args).
2. Object-Oriented Programming (OOP)
Classes and Objects:
Class: Defines the properties (attributes) and behaviors (methods) that objects created from the class can have.
Object: An instance of a class.
Inheritance: Allows a class to inherit fields and methods from another class. This promotes code reusability.
Polymorphism: Allows objects to be treated as instances of their parent class rather than their actual class. This can be achieved through method overriding and method overloading.
Encapsulation: Bundles the data (variables) and methods (functions) that operate on the data into a single unit or class, and restricts access to some of the object's components.
Abstraction: Hides the complex implementation details and exposes only the necessary features of an object.
3. Basic Data Types
Primitive Types: The most basic data types provided by Java. Examples include:
int: Represents an integer value.
char: Represents a single 16-bit Unicode character.
double: Represents a double-precision 64-bit floating point.
boolean: Represents a true or false value.
Non-Primitive Types: Also known as reference types, they refer to objects. Examples include:
String: Represents a sequence of characters.
Array: A collection of variables of the same type.
Classes: User-defined data types.
4. Control Structures
Conditional Statements: Allow the program to make decisions based on conditions.
if, else if, else: Execute different blocks of code based on boolean conditions.
switch: Select one of many code blocks to execute.
Loops: Allow the execution of a block of code multiple times.
for: Iterates over a range of values.
while: Repeats a block of code while a condition is true.
do-while: Similar to while but the block of code executes at least once.
5. Standard Libraries
Java Standard Library: Provides a wide array of classes and methods to perform various tasks.
Common Packages:
java.lang: Contains fundamental classes like String, Math, and System.
java.util: Contains utility classes such as collections framework classes (ArrayList, HashMap).
java.io: Provides classes for input and output through data streams, serialization, and the file system.
Key Theoretical Concepts
Class and Object Example
Class Definition: A class encapsulates data for the object. It has fields (attributes) and methods (functions).
Object Instantiation: Creating an object from a class involves using the new keyword.
Encapsulation
Achieved by making fields private and providing public getter and setter methods.
Promotes data hiding and ensures that the object's data is accessed only through defined methods.
Inheritance
Allows the creation of a new class that inherits the properties and methods of an existing class.
Promotes code reuse and establishes a hierarchical relationship between classes.
Polymorphism
Method Overloading: Multiple methods in the same class with the same name but different parameters.
Method Overriding: A subclass provides a specific implementation of a method already defined in its superclass.
                
                ''',
                reviews=["Excellent read!", "Comprehensive and well-structured content."],
                price="$40.00"
            ),
            Book(
                title="Book 3: Machine Learning with Python",
                author="Shake appe",
                rating=4.0,
                summary="Machine Learning with Python introduces readers to the fundamental concepts of machine learning and its practical applications using Python libraries like scikit-learn and TensorFlow. Includes hands-on exercises and real-world case studies.",
                reviews=["Good book!", "Clear explanations and practical examples."],
                price="$45.99"
            ),
            Book(
                title="Book 4: Data Science Handbook",
                author="Mahdendr",
                rating=4.2,
                summary="Data Science Handbook covers essential topics in data science, including statistical analysis, data visualization, and machine learning algorithms. It provides insights into best practices and tools used by data scientists in industry.",
                reviews=["Informative and well-written.", "Useful for beginners and professionals alike."],
                price="$38.75"
            ),
            Book(
                title="Book 5: Web Development with Django",
                author="Shake williams",
                rating=4.8,
                summary="Web Development with Django is a comprehensive guide to building web applications using the Django framework. It covers Django's MVC architecture, ORM, security features, and deployment strategies.",
                reviews=["Great book for Django enthusiasts!", "Practical examples and clear explanations."],
                price="$42.50"
            ),
            Book(
                title="Book 6: Cybersecurity Fundamentals",
                author="cyber-star",
                rating=4.1,
                summary="Cybersecurity Fundamentals provides an overview of cybersecurity principles, threats, and defense strategies. It covers topics such as network security, cryptography, and ethical hacking techniques.",
                reviews=["Essential reading for cybersecurity professionals.", "Well-structured and informative content."],
                price="$37.25"
            ),
            # Add more books here
        ]

        self.create_widgets()

    def create_widgets(self):
        # Title
        lbl_title = Label(self.master, text="Book Verse", font=("Helvetica", 24, "bold"), fg="blue")
        lbl_title.grid(row=0, column=0, columnspan=3, pady=10)

        # Book Grid
        row_num = 1
        col_num = 0
        for book in self.books:
            frame = Frame(self.master, bd=2, relief=RIDGE)
            frame.grid(row=row_num, column=col_num, padx=10, pady=10)

            lbl_book_title = Label(frame, text=f"{book.title}", font=("Helvetica", 12, "bold"), fg="green")
            lbl_book_title.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

            lbl_author = Label(frame, text=f"Author: {book.author}")
            lbl_author.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

            lbl_rating = Label(frame, text=f"Rating: {book.rating}")
            lbl_rating.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

            lbl_price = Label(frame, text=f"Price: {book.price}")
            lbl_price.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

            btn_buy = Button(frame, text="Buy", command=lambda b=book: self.buy_ebook(b))
            btn_buy.grid(row=4, column=0, pady=5, padx=5, sticky="ew")

            btn_summary = Button(frame, text="Summary", command=lambda b=book: self.get_summary(b))
            btn_summary.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

            btn_reviews = Button(frame, text="Reviews", command=lambda b=book: self.view_reviews(b))
            btn_reviews.grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            btn_rating = Button(frame, text="Rating", command=lambda b=book: self.view_rating(b))
            btn_rating.grid(row=6, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1

    def buy_ebook(self, book):
        messagebox.showinfo("Buy eBook", f"You have bought '{book.title}' by {book.author} for {book.price}.")

    def get_summary(self, book):
        messagebox.showinfo("Book Summary", f"Summary of '{book.title}':\n\n{book.summary}")

    def view_reviews(self, book):
        reviews = "\n".join(book.reviews)
        messagebox.showinfo("Customer Reviews", f"Customer Reviews for '{book.title}':\n\n{reviews}")

    def view_rating(self, book):
        messagebox.showinfo("Book Rating", f"The rating for '{book.title}' is {book.rating}.")


def loginlibr():
    global window
    connectdb()
    cur.execute("SELECT * FROM Login WHERE userid=%s AND branch=%s", (e1.get().strip(), e2.get().strip()))
    data = cur.fetchone()
    if data:
        closedb()
        libr()
    else:
        messagebox.showerror("Login Error", "Invalid Credentials")
        window.withdraw()
        closedb()
        home()


def libr():
    global window
    window.withdraw()
    global win, b1, b2, b3, b4,w1,wo
    win = Tk()
    win.title('Library')
    win.geometry("500x600+480+180")
    win.resizable(False, False)
    w1 =Button(win,height=2,width=25,text="Get random Questions",command=randomquest)
    w1.place(x=110,y=430)
    wo = Button(win, height=2, width=25, text="Ask questions", command=quest)
    wo.place(x=110, y=480)

    bo = Button(win, height=2, width=25,text=' View All Books ',command=viewallbooks)
    b1 = Button(win, height=2, width=25, text=' Add Book ', command=addbook)
    b2 = Button(win, height=2, width=25, text=' Issue Book ', command=issuebook)
    b3 = Button(win, height=2, width=25, text=' Return Book ', command=returnbook)
    b4 = Button(win, height=2, width=25, text=' View Book ', command=viewbook)
    b5 = Button(win, height=2, width=25, text=' Issued Book ', command=issuedbook)
    b6 = Button(win, height=2, width=25, text=' Delete Book ', command=deletebook)
    b7 = Button(win, height=2, width=25, text=' LogOut ', command=logout)
    bo.place(x=110, y=30)
    b1.place(x=110, y=80)
    b2.place(x=110, y=130)
    b3.place(x=110, y=180)
    b4.place(x=110, y=230)
    b5.place(x=110, y=280)
    b6.place(x=110, y=330)
    b7.place(x=110, y=380)
    win.mainloop()

def viewallbooks():
    global win
    win.destroy()
    win = Tk()
    win.title('View All Book')
    win.resizable(False, False)
    app = BookVerseApp(win)
    win.mainloop()



def addbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Add Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    sub = Label(win, text='SUBJECT')
    tit = Label(win, text='TITLE')
    auth = Label(win, text='AUTHOR')
    ser = Label(win, text='SERIAL NO')
    global e1, b, b1
    e1 = Entry(win, width=25)
    global e2
    e2 = Entry(win, width=25)
    global e3
    e3 = Entry(win, width=25)
    global e4
    e4 = Entry(win, width=25)
    b = Button(win, height=2, width=21, text=' ADD BOOK TO DB ', command=addbooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=closebooks)
    sub.place(x=70, y=50)
    tit.place(x=70, y=90)
    auth.place(x=70, y=130)
    ser.place(x=70, y=170)
    e1.place(x=180, y=50)
    e2.place(x=180, y=90)
    e3.place(x=180, y=130)
    e4.place(x=180, y=170)
    b.place(x=180, y=210)
    b1.place(x=180, y=252)
    win.mainloop()


def addbooks():
    connectdb()
    q = 'INSERT INTO Book VALUE("%s","%s","%s","%i")'
    global cur, con
    cur.execute(q % (e1.get(), e2.get(), e3.get(), int(e4.get())))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Added")
    closedb()
    libr()


def closebooks():
    global win
    win.destroy()
    libr()


def issuebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    name = Label(win, text='ISSUE ', font='Helvetica 30 bold')
    branch = Label(win, text='BOOK', font='Helvetica 30 bold')

    sid = Label(win, text='STUDENT ID')
    no = Label(win, text='BOOK NO')
    issue = Label(win, text='ISSUE DATE')
    exp = Label(win, text='EXPIRY DATE')
    global e1, b, b1
    e1 = Entry(win, width=25)
    global e4
    e4 = Entry(win, width=25)
    global com1y, com1m, com1d, com2y, com2m, com2d
    com1y = Combobox(win, value=y, width=5)
    com1m = Combobox(win, value=month, width=5)
    com1d = Combobox(win, value=d, width=5)
    com2y = Combobox(win, value=y, width=5)
    com2m = Combobox(win, value=month, width=5)
    com2d = Combobox(win, value=d, width=5)
    now = datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month - 1])
    com1d.set(now.day)

    com2y.set(now.year)
    com2m.set(month[now.month - 1])
    com2d.set(now.day)

    b = Button(win, height=2, width=21, text=' ISSUE BOOK ', command=issuebooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=closebooks)
    name.place(x=55, y=30)
    branch.place(x=225, y=30)
    sid.place(x=70, y=130)
    no.place(x=70, y=170)
    issue.place(x=70, y=210)
    exp.place(x=70, y=240)
    e1.place(x=180, y=130)
    e4.place(x=180, y=170)
    com1y.place(x=180, y=210)
    com1m.place(x=230, y=210)
    com1d.place(x=280, y=210)
    com2y.place(x=180, y=240)
    com2m.place(x=230, y=240)
    com2d.place(x=280, y=240)
    b.place(x=178, y=270)
    b1.place(x=178, y=312)
    win.mainloop()


def issuebooks():
    connectdb()
    q = 'INSERT INTO BookIssue VALUE("%s","%s","%s","%s")'
    i = datetime.datetime(int(com1y.get()), month.index(com1m.get()) + 1, int(com1d.get()))
    e = datetime.datetime(int(com2y.get()), month.index(com2m.get()) + 1, int(com2d.get()))
    i = i.isoformat()
    e = e.isoformat()
    cur.execute(q % (e1.get(), e4.get(), i, e))
    con.commit()
    win.destroy()
    messagebox.showinfo("Book", "Book Issued")
    closedb()
    libr()


def returnbook():
    global win
    # win.destroy()
    win = Tk()
    win.title('Return Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    ret = Label(win, text='RETURN ', font='Helvetica 30 bold')
    book = Label(win, text='BOOK', font='Helvetica 30 bold')
    no = Label(win, text='BOOK NO')
    date = Label(win, text='RETURN DATE')
    exp = Label(win, text='')
    global b, b1
    global e4
    e4 = Entry(win, width=25)
    global com1y, com1m, com1d, com2y, com2m, com2d
    com1y = Combobox(win, value=y, width=5)
    com1m = Combobox(win, value=month, width=5)
    com1d = Combobox(win, value=d, width=5)
    '''com2y=Combobox(win,width=5)
    com2m=Combobox(win,width=5)
    com2d=Combobox(win,width=5)'''
    now = datetime.datetime.now()
    com1y.set(now.year)
    com1m.set(month[now.month - 1])
    com1d.set(now.day)

    b = Button(win, height=2, width=21, text=' RETURN BOOK ', command=returnbooks)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=closebooks)
    ret.place(x=55, y=30)
    book.place(x=225, y=30)
    no.place(x=70, y=120)
    date.place(x=70, y=160)
    exp.place(x=70, y=200)
    e4.place(x=180, y=120)
    com1y.place(x=180, y=160)
    com1m.place(x=230, y=160)
    com1d.place(x=280, y=160)
    '''com2y.place(x=180,y=200)
    com2m.place(x=230,y=200)
    com2d.place(x=280,y=200)'''
    b.place(x=178, y=200)
    b1.place(x=178, y=242)
    win.mainloop()


def returnbooks():
    connectdb()
    q = 'SELECT exp FROM BookIssue WHERE serial="%s"'
    cur.execute(q % (e4.get()))
    e = cur.fetchone()
    e = str(e[0])
    i = datetime.date.today()
    e = datetime.date(int(e[:4]), int(e[5:7]), int(e[8:10]))
    if i <= e:
        a = 'DELETE FROM BookIssue WHERE serial="%s"'
        cur.execute(a % e4.get())
        con.commit()
    else:
        t = str((i - e) * 10)
        messagebox.showinfo("Fine", t[:4] + ' Fine ')
    win.destroy()
    closedb()
    libr()

def viewbook():
    win = Tk()
    win.title('View Books')
    win.geometry("800x300+270+180")
    win.resizable(False, False)

    treeview = Treeview(win, columns=("Subject", "Title", "Author", "Serial No"), show='headings')
    treeview.heading("Subject", text="Subject")
    treeview.heading("Title", text="Title")
    treeview.heading("Author", text="Author")
    treeview.heading("Serial No", text="Serial No")
    treeview.column("Subject", anchor='center')
    treeview.column("Title", anchor='center')
    treeview.column("Author", anchor='center')
    treeview.column("Serial No", anchor='center')
    index = 0
    iid = 0
    connectdb()
    q = 'SELECT * FROM Book'
    cur.execute(q)
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, iid, value=row)
        index = iid = index + 1
    treeview.pack()
    win.mainloop()
    closedb()


def issuedbook():
    connectdb()
    q = 'SELECT * FROM BookIssue'
    cur.execute(q)
    details = cur.fetchall()
    if len(details) != 0:
        win = Tk()
        win.title('View Books')
        win.geometry("800x300+270+180")
        win.resizable(False, False)
        treeview = Treeview(win, columns=("Student ID", "Serial No", "Issue Date", "Expiry Date"), show='headings')
        treeview.heading("Student ID", text="Student ID")
        treeview.heading("Serial No", text="Serial No")
        treeview.heading("Issue Date", text="Issue Date")
        treeview.heading("Expiry Date", text="Expiry Date")
        treeview.column("Student ID", anchor='center')
        treeview.column("Serial No", anchor='center')
        treeview.column("Issue Date", anchor='center')
        treeview.column("Expiry Date", anchor='center')
        index = 0
        iid = 0
        for row in details:
            treeview.insert("", index, iid, value=row)
            index = iid = index + 1
        treeview.pack()
        win.mainloop()
    else:
        messagebox.showinfo("Books", "No Book Issued")
    closedb()


def deletebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Delete Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    usid = Label(win, text='Serial NO')
    paswrd = Label(win, text='PASSWORD')
    global e1
    e1 = Entry(win)
    global e2, b2
    e2 = Entry(win)
    b1 = Button(win, height=2, width=17, text=' DELETE ', command=deletebooks)
    b2 = Button(win, height=2, width=17, text=' CLOSE ', command=closebooks)
    usid.place(x=80, y=100)
    paswrd.place(x=70, y=140)
    e1.place(x=180, y=100)
    e2.place(x=180, y=142)
    b1.place(x=180, y=180)
    b2.place(x=180, y=230)
    win.mainloop()


def deletebooks():
    connectdb()
    if e2.get() == 'stud':
        q = 'DELETE FROM Book WHERE serial="%i"'
        cur.execute(q % (int(e1.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Delete", "Book Deleted")
        closedb()
        libr()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()


def loginadmin():
    if e1.get() == 'admin' and e2.get() == 'admin':
        admin();


def admin():
    window.withdraw()
    global win, b1, b2, b3, b4, cur, con
    win = Tk()
    win.title('Admin')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    b1 = Button(win, height=2, width=25, text=' Add User ', command=adduser)
    b2 = Button(win, height=2, width=25, text=' View User ', command=viewuser)
    b3 = Button(win, height=2, width=25, text=' Delete User ', command=deleteuser)
    b4 = Button(win, height=2, width=25, text=' LogOut ', command=logout)
    b1.place(x=110, y=70)
    b2.place(x=110, y=120)
    b3.place(x=110, y=170)
    b4.place(x=110, y=220)
    win.mainloop()


def logout():
    win.destroy()
    try:
        closedb()
    except:
        print("Logged Out")
    home()


def closedb():
    global con, cur
    cur.close()
    con.close()


def adduser():
    global win
    win.destroy()
    win = Tk()
    win.title('Add User')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    name = Label(win, text='NAME')
    usid = Label(win, text='USER ID')
    branch = Label(win, text='BRANCH')
    mob = Label(win, text='MOBILE NO')
    global e1, b
    e1 = Entry(win, width=25)
    global e2
    e2 = Entry(win, width=25)
    global e3
    e3 = Entry(win, width=25)
    global e4
    e4 = Entry(win, width=25)
    b = Button(win, height=2, width=21, text=' ADD USER ', command=addusers)
    b1 = Button(win, height=2, width=21, text=' CLOSE ', command=closeusers)
    name.place(x=70, y=100)
    usid.place(x=70, y=140)
    branch.place(x=70, y=180)
    mob.place(x=70, y=220)
    e1.place(x=180, y=100)
    e2.place(x=180, y=140)
    e3.place(x=180, y=180)
    e4.place(x=180, y=220)
    b.place(x=178, y=250)
    b1.place(x=178, y=293)
    win.mainloop()


def addusers():
    connectdb()
    q = 'INSERT INTO Login VALUE("%s","%i","%s","%i")'
    global con, cur
    cur.execute(q % (e1.get(), int(e2.get()), e3.get(), int(e4.get())))
    con.commit()
    win.destroy()
    messagebox.showinfo("User", "User Added")
    closedb()
    admin()


def closeusers():
    global win
    win.destroy()
    admin()


def viewuser():
    win = Tk()
    win.title('View User')
    win.geometry("800x300+270+180")
    win.resizable(False, False)
    treeview = Treeview(win, columns=("Name", "User ID", "Branch", "Mobile No"), show='headings')
    treeview.heading("Name", text="Name")
    treeview.heading("User ID", text="User ID")
    treeview.heading("Branch", text="Branch")
    treeview.heading("Mobile No", text="Mobile No")
    treeview.column("Name", anchor='center')
    treeview.column("User ID", anchor='center')
    treeview.column("Branch", anchor='center')
    treeview.column("Mobile No", anchor='center')
    index = 0
    iid = 0
    connectdb()
    details = cur.fetchall()
    for row in details:
        treeview.insert("", index, iid, value=row)
        index = iid = index + 1
    treeview.pack()
    win.mainloop()
    closedb()


def deleteuser():
    global win
    win.destroy()
    win = Tk()
    win.title('Delete user')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    usid = Label(win, text='USER ID')
    paswrd = Label(win, text='ADMIN \n PASSWORD')
    global e1
    e1 = Entry(win)
    global e2, b2
    e2 = Entry(win)
    b1 = Button(win, height=2, width=17, text=' DELETE ', command=deleteusers)
    b2 = Button(win, height=2, width=17, text=' CLOSE ', command=closeusers)
    usid.place(x=80, y=100)
    paswrd.place(x=70, y=140)
    e1.place(x=180, y=100)
    e2.place(x=180, y=142)
    b1.place(x=180, y=180)
    b2.place(x=180, y=230)
    win.mainloop()


def deleteusers():
    connectdb()
    if e2.get() == 'admin':
        q = 'DELETE FROM Login WHERE userid="%i"'
        cur.execute(q % (int(e1.get())))
        con.commit()
        win.destroy()
        messagebox.showinfo("Delete", "User Deleted")
        closedb()
        admin()
    else:
        messagebox.showinfo("Error", "Incorrect Password")
        closedb()


def connectdb():
    global con, cur
    # Enter your username and password of MySQL
    con = p.connect(host="localhost", user="root", passwd="nandini2123")
    cur = con.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS Library')
    cur.execute('USE Library')
    global enter
    if enter == 1:
        l = 'CREATE TABLE IF NOT EXISTS Login(name varchar(20),userid varchar(20),branch varchar(20),mobile bigint)'
        b = 'CREATE TABLE IF NOT EXISTS Book(subject varchar(20),title varchar(20),author varchar(20),serial int(20))'
        i = 'CREATE TABLE IF NOT EXISTS BookIssue(stdid varchar(20),serial varchar(20),issue date,exp date)'
        cur.execute(l)
        cur.execute(b)
        cur.execute(i)
        enter = enter + 1
    query = 'SELECT * FROM Login'
    cur.execute(query)


def home():
    try:
        global window, b1, b2, e1, e2, con, cur, win
        window = Tk()
        window.title('BOOK-VERSE')
        window.resizable(False, False)
        window.geometry("400x400+480+180")
        # wel=Label(window,text='LIBRARY',font='Helvetica 28 bold')
        # lib=Label(window,text='MANAGEMENT',font='Helvetica 28 bold')
        usid = Label(window, text='USER ID')
        paswrd = Label(window, text='PASSWORD')
        e1 = Entry(window, width=22)
        e2 = Entry(window, width=22)
        b1 = Button(window, text=' LOGIN AS BookVerse', height=2, width=20, command=loginlibr)
        b2 = Button(window, text=' LOGIN AS ADMIN ', height=2, width=20, command=loginadmin)
        # wel.place(x=160,y=20)
        # lib.place(x=110,y=70)
        usid.place(x=70, y=100)
        paswrd.place(x=70, y=140)
        e1.place(x=180, y=100)
        e2.place(x=180, y=140)
        b1.place(x=175, y=180)
        b2.place(x=175, y=225)
        window.mainloop()
    except Exception:
        window.destroy()


enter = 1
home()