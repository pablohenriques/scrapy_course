from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    # for child in bs.find('table', {'id': 'giftList'}).children:
    for child in bs.find('table', {'id': 'giftList'}).descendants:
        print(child)
