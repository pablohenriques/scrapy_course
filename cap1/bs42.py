from urllib.error import HTTPError
from urllib.error import URLError
from urllib.request import urlopen

if __name__ == '__main__':
    try:
        html = urlopen("http://www.pythonscraping.com/pages/page1.html")
    except HTTPError as e:
        print("The server cloud returned un HTTP error")
    except URLError as e:
        print("The server cloud not be found")
    else:
        print(html.read())
