import openpyxl as xl
from urlextract import URLExtract

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
        if user_item_input in entry.value:
          item_input = entry.value
          return item_input
      except (AttributeError, TypeError):
        continue

item_input = itemChecker(input("what item are you looking for? "))

#url extractor method that takes unparsed hyperlink
for url in urlExtractor.gen_urls(item_input):
  found_item_url = url
  print(found_item_url)
