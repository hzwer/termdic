# coding: utf-8

from setuptools import setup, find_packages

version = '0.0.1'

setup(name = 'termdic',
      version = version,
      author = 'hzwer',
      author_mail = '598460606@163.com',
      url = 'https://github.com/hzwer/termdic',
      description = '终端下英文字典',
      keywords = 'dictionary in terminal',
      packages = find_packages(),
      include_package_data = True,
      zip_safe = False,
      install_requires = [
          'BeautifulSoup4',
          'requests',
      ],
      entry_points={
        'console_scripts':[
            'lk = termdic.termdic:main'
        ]
      },     
)
      
