"""
Webscraping example
"""

import requests
from bs4 import BeautifulSoup as bs

#getting or loading the webpage content
link = "https://keithgalli.github.io/web-scraping/example.html"
link1 = "http://www.google.com/nothere"

#requests implements browser style ssl verification
try:
    r = requests.get(link)
    r.raise_for_status()
except requests.exceptions.HTTPError as err404:
    #will occur if the webpage doesn't exist
    raise SystemExit(err404)
except requests.exceptions.ConnectionError as errc:
    #will occur if there is an error connecting to webpage
    raise SystemExit(errc)
except requests.exceptions.RequestException as e:
    #prints an error and calls system exist
    print('exit')
    raise SystemExit(e)

#convert response to beautiful soup object
soup = bs(r.content, features = "html.parser")

#print(soup.prettify())
print('Title of the webpage: ', soup.title.string)

#headers in html
headers = soup.find_all(['h1','h2'])
headers = [head.string for head in headers ]

#links in html (There is only one)
href_links = soup.find('a').get('href')

print(href_links)
print(headers)
