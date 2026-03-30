import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error 
from sklearn.metrics import mean_absolute_error




def avaliacao_modelo(nome_modelo, y_teste, previsao):
    r2 = r2_score(y_teste, previsao)
    RSME = np.sqrt(mean_squared_error(y_teste, previsao))
    MAE = mean_absolute_error(y_teste, previsao)
    
    return f'model: {nome_modelo}\nMean Absolute Error: {MAE}\nRoot Mean Square Error: {RSME:.2f}\nR² Score: {round(r2*100, 2)}% \n--------------------------------------------'
