import json
import os
import time
import subprocess
import yagmail
import openai

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def message():
    prompt=""
    evernote=""
    try:
        with open(os.path.join(os.path.dirname(__file__), "students.json"),'r') as jsonfile:
            # First we load existing data into a dict.
            students = json.load(jsonfile)
            studentList=', '.join(students.keys())
    except:
        input("Error reading file. Please reinstall program and or check for json file existance.")
        quit()
    
    while True:
        student=input(f"Student's name? ({studentList}): ")
        if student in students.keys():
            parent= students[student]["parent"]
            # email = students[student]["email"]
            email = 'ethansalter3.7d4e112@m.evernote.com'
            rate = students[student]["rate"]
            break
        elif student =="quit":
            quit()
        print("Please enter a valid name.")
    
    while True:
        hours = input("How many hours was the session? (ex. '1', '1.5'): ")
        try:
            float(hours)
            break
        except:
            print("Please enter a valid number.")

    payment = str(round(float(rate)*float(hours)))+"$"
    subject = input("The subject of today's session was (math, chemistry, ect.) ___: ")
    specificSubject = input("Today we covered ___: ")
    while True:
        g= input("Out of 5, how well did he understand the material? (0-5): ")
        try:
            if int(g)>=0 and int(g)<=5:
                break
        except:
            print("Please enter a valid number.")
    confusion = input("He was confused by ___: ")
    if confusion!="":
        confusion = f"Mention that {student} was confused by {confusion}. Please explain how to do this correctly. "
    strength = input("During the session, I was impressed by ___: ")
    if strength!="":
        strength = f"Mention that you were impressed by {strength}. "
    suggestion = input (f"I suggest that {student} ___: ")
    if suggestion!="":
        suggestion = f"Suggest that {student} {suggestion}. Please explain why {student} should do this. "
    parentSuggestion = input (f"I suggest that {parent} helps {student} by ___: ")
    if parentSuggestion!="":
        parentSuggestion = f"Suggest that {parent} helps {student} by "+parentSuggestion+". "
    goal = input(f"My goal for {student} is to ___: ")
    if goal!="":
        goal = f"Mention that your goal for {student} is to {goal}. Please offer {parent} advice on how {student} can achieve this goal. "

    prompt=f"You are a tutor named Ethan and your task is to write a tutoring summary for your student {student}. Please write an informative summary to his parent, {parent}. In the into, say 'Hi {parent}, I hope you are doing well! I had a productive {hours} hour long tutoring session with {student}.' Next, mention that the topic of the session today was {specificSubject}. Give {parent} an overview of this topic. Please make a list of the subtopics covered but do not use bullet points. After the list, please explain the significance of the topic and why it is important to learn it. {strength}{confusion}{suggestion}{parentSuggestion}{goal}In the conclusion, please make sure to thank {parent} and wish them a good night."
    
    #copy prompt to clipbord as a failsafe in case the AI writes a terrible message
    copy2clip(prompt)
    
    # evernote formatting
    evernote+=f"Date: {time.strftime('%m/%d/%y')}"+chr(10)
    evernote+=f"Subject: {subject}"+chr(10)
    evernote+=f"Content mastery: {int(g)*chr(9733)}{(5-int(g))*chr(9734)}"+chr(10)
    if float(hours)>1:
        evernote+=f"Session length: {hours}"+" hours"+chr(10)
    else:
        evernote+=f"Session length: {hours}"+" hour"+chr(10)
    evernote+=f"Cost: {payment}"+chr(10)
    evernote+=aiChat(prompt)
    sendEmail(student, email, evernote, subject)
    time.sleep(1)

def aiChat(prompt):
    try:
        print("Generating AI message...")
        api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
            )
        return response["choices"][0]["message"]["content"]
    except:
        print("Error generating message. Trying again.")
        return aiChat(prompt)

def sendEmail(student, email, message, subject):
    try:
        print("Uploading to Evernote...")
        title = (f"""{student}'s {subject} tutoring summary {time.strftime('%m/%d/%y')} @Tutoring #tutoringsummary""")
        yag = yagmail.SMTP('ethansalter3@gmail.com', 'tzpuoshogfilbtcd')
        yag.send(to = email, subject = title, contents = message)
        print("Message uploaded to Evernote.")
        return 0
    except:
        print("Error. Message could not be uploaded. Trying again...")
        sendEmail(student, email, message, subject)
        return 0

if __name__ == "__main__":
    while True:
        message()
