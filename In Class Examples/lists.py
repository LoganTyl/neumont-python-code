my_fish = [1,2,"red", "blue"]
print(my_fish)
print(my_fish[2])

my_fish.append("blue")
my_fish.append(True)
print(my_fish)

print(len(my_fish))

print(my_fish[:-2])
print(my_fish[::-1])

print(my_fish.index("blue"))
print(my_fish.count("blue"))
print("blue" in my_fish)

import copy
my_list = copy.deepcopy(my_fish) #deep copy
# my_list = my_fish.copy() shallow copy
# my_list = my_fish.[:] works like above
my_fish[3] = "green"
print(my_list, my_fish)