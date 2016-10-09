import datetime
import pandas as pd


def today(utc=False, **kwargs):
    '''return today's date in %Y-%m-%d format
    Args:
        utc: (bool) whether to return UTC day and time. Default is False
    '''
    now = datetime.datetime.utcnow() if utc else datetime.datetime.now()
    return pd.to_datetime(now.date(), **kwargs)


def today_as_string(date_format='%Y-%m-%d', **kwargs):
    '''format today's date and return a string'''
    format_base = '{:' + date_format + '}'
    return format_base.format(today(**kwargs))
