import json
from elasticsearch import Elasticsearch
def lambda_handler(event, context):
    elastic_user='imunizacao_public'
    elastic_host="https://imunizacao-es.saude.gov.br:443"
    elastic_password='qlto5t&7r_@+#Tlstigi'
    elastic_client = Elasticsearch(elastic_host,basic_auth=(elastic_user,elastic_password))

    query={
        "bool": {
            "filter": {
                "term":{"estabelecimento_municipio_codigo":"150680"}
                }
            }
    }

    res=elastic_client.count(query=query)
    totalDoses=res['count']
    
    resJson={
        "Contexto":"Quantidade de total de doses de vacina contra covid-19 aplicadas no municipio de Santarém",
        "dados":{
            "Total": totalDoses
        }
        
    }
    
    return {
        'statusCode': 200,
        'headers': {"content-type": "application/json"},
        'body': json.dumps(resJson,ensure_ascii=False)
    }
