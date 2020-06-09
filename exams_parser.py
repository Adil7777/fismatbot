from bs4 import BeautifulSoup
import requests

url = 'https://almaty.fizmat.kz/uchenikam/akr-i-yekzameny/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
page = requests.get(url, headers)
content = BeautifulSoup(page.content, 'html.parser')
exams_1 = content.findAll('td', {'width': '139'})
exams = []
counter = 0
for text in exams_1:
    a = text.text.replace('\n', ' ')
    # a = a.replace(',', '')
    if counter <= 3:
        exams.append(a)
    else:
        if counter == 4:
            exams[counter - 4] += ' {} английский язык'.format(a)
        else:
            exams[counter - 4] += ' {}'.format(a)
    counter += 1

