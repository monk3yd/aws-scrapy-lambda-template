# AWS Lambda Basic Template (invoke)

import os
# import json
# import requests

from loguru import logger
from spider_manager import SpiderManager
from ip import IPSpider

# Cross Origin Resource Share (CORS) headers
CORS = {
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
    "Content-Type": "application/json"
}

def lambda_handler(event=dict(), context=dict()):
    key = os.getenv("KEY")
    logger.debug(f"Key: {key}")

    logger.debug(f"Event: {event}")

    handler = SpiderManager()
    handler.run_spider(IPSpider, event)

    # 200OK lambda response
    # TODO: return spider job id
    return {
        "statusCode": 200,
        "headers": CORS,
        "message": "init spider"
    }

# --- Local ---
if __name__ == "__main__":
    payload = {
        "name": "monk3yd"
    }
    lambda_response = lambda_handler(event=payload)
    print(f"Lambda response {type(lambda_response)}: {lambda_response}")
