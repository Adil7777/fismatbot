import re
import os.path
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

host = 'https://almaty.fizmat.kz'
url = 'https://almaty.fizmat.kz/o-shkole/novosti-i-meropriyatiya/'

last_key = ''
last_key_file = ''

r = requests.get(url)
html = BeautifulSoup(r.content, 'html.parser')

s = html.findAll('h2', {'class': 'ttl'})
print(s)
