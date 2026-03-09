# Projeto Automação de Calculo e Envio de Indicadores

### Objetivo: Criar um Programa que envolva a automatização de um processo feito no computador, utilizando as bibliotecas Pandas, Pathlib e win32com.client.

### Descrição:

O programa visa automatizar a análise de dados de vendas de uma rede de lojas de roupa com 25 lojas espalhadas por todo o Brasil, calcular os chamados One Pages de cada loja (principais indicadores em 1 página, permitindo verificar o desempenho em relação às metas estabelecidades) e enviar para o gerente de cada loja o OnePage da sua loja.

### Arquivos e Informações Importantes

- Arquivo Emails.xlsx com o nome, a loja e o e-mail de cada gerente. 

- Arquivo Vendas.xlsx com as vendas de todas as lojas. 

- Arquivo Lojas.csv com o nome de cada Loja.

- As planilhas de cada loja, criadas pelo programa. são salvas dentro da pasta da loja com a data da planilha, a fim de criar um histórico de backup

Ao final, o programa deve enviar ainda um e-mail para a diretoria com 2 rankings das lojas em anexo, 1 ranking do dia e outro ranking anual. Além disso, no corpo do e-mail, deve ressaltar qual foi a melhor e a pior loja do dia e também a melhor e pior loja do ano. O ranking de uma loja é dado pelo faturamento da loja.

### Indicadores do OnePage

- Faturamento -> Meta Ano: 1.650.000 / Meta Dia: 10
- Diversidade de Produtos (quantos produtos diferentes foram vendidos naquele período) -> Meta Ano: 120 / Meta Dia: 4
- Ticket Médio por Venda -> Meta Ano: 500 / Meta Dia: 500