monsters1 = ["vampire", "zombie", "ghost"]
monsters2 = ["vampire", "zombie", "ghost"]
monsters3 = ["vampire", "zombie", "werewolf"]

if monsters1 == monsters2:
    print("Yay, monsters are equal")

print(monsters1==monsters3)
print(monsters1!=monsters3)
print()

boolT = True
boolF = False

print(not boolT)    #!boolT does not work
print(not boolT == boolF)
print(not boolT is boolF)

print(isinstance(7,int))
print(isinstance(7.0,float))
print(isinstance("Zombie",str))
print(isinstance(boolT,bool))
print(isinstance("Zombie",int))
print()

if boolT and boolF is False:
    print("Wow, both are True")