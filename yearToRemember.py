import random

userScore = 0

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
print()

for event in range(len(eventInfo)-1):
    eventName = eventInfo[event][0]
    eventYear = eventInfo[event][1]
    userGuess = input(f"In what year was {eventName}? Your Answer: ")
    try:
        userGuess = int(userGuess)
        if userGuess==eventYear:
            userScore += 10
            print(f"You got it right! You got 10 points. Your score is now {userScore}")
        elif abs(userGuess-eventYear) <= 5:
            userScore += 5
            print(f"So close! The correct year was {eventYear}. You got 5 points. Your score is now {userScore}.")
        elif abs(userGuess-eventYear) <= 10:
            userScore += 2
            print(f"Not quite. The correct year was {eventYear}. You got 2 points. Your score is now {userScore}.")
        elif abs(userGuess-eventYear) <= 20:
            userScore += 1
            print(f"That barely counts... The correct year was {eventYear}. You got 1 point. Your score is now {userScore}.")
        else:
            print(f"Ouch. Not even close. The correct year was {eventYear}.  Your score is still {userScore}.")
        print()
    except:
        quit()

feedback = ""

if userScore == 100:
    feedback = "You got a perfect score. Congratulations!"
elif userScore >= 80:
    feedback = "You almost got it! Give that little extra push!"
elif userScore >= 60:
    feedback = "You've got a general idea. Remember to keep those dates in mind!"
elif userScore >= 40:
    feedback = "Not bad, but you might want to hit the history books soon."
elif userScore >= 20:
    feedback = "There's a lot of room for improvement."
elif userScore >= 0:
    feedback = "Unfortunate."
else:
    feedback = "How did you even get this score?"

print(f"Your final score is {userScore}. {feedback}")
