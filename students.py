import json

# Used to edit the students.json file in terminal
# Alternatively, just edit the .json directly

data = {
    "student": "",
    "parent": "",
    "email": "",
    "rate": ""
} 

def new_student(name, data, filename=fr".\students.json"):
    with open(filename,'r+') as jsonfile:
          # First we load existing data into a dict.
        students = json.load(jsonfile)
        # Join new_data with file_data inside students
        students[name]=data
        # Sets file's current position at offset.
        jsonfile.seek(0)
        # convert back to json.
        json.dump(students, jsonfile, indent = 4)

def delete_student(name, filename=fr".\students.json"):
    with open(filename,'r+') as jsonfile:
          # First we load existing data into a dict.
        students = json.load(jsonfile)
        # Join new_data with file_data inside students
        if name in students:
            print("Entry deleted successfully.")
            del students[name]
        else:
            print("Entry not found in dictionary.")
            return 0
        # Sets file's current position at offset.
    with open(filename,'w') as jsonfile:
        json.dump(students, jsonfile, indent = 4)

def delete_all_students(filename=fr".\students.json"):
    with open (filename, 'w') as jsonfile:
        empty = {}
        json.dump(empty, jsonfile, indent = 4)

def update_student(name, data, newvalue, filename=fr".\students.json"):
    with open(filename,'r+') as jsonfile:
          # First we load existing data into a dict.
        students = json.load(jsonfile)
        # Join new_data with file_data inside students
        try:
            x=students[name][data]
            students[name][data]=newvalue
            print("Entry updated successfully.")
        except:
            print("Entry not found in dictionary.")
            return 0
        # Sets file's current position at offset.
        jsonfile.seek(0)
        # convert back to json.
        json.dump(students, jsonfile, indent = 4)

# while True:
#     t = input("Selection: ")
#     if t == '1':
#         newname = input("Name: ")
#         new_student(newname, data)
#     if t == '2':
#         newname = input("Name: ")
#         delete_student(newname)
#     if t =='3':
#         newname = input("Name: ")
#         index = input("What will you update: ")
#         newvalue = input(f"New value for '{index}': ")
#         update_student(newname, index, newvalue)
#     if t =='4':
#         delete_all_students()

