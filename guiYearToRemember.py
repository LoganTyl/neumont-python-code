from tkinter import Tk, Label, Frame, Button, Entry, Message
import random

eventInfo = [
    ("the start of the Revolutionary War", 1775), 
    ("the US Constitution signed", 1783),
    ("President Lincoln assassinated", 1865),
    ("Theodore Roosevelt's first day in office as President of the US", 1901),
    ("the beginning of WW2", 1939),
    ("the first personal computer introduced", 1975),
    ("the Berlin Wall taken down", 1989),
    ("the end of WW1", 1918),
    ("Pokemon first released", 1996),
    ("Hawaii officially part of the US", 1959)
]
random.shuffle(eventInfo)

userScore = 0
questionNum = 0
userGuess = 0
eventYear = ""
feedback = ""

root = Tk()
root.title('GUI Year to Remember')

def finishGame():
    global userScore
    message_question.config(text="Game Over!\nYour final score is " + str(userScore) + ".")

def changeQuestion():
    global questionNum
    entry_guess.delete(0, 'end')
    questionNum += 1
    if questionNum >= len(eventInfo):
        finishGame()
    else:
        message_question.config(text="In what year was " + eventInfo[questionNum][0] + "?")

def checkAnswer():
    global userScore
    global eventYear
    global feedback
    global userGuess
    eventYear = eventInfo[questionNum][1]
    try:
        userGuess = int(entry_guess.get())
        if userGuess==eventYear:
            userScore += 10
            feedback = "You got it right! You got 10 points."
        elif abs(userGuess-eventYear) <= 5:
            userScore += 5
            feedback = f"So close! The correct year was {eventYear}. You got 5 points."
        elif abs(userGuess-eventYear) <= 10:
            userScore += 2
            feedback = f"Not quite. The correct year was {eventYear}. You got 2 points."
        elif abs(userGuess-eventYear) <= 20:
            userScore += 1
            feedback = f"That barely counts... The correct year was {eventYear}. You got 1 point."
        else:
            feedback = f"Ouch. Not even close. The correct year was {eventYear}."
    except:
        print("Exiting game")
        root.destroy()
    label_score.config(text="Score: " + str(userScore))
    message_question.config(text=feedback)
    root.after(3000, changeQuestion)

message_question = Message(
    text= "In what year was " + eventInfo[questionNum][0] + "?",
    bg = '#dda0dd', 
    fg = 'black',
    font = 'Verdana 20 italic'
)
message_question.grid(column = 0, row = 0)

frame_entry = Frame(root)
frame_entry.grid(column=0, row=1)

entry_guess=Entry(frame_entry)
entry_guess.pack(side = 'top')

btn_entry = Button(frame_entry,
    text = 'Submit',
    width = 9,
    command = checkAnswer
)
btn_entry.pack(side = 'top')

label_score = Label(
    text = "Score: 0",
    fg = 'black',
    font = 'Verdana 10'
)
label_score.grid(column = 0, row = 2)

root.mainloop()
