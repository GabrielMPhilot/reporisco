from os import sep
from re import A
import numpy as np
import pandas as pd
from computer.funcomputer import *
from computer.data_process import *
import streamlit as st


# Intervalo de datas
datas=pd.read_csv("./csvs/interval_datas.csv")
del datas['Unnamed: 0']
datas=datas.replace(np.inf, 0)
datas_list=datas["0"].tolist()
data_inicial = datas_list[0]
data_final = datas_list[1]

# numero de clientes
# total de ns 
ns_total = total_quartil["namespace"].tolist()
ns_total = int(len(ns_total))

# número de clientes pedagogico
ns_peda = split_dataframe(total_quartil,"Produto","Pedagógico")
ns_peda = int(len(ns_peda["namespace"].tolist()))

# número de clientes diagnostico
ns_diag = split_dataframe(total_quartil,"Produto","Diagnóstico")
ns_diag = int(len(ns_diag["namespace"].tolist()))

# número de clients escola +
ns_emais = split_dataframe(total_quartil,"Deal Owner","Magnum Queiroz")
ns_emais = int(len(ns_emais["namespace"].tolist()))

# número de clientes diagnostico
ns_banc = split_dataframe(total_quartil,"Produto","Banco")
ns_banc = int(len(ns_banc["namespace"].tolist()))

# Número de clientes sem banco
ns_semb = total_quartil[(total_quartil["Produto"]!="Banco")]
############### Número CARD ################
ns_semb_num = ns_semb["namespace"].shape[0]

############## Porcentagem em Risco alto #################
# Extraindo soma
ns_porcen = ns_semb.groupby(['Risco'])[['quartil']].count().reset_index()
aux_ns_porcen = ns_porcen["quartil"].sum()
ns_porcen["Porcentagem"]=((ns_porcen["quartil"]/aux_ns_porcen)*100).round(2)
ns_porcen=ns_porcen[(ns_porcen["Risco"]=="Risco alto")]
ns_porcen=ns_porcen["Porcentagem"].sum()

# Preparando dados para gráfico principal da classificação
# /Porcentagem de risco (Repositorio)
# todos produtos - banco
grafico_um= df_set_plotly_rik(ns_semb)
# produto pedagogico
grafico_um_peda = split_dataframe(ns_semb,"Produto","Pedagógico")
grafico_um_peda = grafico_um_peda[(grafico_um_peda["Deal Owner"]!="Magnum Queiroz")]
grafico_um_peda = df_set_plotly_rik(grafico_um_peda)
grafico_um_peda["Produto"]="Pedagógico"
# produto pedagogico
grafico_um_diag = split_dataframe(ns_semb,"Produto","Diagnóstico")
grafico_um_diag = grafico_um_diag[(grafico_um_diag["Deal Owner"]!="Magnum Queiroz")]
grafico_um_diag = df_set_plotly_rik(grafico_um_diag)
grafico_um_diag["Produto"]="Diagnóstico"
# produto escola +
grafico_um_emais =df_set_plotly_rik(split_dataframe(ns_semb,"Deal Owner","Magnum Queiroz"))
grafico_um_emais["Produto"]="Escola+"
# produto banco
grafico_um_banco = df_set_plotly_rik(split_dataframe(total_quartil,"Produto","Banco"))
grafico_um_banco["Produto"]="Banco"
# Unindo pro gráfico escolhido
lista_grafico_esco = [grafico_um_peda,grafico_um_diag,grafico_um_emais,grafico_um_banco]
grafico_um_escolhido = append_dataframes(lista_grafico_esco)

# Receita Hubspot
receita_hubtotal_aux = ns_semb[(ns_semb["Risco"]=="Risco alto") & (ns_semb["receita 2021"]!="S/Receita 2021 Hubspot")]
receita_hubtotal = (receita_hubtotal_aux["receita 2021"]).astype(float).sum()

# Número de namespaces em risco alto
numero_nsaltorisco = ns_semb[(ns_semb["Risco"]=="Risco alto")]
numero_nsaltorisco = numero_nsaltorisco["namespace"].shape[0]

# Número de namespaces em risco alto com receita2021 prenchida
numero_nsaltorisco_comreceita = receita_hubtotal_aux["namespace"].shape[0]
receita_risco_estimativa = ((receita_hubtotal/numero_nsaltorisco_comreceita)*numero_nsaltorisco).round(2)

# Preparando dados para gráficos de métricas para amostra de alto risco
df_show_altorisco_all = split_dataframe(total_pontos,"namespace","overnascimentodecastro")
# tabela conteudos
df_show_altorisco = get_columns(df_show_altorisco_all, t_conteudos)
df_show_altorisco = df_set_plotly(df_show_altorisco)
# tabela rela 
rela_show_altorisco = get_columns(df_show_altorisco_all, t_relas)
rela_show_altorisco = df_set_plotly(rela_show_altorisco)
# tabela questoes
ques_show_altorisco = get_columns(df_show_altorisco_all, t_quest)
ques_show_altorisco = df_set_plotly(ques_show_altorisco)
# tabela engajamento
engj_show_altorisco = df_set_plotly(get_columns(df_show_altorisco_all, t_engaj))

# Preparando dados para gráficos de métricas para amostra de baixo risco
df_show_brisco = split_dataframe(total_pontos,"namespace","colegioiguatemy")
# tabela conteudos
cont_show_brisco = df_set_plotly(get_columns(df_show_brisco, t_conteudos))
# tabela rela
rela_show_brisco = df_set_plotly(get_columns(df_show_brisco, t_relas))
# tabela questoes
quest_show_brisco = df_set_plotly(get_columns(df_show_brisco, t_quest))
# tabela engajamento
engj_show_brisco = df_set_plotly(get_columns(df_show_brisco, t_engaj))


# Começa os filtros
# Filtro por produto
# Arrumar colunas
filtro_todos = total_quartil.drop(['soma','quartil','n_usuarios','receita 2021','namespace hubspot'], axis=1)
produto_filtro = emojis_column_risk(filtro_todos)
produto_filtro = emojis_column_dealo(produto_filtro)
produto_filtro = produto_escola_mais(produto_filtro)

# Deal owner list
dealolist = produto_filtro["Deal Owner"].drop_duplicates().values.tolist()

# Grau de risco
grauriscolist = tuple(produto_filtro["Risco"].drop_duplicates().values.tolist())

# Namespace list
namespace_list = tab_unida_prod["namespace"].tolist()


