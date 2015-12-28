# coding: utf-8

from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name = 'termdic',
    version = version,
    author = 'hzwer',
    author_mail = '598460606@163.com',
    url = 'https://github.com/hzwer/termdic',
    description = 'Dictionary in your terminal',
    keywords = 'dictionary, terminal',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'requests',
        'termcolor',
    ],
    entry_points = {
        'console_scripts': [
            'tdic = termdic.termdic:main'
        ]
    },
)
