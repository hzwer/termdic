# coding: utf-8

import sys
import requests
from bs4 import BeautifulSoup as bs

def look_up(word):
    url = 'http://dict.youdao.com/search?q='
    r = requests.get(url + word)
    content = r.text
    soup = bs(content, "lxml")

    try:
        ps = soup.find('div', {'class': 'baav'}).find_all('span', {'class': 'phonetic'})
        mean = soup.find('div', {'class': 'trans-container'}).find('ul').get_text()
    except:
        print('Can\'t find it')
        return
        
    if len(ps) is 2:
        print('英{} 美{}'.format(ps[0].get_text(), ps[1].get_text()))
    else:
        try:
            print(ps[0].get_text())
        except:
            pass
    print(mean.strip())

if __name__ == '__main__':
    args = sys.argv[1:]
    word = " ".join(args)
    if word:
        look_up(word)
    else:
        pass
