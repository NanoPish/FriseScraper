import requests
from xml.etree import ElementTree

from historical_event import historical_event
from harvester import harvester

class vizgr_api_wrapper(harvester):
    url_endpoint = 'http://www.vizgr.org/historical-events/search.php'
    source_name = 'wikipedia'
        
    def __init__(self):
        self.query_result = None
        self.event_list = []
        
    def harvest(self):
        query_dict = {
            'begin_date':'20100000',
            'end_date':'20200000',
            'format':'xml',
            'html_link':'false',
            'links':'true',
            'order':'asc',
            'related':'false'
        }
        self.query_result = requests.get(vizgr_api_wrapper.url_endpoint, params=query_dict)
        self.make_event_list()
        
    def make_event_list(self):
        self.event_list = []
        tree = ElementTree.fromstring(self.query_result.content)
        for event in tree.findall('event'):
            current_event = historical_event(description=event.find('description').text,
                                             date=event.find('date').text,
                                             source=self.source_name)
            self.event_list.append(current_event)
