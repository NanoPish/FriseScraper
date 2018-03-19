from wikipedia import vizgr_api_wrapper
from historical_event import historical_event
from mysql_database import mysql_database

from leagueOfLegends import league_of_legends
from french_historical import french_historical

def insert_events(events):
    database = mysql_database()
    for event in events:
       print('Trying to insert event: \n', event, '\n')
       insert_event_query = ('INSERT INTO events '
                             '(name, description, url, source, date) '
                             'VALUES (%s, %s, %s, %s, %s)')
       database.query(insert_event_query, (event.name, event.description, event.url, event.source, event.date))
    database.cnx.commit()
    
if __name__ == '__main__':
    french_historical = french_historical()
    french_historical_links = french_historical.get_event_links()
    events_french_historical = french_historical.get_event_list(french_historical.scrap(french_historical_links))

    leagueOfLegends = league_of_legends()
    leagueOfLegends.make_query()
    events_league = leagueOfLegends.get_event_list()


    #example querying all events between 1990 and 1992 from wikipedia using vizgr api
    wikipedia = vizgr_api_wrapper()
    wikipedia.make_query(begin_date='19900000', end_date='19900200')
    wikipedia_events = wikipedia.get_event_list()
    insert_events(wikipedia_events)

