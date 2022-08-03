import requests
from bs4 import BeautifulSoup

url='https://www.bbc.com/news'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')

found = []
header_count = 0
i = 0

## while less than 10 headers in the found array, look for next one
## stop when there are 10 headers in found array
while header_count < 11:
    if headlines[i].text.strip() not in found:
        header_count = header_count + 1
        found.append(headlines[i].text.strip())
    i = i + 1

#print(*found, sep='\n')
links=[]
headers=[]
### print headers and hrefs
headers = soup.find_all("a", {"class": "gs-c-promo-heading nw-o-link gs-o-bullet__text gs-o-faux-block-link__overlay-link gel-pica-bold gs-u-pl-@xs"})
for link in headers:
	print("LINK: ", link['href'])
	t = link.find('span',{'class':'gs-c-promo-heading__title gel-pica-bold'})
	print("HEADER: ", t.text)
    
