import requests
from xml.etree import ElementTree

from historical_event import historical_event
from harvester import harvester

import logging

class vizgr_api_wrapper(harvester):
    url_endpoint = 'http://www.vizgr.org/historical-events/search.php'
    source_name = 'wikipedia'
        
    def __init__(self):
        self.query_result = None
        self.event_list = []
        
    def harvest(self):
        query_dict = {
            'begin_date':'1000' + '10' + '10',
            'end_date':  '2020' + '01' + '01',
            'lang':'en',
            'format':'xml',
            'html':'false',
            'links':'false',
            'order':'asc',
            'related':'false'
        }
        logging.info('Making api call in wikipedia...')
        self.query_result = requests.get(vizgr_api_wrapper.url_endpoint, params=query_dict)
        self.make_event_list()
        
    def make_event_list(self):
        self.event_list = []
        logging.info('Parsing wikipedia results...')
        tree = ElementTree.fromstring(self.query_result.content)
        for event in tree.findall('event'):
            current_event = historical_event(description=event.find('description').text,
                                             date=event.find('date').text,
                                             source=self.source_name)
            if ('/' not in current_event.date):
                current_event.date = current_event.date + '/01/01'
            self.event_list.append(current_event)

        
