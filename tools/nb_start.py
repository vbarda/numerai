%matplotlib inline
%load_ext autoreload
%autoreload 2

import sys
sys.path.append('../../numerai/')

import pandas as pd
import numpy as np
import funcy
import os

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.feature_selection import RFECV, SelectKBest
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import LogisticRegression, LinearRegression, LassoCV, LassoLarsCV
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor

from models.cross_validation import CrossValidation
from models.inspection import ModelInspector
from tools.helpers import binarize
from tools.stats import display_biggest_corrs
from tools.load_datasets import (
    get_training_data, get_tournament_data, save_training_data, save_tournament_data
)
