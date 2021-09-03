from re import T
import streamlit as st
import numpy as np
import pandas as pd
import base64
import plotly.graph_objects as go
import plotly.express as px
from PIL import Image
from computer.data_process import *
from computer.data_front import *
from computer.funcomputer import *

import time

st.image('[LOGO] Eduqo.png')

# Titulo


"""
# 🌡️ Repositorios - Produto


"""
image = Image.open('[LOGO] Eduqo.png')
st.sidebar.image(image,caption='Eduqo - Plataforma QMágico',use_column_width=True)

st.sidebar.markdown('Feito por: Gabriel Philot (Tio Gibbs)')
st.sidebar.write('#### Material de apoio, caso queira saber mais sobre o projeto.')
st.sidebar.write('####')
st.sidebar.write("##### Github:  [link](https://github.com/GabrielMPhilot/Repository_Score)")
st.sidebar.write('#')

"""
### 💡 Grande ideia do Projeto
O objetivo desse projeto é criar um HealthScore escalavel e preciso sobre nossos clientes.
Utilizamos primeiramente dados diversos da usabilidade do Produto (por enquanto), para criarmos
métricas que consigam mapear se nossos clientes estão utilizando a plataforma de maneira adequada,
com as métricas é formado um modelo para Rankear cada escola em um grau de risco especifico.

### 💾 Dados utilizados
Os dados utilizados foram segmentados (por enquanto) em 4 diferentes tabelas.
"""
"""
#### 1. Tabela de Conteudos:
"""
expander = st.expander(" -> (clique aqui 🖱️)")
expander.write(" Essa tabela contempla dados de conteúdos de todos os tipos do caderno, segmenta cada tipo, como por exemplo PDFS, Videos, Tarefas e S.Exercicios.")
"""
#### 2. Tabela de Questões:
"""
expander = st.expander(" -> (clique aqui 🖱️)")
expander.write(" Essa Tabela contempla dados do n° de questões totais subidas(prof/admin), n° de questões discursivas subidas(profs/admin),n° de questões totais do banco subidas (prof/admin).")
"""
#### 3. Tabela de Relatórios:
"""
expander = st.expander(" -> (clique aqui 🖱️)")
expander.write("Essa Tabela contempla dados do n° de vizualização de relátorios (proffs/admin/alunos) de A.A's, n° de vizualização de relátorios (prof/admin/alunos) de S.Exs,n° de vizualização de relátorios (prof/admin) de Cadernos, n° de vizualização de relátorios (admin) de AD's, n° de vizualização de relátorios (admin) Mensais (QBR,Mensal).")
"""
#### 4. Tabela de Engajamento com funcionalidades diferenciadas:
"""
expander = st.expander(" -> (clique aqui 🖱️)")
expander.write("Essa Tabela contempla dados de n° correções/interações não automatizadas com os alunos (prof/admin), n° de resultados baixados (prof/admin), n° de comentarios no forum (prof/admin/aluno), n° de likes/dislikes em conteúdos (alunos) e n° de upload de vídeos/áudios subidos (alunos). ")

st.write('#### ⏳ Dados extraídos de:',data_inicial,"  até",data_final)
"""
### 
"""
"""
### 📑 Número de namespaces analisados por tipo de produto
"""
st.write('#### O número total de namespaces analisados foi:',ns_total)
st.write('#### Namespaces do produto Pedagógico:',ns_peda-4)
st.write('#### Namespaces do produto Diagnóstico:',ns_diag-1)
st.write('#### Namespaces do produto Escola+:',ns_emais)
st.write('#### Namespaces do produto Banco:',ns_banc)

"""
### 
"""
"""
### 👩🏽‍🏫 Metodologia
"""
expander = st.expander(" -> (clique aqui 🖱️)")
expander.write("1. Com os dados são criadas métricas para parametrizar o tamanho da escola. Exemplo: Número total de PDFS/total de conteúdos")
expander.write("2. Com as métricas os namespaces são separados por produto e pelo número de licenças, para realizarmos a normalização que seja coerente ao contexto de cada namespace.")
expander.write("Obs item 2: No caso do produto Escola+, não temos uma quantidade grande de escolas e nem uma distanção clara via usabilidade de produto, portanto esse foi classificado dentro dos produtos Pedagógico e Dignóstico.")
expander.write("3. São somados os valores de 0 a 1 da normalização é aplicado um modelo de quartil's que nos dá a **classificação de risco**")
"""
"""
"""
### 🔍 Certo agora vamos para os **Resultados**.

Obs: Por motivos de estratégia que envolvem maior quantidade de receita e dificuldade de traquear usabilidade, o produto **Banco** não entrará próximas discussões/analises.

"""
# CARDS

figa = go.Figure()

figa.add_trace(go.Indicator(
    #mode = "number+delta",
    value = ns_semb_num ,
    domain = {'x': [0.25, 0.75], 'y': [0.7, 1]},
    title = {"text": "N° de escolas analisadas<br><span style='font-size:0.8em;color:gray'>"}))
    ##delta = {'reference': 400, 'relative': True, 'position' : "top"}))
figa.add_trace(go.Indicator(
    #mode = "number+delta",
    value = ns_porcen,
    domain = {'x': [0.25, 0.75], 'y': [0, 0.3]},
    title = {"text": "<span style='font-size:1em;color:red'>%<br><span style='font-size:0.8em;color:red'>de escolas em Risco alto (Repositórios)</span><br>"}))
    ##delta = {'reference': 400, 'relative': True, 'position' : "top"}))
st.plotly_chart(figa)

# Gráfico 1. Health Score - Pontuação via nosso modelo


fig =px.bar(grafico_um, x='Risco', y='Quantidade de escolas',
           color='Risco',
           color_discrete_sequence=["#E45756","#F58518","#54A24B","#4C78A8"],
           #color_discrete_sequence=px.colors.qualitative.T10,
            text=grafico_um['Porcentagem'])


fig.update_xaxes(showgrid=False)
fig.update_layout(title = "Distribuição no N° de escolas por grau de Risco")

st.plotly_chart(fig)
"""
#### Gráfico 1. Utiliza os namespaces com Produtos (Pedagógico, Diagnóstico e Escola+)
#
"""
if st.checkbox(" <-  (clique aqui 🖱️) Se quiser visualizar esse mesmo gráfico de um determinado produto "):
    genre = st.radio("Escolha o tipo de Produto.",('Pedagógico', 'Diagnóstico','Escola+','Banco'))
    grafico_um_escolhido_plot=split_dataframe(grafico_um_escolhido,"Produto",genre)
    figesco =px.bar(grafico_um_escolhido_plot, x='Risco', y='Quantidade de escolas',
           color='Risco',
           color_discrete_sequence=["#E45756","#F58518","#54A24B","#4C78A8"],
           #color_discrete_sequence=px.colors.qualitative.T10,
            text=grafico_um_escolhido_plot['Porcentagem'])


    figesco.update_xaxes(showgrid=False)
    figesco.update_layout(title = "Distribuição no N° de escolas por grau de Risco")

    st.plotly_chart(figesco)
    st.write('#### Gráfico 1.1 Utiliza os namespaces com o Produto:',genre)
    st.write('#')


"""
### 🤔  Discussão desses resultados para nosso contexto
Temos três **OKR's** diretamente ligados com evitar o **CHURN** de nossas escolas e estes são:
"""
st.image('orkrs.png')

"""
Portanto foi feita uma estimativa do valor que temos em **Risco alto** de receita.
"""

st.write('## 💰 Valor estimado de: R$',receita_risco_estimativa)
#st.write('Utilizamos dados do Hubspot para obter esse valor, onde de ',numero_nsaltorisco,'namespaces apenas',numero_nsaltorisco_comreceita,'tinham a informação de receita 2021 preenchida')
expander = st.expander("OBS importante: -> (clique aqui 🖱️)")
expander.write("Utilizamos dados do Hubspot para obter esse valor, tivemos algumas dificuldades para conseguir achar informações de diversos tipos, como a mais importante nesse caso: O próprio **Namespace no Hubspot** (esse campo é muito importante para conseguirmos ligar os dados do Hub com os dados de produto). Então lembrando que estamos falando de apenas uma estimativa que pode ser muito melhorada, algo que será foco em nossos próximos sprints.")

"""
### 💡 É valido reforçar
 1. O objetivo inicial desse relátorio é ressaltar o grau de risco de um namespace, e para isso utilizamos o modelo de quartil's para fazer a análise.
 2. No modelo de quartil's devemos entender que funciona como uma corrida, ou seja sempre teremos últimos lugares e primeiros lugares.
 3. Então a prioridade de ajuda deve ser sempre em função dos clientes que estão nos últimos lugares da corrida.
"""
st.image('corrida.png')
"""
### 🚀 Como extrair valor do modelo de quartil's
 1. Olhar como os primeiros colocados se saem pelas métricas (/visitar seus namespaces) e tentar trazer seus exemplos de uso para outras escolas.
 2. Priorizar o foco de ajuda nós últimos colocados.
 3. É uma boa pratica na hora de visualizar as diferenças entre últimos colocados e primeiros colocados, escolher namespace das mesmas categorias, ou seja
 namespaces com mesmo produto e número de licenças, assim estaria aviliando namespaces do mesmo contexto e sistema de pontuação (**categoria**).
"""
"""
##
"""
"""
### 🧪 Teste para um caso de **Risco alto** e **Risco Baixo**.
"""

"""
### 🔥 Risco alto
"""
if st.checkbox('<-  (clique aqui 🖱️) '):
    zxns01="overnascimentodecastro"
    st.write('No resultado do modelo apareceu que o namespace **overnascimentodecastro** foi classificado com **Risco alto**')
    st.write('Ressaltando que este namespace é do produto **Pedagógico** e tem **474** usuários portanto está no grupo de licenças de **400 - 800**.')
    st.write('Certo vamos olhar as pontuações que o mesmo obteve no modelo em relação a sua **categoria**.')
    st.write('Os gráficos que serão exibidos são referentes a cada tabela de métricas.')
    expander = st.expander("Como observar o valor de cada gráfico ? -> (clique aqui 🖱️)")
    expander.write('Simples, o valor médio de cada categoria será sempre **1**, então se o namespace se saiu bem estará com o valor próximo ou maior a **1**, se o namespace se saiu mal estará com o valor inferior a **1**.')
    


    fig_cont =px.bar(df_show_altorisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=df_show_altorisco['Valor'])

    fig_cont.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_cont.update_xaxes(showgrid=False)
    fig_cont.update_layout(title = "Métricas na Tabela de Conteúdos")
    st.plotly_chart(fig_cont)


    expander = st.expander("Obs Gráfico de conteúdos: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
    expander.write("Nesse gráfico as métricas relacionadas a PDF's, e vídeos são inversamente proporcionais a pontuação, ou seja quanto menor a quantidade de conteúdos destes tipos maior será a pontuação.")
    
    fig_rela =px.bar(rela_show_altorisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=rela_show_altorisco['Valor'])

    fig_rela.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_rela.update_xaxes(showgrid=False)
    fig_rela.update_layout(title = "Métricas na Tabela de Relátorios")
    st.plotly_chart(fig_rela)

    fig_quest =px.bar(ques_show_altorisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=ques_show_altorisco['Valor'])

    fig_quest.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_quest.update_xaxes(showgrid=False)
    fig_quest.update_layout(title = "Métricas na Tabela de Questões")
    st.plotly_chart(fig_quest)

    fig_engaj =px.bar(engj_show_altorisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=engj_show_altorisco['Valor'])

    fig_engaj.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_engaj.update_xaxes(showgrid=False)
    fig_engaj.update_layout(title = "Métricas na Tabela de Engajamento")
    st.plotly_chart(fig_engaj)
    expander = st.expander("Obs Gráfico de engajamento: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
    expander.write("Nesse gráfico a métrica relacionada a baixar resultados é inversamente proporcional, ou seja quanto menos resultados a escola baixar maior será a pontuação, pois esse dado indica que a escola não está utilizando nossas ferramentas de relátorios e isso pode vir a ser uma grande dor da escola, exemplo desse dor: Colégio Eccos.")
    st.write('##')
    st.write('### 📝 Diagnóstico com a as tabelas e olhando namespace')
    st.write("#### Link do namespace:  [link](https://overnascimentodecastro.qmagico.com.br/cadernos/todos_cadernos)")
    st.write('##')
    st.write('1. Primeira tabela, logo de cara fica evidente que a escola não tem uma grande variabilidade de tipos de conteúdos em seus cadernos. Podemos ver a **total ausência** de tarefas e S.e. Entretanto aparecem pontuações relativamente boas na parte de PDF e Videos, fui investigar os cadernos do namespace e verifiquei que o mesmo utiliza muitos power points, algo que deixei escapar para montar as métricas (irei atualizar esse tipo dentro do quadro de PDFS) indicando que então sua pontuação de PDFS seria bem baixa (inversamente proporcional).')
    st.write('2. Segunda tabela, maior parte das métricas nulas e as que tem algum uso são bem baixas, indicando que o namespace não faz uso dessa ferramenta tão importante.')
    st.write('3. Terceira tabela, não tem nenhuma questão discursiva, baixxima utilização de questões e questões do banco')
    st.write('4. Quarta tabela, engajamento nulo na maioria das métricas, vale a pena ressaltar aqui que seus **Admins** estão baixando bastante resultados e não utilizando nada de visualização de relátorios, problema parecido com o que tivemos recentemente com o colégio Eccos.')
    st.write('### 💣 Conclusão do Diagnóstico')
    st.write('Primeiramente convido a quem estiver lendo ir para o namespace na parte dos cadernos (e também procurar por interações dos alunos) com seus proprios olhos.')
    st.write('A partir dos resultados e insights das tabelas podemos ir e validar isso no namespace, portanto, conseguimos caracterizar esse namespace como **Risco Alto** e antecipar o mal uso dessa plataforma, antes que ela nos comunicasse que não enxerga valor na plataforma, podendo resultar em um churn. Essa baixa utilização das ferramentas que nos diferenciam de outros competidores, como o Google Classroom, será sempre uma ameaça e precisamos combatê-la ativamente e mostrar ao colégio oportunidades de extrair ainda mais da plataforma e que ele possa estar perdendo.')


"""
### 🥇 Risco Baixo
"""

if st.checkbox('<-   (clique aqui 🖱️) '):
    st.write('No resultado do modelo apareceu que o namespace **colegioiguatemy** foi classificado com **Risco baixo**')
    st.write('Ressaltando que este namespace é do produto **Pedagógico** e tem **481** usuários portanto está no grupo de licenças de **400 - 800**.')
    st.write('Certo vamos olhar as pontuações que o mesmo obteve no modelo em relação a sua **categoria**.')
    st.write('Os gráficos que serão exibidos são referentes a cada tabela de métricas.')
    expander = st.expander("Como observar o valor de cada gráfico ? -> (clique aqui 🖱️)")
    expander.write('Simples, o valor médio de cada categoria será sempre **1**, então se o namespace se saiu bem estará com o valor próximo ou maior a **1**, se o namespace se saiu mal estará com o valor inferior a **1**.')

    fig_cont1 =px.bar(cont_show_brisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=cont_show_brisco['Valor'])

    fig_cont1.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_cont1.update_xaxes(showgrid=False)
    fig_cont1.update_layout(title = "Métricas na Tabela de Conteúdos")
    st.plotly_chart(fig_cont1)


    expander = st.expander("Obs Gráfico de conteúdos: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
    expander.write("Nesse gráfico as métricas relacionadas a PDF's, e vídeos são inversamente proporcionais a pontuação, ou seja quanto menor a quantidade de conteúdos destes tipos maior será a pontuação.")
    
    fig_rela1 =px.bar(rela_show_brisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=rela_show_brisco['Valor'])

    fig_rela1.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_rela1.update_xaxes(showgrid=False)
    fig_rela1.update_layout(title = "Métricas na Tabela de Relátorios")
    st.plotly_chart(fig_rela1)

    fig_quest1 =px.bar(quest_show_brisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=quest_show_brisco['Valor'])

    fig_quest1.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_quest1.update_xaxes(showgrid=False)
    fig_quest1.update_layout(title = "Métricas na Tabela de Questões")
    st.plotly_chart(fig_quest1)

    fig_engaj1 =px.bar(engj_show_brisco, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=engj_show_brisco['Valor'])

    fig_engaj1.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
    fig_engaj1.update_xaxes(showgrid=False)
    fig_engaj1.update_layout(title = "Métricas na Tabela de Engajamento")
    st.plotly_chart(fig_engaj1)
    expander = st.expander("Obs Gráfico de engajamento: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
    expander.write("Nesse gráfico a métrica relacionada a baixar resultados é inversamente proporcional, ou seja quanto menos resultados a escola baixar maior será a pontuação, pois esse dado indica que a escola não está utilizando nossas ferramentas de relátorios e isso pode vir a ser uma grande dor da escola, exemplo desse dor: Colégio Eccos.")
    st.write('##')
    st.write('### 📝 Diagnóstico com a as tabelas e olhando namespace')
    st.write("#### Link do namespace:  [link](https://colegioiguatemy.qmagico.com.br/cadernos/todos_cadernos)")
    st.write('##')
    st.write('1. Primeira tabela, métricas em sua maioria próxima a média da categoria, salvando a de tarefas que tem um altissmo desempenho de **2,5** o valor médio, indicando uma grande variabilidade de tipo de conteúdos e personalização.')
    st.write('2. Segunda tabela, métricas em sua maioria bem acima da média! Mostrando que geramos muito valor com nossos relátorios para eles (diferencial Eduqo).')
    st.write('3. Terceira tabela, novamente métricas bem acima da média, em especial fazem um uso bem grande de questões discursivas mostrando uma boa personalização do ensino. Também tem um bom uso de nosso banco de questões, algo que é um diferencial de Eduqo e mostra que geramos valor novamente.')
    st.write('4. Quarta tabela,  métricas absurdamente acima da média, **20** vezes o valor da média em comentario em forums, definitivamente eles interagem bem com seus alunos, mostrando um alto nível de personalização e geração de valor para as famílias. Obs notei algo de estranho com a métrica de baixar resultados vou conferir nos códigos o que houve pois pode ser que por eles não usarem a ferramenta isso possa ter zerado o valor.')
    st.write('### 🎉 Conclusão do Diagnóstico')
    st.write('Primeiramente convido a quem estiver lendo ir para o namespace na parte dos cadernos (e também procurar por interações dos alunos) com seus proprios olhos.')
    st.write('Esse resultado parece bem obvio e já era sabido que esse namespace tem um uso bem acima da média. Porém ele pode ser usado para testar o modelo, que conseguiu demonstrar que o namespace tem um **Risco baixo**.')



"""
###  🧾 Exposição de todos os resultados métricas 
"""
opcao = st.radio("Escolha o tipo de vizualização dos resultados.",('Produto', 'Deal Owner','Grau de Risco','Todos os namespaces'))
if opcao =="Produto":
    opcao2 = st.radio("Escolha o tipo de Produto. ",('Pedagógico', 'Diagnóstico','Escola+','Banco'))
    produto_filtro_produto=split_dataframe(produto_filtro,"Produto",opcao2)
    expander = st.expander("Tabela de resultados pelo produto escolhido: -> (clique aqui 🖱️)")
    expander.dataframe(produto_filtro_produto)
elif opcao =="Deal Owner":
    st.write('Lembrando que por conta da auscencia do campo namespace no Hubspot não conseguimos ligar todos os Deal Owners! por isso o ✖️')
    select = st.selectbox('Deal Owner', dealolist, key='2')
    produto_filtro_dealo=split_dataframe(produto_filtro,"Deal Owner",select)
    expander = st.expander("Tabela de resultados pelo Deal Owner escolhido: -> (clique aqui 🖱️)")
    expander.table(produto_filtro_dealo)
elif opcao == "Grau de Risco":
    opcao3 = st.radio("Escolha o Grau de Risco.",grauriscolist)
    produto_filtro_risco = split_dataframe(produto_filtro,"Risco",opcao3)
    expander = st.expander("Tabela de resultados pelo Grau de Risco escolhido: -> (clique aqui 🖱️)")
    expander.dataframe(produto_filtro_risco)
else:
    expander = st.expander("Tabela de resultados de Todos os namespaces: -> (clique aqui 🖱️)")
    expander.dataframe(produto_filtro)

"""
Após checar os resultados, é uma boa pratica, caso tenha alguma dúvida ou queira fazer alguma analise, checar as métricas de seu namespace de escolha.

"""

"""
###  📊 Visualização de todas as métricas por **Namespace**
"""
select2 = st.selectbox('',namespace_list, key='1')
filtronamespace = split_dataframe(total_pontos,"namespace",select2)
contshow = df_set_plotly(get_columns(filtronamespace,t_conteudos))
relashow = df_set_plotly(get_columns(filtronamespace,t_relas))
questshow = df_set_plotly(get_columns(filtronamespace, t_quest))
engjshow = df_set_plotly(get_columns(filtronamespace, t_engaj))

fig_cont11 =px.bar(contshow, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=contshow['Valor'])

fig_cont11.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
fig_cont11.update_xaxes(showgrid=False)
fig_cont11.update_layout(title = "Métricas na Tabela de Conteúdos")
st.plotly_chart(fig_cont11)

expander = st.expander("Obs Gráfico de conteúdos: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
expander.write("Nesse gráfico as métricas relacionadas a PDF's, e vídeos são inversamente proporcionais a pontuação, ou seja quanto menor a quantidade de conteúdos destes tipos maior será a pontuação.")
fig_rela11 =px.bar(relashow, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=relashow['Valor'])

fig_rela11.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
fig_rela11.update_xaxes(showgrid=False)
fig_rela11.update_layout(title = "Métricas na Tabela de Relátorios")
st.plotly_chart(fig_rela11)

fig_quest11 =px.bar(questshow, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=questshow['Valor'])

fig_quest11.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
fig_quest11.update_xaxes(showgrid=False)
fig_quest11.update_layout(title = "Métricas na Tabela de Questões")
st.plotly_chart(fig_quest11)

fig_engaj11 =px.bar(engjshow, x='Métricas', y='Valor',
               color='Namespace',barmode='group',
               color_discrete_sequence=["rgb(102, 197, 204)","rgb(248, 156, 116)"],#)#"#54A24B","#4C78A8"],
               #color_discrete_sequence=px.colors.qualitative.T10,
                text=engjshow['Valor'])

fig_engaj11.add_hline(y=1, line_dash="dot", col="all",
              annotation_text="Média Categoria", 
              annotation_position="bottom right")
fig_engaj11.update_xaxes(showgrid=False)
fig_engaj11.update_layout(title = "Métricas na Tabela de Engajamento")
st.plotly_chart(fig_engaj11)
expander = st.expander("Obs Gráfico de engajamento: Métricas inversamente proporcionais -> (clique aqui 🖱️)")
expander.write("Nesse gráfico a métrica relacionada a baixar resultados é inversamente proporcional, ou seja quanto menos resultados a escola baixar maior será a pontuação, pois esse dado indica que a escola não está utilizando nossas ferramentas de relátorios e isso pode vir a ser uma grande dor da escola, exemplo desse dor: Colégio Eccos.")
"""
### 💎 Iluminações ( Insights )
O foco ( por enquanto ) será em cima do mal uso da plataforma.
"""

expander_cont = st.expander("Métricas de Conteúdos -> (clique aqui 🖱️)")
expander_cont.write("(1) Escolas com personalização alta geralmente fazem bom uso de tarefas e série de exercícios. (2) Escolas que usam a plataforma como repositórios tendem a utilizar muitos vídeos e pdfs.")
expander_rel = st.expander("Métricas de Relátorios -> (clique aqui 🖱️)")
expander_rel.write("(1) Visualização de relatórios: Os nossos relatórios são um de nossos diferenciais para os concorrentes, e sua subutilização também pode indicar um mal uso da plataforma.")
expander_que = st.expander("Métricas de Questões -> (clique aqui 🖱️)")
expander_que.write("(1) Escolas que utilizam pouco o banco não valorizam um de nossos principais diferenciais competitivos em relação ao Google Classroom, então pode ser uma questão perigosa para potenciais churns. (2) Baixo uso de questões discursivas pode significar uma baixa personalização do uso da plataforma.")
expander_eng = st.expander("Métricas de Engajamento -> (clique aqui 🖱️)")
expander_eng.write("(1) Escolas engajadas e personalizadas, fazem uso de ferramentas como marcar/interagir com aluno para corrigir seus trabalhos (correções com interações com alunos). (2) Escolas engajadas e personalizadas interagemm e dão feedbacks constantes para seus alunos, então a conversa com alunos através de forums deve ser uma forma boa de feedback para os estudos dos alunos. (3) Baixar resultados significa que a escola não faz um bom uso de nossas ferramentas de relátorios. (4) Alunos interagindo e curtindo contéudos são um bom sinal de engajamento com a escola. (5) Alunos subindo vídeos e áudios são um bom sinal de engajamento e personalização do ensino.")


"""
### 🛠️ Próximos Passos
(1) - Receber feedback sobre nossos dados utilizados e ver se temos algo a acrescentar
"""
"""
(2) - Olhar mais a fundo as métricas de tarefas e questões discursivas pois elas podem enganar,
exemplo: Guilherme de almeida
"""
"""
(3) - Melhorar visualização na parte das tabelas das Métricas.
"""
"""
(4) - Melhorar fluxo de informações do relátorio.
"""
"""
(5) - Estatística e Machine Learning para avaliar as correlações entre as váriaveis.
"""