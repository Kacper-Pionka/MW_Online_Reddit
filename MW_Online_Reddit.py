# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup
from datetime import datetime

def newBaba():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S:%d:%b:%Y")

    #while True:
    url = 'https://www.reddit.com/r/modernwarfare/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    i = soup.find_all("div", attrs={"class": "_3XFx6CfPlg-4Usgxm0gK8R"})
    
    f = open('note.txt','a+')
    f.write(i[0].contents[1] + ' ')
    f.write(current_time + '\r')
    f.close()
    
    print(i[1].contents[0], current_time)
    time.sleep(600)

while True:
    newBaba()
