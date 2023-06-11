import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.append(parent_dir)


# Import adequated models for the competition
from Tuneling.ModelOptimizer import ModelOptimizer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, BaggingRegressor, ExtraTreesRegressor

#import splitter
from sklearn.model_selection import  train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.pipeline import Pipeline

#import aux libraries

import pandas as pd

#import model paramters
from ModelParams import *
#setup path to the current script path

#import env Vars

from Env.EnvVars import *

import warnings
warnings.filterwarnings('ignore')

#load file and split data
dataset = pd.read_csv(DATASET_PATH + "/Salary_Data_preprocessed.csv")



X  = dataset.drop('Salary',axis = 1).values
y = dataset['Salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = TEST_SIZE, random_state = SEED)


#Instiate scalers
minMaxScaler = ('MinMaxScaler', MinMaxScaler())
stdScaler = ('StandardScaler', StandardScaler() )


#setup the models

models = [

    ('CART', DecisionTreeRegressor())


]


pipelines  = [
    (name + '-minMax', Pipeline(steps=[minMaxScaler, (name,model) ])) for name, model in models
    
]
scaler = "minMax"

kfolds = 5
score_type = 'neg_mean_squared_error'

#optimize models and save it

model_optimizer= ModelOptimizer( kfolds, score_type)
model_optimizer.optimize_models(X_train, y_train, pipelines, MODELS_PARAMS_GRIDS, '')