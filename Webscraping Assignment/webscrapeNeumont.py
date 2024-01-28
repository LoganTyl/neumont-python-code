from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://neumont.smartcatalogiq.com/2019-2020/Catalog/Academic-Calendar-2018-2019"
page = urlopen(url)

soup = BeautifulSoup(page, "html.parser")

the_headings = soup.find_all('h2')
the_tables = soup.find_all('table')

total_list = []
calendar_list = []
alreadyPrinted = False

for i in range(len(the_tables)):
    contents = the_headings[i].text.strip()
    contents = str(contents)
    total_list.append(contents + "\n")
    print(contents)
    for element in the_tables[i]:
        if not alreadyPrinted:
            the_tds = the_tables[i].find_all('td')
            for element2 in the_tds:
                contents = element2.contents[0]
                contents = str(contents)
                calendar_list.append(contents)
                if len(calendar_list) == 2:
                    total_list.append(calendar_list[0] + ": " + calendar_list[1])
                    total_list.append("\n")
                    print(calendar_list[0] + ": " + calendar_list[1])
                    calendar_list.clear()
                    alreadyPrinted = True
    total_list.append("\n")
    print("")
    alreadyPrinted = False
    
file = open("webscrape.txt", "w")
for i in range(len(total_list)):
    list_string = str(total_list[i])
    file.write(list_string)
file.close()
