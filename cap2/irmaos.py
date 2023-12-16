from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    for siblings in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
        print(siblings)
