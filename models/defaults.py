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


poly_lasso = make_polynomial_pipeline('lasso', LassoCV)


poly_log_reg = make_polynomial_pipeline('log_reg', LogisticRegression)


poly_lin_reg = make_polynomial_pipeline('lin_reg', LinearRegression)


pca_log_reg = Pipeline([
                ('pca', PCA()),
                ('log_reg', LogisticRegression())
              ])


poly_dt = make_polynomial_pipeline('decision_tree', DecisionTreeClassifier)


poly_random_forest = make_polynomial_pipeline('random_forest', RandomForestClassifier)
