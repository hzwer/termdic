# coding: utf-8

import re
import sys
import requests
from termcolor import colored as cl


def look_up(word):
    url = 'http://dict.youdao.com/search?q='
    r = requests.get(url + word)
    content = r.text

    try:
        ps = re.findall(re.compile('"phonetic">(.*?)</span>'), content)
        pattern = re.compile('"trans-container">(.*?)</div>', re.S)
        tmp = re.findall(pattern, content)
        mean = re.findall(re.compile('<li>(.*?)</li>'), tmp[0])
    except:
        print('Can\'t find it')
        return

    if len(ps) is 2:
            print(cl(u'英{0} 美{1}'.format(ps[0], ps[1]), 'cyan'))
    else:
        try:
            print(cl(ps[0]), 'cyan')
        except:
            pass
    for line in mean:
        words = line.split('.', 1)
        if len(words) is 2:
            words[0] += '.'
            print(u'{0}{1}'.format(cl(words[0], 'green'), cl(words[1], 'blue')))
            # word
        else:
            print(u'{0}'.format(cl(words[0], 'blue')))
            # phrase


def main():
    args = sys.argv[1:]
    word = " ".join(args)
    if word:
        look_up(word)
    else:
        pass

if __name__ == '__main__':
    main()
