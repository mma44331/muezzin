from fastapi import APIRouter
from elasticsearch_client import ElasticsearchClient
from shards.logger_menager import Logger
from config import MetadataConfig



logger = Logger.get_logger(name="SERVICE_E",index="muezzin_metadata_e")
route = APIRouter()
config = MetadataConfig()
elasticsearch = ElasticsearchClient(config.es,config.index_name,logger)



@route.get('/get_10_top')
def get_10_top():
    query = {
        "size": 10,
        "query": {
            "match_all": {}
        },
        "sort": [
            {
                "bds_percen": {
                    "order": "desc"
                }
            }
        ],
        "_source": ["id", "name", "bds_percen", "bds_threat_level", "text"]
    }
    try:
        response = elasticsearch.get_from_elastic(query)
        logger.info(f"found {len(response)} responses")
        return response
    except Exception as e:
        logger.error(f"Error retrieving data from Elasticsearch: {e}")

@route.get('/get_10_top/{free_text}')
def get_by_free_text(free_text):
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"text": free_text}},
                    {"term": {"is_bds": True}}
                ]
            }
        }
    }
    try:
        response = elasticsearch.get_from_elastic(query)
        logger.info(f"found {len(response)} responses")
        return response
    except Exception as e:
        logger.error(f"Error retrieving data from Elasticsearch: {e}")

@route.get('/search_by_threat_type')
def search_by_threat_type():
    query = {
        "size": 0,
        "aggs": {
            "threat_distribution": {
                "terms": {"field": "bds_threat_level.keyword"}
            }
        }
    }
    try:
        response = elasticsearch.get_from_elastic(query)
        logger.info("found responses")
        return response
    except Exception as e:
        logger.error(f"Error retrieving data from Elasticsearch: {e}")

@route.get('/search_by_time')
def search_by_time():
    query = {
        "query": {
            "term": {"is_bds": True}
        },
        "aggs": {
            "timeline": {
                "date_histogram": {
                    "field": "create_at.keyword",
                    "calendar_interval": "day"
                }
            }
        }
    }
    try:
        response = elasticsearch.get_from_elastic(query)
        logger.info(f"found {len(response)} responses")
        return response
    except Exception as e:
        logger.error(f"Error retrieving data from Elasticsearch: {e}")

@route.get('/big_podcasts')
def big_podcasts():
    query = {
        "query": {
            "bool": {
                "filter": [
                    {"term": {"is_bds": True}},
                    {"range": {"size_bytes": {"gt": 5000000}}}
                ]
            }
        }
    }
    try:
        response = elasticsearch.get_from_elastic(query)
        logger.info(f"found {len(response)} responses")
        return response
    except Exception as e:
        logger.error(f"Error retrieving data from Elasticsearch: {e}")

