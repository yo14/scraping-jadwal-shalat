import bs4
import requests

url = 'https://jadwalsholat.pkpu.or.id/?id=67'

contents = requests.get(url)

print(contents.text)