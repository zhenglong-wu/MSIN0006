import os
from dotenv import load_dotenv
load_dotenv()
import requests


pushshift_url = os.getenv('url')


def query_reddit(keyword: str, size: str, before, after):

    url = f'{pushshift_url}?q={keyword}&size={size}&before={before}&after={after}'

    try:
        return requests.get(url=url)
    except:
        return 'error'


print(query_reddit(keyword='potter', 
                   size='10', 
                   before='30d', 
                   after='40d'))