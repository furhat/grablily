import requests
import lxml
from bs4 import BeautifulSoup
import time

import re

url = "http://101.200.181.254/index.php"
resource_list = []

for i in range(191000, 192000):
    # print(f'Checking {i}')
    code = f"{i:06d}"
    print(code)
    data = {"trun": 1, "code": code}
    #data = {"trun": 1, "code": 567890}

    html_page=requests.post(url, data).text


    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        #print(f'Checking {i}')
        #if(i % 100 == 0):

        res_link = link.get('href')
        if(res_link):
            print(i, res_link)
            # print(html_page)
            resource_list.append((code, res_link))
    time.sleep(0.01)

with open('your_file.txt', 'a') as f:
    for code, link in resource_list:
        f.write("%s    %s\n" % (code, link))






