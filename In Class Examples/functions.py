def hello(name):
    print("Hello " + name)

hello("Bob")

people = ("Fred", "Sally", "Jim", "Diane")

def greetPeople(greeting, peeps):
    for person in peeps:
        print(f"{greeting} {person}!")

greetPeople("Hey", people)