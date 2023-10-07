#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 10:07:03 2023

@author: jonnathann
"""

import matplotlib.pyplot as plt



def allcategoricalPlotBar(df, _type = 'sep'):
    
    for col in df.columns:
        if col not in ['Churn','tenure', 'customerID', 'MonthlyCharges', 'TotalCharges']:
            if _type == 'sep':
                plt.subplot(1, 2, 1)

                df[df.Churn == 'No'][col].value_counts().plot(kind='bar')
                plt.title(col+' - NO-CHURN')

                plt.subplot(1, 2, 2)
                df[df.Churn == 'Yes'][col].value_counts().plot(kind='bar')
                plt.title(col+' - CHURN')
                plt.show()
            elif _type == 'gnr':
                df[col].value_counts().plot(kind='bar')
                plt.title(col)
                plt.show()
                
def allcontinuePlotBar(df, _type= 'sep'):
    for col in df.columns:
        if col in ['tenure','MonthlyCharges', 'TotalCharges']:
            
            if _type == 'sep':
                plt.subplot(1, 2, 1)

                df[df.Churn == 'No'][col].hist(bins=20)
                plt.title(col+' - NO-CHURN')


                plt.subplot(1, 2, 2)
                df[df.Churn == 'Yes'][col].hist(bins=20)
                plt.title(col+' - CHURN')
                plt.show()
            elif _type == 'gnr':
                df[col].hist(bins=20)
                plt.title(col)
                plt.show()
                
def pre_processing_data(df):
    df.SeniorCitizen.replace({0:'No', 1:'Yes'}, inplace=True)
    df['MonthlyCharges'] = df.MonthlyCharges.str.replace(',', '.')
    df['TotalCharges'] = df.TotalCharges.str.replace(',', '.')
    df['MonthlyCharges'] = df.MonthlyCharges.astype('float')
    df['TotalCharges'] = df.TotalCharges.astype('float')
    return df
    

def pre_processing_model(df):
    _dict = {
        
        'No':0,
        'Yes':1,
        'No internet service':2,
        'No phone service':2,
        
        'Male':0,
        'Female':1,
        
        'DSL':1,
        'Fiber optic':2,
        
        'Month-to-month':0,
        'One year':1,
        'Two year':2,
        
        'Electronic check':0,
        'Mailed check':1,
        'Bank transfer (automatic)':2,
        'Credit card (automatic)':3
        
    }
    return df.replace(_dict)