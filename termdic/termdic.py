# coding: utf-8

import re
import sys
import requests
from termcolor import colored 

def look_up(word):
    url = 'http://dict.youdao.com/search?q='
    r = requests.get(url + word)
    content = r.text

    try:
        ps = re.findall(re.compile('<span class="phonetic">(.*?)</span>'), content)
        tmp = re.findall(re.compile('<div class="trans-container">(.*?)</div>', re.S), content)
        mean = re.findall(re.compile('<li>(.*?)</li>'), tmp[0])
    except:
        print('Can\'t find it')
        return
    
    if len(ps) is 2:
        try:
            print(colored('英{} 美{}'.format(ps[0], ps[1]), 'cyan'))
        except:
            pass
    else:
        try:
            print(colored(ps[0]), 'cyan')
        except:
            pass
    
    for line in mean:
        words = line.split('.', 1)
        words[0] += '.'
        print('{}{}'.format(colored(words[0], 'green'), colored(words[1], 'blue')))

def main():
    args = sys.argv[1:]
    word = " ".join(args)
    if word:
        look_up(word)
    else:
        pass

if __name__ == '__main__':
    main()
