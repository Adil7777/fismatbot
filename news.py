import os.path
import requests
from bs4 import BeautifulSoup


class News:
    host = 'https://almaty.fizmat.kz'
    url = 'https://almaty.fizmat.kz/o-shkole/novosti-i-meropriyatiya/'
    last_key = ''
    last_key_file = ''

    def __init__(self, lastkey_file):
        self.lastkey_file = lastkey_file

        if os.path.exists(self.lastkey_file):
            self.lastkey = open(lastkey_file, 'r').read()
        else:
            f = open(lastkey_file, 'w')
            self.lastkey = self.get_news()
            # print(self.lastkey)
            f.write(self.lastkey)
            f.close()

    def get_news(self):
        r = requests.get(self.url)
        html = BeautifulSoup(r.content, 'html.parser')

        s = html.findAll('h2', {'class': 'ttl'})
        mas = []
        mas2 = []
        for i in s:
            mas2.append(str(i).replace('<h2 class="ttl">', '').replace('\n', '').replace('</h2>', '').replace('<a ',
                                                                                                              '').replace(
                '</a>', ''))
            mas.append(i.text)

        # print(mas2[0][6:73])

        return str(mas[0])

    def new_news(self):
        r = requests.get(self.url)
        html = BeautifulSoup(r.content, 'html.parser')

        s = html.findAll('h2', {'class': 'ttl'})
        mas = []
        mas2 = []
        for i in s:
            mas2.append(str(i).replace('<h2 class="ttl">', '').replace('\n', '').replace('</h2>', '').replace('<a ',
                                                                                                              '').replace(
                '</a>', ''))
            mas.append(i.text)

        self.href = mas2[0][6:73]
        self.new = str(mas[0])
        old = open(self.lastkey_file, 'r').read()
        if self.new == old:
            return True
        else:
            f = open(self.lastkey_file, 'w')
            f.write(self.new)
            f.close()
            return False

    def get_href(self):
        return self.href, self.new
