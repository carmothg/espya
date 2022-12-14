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
        "fabricantes": {
            "terms": {
                "field": "vacina_fabricante_nome"
            }
	    }
    }
    res=elastic_client.search(query=query,aggs=aggs,size=0)
    registros=res["aggregations"]["fabricantes"]["buckets"]
    doses={}
    for registro in registros:
        doses[registro["key"]]=registro["doc_count"]
    
    resjson={
        "Contexto":"Total de doses de vacina contra covid-19 aplicadas no municipio de Santarém agrupadas de acordo com a fabricante de cada uma",
        "dados":doses
    }
    
    return {
        'statusCode': 200,
        'headers': {"content-type": "application/json"},
        'body': json.dumps(resjson,ensure_ascii=False)
    }
