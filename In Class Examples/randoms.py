import random

results = ""
for i in range(50):
    results += str(random.randint(1,10)) + " "  # 1 and 10 are inclusive

print(results)
print()

results = ""
for i in range(50):
    results += str(random.random()) + " " 

print(results)
print()

my_list = [4, "George", True, 18, "Sally", "bread"]
for i in range(10):
    print(random.choice(my_list))
print()

my_list = ["one", "two", "three", "four", "five"]
random.shuffle(my_list)
print(my_list)
print()

results = ""
for i in range(50):
    results += str(random.randrange(1,10,2)) + " " 
print(results)
print()

results = ""
for i in range(50):
    results += str(random.randrange(2,10,2)) + " "      # 10 is exclusive
print(results)
print()