import requests
from xml.etree import ElementTree

class pandascore_api:
    url_endpoint = '/teams'
    source_name = 'panda_score'

    def __init__(self):
        self.query_result = None

    def make_query(self):
        query_dict = {
            'access_token':'lvyy4BTBrK_e3Xt2WLxi-KpFYq448BwPrRyweHHm2cYg_BDYqGE'
        }
        
        self.query_result = requests.get(pandascore_api.url_endpoint, params=query_dict)
        print(self.query_result)

    def get_event_list(self):
        event_list = []
