import urllib2
import pandas as pd
from StringIO import StringIO


def safe_url_open(url):
    '''Use urllib2.Request with {"User-Agent": "Magic Browser"} header injected'''
    headers = {'User-Agent' : "Magic Browser"}  # this line allows to avoid 403 error
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request)


def safe_read_csv_from_url(csv_url):
    '''Read csv from url with safe_url_open, StringIO and pd.read_csv'''
    url_open = safe_url_open(csv_url)
    return pd.read_csv(StringIO(url_open.read()))


def filter_url_list(url_list, filter_keyword):
    '''Filter the url list and extract url that matches filter keyword'''
    return [url for url in url_list if filter_keyword in url][0]
