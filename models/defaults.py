from funcy import pluck_attr, zipdict
from inspect import isfunction

from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, LassoCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeClassifier

def make_polynomial_pipeline(model_name, model):
    '''Make scikit pipeline with polynomial features and a classifier / regressor
    Args:
        model_name: (str) name of the model that will be displayed in keys of pipeline.named_steps
        model: scikit classifier / regressor
    '''
    return Pipeline([
            ('polynomial_features', PolynomialFeatures()),
            (model_name, model())
           ])


def poly_lasso():
    '''PolynomialFeatures, LassoCV'''
    return make_polynomial_pipeline('lasso', LassoCV)


def poly_log_reg():
    '''PolynomialFeatures, LogisticRegression'''
    return make_polynomial_pipeline('log_reg', LogisticRegression)


def poly_lin_reg():
    '''PolynomialFeatures, LinearRegression'''
    return make_polynomial_pipeline('lin_reg', LinearRegression)


def pca_log_reg():
    '''PCA, LogisticRegression'''
    return Pipeline([
            ('pca', PCA()),
            ('log_reg', LogisticRegression())
           ])

def poly_dt():
    '''PolynomialFeatures, DecisionTreeClassifier'''
    return make_polynomial_pipeline('decision_tree', DecisionTreeClassifier)


def poly_random_forest():
    '''PolynomialFeatures, RandomForestClassifier'''
    return make_polynomial_pipeline('random_forest', RandomForestClassifier)


def model_dict(model_names, models):
    '''Create a dictionary of model names and models'''
    if model_names is None:
        model_names = pluck_attr('__name__', models)
    models_to_dict = []
    for model in models:
        if isfunction(model):
            models_to_dict.append(model())
        else:
            models_to_dict.append(model)
    return zipdict(model_names, models_to_dict)
