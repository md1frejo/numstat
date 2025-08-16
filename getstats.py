#!/usr/bin/env python

# scp webcheck.py md1frejo@ssh.pythonanywhere.com:webmalist

from urllib.request import urlopen
from urllib.parse import urlencode
from IPython.core.debugger import Pdb
from pdb import set_trace as B
from numpy import array,zeros,save,load,dot
from numpy.linalg import norm as norm2
from requests import get
from datetime import datetime
from datetime import date as dt
from urllib.parse import urljoin
import json as js

from json import loads
import requests as req
from selenium import webdriver as we
import re
import yfinance as yf
from bs4 import BeautifulSoup as bs
import pandas as pd

def getcountries():
# read all the countires from worldfacts.us

    headers = {
        "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",  # Do Not Track
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*looptcp.awk*;q=0.8"
    }

    url='https://worldfacts.us'
    res=get(url,headers=headers)
    sp=bs(res.content,"html.parser")

    cstat={}
    
    for k in sp.find_all('a',href=True):
        cstat[k.text]=k['href']

    return cstat

def getstats(cstat):
# get all stats from worldfacts.us

    stats={}
    
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "DNT": "1",  # Do Not Track
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*looptcp.awk*;q=0.8"
    }

    s1=re.compile(r'Location')
    
    for (k,v) in cstat.items():
        stats[k]={"history":"na","location":"na","coordinates":{"N":"na","E":"na"},"map_references":"na"}
        stats[k]={}
        url='https://worldfacts.us/'+v.split('/')[-1]
        res=get(url,headers=headers)
        sp=bs(res.content,"html.parser")
        ma=sp.find("img",attrs={"alt":k})
        if ma:
            te=ma.next
            stats[k]['history']=te.strip()
        elem=sp.find_all("td",attrs={"valign":"bottom"})
        for l in sp.find_all("td",attrs={"valign":"bottom"}):
            key1=list(l.previous_elements)[2].string.strip()[:-1]
            stats[k][key1]=l.text.replace('\n',' ')

    with open("stats.json","w") as f:
        js.dump(stats,f)

    return stats
            
def main():

    # get all country names
    cstat=getcountries()
    stats=getstats(cstat)

    return stats
