from os import listdir
from PIL import Image

def checkCounter(counter):
    while len(str(counter)) != 4:
        counter = "0" + str(counter)
    return counter

counter = 1

image_list = listdir('images/')
for i in range(len(image_list)):
    counter = checkCounter(counter)
    outfile = "new_images/pic" + counter + ".png"
    infile = Image.open("images/" + image_list[i])
    infile = infile.convert("LA")
    infile = infile.rotate(270)
    infile = infile.crop((25, 0, 225, 200))
    infile = infile.resize((75, 75))
    infile.save(outfile, "PNG")
    counter = int(counter)
    counter += 1
