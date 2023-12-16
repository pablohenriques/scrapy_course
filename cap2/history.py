from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = urlopen('https://pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    name_list = bs.findAll('span', {'class': 'green'})

    for name in name_list:
        print(name.get_text())
