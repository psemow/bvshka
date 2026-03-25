import numpy as np
from catboost import CatBoostRegressor, CatBoostClassifier
from sklearn.model_selection import train_test_split

def catboost_regression(X, y, test_size=0.2, verbose=False):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    model = CatBoostRegressor(iterations=500, learning_rate=0.05, depth=6, verbose=verbose, random_seed=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    return y_pred, r2, model

def catboost_classification(X, y, test_size=0.2, verbose=False):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    model = CatBoostClassifier(iterations=500, learning_rate=0.05, depth=6, verbose=verbose, random_seed=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return y_pred, acc, model

def catboost_regression_full(X, y, verbose=False):
    model = CatBoostRegressor(iterations=500, learning_rate=0.05, depth=6, verbose=verbose, random_seed=42)
    model.fit(X, y)
    y_pred = model.predict(X)
    return y_pred, r2_score(y, y_pred), model
