#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:21:10 2023

@author: jonnathann
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class FeatureImportance:
    
    def __init__(self, x_train, y_train, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    
    def feature_importance_analysis(self):
        
        rf = RandomForestClassifier()
        rf.fit(self.x_train, self.y_train)
        predict = rf.predict(self.x_test)
        
        feature_importances = pd.DataFrame(rf.feature_importances_, index=self.x_train.columns, columns=['importance']).sort_values('importance')
        plt.rcParams.update({'font.size': 40}) 
        feature_importances.plot.barh(figsize=(50, 30))
        plt.show()
        return accuracy_score(self.y_test, predict)
        
        