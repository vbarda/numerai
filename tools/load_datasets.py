from bs4 import BeautifulSoup
import os
import pandas as pd
import urllib2

from paths import (EXISTING_TRAIN_DATA_PATH, EXISTING_TOURNAMENT_DATA_PATH,
                   NEW_TRAIN_DATA_PATH, NEW_TOURNAMENT_DATA_PATH, NEW_DATA_PATH)
from tools.decorator_utils import check_against_cache
from tools.path_utils import mkdir_if_not_there
from tools.url_utils import  safe_unzip_from_url, safe_url_open


DEFAULT_NUMERAI_URL = 'https://numer.ai/rules'
DEFAULT_NUMERAI_DATA_KEYWORD = 'dataset'


def _get_data_urls(url=DEFAULT_NUMERAI_URL, data_keyword=DEFAULT_NUMERAI_DATA_KEYWORD):
    '''Get a list of urls to csvs that contain train and test data
    Args:
        url: (str) the url of the page that has the links to the data files
        data_keyword: (str) used to filter which links to return.
            Default is DEFAULT_NUMERAI_DATA_KEYWORD
    '''
    url_string = safe_url_open(url).read()
    soup = BeautifulSoup(url_string, "html.parser")
    # extract all links from the url page & return only links which contain data_keyword
    links = filter(lambda x: data_keyword in x, [tag.get('href') for tag in soup('a')])
    # keeping this in case they ever change it again, as it used to be two separate links
    if len(links) == 1:
        return links[0]
    return links


def refresh_data(path=NEW_DATA_PATH):
    '''extract the train and test data from zip on the website and write to today's folder'''
    mkdir_if_not_there(path)
    safe_unzip_from_url(_get_data_urls(), path)


@check_against_cache(EXISTING_TRAIN_DATA_PATH)
def get_training_data(from_cache=True):
    '''Get Numerai training data as pd.DataFrame
    Args:
        from_cache: (bool) if from_cache is True, data will be loaded from EXISTING_TRAIN_DATA_PATH
    '''
    if from_cache:
        return pd.read_csv(EXISTING_TRAIN_DATA_PATH)
    refresh_data()
    return pd.read_csv(NEW_TRAIN_DATA_PATH)


@check_against_cache(EXISTING_TOURNAMENT_DATA_PATH)
def get_tournament_data(from_cache=True):
    '''Get Numerai tournament data as pd.DataFrame
    Args:
        from_cache: (bool) if from_cache is True,
            data will be loaded from EXISTING_TOURNAMENT_DATA_PATH
    '''
    if from_cache:
        return pd.read_csv(EXISTING_TOURNAMENT_DATA_PATH)
    refresh_data()
    return pd.read_csv(NEW_TOURNAMENT_DATA_PATH)


def _save_data(getter, path):
    '''wrapper around data getters to save to csv'''
    return getter().to_csv(path, index=False)
