#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : btny99
# Created Date: 1/12/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""  #Line 4
# ---------------------------------------------------------------------------
# Imports Line 5
# ---------------------------------------------------------------------------
#from ... import ...  #Line 6
"""
function for data cleaning 
"""

import pandas as pd
#import nltk
#nltk.download('punkt')
import numpy as np
#import geopandas as gpd
#from shapely import wkt 

import statsmodels.api as sm
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
import math
from sklearn.model_selection import train_test_split


"""
Part IV : Régressions  
"""


def get_OLS_reg(Xcolumn,Ycolumn): 
    Xcolumn= sm.add_constant(Xcolumn) #on ajoute une constante au vecteur de prédiction 
    return(print(sm.OLS(Ycolumn, Xcolumn).fit().summary())) #on #on définit le modèle de régression linéaire et la fonction summary permet d'afficher le tableau récapitulatif

def get_qqplot(Xcolumn,Ycolumn):
    Xcolumn= sm.add_constant(Xcolumn) #on ajoute une constante au vecteur de prédiction
    model = sm.OLS(Ycolumn, Xcolumn).fit() #on définit le modèle de régression linéaire
    res = model.resid #on crée la variable res qui correspond aux résidus du modèle
    fig = sm.qqplot(res, fit=True, line="45") #
    return (plt.show())

def get_bp_test_OLS(Xcolumn,Ycolumn):
    Xcolumn= sm.add_constant(Xcolumn)
    model = sm.OLS(Ycolumn, Xcolumn).fit()
    res = model.resid
    bp_test=sm.stats.diagnostic.het_breuschpagan(res,Xcolumn)
    labels = ['LM Statistic', 'LM-Test p-value', 'F-Statistic', 'F-Test p-value']
    return('breusch_pagan_results=',dict(zip(labels, bp_test)))

def get_RLM(Xcolumn, Ycolumn):
    Xcolumn = sm.add_constant(Xcolumn) #on ajoute l'intercept à la variable explicative.
    return(print(sm.RLM(Ycolumn, Xcolumn).fit().summary()))

def get_sklearn_regression(Xcolumn,Ycolumn,nomX,nomY):
    X=np.array(Xcolumn).reshape(-1,1) ##on transforme Y et X en matrices colonnes
    Y = np.array(Ycolumn).reshape(-1,1)
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,train_size=0.7)
    lin= LinearRegression()
    reg = lin.fit(X_train,Y_train)
    pred_train = lin.predict(X_train)
    pred_test = lin.predict(X_test)
    coefficients_sans_cst= reg.coef_
    r_2 = reg.score(X_train,Y_train)
    
    plt.scatter(X_train, Y_train, color='red') # plotting the observation line
    plt.plot(X_train, lin.predict(X_train), color='blue') # plotting the regression line
    plt.xlabel(nomX) # adding the name of x-axis
    plt.ylabel(nomY) # adding the name of y-axis
    plt.show() # specifies end of graph
    
    return ({'r_square=': r_2, 'coefficients_sans_cst=': float(coefficients_sans_cst[0])})