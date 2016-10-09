import os

from constants import PROJECT_PATH
from tools.date_utils import today_as_string
from tools.path_utils import get_most_recent_folder_path, make_data_file_path

FILENAME_BASE = 'numerai_{}_data.csv'
DATA_DIR_PATH = os.path.join(PROJECT_PATH, 'data')


def make_train_data_path(dir_path):
    '''wrapper around make_data_file_path for training_data'''
    return make_data_file_path(dir_path, FILENAME_BASE, 'training')


def make_tournament_data_path(dir_path):
    '''wrapper around make_data_file_path for training_data'''
    return make_data_file_path(dir_path, FILENAME_BASE, 'tournament')


MOST_RECENT_DATA_PATH = get_most_recent_folder_path(DATA_DIR_PATH)
EXISTING_TRAIN_DATA_PATH = make_train_data_path(MOST_RECENT_DATA_PATH)
EXISTING_TOURNAMENT_DATA_PATH = make_tournament_data_path(MOST_RECENT_DATA_PATH)

NEW_DATA_PATH = os.path.join(DATA_DIR_PATH, today_as_string())  # make a folder with today's date
NEW_TRAIN_DATA_PATH = make_train_data_path(NEW_DATA_PATH)
NEW_TOURNAMENT_DATA_PATH = make_tournament_data_path(NEW_DATA_PATH)
