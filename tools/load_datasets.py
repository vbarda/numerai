from bs4 import BeautifulSoup
import os
import pandas as pd
import urllib2

from paths import (EXISTING_TRAIN_DATA_PATH, EXISTING_TOURNAMENT_DATA_PATH,
                   NEW_TRAIN_DATA_PATH, NEW_TOURNAMENT_DATA_PATH)
from tools.decorator_utils import check_against_cache
from tools.path_utils import mkdir_if_not_there
from tools.url_utils import safe_read_csv_from_url, filter_url_list, safe_url_open


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
    links = [tag.get('href') for tag in soup('a')]  # extract all links from the url page
    # return only links which contain data_keyword
    return [link for link in links if data_keyword in link]


@check_against_cache(EXISTING_TRAIN_DATA_PATH)
def get_training_data(from_cache=False):
    '''Get Numerai training data as pd.DataFrame
    Args:
        from_cache: (bool) if from_cache is True, data will be loaded from EXISTING_TRAIN_DATA_PATH
    '''
    if from_cache:
        return pd.read_csv(EXISTING_TRAIN_DATA_PATH)
    training_data_csv_url = filter_url_list(_get_data_urls(), 'training')
    return safe_read_csv_from_url(training_data_csv_url)


@check_against_cache(EXISTING_TOURNAMENT_DATA_PATH)
def get_tournament_data(from_cache=False):
    '''Get Numerai tournament data as pd.DataFrame
    Args:
        from_cache: (bool) if from_cache is True,
            data will be loaded from EXISTING_TOURNAMENT_DATA_PATH
    '''
    if from_cache:
        return pd.read_csv(EXISTING_TOURNAMENT_DATA_PATH)
    tournament_data_csv_url = filter_url_list(_get_data_urls(), 'tournament')
    return safe_read_csv_from_url(tournament_data_csv_url)


def _save_data(getter, path):
    '''wrapper around data getters to save to csv'''
    mkdir_if_not_there(path)
    return getter().to_csv(path, index=False)


def save_training_data(path=NEW_TRAIN_DATA_PATH):
    '''save training data'''
    return _save_data(getter=get_training_data, path=path)


def save_tournament_data(path=NEW_TOURNAMENT_DATA_PATH):
    '''save tournament data'''
    return _save_data(getter=get_tournament_data, path=path)
