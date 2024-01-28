from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_best-selling_video_games"
page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")

the_table = soup.find(class_="wikitable")
the_tds = the_table.find_all('td')

total_list = []
game_list = []

for element in the_tds:
    if element.find("a"):
        contents = element.find("a").contents[0]
    elif element.find("span"):
        contents = element.find("span").contents[0]
    else:
        contents = element.contents[0]
    
    contents = str(contents)
    contents = contents.replace("\n", "")
    
    game_list.append(contents)
    if len(game_list) == 7:
        total_list.append(game_list.copy())
        game_list.clear()

print(total_list)
# for i in range(len(total_list)):
#     print(total_list[i])