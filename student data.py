from tkinter import *
from tkinter import messagebox
import mysql.connector

def add_funct():
    if rollno.get() == "" or name.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields")
    else:
        conn = mysql.connector.connect(host="localhost", user="root", password="nandini2123", database="customerdata")
        curr = conn.cursor()
        curr.execute("INSERT INTO studentdata VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                     (rollno.get(), name.get(), unit1.get(), unit2.get(), unit3.get(), unit4.get(), unit5.get(), record_submitted.get()))
        try:
            conn.commit()
            messagebox.showinfo("Success", "Data entered successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            conn.close()


win = Tk()
win.geometry("1370x700+0+0")
win.title("Book verse")

tit = Label(win, text="Book verse", bg="red", font=("ARIAL", 30), fg="blue")
tit.pack(side=TOP, fill='x')

fr = Frame(win, border=12, bg="lightgrey")
fr.place(x=350, y=95, height=700, width=700)

name = StringVar()
rollno = StringVar()
unit1 = StringVar()
unit2 = StringVar()
unit3 = StringVar()
unit4 = StringVar()
unit5 = StringVar()
record_submitted = BooleanVar()

namelbl = Label(fr, text="Reading now : ", font=("ARIAL", 20), bg="lightgrey")
namelbl.grid(row=0, column=1, padx=12, pady=2)
nameent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=name)
nameent.grid(row=0, column=2, padx=12, pady=2)

rollnolbl = Label(fr, text="Books and documents : ", font=("ARIAL", 20), bg="lightgrey")
rollnolbl.grid(row=1, column=1, padx=12, pady=2)
rollnoent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=rollno)
rollnoent.grid(row=1, column=2, padx=12, pady=2)

unit1lbl = Label(fr, text="Favorites :", font=("ARIAL", 20), bg="lightgrey")
unit1lbl.grid(row=2, column=1, padx=12, pady=2)
unit1ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit1)
unit1ent.grid(row=2, column=2, padx=12, pady=2)

unit2lbl = Label(fr, text="Saved : ", font=("ARIAL", 20), bg="lightgrey")
unit2lbl.grid(row=3, column=1, padx=12, pady=2)
unit2ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit2)
unit2ent.grid(row=3, column=2, padx=12, pady=2)

unit3lbl = Label(fr, text="Download : ", font=("ARIAL", 20), bg="lightgrey")
unit3lbl.grid(row=4, column=1, padx=12, pady=2)
unit3ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit3)
unit3ent.grid(row=4, column=2, padx=12, pady=2)

unit4lbl = Label(fr, text="Collections : ", font=("ARIAL", 20), bg="lightgrey")
unit4lbl.grid(row=5, column=1, padx=12, pady=2)
unit4ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit4)
unit4ent.grid(row=5, column=2, padx=12, pady=2)

unit5lbl = Label(fr, text="Trash :", font=("ARIAL", 20), bg="lightgrey")
unit5lbl.grid(row=6, column=1, padx=12, pady=2)
unit5ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit5)
unit5ent.grid(row=6, column=2, padx=12, pady=2)
unit6lbl = Label(fr, text="Feedback : ", font=("ARIAL", 20), bg="lightgrey")
unit6lbl.grid(row=6, column=1, padx=12, pady=2)
unit6ent = Entry(fr, font=("ARIAL", 20), bg="lightgrey", textvariable=unit5)
unit6ent.grid(row=6, column=2, padx=12, pady=2)

submit_checkbox = Checkbutton(fr, text="Record Submitted", font=("ARIAL", 16), bg="lightgrey",
                              variable=record_submitted)
submit_checkbox.grid(row=7, columnspan=3, padx=12, pady=2)
Submit_btn = Button(fr, text="Save Data", bd=5, command=add_funct)
Submit_btn.place(x=100, y=350, height=50, width=200)

win.mainloop()
