for i in range(5):  #whitespace matters, for loops end when not indented
    print(i)
print()

for i in range(5,10):
    print(i)
print()

for i in reversed(range(5)):
    print(i)
print()

for i in range(2, 10, 2):
    print(i)
print()

for i in range(10, 2, -1):
    print(i)
print()

monsters = ("ghost", "vampire", "werewolf", "zombie")

for monster in monsters:
    print(monster)
print()

for idx, monster in enumerate(monsters):
    print(idx, monster)
print()

harry = {
    "name": "Harry",
    "age": 42,
    "species": "werewolf"
}

for i in harry.values():
    print(i)
print()

for key, val in harry.items():
    print(key, val)
print()

questions = ["name", "age", "species"]
answers = ["Bob", 21, "zombie"]

for question, answer in zip(questions, answers):
    print(f"What is your {question}? My {question} is {answer}.")
print()

i = 0
while i < 5:
    print(i)
    i += 1
print()