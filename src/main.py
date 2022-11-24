from urllib.request import Request, urlopen
import re
from bs4 import BeautifulSoup

# Function to get the page content
def get_page_content(url, head):
  """
  Function to get the page content
  """
  req = Request(url, headers=head)
  return urlopen(req)

url = 'https://www.ticketswap.nl/event/qlimax-2022/regular-ticket/56938753-d3c2-4c78-bc5f-0144f4c6ee76/1821874?'
head = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
  'Accept-Encoding': 'none',
  'Accept-Language': 'en-US,en;q=0.8',
  'Connection': 'keep-alive',
  'refere': 'https://ticketswap.nl',
  'cookie': """your cookie value ( you can get that from your web page) """
}

data = get_page_content(url, head).read()
# findlink = re.compile("www.ticketswap.nl/listing/qlimax-2022/*")
# data = data.decode('utf-8')
# links = re.findall(findlink, data)
# print(links)

soup = BeautifulSoup(data, "html.parser")

# traverse paragraphs from soup

links = []

for link in soup.find_all('a'):
#    print(link)
   data = link.get('href')
   links.append(data)

print(links[10])

   



