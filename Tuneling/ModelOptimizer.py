from sklearn.model_selection import GridSearchCV
from joblib import dump

class ModelOptimizer():
    
    def __init__(self, kfolds, score_type):
        
        self.kfolds = kfolds
        self.score_type = score_type
        self.best_models = []
        
    def __save_model(self, model, path, filename):
        dump(model, path + filename + '.joblib')
        
        
    def optimize_models(self, X_train, y_train, models, grids_params, save_at_path):
        
        best_models = []
        for name, model in models:

            
            print('*' *100)
            model_param_grid = grids_params[name]
            
            print('*'*100)
            print(  20 * '='+ f" Making Tuneling of {name} model " + 20 * '=')  
            
            grid = GridSearchCV(estimator=model, param_grid= model_param_grid, scoring='neg_mean_squared_error', cv=5)

            print(f'Performing  {name} model hyperparameter tuneling')
            grid.fit(X_train, y_train)
            print(f'{name} model hyperparameter tuneling Done!')




            print(f'best model found: {grid.best_estimator_}')
            print(f'best model params: {grid.best_params_}')
            

            # Save the best_estimator_ to a file
            print('Saving model...')
            

            best_models.append(grid.best_estimator_)
            print('Model saved !')
            self.__save_model(grid.best_estimator_, save_at_path, name)
        
        self.best_models = best_models
        print('Tuneling completed successfully ! ') 
        
        
        def get_best_models():
            
            return self.best_models
    