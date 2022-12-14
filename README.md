# Espya
API Espya - Dados da vacinação contra covid-19 na cidade de Santarém

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/carmothg/espya/blob/main/LICENSE) 

# Sobre o projeto
A API Espya foi desenvolvida como instrumento de avaliação para trabalho de conclusão de curso na Univerdidade Luterana do Brasil - ULBRA. Desta forma todo o processo de desenvolvimento está descrito no artigo acadêmico disponivel [aqui](www.google.com.br). O objetivo do projeto é apresentar um modelo de consumos de dados do portal de dados aberto do governo através da linguagem Python e utilizando as querys do elasticsearch (mecanismo que está por trás da portal de dados). Os dados que serviram de base para o projeto são referentes a campanha de vacinação contra covid-19 no Brasil e os dados retornados na API Espya referem-se as doses aplicadas na cidade de Satarém no Pará. 


## Arquitetura do trabalho
A API foi desenvolvida utilizando serviços da AWS com o intuito de torna-la servless. Para isso utilizou-se os serviços API Gateway e AWS Lambda. Para a análise dos dados foi utilizado Linguaguem Python e as querysdsl do elasticsearch. 

## Estrutura da API
As funções funções lambdas utilizads na AWS estão disponiveis neste repositório e são invocadas através da URL descrita na seçao abaixo. 


# Tecnologias utilizadas
## API
- Lambda Functions
- API Gateway
- IAM
- Cognito
## Código
- Python
- Biblioteca elasticsearch
- Biblioteca json
- Google Collab
- Postman

# Como acessar a API
A Espya é uma API HTTP com metódos GET nas seguintes rotas:
- /info
- /VacinaPorDoses
- /TotalVacinas
- /VacinaPorFabricante

## URL

```bash
https://XXXXXXXXXXX.execute-api.sa-east-1.amazonaws.com/espya
```

## Basic Authentication

Usuário
```bash
vacinacao-espya
```
Senha
```bash
a1b2c3d4
```

# Autor

Thiago Pereira do Carmo

https://www.linkedin.com/in/carmothg

