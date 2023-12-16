from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
    html = urlopen('https://pythonscraping.com/pages/page3.html')
    bs = BeautifulSoup(html.read(), 'html.parser')

    find = bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()
    print(find)
