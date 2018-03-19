import requests
import json
from xml.etree import ElementTree
from collections import namedtuple

from historical_event import historical_event
from mysql_database import mysql_database
from harvester import harvester

class league_of_legends:
    url_endpoint = 'https://api.pandascore.co/videogames/1/tournaments'

    def __init__(self):
        self.source = 'pandaLOL'
    
    def __init__(self):
        self.query_result = None
        self.event_list = []
        
    def harvest(self):
        query_dict = {'token' : 'lvyy4BTBrK_e3Xt2WLxi-KpFYq448BwPrRyweHHm2cYg_BDYqGE'}
        self.query_result = requests.get(league_of_legends.url_endpoint, params=query_dict)

    def make_event_list(self):
        self.event_list = []
        events = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('x', d.keys())(*d.values()))
        for event in events:
            current_event = historical_event(event.begin_at, None, self.source, event.name, None)
            self.event_list.append(current_event)
