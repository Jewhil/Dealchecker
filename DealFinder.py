#!/usr/local/bin/python3.4
import requests
import re
import csv
from bs4 import BeautifulSoup

link = ""  #only works for this currently 

# make GET request 
page = requests.get(link)

htmlCode = BeautifulSoup(page.content, 'html.parser')#HTML code is saved as a variable (One big stream) Create BeautifulSoup object to parse html
pattern = ">([^<>/,]*?)<" #pattern uses regex to parse code. Link:   https://regex101.com/

titles = htmlCode.find_all(class_='deal__title') # finds html class for deal title on webpage 
deals = htmlCode.find_all(class_='deal__info') # finds html class for deal infos on webpage #deal__modal--content--description
#contents = htmlCode.find_all(class_='deal__modal--content--description')
title_list = re.split(pattern, str(titles))#splits titles into list
deal_list = re.split(pattern, str(deals)) #same but deals
#contents_list = re.split(pattern, str(contents))
'''
# check html status code for response (success code - 200)
print(page)
# prints content of request 
print(page.content)
'''
print("Checking URL: " + page.url + " for deals")
#print status code
#print("Response code: " + str(page.status_code))
#print(htmlCode.prettify())
print()
#print(htmlCode.string) # print title tag
print(htmlCode.title.string) # get name of the tag
# Getting the name of parent tag
#print(htmlCode.title.parent.name)
#print(titles)
#print(deals)
for title, deal in zip(title_list, deal_list):
    print("==============")
    print(title) #for some reason, not printing correctly
    print(deal)
    #print(content)
    print("==============")