import requests
import bs4
data = requests.get("https://kun.uz/")
print(data)
soup = bs4.BeautifulSoup(data.text, "html.parser")
rows = soup.select("#mob-container > li")
print("-------------------------")
for row in rows:
    columns = row.find_all("td")
    # print(columns)
    if len(columns) >= 4:
            print(column.text.strip())
