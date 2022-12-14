import json
from elasticsearch import Elasticsearch
def lambda_handler(event, context):
    elastic_host="https://imunizacao-es.saude.gov.br:443"
    elastic_user='imunizacao_public'
    elastic_password='qlto5t&7r_@+#Tlstigi'
    elastic_client = Elasticsearch(elastic_host,basic_auth=(elastic_user,elastic_password))

    query={
        "bool": {
            "filter": {
                "term":{"estabelecimento_municipio_codigo":"150680"}
                }
                }
    }
    aggs={
            "doses":{
                "terms":{
                    "field": "vacina_descricao_dose"
                }
            }
        }

    res=elastic_client.search(query=query,aggs=aggs,size=0)
    registros=res["aggregations"]["doses"]["buckets"]
    doses={}
    for registro in registros:
        doses[registro["key"]]=registro["doc_count"]
    
    resjson={
        "Contexto":"Quantidades de doses de vacinas aplicadas no municipio de Santarém (PA) de acordo com o tipo de dose",
        "dados": doses
    }
    
    response = {
        'statusCode': 200,
        'headers': {"content-type": "application/json"},
        'body': json.dumps(resjson,ensure_ascii=False)
    }
    
    return response
