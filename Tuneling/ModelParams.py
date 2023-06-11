MODELS_PARAMS_GRIDS =  {
  'BAG-minMax': {
      'BAG__n_estimators': [100, 500, 800, 1000],
      'BAG__max_samples' : [0.6, 0.7, 0.8, 1.0, 1.1],
      'BAG__max_features': [0.8, 0.85, 0.90, 0.92, 0.95, 1.0],
      'BAG__bootstrap' : [True, False],
      'BAG__bootstrap_features': [True, False],
      'BAG__oob_score': [True, False],
      'BAG__warm_start': [True, False]
  },
  'ETR-minMax': {
    'ETR__n_estimators': [100,500,800,1000],
    'ETR__criterion': ['mse'],
    'ETR__max_depth': [40,80,100,None],
    'ETR__min_samples_split': [2,4,6],
    'ETR__min_samples_leaf': [1,2],
    'ETR__oob_score': [True, False],
    'ETR__max_features': ['auto','sqrt','log2'],    
    'ETR__bootstrap': [True, False],
    'ETR__warm_start': [True, False],
  },
  'RF-minMax': {
      'RF__n_estimators': [100, 500, 800, 1000],
      'RF__max_features': [0.8, 0.85, 0.90, 0.92, 0.95, 1.0],
      'RF__max_depth': [40,80,100,None],
      'RF__max_features': ['auto', 'sqrt'],
      'RF__min_samples_leaf': [1, 2, 4],
      'RF__min_samples_split': [2, 5, 10],
      'RF__bootstrap': [True, False],
  },
  'CART-minMax': {
      'CART__criterion':['mse', 'friedman_mse', 'absolute_error', 'poisson'],
      'CART__max_depth': [40,80,100,None],
      'CART__max_features': [2, 3],
      'CART__min_samples_leaf': [3, 4, 5],
      'CART__min_samples_split': [8, 10, 12],

  }

}