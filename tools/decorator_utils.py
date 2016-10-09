import os
import pandas as pd

from tools.path_utils import strip_base_folder_name


DEFAULT_DECIMALS_TO_CHECK = 6
NO_FILE_WARNING = 'WARNING: file doesn\'t exist - cannot check against cache'
FILE_CHANGED_WARNING = 'WARNING: the dataset has changed since the last cached vesion as of {}'

def check_against_cache(existing_path):
    '''decorator to check if the new data is different from cached'''
    def path_decorator(func):
        def func_wrapper(existing_path=existing_path):
            df = func()
            if not os.path.exists(existing_path):
                print NO_FILE_WARNING
                return df
            existing_data = pd.read_csv(existing_path)
            if not (existing_data.round(DEFAULT_DECIMALS_TO_CHECK)
                    .equals(df.round(DEFAULT_DECIMALS_TO_CHECK))):
                print FILE_CHANGED_WARNING.format(strip_base_folder_name(existing_path))
            return df
        return func_wrapper
    return path_decorator
