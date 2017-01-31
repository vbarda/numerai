import urllib2
import pandas as pd
from StringIO import StringIO
from zipfile import ZipFile
import warnings


def safe_url_open(url):
    '''Use urllib2.Request with {"User-Agent": "Magic Browser"} header injected'''
    headers = {'User-Agent' : "Magic Browser"}  # this line allows to avoid 403 error
    request = urllib2.Request(url, headers=headers)
    return urllib2.urlopen(request)


def safe_read_csv_from_url(csv_url):
    '''Read csv from url with safe_url_open, StringIO and pd.read_csv'''
    url_open = safe_url_open(csv_url)
    with warnings.catch_warnings():
        warnings.simplefilter('always')
        warnings.warn('Use safe_unzip_from_url', DeprecationWarning)
    return pd.read_csv(StringIO(url_open.read()))

def safe_unzip_from_url(zip_url, extract_path):
    '''Read zip from url with safe_url_open, StringIO and unzip to extract_path'''
    url_open = safe_url_open(zip_url)
    with ZipFile(StringIO(url_open.read()), 'r') as f:
        f.extractall(extract_path)
