bob = {
    "name": "Bob",
    "age": 21,
    "species": "zombie"
}
print(bob)
bob["age"] = 22
print(bob["age"])
print(bob["species"])

bobs_hobbies = ["eating brains", "walking aimlessly", "moaning"]
bob["hobbies"] = bobs_hobbies
print(bob)
print(bob["hobbies"][1]) 

my_fish = [1, 2, "red", "blue"]
my_fish.append(bob)
print(my_fish)
print(my_fish[4]["hobbies"][2])

monsters = {
    1: "Zombie",
    2: "Vampire",
    3: "Ghost",
    0: "Werewolf"
}

print(monsters[2])