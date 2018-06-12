#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = "https://www.humblebundle.com/books/pocket-primers-books"
rsp = requests.get(url)

soup = BeautifulSoup(rsp.text, 'html.parser')



tier_headers = soup.select(".dd-header-headline")
for tier in tier_headers:
	print(tier.text.strip())

#we need to snag tier name and prices
#proto-datastructure below
tiers = {
	"tier1":{
		"price":500,
		"products":[
			"name1",
			"name2"
		]
	},
	"tier2":{
		"price":700,
		"products":[
			"name1",
			"name2"
		]
	}
}	

# python list comprehensions
# [key for key in var.keys()]
# makes list from another operation


