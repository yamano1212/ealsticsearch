from elasticsearch import Elasticsearch,RequestsHttpConnection

def setting_es():
	settings = """
	{
		"settings": {
			"analysis": {
				"analyzer": {
					"kuromoji_analyzer": {
						"type":"custom",
						"tokenizer": "kuromoji_tokenizer"
					}
				}
			}
		},
		"mappings":{
			"/asdfasdf": {
				"properties": {
					"adsfadsf": {
						"type": "string",
						"analyzer": "kuromoji_analyzer"
					}
				}
			}
		}
	}
	"""
	return settings

def get_indexes(es):
	indices = [i for i in es.indices.get_alias()]
	return indices

def make_index(es,index_name,alias_name):
	_body = setting_es()
	try:
		es.indices.create(index=index_namme,body=_body)
		es.indices.put_alias(index=index_name,name=alias_name)
		return True
	except Exception as e:
		print(e)
		return False


