# Analisando os Dados Sobre Cancelamento de Clientes

## Descrição

Este projeto visa analisar uma base de dados de clientes inativos, ou seja, que já cancelaram o serviço. O objetivo é entender os principais motivos desses cancelamentos e identificar as ações mais eficientes para reduzir esse número.

## Estrutura do Projeto

1. **Leitura e Pré-processamento dos Dados**
    - Importação do arquivo CSV contendo os dados dos cancelamentos.
    - Remoção da coluna `CustomerID` que não será necessária para a análise.
    - Identificação e remoção de valores vazios.

2. **Análise Exploratória dos Dados**
    - Contagem de clientes que cancelaram e não cancelaram.
    - Análise da distribuição da duração dos contratos.
    - Agrupamento dos dados por duração do contrato e cálculo das médias.

3. **Identificação de Problemas**
    - Verificação da alta taxa de cancelamento entre contratos mensais.
    - Filtragem dos dados para remover contratos mensais.
    - Análise adicional para identificar outras causas de cancelamento.

4. **Visualização dos Dados**
    - Criação de gráficos para melhor visualização dos dados utilizando Plotly Express.
    - Identificação de padrões de cancelamento relacionados a atrasos e interações com o call center.

5. **Conclusões e Recomendações**
    - Identificação das três principais causas de cancelamento: forma de contrato mensal, necessidade de ligações no call center, e atraso no pagamento.
    - Sugestões de ações para reduzir a taxa de cancelamento.
