"""
Webscraping example
made modifications to include getpass4 and getpass

getpass -> builtin python package
getpass -> updated version...use this when you have real password and stuff.
"""

import requests
from bs4 import BeautifulSoup as bs
#import getpass4 as gp #prompts user for password without echoing to screen
import getpass as gp
from requests.auth import HTTPBasicAuth    #Basic authentication credentials
                                           #If different kind of authentication then change import


#getting or loading the webpage content
link = "https://keithgalli.github.io/web-scraping/example.html"
link1 = "http://www.google.com/nothere"

#requests implements browser style ssl verification
try:
    r = requests.get(
        link,
        auth = HTTPBasicAuth( input('username: '), gp.getpass('Pword: ') )
        )
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
