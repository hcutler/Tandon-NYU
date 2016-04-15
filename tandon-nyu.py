import urllib2
import time
from bs4 import BeautifulSoup as bsoup
from bs4 import BeautifulSoup
from yaml import load, Loader
import requests as rq
import re


#get contents of Tandon School of Engineering NYU page
base_url = "http://engineering.nyu.edu/people?"
r = rq.get(base_url)
soup = bsoup(r.text, "lxml")

page_count_links = soup.find_all("a",href=re.compile(r".*javascript:goToPage.*"))
try: # Make sure there are more than one page, otherwise, set to 1.
    num_pages = int(page_count_links[-1].get_text())
except IndexError:
    num_pages = 27


url_list = ["{}page={}".format(base_url, str(page)) for page in range(1, num_pages + 1)]

url_list.insert(0, "http://engineering.nyu.edu/people")

# ---
for url in url_list:
  html_doc = urllib2.urlopen(url).read()
  soup = BeautifulSoup(html_doc, "lxml")


  contents = soup.find_all('div', attrs={"class": "col-3"})

  people = []
  for item in contents:
      name = item.text
      # baselink = "http://engineering.nyu.edu/people/"
      # link = item.find_all('a', attrs="href")
      # full_link = baselink, link

  #     people.append({'name': name,'link': link})
      people.append({'name': name})
  
  for p in people:
    print p

