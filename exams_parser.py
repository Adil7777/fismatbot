from bs4 import BeautifulSoup
import requests


class Exam:
    def __init__(self):
        self.url = 'https://almaty.fizmat.kz/uchenikam/akr-i-yekzameny/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def parse_11(self):
        page = requests.get(self.url, self.headers)
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
        return '\n\n'.join(exams)


class Themes:
    def __init__(self):
        self.url = 'https://almaty.fizmat.kz/uchenikam/akr-i-yekzameny/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

    def parse(self):
        page = requests.get(self.url, self.headers)
        content = BeautifulSoup(page.content, 'html.parser')
        themes_1 = content.findAll('a', {'target': '_blank', 'rel': 'noopener'})
        first = []
        second = []
        third = []
        counter = 0
        second.append(
            'https://almaty.fizmat.kz/wp-content/uploads/sites/2/2019/11/AP_Calculus.jpg AP Calculus_Темы АКР (скачать)')

        for i in themes_1:
            if counter <= 5:
                first.append(str(i).replace('<a href="', '').replace('" rel="noopener" target="_blank">', ' ').replace(
                    '(скачать)</a>', ''))
            elif counter > 5 and counter <= 8:
                second.append(str(i).replace('<a href="', '').replace('" rel="noopener" target="_blank">', ' ').replace(
                    '(скачать)</a>', ''))
            elif counter <= 11:
                third.append(str(i).replace('<a href="', '').replace('" rel="noopener" target="_blank">', ' ').replace(
                    '(скачать)</a>', ''))
            counter += 1
        second.append(
            'https://almaty.fizmat.kz/wp-content/uploads/sites/2/2019/11/Informatika.pdf Информатика (скачать)')
        third.append(
            'https://almaty.fizmat.kz/wp-content/uploads/sites/2/2020/01/Angliyskiy-3-ch_compressed.pdf Английс'
            'кий язык (скачать)')
        third.append(
            'https://almaty.fizmat.kz/wp-content/uploads/sites/2/2020/01/3-ch-Kaz.yaz-i-literatura_rotated.pdf '
            'Каз.яз и литература (скачать)')
        first = '\n\n'.join(first)
        second = '\n\n'.join(second)
        third = '\n\n'.join(third)
        return first, second, third


a = Themes()
a.parse()
