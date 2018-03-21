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
            'begin_date':'0900' + '00' + '00',
            'end_date':  '0901' + '00' + '00',
            'lang':'en',
            'format':'xml',
            'html':'false',
            'links':'false',
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
            if ('/' not in current_event.date):
                current_event.date = current_event.date + '/00/00'
            self.event_list.append(current_event)

        
