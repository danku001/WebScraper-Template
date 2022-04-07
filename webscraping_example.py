"""
Webscraping example
made modifications to include getpass4 and getpass

getpass -> builtin python package
getpass -> updated version...use this when you have real password and stuff.
Beautiful soup is only useful for html and xml files
"""

import requests
from bs4 import BeautifulSoup as bs
#import getpass4 as gp #prompts user for password without echoing to screen
import getpass as gp
from requests.auth import HTTPBasicAuth    #Basic authentication credentials
                                           #If different kind of authentication then change import
#import json   #For those sites that use json...but not used.


#getting or loading the webpage content
#link = "https://keithgalli.github.io/web-scraping/example.html"
#link1 = "http://www.google.com/nothere"
#link2 = "https://api.github.com/users/" + user
#use this link to test basic auth python request https://postman-echo.com/basic-auth
##username is postman, password is password.

link = input('Enter the url for the website to be scraped: ').strip()
user = input('Enter user: ').strip()

#requests implements browser style ssl verification
try:
    r = requests.get(
        link,
        auth = HTTPBasicAuth( user, gp.getpass('Pword: ') )
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
    raise SystemExit(e)


#for html links
#convert response to beautiful soup object
soup = bs(r.content, features = "html.parser")

print(soup.prettify())

print('Title of the webpage: ', soup.title.string)

#headers in html
headers = soup.find_all(['h1','h2'])
headers = [head.string for head in headers ]

#links in html (There is only one)
href_links = soup.find('a').get('href')


#jsonStuff = json.dumps( r.json() )

#print(jsonStuff)
print(href_links)
print(headers)



input('Press any key to exit.')
