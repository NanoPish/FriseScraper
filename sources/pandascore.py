import requests
import json

import datetime
import logging
import dateutil.parser
from collections import namedtuple
from harvester import harvester
from historical_event import historical_event

class pandascore_dota_api(harvester):
    url_endpoint = 'https://api.pandascore.co/videogames/4/tournaments/'
    url_team = 'https://api.pandascore.co/teams'
    source_name = 'panda_score'

    def __init__(self):
        self.query_result = None
        self.event_list = []

    def harvest(self):
        logging.info("Going to make panda_score api call...")
        query_dict = {
            'token':'JBsdKIMFwx962sNhH_tqrAzRDKn_AK82_UXbYKYeDP2v9lMRXXE'
        }
        self.query_result = requests.get(pandascore_dota_api.url_endpoint, params=query_dict)
        tournaments = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        logging.info("Going to make panda_score event_list")
        for tournament in tournaments:
            if tournament.winner_id != None:
                self.url_team = 'https://api.pandascore.co/teams/' + str(tournament.winner_id)
                self.query_result = requests.get(self.url_team, params=query_dict)
                team = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
                # print("TOURNAMENT : " + tournament.slug + " " + tournament.name  + " WIN BY : " + team.name + " AT " + tournament.begin_at)
                self.event_list.append(historical_event(description="TOURNAMENT " + tournament.slug + " " + tournament.name + " WIN BY " + tournament.name, date=dateutil.parser.parse(tournament.begin_at).date(), source=self.source_name, name="DOTA 2"))
