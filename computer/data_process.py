# Aqui iremos receber / unir os dataframes, fazer copias para front
# normalizar dados, tirar medias e classificar os quartil's

from os import sep
import numpy as np
import pandas as pd
from computer.funcomputer import *



# Recebendo os dataframes dados

## Tabela de conteudos
t_conteudos=pd.read_csv("./csvs/tab_conteudos.csv")
del t_conteudos['Unnamed: 0']
t_conteudos=t_conteudos.replace(np.inf, 0)

## Tabela de relátorios
t_relas=pd.read_csv("./csvs/tab_rela23.csv")
del t_relas['Unnamed: 0']
t_relas=t_relas.replace(np.inf, 0)

# Tabela de questoes
t_quest=pd.read_csv("./csvs/tab_quest.csv")
del t_quest['Unnamed: 0']
t_quest=t_quest.replace(np.inf, 0)

# Tabela de engajamento
t_engaj=pd.read_csv("./csvs/tab_engaja.csv")
del t_engaj['Unnamed: 0']
t_engaj=t_engaj.replace(np.inf, 0)

# Tabela de Produto/Dealowner (separar)
t_prod=pd.read_csv("./csvs/produto_deal_licen_receita.csv")
del t_prod['Unnamed: 0']

# Vamos agora separar as tabelas por produto e licenças
tab_prod=reorder_columns(t_prod,"licenças",2).iloc[:,:3]

# unindo e inserindo a tabela de produto no restando das tabelas

# conteudos
tab_unida_prod = pd.merge(t_conteudos, t_relas, on="namespace", how='outer')
tab_unida_prod = pd.merge(tab_unida_prod, t_quest, on="namespace", how='outer')
tab_unida_prod = pd.merge(tab_unida_prod, t_engaj, on="namespace", how='outer')
tab_unida_prod = pd.merge(tab_unida_prod, t_prod, on="namespace", how='outer')
tab_unida_prod = tab_unida_prod.replace(np.nan, 0)

# Separando por produto e licenças

# Váriavel de tamanho para retirar a tabela produto para normalização e avg
vsize=tab_unida_prod.shape[1]

###################   Pedagogico ####################
# 0 - 30
prod_pedago_030 = split_dataframe(tab_unida_prod,"Produto","Pedagógico","licenças", "0 - 30").iloc[:,:vsize-6]
norm_pedago_030 = norm_dataframe(prod_pedago_030)
avg_pedago_030 = media_das_colunas(norm_pedago_030)
pont_pedago_030 = avg_ratio(norm_pedago_030, avg_pedago_030)
quartil_pegado_030 = quartiles_classification(sumx_arranging(norm_pedago_030))

# 30 - 400
prod_pedago_34 = split_dataframe(tab_unida_prod,"Produto","Pedagógico","licenças", "30 - 400").iloc[:,:vsize-6]
norm_pedago_34 = norm_dataframe(prod_pedago_34)
avg_pedago_34 = media_das_colunas(norm_pedago_34)
pont_pedago_34 = avg_ratio(norm_pedago_34, avg_pedago_34)
quartil_pegado_34 = quartiles_classification(sumx_arranging(norm_pedago_34))

# 400 - 800
prod_pedago_48 = split_dataframe(tab_unida_prod,"Produto","Pedagógico","licenças","400 - 800").iloc[:,:vsize-6]
norm_pedago_48 = norm_dataframe(prod_pedago_48)
avg_pedago_48 = media_das_colunas(norm_pedago_48)
pont_pedago_48 = avg_ratio(norm_pedago_48, avg_pedago_48)
quartil_pegado_48 = quartiles_classification(sumx_arranging(norm_pedago_48))

# 800 - 1200
prod_pedago_812 = split_dataframe(tab_unida_prod,"Produto","Pedagógico","licenças","800 - 1200").iloc[:,:vsize-6]
norm_pedago_812 = norm_dataframe(prod_pedago_812)
avg_pedago_812 = media_das_colunas(norm_pedago_812)
pont_pedago_812= avg_ratio(norm_pedago_812, avg_pedago_812)
quartil_pegado_812 = quartiles_classification(sumx_arranging(norm_pedago_812))

# 1200 - x
prod_pedago_12x = split_dataframe(tab_unida_prod,"Produto","Pedagógico","licenças","1200 - x").iloc[:,:vsize-6]
norm_pedago_12x = norm_dataframe(prod_pedago_12x)
avg_pedago_12x = media_das_colunas(norm_pedago_12x)
pont_pedago_12x = avg_ratio(norm_pedago_12x, avg_pedago_12x)
quartil_pegado_12x = quartiles_classification(sumx_arranging(norm_pedago_12x))

###################   Diagnístico ####################

# 0 - 30 -> DEU VAZIO
proddia03 = split_dataframe(tab_unida_prod,"Produto","Diagnóstico","licenças","0 - 30").iloc[:,:vsize-6]
normdia03 = norm_dataframe(proddia03)
avgdia03 = media_das_colunas(normdia03)
pontdia03 = avg_ratio(normdia03, avgdia03)
quartildia03 = quartiles_classification(sumx_arranging(normdia03))

# 30 - 400
proddia34 = split_dataframe(tab_unida_prod,"Produto","Diagnóstico","licenças","30 - 400").iloc[:,:vsize-6]
normdia34 = norm_dataframe(proddia34)
avgdia34 = media_das_colunas(normdia34)
pontdia34 = avg_ratio(normdia34, avgdia34)
quartildia34 = quartiles_classification(sumx_arranging(normdia34))

# 400 - 800
proddia48 = split_dataframe(tab_unida_prod,"Produto","Diagnóstico","licenças","400 - 800").iloc[:,:vsize-6]
normdia48 = norm_dataframe(proddia48)
avgdia48 = media_das_colunas(normdia48)
pontdia48 = avg_ratio(normdia48, avgdia48)
quartildia48 = quartiles_classification(sumx_arranging(normdia48))

# 800 - 1200 -> Deu vazio
proddia812 = split_dataframe(tab_unida_prod,"Produto","Diagnóstico","licenças","800 - 1200").iloc[:,:vsize-6]
normdia812 = norm_dataframe(proddia812)
avgdia812 = media_das_colunas(normdia812)
pontdia812 = avg_ratio(normdia812, avgdia812)
quartildia812 = quartiles_classification(sumx_arranging(normdia812))

# 1200 - x
proddia12x = split_dataframe(tab_unida_prod,"Produto","Diagnóstico","licenças","1200 - x").iloc[:,:vsize-6]
normdia12x = norm_dataframe(proddia12x)
avgdia12x = media_das_colunas(normdia12x)
pontdia12x = avg_ratio(normdia12x, avgdia12x)
quartildia12x = quartiles_classification(sumx_arranging(normdia12x))

###################   Banco   ####################

# 0 - 30 -> DEU VAZIO
prodbc03 = split_dataframe(tab_unida_prod,"Produto","Banco","licenças","0 - 30").iloc[:,:vsize-6]
normbc03 = norm_dataframe(prodbc03)
avgbc03 = media_das_colunas(normbc03)
pontbc03 = avg_ratio(normbc03, avgbc03)
quartilbc03 = quartiles_classification(sumx_arranging(normbc03))

# 30 - 400
prodbc34 = split_dataframe(tab_unida_prod,"Produto","Banco","licenças","30 - 400").iloc[:,:vsize-6]
normbc34 = norm_dataframe(prodbc34)
avgbc34 = media_das_colunas(normbc34)
pontbc34 = avg_ratio(normbc34, avgbc34)
quartilbc34 = quartiles_classification(sumx_arranging(normbc34))

# 400 - 800
prodbc48 = split_dataframe(tab_unida_prod,"Produto","Banco","licenças","400 - 800").iloc[:,:vsize-6]
normbc48 = norm_dataframe(prodbc48)
avgbc48 = media_das_colunas(normbc48)
pontbc48 = avg_ratio(normbc48, avgbc48)
quartilbc48 = quartiles_classification(sumx_arranging(normbc48))

# 800 - 1200 -> Deu vazio
prodbc812 = split_dataframe(tab_unida_prod,"Produto","Banco","licenças","800 - 1200").iloc[:,:vsize-6]
normbc812 = norm_dataframe(prodbc812)
avgbc812 = media_das_colunas(normbc812)
pontbc812 = avg_ratio(normbc812, avgbc812)
quartilbc812 = quartiles_classification(sumx_arranging(normbc812))

# 1200 - x
prodbc12x = split_dataframe(tab_unida_prod,"Produto","Banco","licenças","1200 - x").iloc[:,:vsize-6]
normbc12x = norm_dataframe(prodbc12x)
avgbc12x = media_das_colunas(normbc12x)
pontbc12x = avg_ratio(normbc12x, avgbc12x)
quartilbc12x = quartiles_classification(sumx_arranging(normbc12x))

# joining the pieces

# total quartile dataframe
lista_quartil = [quartil_pegado_030, quartil_pegado_34, quartil_pegado_48, quartil_pegado_812, quartil_pegado_12x, quartildia03, quartildia34, quartildia48, quartildia812, quartildia12x, quartilbc03, quartilbc34, quartilbc48, quartilbc812, quartilbc12x]
total_quartil = append_dataframes(lista_quartil).sort_values(by=['quartil','soma'], ascending=[False,True]).reset_index(drop=True)
total_quartil = pd.merge(total_quartil, t_prod, on="namespace", how='left')


# total points dataframe
lista_pontos = [pont_pedago_030, pont_pedago_34, pont_pedago_48, pont_pedago_812, pont_pedago_12x, pontdia03, pontdia34, pontdia48, pontdia812, pontdia12x, pontbc03, pontbc34, pontbc48, pontbc812, pontbc12x]
total_pontos = append_dataframes(lista_pontos).reset_index(drop=True)
total_pontos = pd.merge(t_prod, total_pontos, on="namespace", how='left')

# total norm dataframe
lista_norm = [norm_pedago_030, norm_pedago_34, norm_pedago_48, norm_pedago_812, norm_pedago_12x, normdia03, normdia34, normdia48, normdia812, normdia12x]
total_norm = append_dataframes(lista_norm).sort_values(by=['namespace'], ascending=[True]).reset_index(drop=True)


# points with riick
point_risk = pd.merge(total_quartil, total_pontos, on="namespace", how='outer')

