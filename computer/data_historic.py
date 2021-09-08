import numpy as np
import pandas as pd
from computer.data_process import *
from computer.data_front import *
from computer.funcomputer import *
from pathlib import Path

# ! Criando o primeiro dataframe com namespace e a primeira coluna de data
#test_variable = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
#test_variable = test_variable.rename(columns={"Risco":data_final})
#test_variable.to_csv("../repoprojeto/csvs/hist_csvs/hist_risk.csv",sep=',')

# Puxando o primeiro Csv de risco de todos os dados
historical_data_rik = pd.read_csv("./csvs/hist_csvs/hist_risk.csv")
del historical_data_rik['Unnamed: 0']

# Pegando a última data no dataframe 
varteste12345 = historical_data_rik.columns.values.tolist()
varteste12345 = varteste12345[-1]

# Validando se houve alguma 
if varteste12345 == data_final:
    pass
else:
    
    # * Historical risk Dataframe
    df_aux_hist = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
    df_aux_hist = df_aux_hist.rename(columns={"Risco":data_final})
    historical_data_rik=pd.merge(historical_data_rik, df_aux_hist, on="namespace", how='outer')
    
    # * Points by categorical avg dataframes
    df_aux_hist_points = get_columns(total_pontos, pont_pedago_030)
    p = Path('../repoprojeto/csvs/hist_csvs/')
    df_aux_hist_points.to_csv(Path(p, 'hist_' + varteste12345 + '.csv'),sep=',')