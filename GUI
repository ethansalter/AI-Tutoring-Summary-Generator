from tkinter import *       
from tkinter.ttk import *
import main

def run():
    output = main.messageReturn(student.get(),hours.get(),subject.get(),topic.get(),confusion.get(),strength.get(),suggestion.get(),goal.get(),g.get())
    T.delete("1.0",END)
    T.insert(END, output)

def upload():
    if main.upload(student.get(),hours.get(),subject.get(),topic.get(),confusion.get(),strength.get(),suggestion.get(),goal.get(),g.get(),T.get("1.0",END)) == 1:
        T.delete("1.0",END)
        T.insert(END, "Uploaded successfully.")

root = Tk()
root.geometry('800x600')     
root.title("Tutoring Summary")

row = Frame(root)
row.pack(side=TOP, padx=5, pady=30)

# Create label
l = Label(row, text = "Tutoring Summary")
Font_tuple = ("Ariel", 20)
l.configure(font = Font_tuple)
l.pack()

#Student name
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=80, text=f"Student's Name:", anchor='w')
label.pack(side=LEFT)
dropdown = StringVar(row)
dropdown_menu = OptionMenu(row, dropdown, "Select:", "Davin", "JT", "Rory")
dropdown_menu.pack(side=RIGHT, expand=YES, fill=X)
student=dropdown

#Time
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"Hours: ", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
hours=entry

#Subject
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"Subject (math, chemistry...)", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
subject=entry

#Topic
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"Topic covered", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
topic=entry

#Out of 5
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"How well did he do out of 5?", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
g=entry

#Confusion
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"Topic of confusion", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
confusion=entry

#Strength
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"Topic of strength", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
strength=entry

#Suggestion
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"My suggestion", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
suggestion=entry

#Goal
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
label = Label(row, width=40, text=f"My goal for the student", anchor='w')
entry = Entry(row)
label.pack(side=LEFT)
entry.pack(side=RIGHT, expand=YES, fill=X, ipadx=100)
goal=entry

#Button
row = Frame(root)
row.pack(side=TOP, padx=5, pady=5)
button = Button(row, text="Generate Summary", command=run)
button.pack(side=LEFT, padx=5, pady=5)

button = Button(row, text="Send Message", command=upload)
button.pack(side=LEFT, padx=5, pady=5)

T = Text(root, wrap=WORD, width = 120)
T.pack(fill=Y, expand=1)
Font_tuple = ("Ariel", 10)
T.configure(font = Font_tuple)
text=T

row = Frame(root)
row.pack(side=TOP, padx=5, pady=10)

root.mainloop()
