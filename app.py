import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=67'

contents = requests.get(url)

response = bs4.BeautifulSoup(contents.text, "html.parser")

data = response.find_all('tr','table_highlight')[0]

shalat = {}
i = 0
for d in data:
    if i == 1:
        shalat['Shubuh'] = d.get_text()
    elif i == 2:
        shalat['Zhuhur'] = d.get_text()
    elif i == 3:
        shalat['Ashr'] = d.get_text()
    elif i == 4:
        shalat['Magrib'] = d.get_text()
    elif i == 5:
        shalat['Isya'] = d.get_text()

    i += 1

print(shalat)














