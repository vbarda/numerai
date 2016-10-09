import os
import pandas as pd
import time


def get_modification_date(path):
    '''get the date and time when the file was last modified'''
    stats = os.stat(path)
    return pd.to_datetime(time.ctime(stats.st_mtime))


def full_path_listdir(path):
    '''return full paths to objects in listdir'''
    if not os.path.exists(path) or not os.listdir(path):
        raise IOError('the path doesn\'t exist or directory is empty')
    return [os.path.join(path, p) for p in os.listdir(path)]


def get_most_recent_folder_path(path):
    '''listdir of path and return the path to the most recent item in the directory'''
    paths = full_path_listdir(path)
    valid_paths = filter(os.path.isdir, paths)
    dates = map(get_modification_date, valid_paths)
    return max(zip(dates, valid_paths))[1]


def make_data_file_path(dir_path, filename_base, *args):
    '''wrapper to join dir_path and filename_base, and format the filename_base with *args'''
    return os.path.join(dir_path, filename_base.format(*args))


def mkdir_if_not_there(path):
    '''check if directory exists and make it if it doesn'\t'''
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def strip_base_folder_name(path):
    '''strip off the base folder name'''
    return os.path.basename(os.path.dirname(path))
