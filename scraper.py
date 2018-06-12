#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/pocket-primers-books"
rsp = requests.get(url)

soup = BeautifulSoup(rsp.text, 'html.parser')