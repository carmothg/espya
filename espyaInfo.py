import json

def lambda_handler(event, context):
    
    resjson={
        "Nome":"API Espya",
        "Desenvolvedor":"Thiago Carmo",
        "E-mail":"carmothg@gmail.com",
        "Descrição":"Aplicação produzida como objeto de artigo acadêmico de conclusão do curso de Sistemas de informação na Ulbra Santarém",
        "Contexto":"Dados utilizados disponinilizados sobre a vacinação contra covid-19 levando em consideração dosese aplicadas nos estabeleciomentos de saúde na cidade de Santarém no estado do Pará"
    }
    return {
        'statusCode': 200,
        'headers':{
            'content-type':'application/json'
        },
        'body': json.dumps(resjson)
    }
