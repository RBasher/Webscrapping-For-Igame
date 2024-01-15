import csv
import requests
from bs4 import BeautifulSoup

url = "https://apps.apple.com/us/genre/ios-games/id6014"
html = requests.get(url)
s = BeautifulSoup(html.content, 'html.parser')
x = s.find(id="selectedcontent")
y = x.find_all("a")
# Create a list to store game names
game = [["Game Name"]]  # Add a header row
for i in y:
    game.append([i.text])
print(game)
with open('igame.csv', 'w+', encoding="utf-8", newline='') as file:
    write = csv.writer(file)
    for row in game:
        write.writerow(row)