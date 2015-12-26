# coding: utf-8

import re
import sys
import requests
from bs4 import BeautifulSoup as bs
from termcolor import colored 
reload(sys)
sys.setdefaultencoding('utf-8')

def look_up(word):
    url = 'http://dict.youdao.com/search?q='
    r = requests.get(url + word)
    content = r.text
    soup = bs(content, "lxml")

    try:
        ps = soup.find('div', {'class': 'baav'}).find_all('span', {'class': 'phonetic'})
        mean = soup.find('div', {'class': 'trans-container'}).find('ul')
    except:
        print('Can\'t find it')
        return
    
    if len(ps) is 2:
        print(colored('英{} 美{}'.format(ps[0].get_text().decode('GBK'), ps[1].get_text().decode('GBK')), 'cyan'))
    else:
        try:
            print(colored(ps[0].get_text().decode()), 'cyan')
        except:
            pass
    
    tmp = re.split("\n", mean.decode().strip())
    for text in tmp:
        print(colored(text, 'cyan'))

def main():
    args = sys.argv[1:]
    word = " ".join(args)
    if word:
        look_up(word)
    else:
        pass

if __name__ == '__main__':
    main()
