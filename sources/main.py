from historical_event import historical_event
from mysql_database import mysql_database

from league_of_legends import league_of_legends
from french_historical import french_historical
from wikipedia import vizgr_api_wrapper
from pandascore import pandascore_dota_api

import logging

def insert_events(events):
    logging.info('Inserting events in database...')
    database = mysql_database()
    for event in events:
        if (event.description != None and
            event.source != None and
            event.date != None):
            insert_event_query = ('INSERT INTO events '
                             '(name, description, url, source, date) '
                             'VALUES (%s, %s, %s, %s, %s)')
            database.query(insert_event_query, (event.name, event.description, event.url, event.source, event.date))
        else:
            logging.warn("Missing required event property, can't insert event in database: " + event.__str__())
    database.cnx.commit()
    
if __name__ == '__main__':
    logging.basicConfig(filename='LaFrise.log', level=logging.INFO)
    logging.info('Started FriseScraper')
    
    #french_historical = french_historical()
    #french_historical.harvest()

    #league_of_legends = league_of_legends()
    #league_of_legends.harvest()
    
    wikipedia = vizgr_api_wrapper()
    wikipedia.harvest()

    pandascore_dota_api = pandascore_dota_api()
    pandascore_dota_api.harvest()

    # save all events in DB
    #insert_events(french_historical.event_list)
    #insert_events(league_of_legends.event_list)
    insert_events(wikipedia.event_list)
    insert_events(pandascore_dota_api.event_list)
    
    logging.info('Exiting FriseScraper')
