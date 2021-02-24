import openpyxl as xl
import re
from urlextract import URLExtract
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

#import items.xlsx and sets up workbook/worksheet
wb = xl.load_workbook('items.xlsx')
ws = wb['itemlist']

#url extractor method setup
urlExtractor = URLExtract()

#function variables
found_item_url = ""

#item checker function that returns unparsed hyperlink
def itemChecker(user_item_input):
  for row in ws.iter_rows():
    for entry in row:
      try:
        if user_item_input in entry.value: #need spell check
          item_input = entry.value
          return item_input
      except (AttributeError, TypeError):
        continue

item_input = itemChecker(input("what item are you looking for?(case sensitive): "))

#url extractor method that takes unparsed hyperlink
for url in urlExtractor.gen_urls(item_input):
  found_item_url = url
  print(found_item_url)

#creates connection to the site's html
uClient = uReq(found_item_url)

#makes it so we can traverse the html
soupy = soup(uClient.read(), "html.parser")
uClient.close()

#finds percentages from the main div's p tags
testContainer = soupy.find("div", {"class": "mw-parser-output"}).findAll('p')
print(testContainer)
#r'\d*%'
testContainerPercents = print(re.findall(r'^d+(\.d{1,2})?$', str(testContainer))) #does not account for decimals in the percentage

#for items in testContainerPercents:
