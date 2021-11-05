#import numpy as np
#import pandas as pd
#from computer.data_process import *
#from computer.data_front import *
#from computer.funcomputer import *
#from pathlib import Path
#from datetime import datetime
#
### ! Criando o primeiro dataframe com namespace e a primeira coluna de data
#test_variable = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
#test_variable = test_variable.rename(columns={"Risco":data_final})
#test_variable.to_csv("../repoprojeto/csvs/hist_csvs/hist_risk.csv",sep=',')
##
### Puxando o primeiro Csv de risco de todos os dados
#historical_data_rik = pd.read_csv("./csvs/hist_csvs/hist_risk.csv")
#del historical_data_rik['Unnamed: 0']
##
## Pegando a última data no dataframe 
#varteste12345 = historical_data_rik.columns.values.tolist()
#varteste12345 = varteste12345[-1]
#
#hoje = str(datetime.today().strftime('%Y-%m-%d'))
#
## Validando se houve alguma 
#if varteste12345 != data_final:
#    
#    pass
#else:
#    # Tabela de conteudos
#    t_conteudos_cru = pd.read_csv("./csvs/tabela_conteudos_crua_2.csv")
#    del t_conteudos_cru['Unnamed: 0']
#    
#    t_relas_cru = pd.read_csv("./csvs/tab_rela_crua.csv")
#    del t_relas_cru['Unnamed: 0']
#    
#    t_quest_cru = pd.read_csv("./csvs/tab_quest_cru.csv")
#    del t_quest_cru['Unnamed: 0']
#    
#    t_engaj_cru = pd.read_csv("./csvs/tab_engaja_cru.csv")
#    del t_engaj_cru['Unnamed: 0']
#    
#    tab_unida_crua = pd.merge(t_conteudos_cru, t_relas_cru, on="namespace", how='outer')
#    tab_unida_crua = pd.merge(tab_unida_crua, t_quest_cru, on="namespace", how='outer')
#    tab_unida_crua = pd.merge(tab_unida_crua, t_engaj_cru, on="namespace", how='outer')
#    tab_unida_crua=tab_unida_crua.replace(np.nan, 0)
#    
#    # * Historical risk Dataframe
#    df_aux_hist = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
#    df_aux_hist = df_aux_hist.rename(columns={"Risco":data_final})
#    historical_data_rik=pd.merge(historical_data_rik, df_aux_hist, on="namespace", how='outer')
#    #historical_data_rik.to_csv("./csvs/hist_csvs/hist_risk.csv",sep=',')
#    
#    # * Points by categorical avg dataframes
#    df_aux_hist_points = get_columns(total_pontos, pont_pedago_030)
#    p = Path('../repoprojeto/csvs/hist_csvs/')
#    df_aux_hist_points.to_csv(Path(p, 'hist_' + varteste12345 + '.csv'),sep=',')
#
#    # ? Parte relacionada a o sucesso do cliente
#    
#    # risco
#    risco = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
#    #var_sc = var_sc.rename(columns={"Risco":str(data_final)+"_Risco"})
#    
#    # pontos
#    var_sc2 = get_columns(total_pontos, pont_pedago_030)
#
#    # merge and treatment
#    
#    var_sc = pd.merge(risco, var_sc2, on="namespace", how='outer')
#    
#    ns_sc=pd.read_csv("./csvs/hist_csvs/namespaces_sc.csv")
#    var_sc = chose_rows(var_sc, ns_sc).reset_index(drop=True)
#    
#    var_sc.to_csv("./csvs/hist_csvs/plan_sc.csv",sep=',')
#    
#    # bruto
#    bru_var_sc = pd.merge(risco, tab_unida_crua, on="namespace", how='outer')
#    bru_var_sc = chose_rows(bru_var_sc, ns_sc).reset_index(drop=True)
#    bru_var_sc = bru_var_sc.replace(np.nan, 0)
#    bru_var_sc.to_csv("./csvs/hist_csvs/plan_sc_bruto.csv",sep=',')
#    gslides = bru_var_sc.copy()
#    var_g = bru_var_sc.iloc[:,2:]
#    aux_var_g = var_g.columns.values.tolist()
#    
#    for item in aux_var_g:
#        gslides[item] = gslides[item].astype(str)
#        for i in range(len(gslides[item])):
#            gslides.loc[i,item]=gslides.loc[i,item].replace(".", ",")
#    
#    gslides.to_csv("./csvs/hist_csvs/gslides.csv",sep=',')
#    