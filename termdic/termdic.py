# coding: utf-8

import os
import re
import sys
import requests
from termcolor import colored as cl


class queryInfo:
	speak = False

info = queryInfo

def speakWord(word):
	if sys.platform == 'darwin':
		os.system('say ' + str(word))
	else:
		os.system('espeak ' + str(word))

def lookUp(word):
	url = 'http://dict.youdao.com/search?q='
	try:
		r = requests.get(url + word)
	except e:
		print e
		return 
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
			print(cl(ps[0], 'cyan'))
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

	if info.speak:
		speakWord(word)


def printVersion():
	from termdic import __version__
	print('termdic v{}'.format(__version__))
	sys.exit(0)


def printUsage():
	print('usage: termdic [-v] [word] [word -p]')
	sys.exit(0)

def terminalModel():
	while True:
		print ">>> ", 
		temp = sys.stdin.readline().strip('\n').split()
		if len(temp) > 1:
			print "Syntax Error!"
			print "Use :q to exit."
			continue
		elif len(temp) == 0: 
			continue
		
		word = temp[0]
		if word == ":q":
			return 
		else:
			lookUp(word)


def main():
	args = sys.argv[1:]
	pivot = ""
	for x in args:
		if x == '-p':
			info.speak = True
		else:
			if pivot:
				print "Syntax Error!"
				print "Use -u to learn the usage."
				return
			else:
				pivot = x
	if pivot == '-v':
		printVersion()
	elif pivot == '-u':
		printUsage()
	elif pivot:
		lookUp(pivot)
	else:
		terminalModel()

if __name__ == '__main__':
	main()
