import requests 
from xml.etree import ElementTree

import event from event

class vizgr_api_wrapper:
    url_endpoint = "http://www.vizgr.org/historical-events/search.php"
    def __init__(self):
        self.query_result = None

        
    def make_query(self, begin_date, end_date, lang='en', keyword=None, format='xml', html_link='false', links='true', limit=None, order='asc', category=None, granularity='year', related='false'):
        query_dict = {
            'begin_date':begin_date,
            'end_date':end_date,
            'format':format,
            'html_link':html_link,
            'links':links,
            'order':order,
            'related':related
        }
        if keyword is not None:
            query_dict['keyword'] = keyword
        if limit is not None:
            query_dict['limit'] = limit
        if category is not None:
            query_dict['category'] = category
        self.query_result = requests.get(vizgr_api_wrapper.url_endpoint, params=query_dict)

        
    def get_event_list(self):
        event_list = []
        tree = ElementTree.fromstring(self.query_result.content)
        for event in tree.findall('event'):
            event_list.append(event.find('description').text, event(event.find('date').text), None, None, self.source_name)
        return (event_list)
