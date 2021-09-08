
# Funçoes
from re import T
import numpy as np
import pandas as pd
from datetime import date, timedelta
import time
import base64
from pandas.core.frame import DataFrame


#### BACK-END FUNCTIONS

# reorder columns
def reorder_columns(dataframe, col_name, position):
    """Reorder a dataframe's column.
    Args:
        dataframe (pd.DataFrame): dataframe to use
        col_name (string): column name to move
        position (0-indexed position): where to relocate column to
    Returns:
        pd.DataFrame: re-assigned dataframe
    """
    temp_col = dataframe[col_name]
    dataframe = dataframe.drop(columns=[col_name])
    dataframe.insert(loc=position, column=col_name, value=temp_col)
    return dataframe

# columns avareges
def media_das_colunas(dataframe):
    """Get averages of each columns in the dataframe.

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: Average dataframe.
    """
    # getting column names
    columns = dataframe.columns.values.tolist()
    columns.remove("namespace")

    # df auxiliar
    df=pd.DataFrame()

    # laço de interação
    for col in columns:
        lista_mean=list()
        m=float("{:.2f}".format((dataframe[col].mean())))
        lista_mean.append(m)
        df_aux=pd.DataFrame(lista_mean)
        df[col]=df_aux.sum()
    
    #atribuindo nome
    df["namespace"]="Média Eduqo"
    # reordenando df
    df=reorder_columns(df,"namespace",0)
    return df

# dataframe normalization
def norm_dataframe(dataframe):
    """Get normalization of each columns in the dataframe.

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: Normalized dataframe.
    """
    # gettings column names
    columns = dataframe.columns.values.tolist()
    columns.remove("namespace")

    # df auxiliar
    df=pd.DataFrame()
    
    # interação normalização
    for col in columns:
        var_min=dataframe[col].min()
        var_max=dataframe[col].max()
        df[col]=((dataframe[col]-var_min)/(var_max-var_min)).round(2)
        df=df.replace(np.inf, 0)
        df=df.replace(np.nan, 0)
    # pegando os namespaces
    df["namespace"]=dataframe["namespace"]
    df=reorder_columns(df, "namespace",0)
    return df

# risc quart's classification with outliers
def quartiles_classification_outlier(dataframe):
    """Classification by dataframe quartile

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe sorted by quartile
    """
    # aux variables for classification of the quartiles
    dataframe["quartil"]=0
    dataframe["Risco"]=0
    col="soma"
    
    
    #removing out liers
    var_quartile_025=dataframe[col].quantile([0.15])
    var_quantile_075=dataframe[col].quantile([0.85])
    for i in range(len(dataframe[col])):
        a=0
        b=0
        var_aux=dataframe[col][i]
        if var_aux > var_quantile_075[0.85]:
            a=1
            b="Risco baixo"
        elif var_aux < var_quartile_025[0.15]:
            a=4
            b="Risco alto"
        else:
            #auxiliar quartil
            aux_var_quartil=dataframe[(dataframe[col]>var_quartile_025[0.15]) & (dataframe[col] < var_quantile_075[0.85])]
            q=(aux_var_quartil[col].max()-aux_var_quartil[col].min())/4
            m=aux_var_quartil[col].min()
            aux=dataframe[col][i]
            if  aux >= m and aux < m +q:
                a=4
                b="Risco alto"
            elif aux >= m+q and aux < m + 2*q:
                a=3
                b="Risco médio alto"
            elif aux >= m+2*q and aux < m + 3*q:
                a=2
                b="Risco médio baixo"
            else:
                a=1
                b="Risco baixo"
        dataframe.loc[i, "quartil"]=a
        dataframe.loc[i,"Risco"]=b
    
    return dataframe

# risc quart's classification  
def quartiles_classification(dataframe):
    """Classification by dataframe quartile

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe sorted by quartile
    """
    # aux variables for classification of the quartiles
    dataframe["quartil"]=0
    dataframe["Risco"]=0
    col="soma"
    
    m=dataframe[col].min()
    q=(dataframe[col].max()-dataframe[col].min())/4
    
    for i in range(len(dataframe[col])):
        a=0
        b=0
        aux=dataframe[col][i]
        if  aux >= m and aux < m +q:
            a=4
            b="Risco alto"
        elif aux >= m+q and aux < m + 2*q:
            a=3
            b="Risco médio alto"
        elif aux >= m+2*q and aux < m + 3*q:
            a=2
            b="Risco médio baixo"
        else:
            a=1
            b="Risco baixo"
        dataframe.loc[i, "quartil"]=float(a)
        dataframe.loc[i,"Risco"]=b
    
    return dataframe
        
# df to link
def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="listanamespaces.csv">Clique aqui para baixar o CSV</a>'
    return href
    
# spliting dataframe based on a value of a column    
def split_dataframe(dataframe, column_name1="a2",var1="a", column_name2="b2", var2="b"):
    """Spliting the dataframe by variable(s)

    Args:
        dataframe(pd.DataFrame): dataframe to use
        column value (any): variable to use
        arbitary second column value (any): variable to use

    Returns:
        pd.Dataframe: splited dataframe
    """
    if var1+var2=="ab" or column_name1+column_name2=="a2+b2":
        return '⚠️ Warning ⚠️ Needs at leat one column name and variable'
    elif (column_name1!="a2" and var1=="a") or (column_name2!="b2" and var2=="b"):
        return '⚠️ Warning ⚠️ Missing a value'
    else:
        df = pd.DataFrame()
        if column_name2+var2=="b2b":
            df = dataframe[(dataframe[column_name1]==var1)].reset_index(drop=True)
            return df
        else:
            df = dataframe[(dataframe[column_name1]==var1) & (dataframe[column_name2]==var2)].reset_index(drop=True)
            return df

# extracting value of each cell by average ratio
def avg_ratio(dataframe, avg_dataframe):
    """extracting value of each cell by average ratio
    
    Args:
        dataframe1(pd.DataFrame): dataframe1 to use
        dataframe2(pd.DataFrame): dataframe2 to use

    Returns:
        pd.Dataframe: dataframe valueted by the ratio avg of each colum
    """
    coluna = avg_dataframe.columns.values.tolist()
    coluna.remove("namespace")
    df = pd.DataFrame()
    for item in coluna:
        v_avg=avg_dataframe.loc[0,item]
        df[item]=(dataframe[item]/v_avg).round(2)
    df["namespace"]=dataframe["namespace"]
    df=reorder_columns(df,"namespace",0)
    df=df.replace(np.nan, 0)
    return df

# sum of all numeric values in axis=x
def sumx_arranging(dataframe):
    """Sum in x axis and arraging dataframe
    
    Args:
        dataframe(pd.DataFrame): dataframe to use
        

    Returns:
        pd.Dataframe: dataframe with the sum in x
    """
    df=pd.DataFrame()
    df=dataframe.copy()
    df["soma"]=df.sum(axis=1 ,numeric_only=True)
    df=reorder_columns(df,"soma",1).iloc[:,:2]
    df=df.sort_values(by="soma", ascending="True").reset_index(drop=True)
    return df 

# appending multiple dataframes on a single one
def append_dataframes(list):
    """Apending multiple dataframes on a single one
    
    Args:
        list(list()): list of dataframes
        

    Returns:
        pd.Dataframe: Dataframe
    """
    df = pd.DataFrame()
    for item in list:
        df=df.append(item)
    return df

# geting     
def get_columns(dataframe1,dataframe2):
    """Chosing the columns to use from a dataframe to other
    
    Args:
        dataframe1 (pd.Dataframe): dataframe with multiple columns
        dataframe2 (pd.Dataframe): dataframe with the columns to keep
        

    Returns:
        pd.Dataframe: Dataframe with only the columns of the dataframe2
    """
    list_aux = dataframe2.columns.values.tolist()
    df = pd.DataFrame()
    for item in list_aux:
        aux_var = dataframe1[item]
        df[item]=aux_var
    
    return df



#### FRONT-END FUNCTIONS

# set up dataframe for plotly bar graph (métrics)
def df_set_plotly(data_frame):
     """Set up dataframe for plotly bar graph (métrics)

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe ready for plot the graph (métrics)
    """
     # gettings column names
     coluna = data_frame.columns.values.tolist()
     coluna.remove("namespace")
     df=pd.DataFrame()
     for col in coluna:
        for i in range(len(data_frame[col])):
            ns=data_frame.loc[i,"namespace"]
            co=col
            valor=data_frame.loc[i, col]
            new_row={'Namespace': ns, 'Métricas': co, 'Valor': valor}
            df=df.append(new_row, ignore_index=True)
     return df

# set up dataframe for plotly bar graph (risk)
def df_set_plotly_rik(dataframe):
    """Set up dataframe for plotly bar graph (risk)

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe ready for plot the graph (risk)
    """
    df = pd.DataFrame()
    df = dataframe.groupby(['Risco'])[['quartil']].count().reset_index()
    aux_df= df["quartil"].sum()
    df["Porcentagem"]=(((df["quartil"]/aux_df)*100).round(2)).astype(str)+'%'
    df = df.rename(columns={"quartil": "Quantidade de escolas"})
    # sorting the df
    df["order"]=0
    for i in range (len(df["Risco"])):
        var_graph_order=0
        var_graph_order=df["Risco"][i]
        if var_graph_order =='Risco alto':
            b=int(1)
        elif var_graph_order =='Risco médio alto':
            b=int(2)
        elif var_graph_order =='Risco médio baixo':
            b=int(3)
        elif var_graph_order =='Risco baixo':
            b=int(4)
        df.loc[i,"order"]=b
    df = df.sort_values(by="order", ascending=True).reset_index(drop=True)
    #df = df.rename(columns={"quartil": "Quantidade de escolas"})
    return df

# ading emojis to the risk column
def emojis_column_risk(dataframe):
    """Add emojis to the risk column

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe with emojis on the risk column
    """
    df = pd.DataFrame()
    df = dataframe.copy()
    col = "Risco"
    for i in range(len(dataframe[col])):
        var_aux = dataframe.loc[i,col]
        if var_aux =='Risco alto':
            df.loc[i,col]='🔥'+' '+"Alto"
        elif var_aux =='Risco médio alto':
            df.loc[i,col]='⚠️'+' '+"Médio alto"
        elif var_aux =='Risco médio baixo':
            df.loc[i,col]='🥈'+' '+"Médio baixo"
        else:
            df.loc[i,col]='🥇'+' '+"Baixo"
    return df

# ading emojis to the dealowner column
def emojis_column_dealo(dataframe):
    """Add emojis to the dealowner column

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe with emojis on the dealowner column
    """
    df = pd.DataFrame()
    df = dataframe.copy()
    col = "Deal Owner"
    for i in range(len(dataframe[col])):
        var_aux = dataframe.loc[i,col]
        if var_aux =='S/Deal Owner Hubspot':
            df.loc[i,col]="✖️"

    return df

#
def produto_escola_mais(dataframe):
    """Set the product escola+ ready for the front us

    Args:
        dataframe(pd.DataFrame): dataframe to use

    Returns:
        pd.Dataframe: dataframe with escola+ ready for the front us
    """
    df = pd.DataFrame()
    df = dataframe.copy()
    col ="Deal Owner"
    col2 = "Produto"
    for i in range(len(df[col])):
        var = df.loc[i, col]
        if var =="Magnum Queiroz":
            df.loc[i,col2]="Escola+"
    return df





















