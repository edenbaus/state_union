#!/bin/python3

from get_state_unions import get_su_url_dict
from bs4 import BeautifulSoup
import requests

url = get_su_url_dict()

for year,link in url.items():
    print('Scraping State of Union address for %s:' %(year[:4]))
    out = requests.get(link)   
    soup = BeautifulSoup(out.content,'lxml') 
    su_content = soup.findAll('div',{'class':'tools'})[0].next_sibling.text
    file_f = year + '.txt'
    f = open(file_f,'w')
    f.write(su_content)
    f.close()
