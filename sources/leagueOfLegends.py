import requests
import json
from xml.etree import ElementTree
from collections import namedtuple

from historical_event import historical_event
from mysql_database import mysql_database

class league_of_legends:
    url_endpoint = 'https://api.pandascore.co/videogames/1/tournaments'

    def __init__(self):
        self.query_result = None

    def make_query(self):
        query_dict = {'token' : 'lvyy4BTBrK_e3Xt2WLxi-KpFYq448BwPrRyweHHm2cYg_BDYqGE'}
        self.query_result = requests.get(league_of_legends.url_endpoint, params=query_dict)
        #for event in events:
        #   print(event.name)
        #   print(event.slug)
        #   print(event.begin_at)
        #   print(event.end_at)
        #   print(event.serie)
        #   print('----------')

    def get_event_list(self):
        event_list = []
        events = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('x', d.keys())(*d.values()))
        for event in events:
            current_event = historical_event(event.begin_at, None, 'https://pandascore.co/', event.name, None)
            event_list.append(current_event)
        return (event_list)
