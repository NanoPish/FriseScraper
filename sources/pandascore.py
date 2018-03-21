import requests
import json

import datetime
import dateutil.parser
from collections import namedtuple
from historical_event import historical_event

class pandascore_dota_api:
    url_endpoint = 'https://api.pandascore.co/videogames/4/tournaments/'
    url_team = 'https://api.pandascore.co/teams'
    source_name = 'panda_score'
    api_result = []

    def __init__(self):
        self.query_result = None

    def make_query(self):
        query_dict = {
            'token':'JBsdKIMFwx962sNhH_tqrAzRDKn_AK82_UXbYKYeDP2v9lMRXXE'
        }
        self.query_result = requests.get(pandascore_dota_api.url_endpoint, params=query_dict)
        tournaments = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        for tournament in tournaments:
            if tournament.winner_id != None:
                self.url_team = 'https://api.pandascore.co/teams/' + str(tournament.winner_id)
                self.query_result = requests.get(self.url_team, params=query_dict)
                team = json.loads(self.query_result.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
                # print("TOURNAMENT : " + tournament.slug + " " + tournament.name  + " WIN BY : " + team.name + " AT " + tournament.begin_at)
                self.api_result.append(historical_event(description="TOURNAMENT " + tournament.slug + " " + tournament.name + " WIN BY " + tournament.name, date=dateutil.parser.parse(tournament.begin_at).date(), source=self.source_name, name="DOTA 2"))
        
    def get_event_list(self):
        return(self.api_result)
            
