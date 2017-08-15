#!/bin/python

import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_su_url_dict():
    page = 'http://www.presidency.ucsb.edu/sou.php'
    soup = BeautifulSoup(requests.get(page).content,'lxml')

    data_dict = {}

    for i in range(1,98,2): #good records for 1913 <
        try:
            x = soup.contents[0].contents[3].contents[1].contents[3].contents[1].contents[1].contents[1].contents[3].contents[4].contents[i].contents[5].a
            url = str(x).strip().split('"')[1]
            year = str(x).strip().split('"')[2].split('>')[1][:4]
            data_dict[year] = url
        except:
            pass
    
        try:
            x = soup.contents[0].contents[3].contents[1].contents[3].contents[1].contents[1].contents[1].contents[3].contents[4].contents[i].contents[7].a
            url = str(x).strip().split('"')[1]
            year = str(x).strip().split('"')[2].split('>')[1][:4]
            data_dict[year] = url
        except:
            pass
    
        try:
            x = soup.contents[0].contents[3].contents[1].contents[3].contents[1].contents[1].contents[1].contents[3].contents[4].contents[i].contents[9].a
            url = str(x).strip().split('"')[1]
            year = str(x).strip().split('"')[2].split('>')[1][:4]
            data_dict[year] = url
        except:
            pass

        try:
            x = soup.contents[0].contents[3].contents[1].contents[3].contents[1].contents[1].contents[1].contents[3].contents[4].contents[i].contents[11].a
            url = str(x).strip().split('"')[1]
            year = str(x).strip().split('"')[2].split('>')[1][:4]
            data_dict[year] = url
        except:
            pass
                           
    return (data_dict)


