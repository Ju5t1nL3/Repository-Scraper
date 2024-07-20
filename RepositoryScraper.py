"""
If the url to a profile's repositories page is copied, the code will first return the response code. It then will
then post the name of every repository followed by if it's public.
"""

from bs4 import BeautifulSoup
import requests

url = 'https://github.com/Ju5t1nL3?tab=repositories'
r = requests.get(url)

print(f"{r}\n")

soup = BeautifulSoup(r.content,'lxml')
title = soup.find_all('h3',class_ = 'wb-break-all')

for t in title:
    print(f"{t.getText().strip()}\n")
