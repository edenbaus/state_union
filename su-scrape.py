#!/bin/python3

from get_state_unions import get_su_url_dict
from bs4 import BeautifulSoup
import requests


#url = {'2007-GWBush':'http://www.presidency.ucsb.edu/ws/index.php?pid=24446',
#       '2008-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=76301',
#       '2009-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=85753',
#       '2010-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=87433',
#       '2011-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=88928',
#       '2012-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=99000',
#       '2013-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=102826',
#       '2014-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=104596',
#       '2015-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=108031',
#       '2016-Obama':'http://www.presidency.ucsb.edu/ws/index.php?pid=111174',
#       '2017-Trump':'http://www.presidency.ucsb.edu/ws/index.php?pid=123408'
#       }

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
