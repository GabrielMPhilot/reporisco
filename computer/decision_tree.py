# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import sklearn
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
# from computer.data_process import *
# from computer.data_front import *
# from computer.funcomputer import *
# from pathlib import Path
# from IPython.display import Image
# import sklearn.tree as tree
# from sklearn import tree
# from sklearn.tree import plot_tree
# 
# arvore_risco = reorder_columns(total_quartil,"Risco",1).iloc[:,:2]
# arvore_risco = arvore_risco[(arvore_risco["Risco"]=="Risco alto") | (arvore_risco["Risco"]=="Risco baixo")]
# 
# arvore_pontos = total_norm.copy()
# arvore_pontos = arvore_pontos.replace(np.nan,0)
# arvore_pontos = get_columns(arvore_pontos, pont_pedago_030)
# coluna_ap = arvore_pontos.columns.values.tolist()
# coluna_ap.remove("namespace")
# for item in coluna_ap:
#     for i in range(len(arvore_pontos["namespace"])):
#         aux_arvore = arvore_pontos.loc[i,item]
#         if aux_arvore >= 0.25 and aux_arvore <2:
#             arvore_pontos.loc[i,item]=1
#         else:
#             arvore_pontos.loc[i,item]=0
# 
# aux_arvore_pontos = total_quartil[(total_quartil["Produto"]=="Banco")]
# arvore_pontos = chose_rows(arvore_pontos,aux_arvore_pontos,False)
# arvore_risco = chose_rows(arvore_risco,aux_arvore_pontos,False)
# arvore_risco_teste = pd.merge(arvore_risco,arvore_pontos,on="namespace", how='left')
# # #
# arv = DecisionTreeClassifier()
# # #
# x = arvore_risco_teste.iloc[:,2:]
# y = arvore_risco_teste.loc[:,"Risco"]
# arv.fit(x, y)
# # #
# y_pred = arv.predict(x)
# # #
# xy=accuracy_score(y, y_pred)
# # #
# # #
# # ##    dot_data = StringIO()
# # ##    
# # ##    tree.export_graphviz(arv,
# # ##                         out_file = dot_data, 
# # ##                         class_names = ['Risco alto',"Risco médio alto","Risco médio baixo" ,'Risco baixo'],
# # ##                         feature_names = x.columns.tolist(),
# # ##                         filled = True,
# # ##                         rounded = True,
# # ##                         special_characters = True)
# # ##    graph = pydotplus.graph_from_dot_data(dot_data.getvalue()) 
# # ##    Image(graph.create_png())
# # #
# xx = x.columns.values.tolist()
# yy = ['Risco alto','Risco baixo']
# # #
# fig, axes = plt.subplots(nrows =1, ncols=1, figsize=(15,15),dpi=300)
# tree.plot_tree(arv, 
#             feature_names=xx, 
#             class_names=yy, 
#             #filled = True,
#             fontsize=14)
# fig.savefig("./computer/treedecision.png")