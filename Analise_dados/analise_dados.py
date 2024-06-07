import pandas as pd
import plotly.express as px

tabela = pd.read_csv("cancelamentos.csv")
tabela = tabela.drop("CustomerID", axis=1)
display(tabela)

# Identificando e removendo valores vazios
display(tabela.info())
tabela = tabela.dropna()
display(tabela.info())

# Quantas pessoas cancelaram ou não cancelaram
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

display(tabela["duracao_contrato"].value_counts(normalize=True))
display(tabela["duracao_contrato"].value_counts())

# Analisando o contrato mensal
display(tabela.groupby("duracao_contrato").mean(numeric_only=True))
# Descobri-se aqui que a média de cancelamentos é 1, ou seja, praticamente todos os contratos mensais cancelaram.

# Percebe-se que contrato mensal é ruim, melhor tirar ele e continuar analisando
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# Chega-se agora em menos da metade de pessoas cancelando, mas ainda tem muitos cancelamentos.
display(tabela["assinatura"].value_counts(normalize=True))
display(tabela.groupby("assinatura").mean(numeric_only=True))

# Os cancelamentos são na média parecidos, então fica difícil tirar alguma conclusão da média, é preciso ir mais a fundo.

# Criação de gráficos para melhorar a vizualização
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()

# Com os gráficos é possível descobrir muita coisa:
# Atraso acima de 20 dias, 100% cancelamento
# Ligações no call center e espera acima de 5 minutos, muitos calncelamentos.

tabela = tabela[tabela["ligacoes_callcenter"]<5]
tabela = tabela[tabela["dias_atraso"]<=20]
display(tabela)
display(tabela["cancelou"].value_counts())
display(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))

# As três principais causas de cancelamento: 
# - Forma de contrato mensal
# - Necessidade de ligações no call center
# - Atraso no pagamento
# Resolvendo esses problemas o cancelamento cai para 18%.
