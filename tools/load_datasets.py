from bs4 import BeautifulSoup
import urllib2

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
    soup = BeautifulSoup(url_string)
    links = [tag.get('href') for tag in soup('a')]  # extract all links from the url page
    # return only links which contain data_keyword
    return [link for link in links if data_keyword in link]


def get_training_data():
    '''Get Numerai training data as pd.DataFrame'''
    training_data_csv_url = filter_url_list(_get_data_urls(), 'training')
    return safe_read_csv_from_url(training_data_csv_url)


def get_tournament_data():
    '''Get Numerai tournament data as pd.DataFrame'''
    training_data_csv_url = filter_url_list(_get_data_urls(), 'tournament')
    return safe_read_csv_from_url(training_data_csv_url)
