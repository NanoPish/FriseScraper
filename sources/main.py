from wikipedia import vizgr_api_wrapper
from historical_event import historical_event
from mysql_database import mysql_database

from leagueOfLegends import league_of_legends
from french_historical import french_historical
from olympic_games import olympic_games

if __name__ == '__main__':
    
    french_historical = french_historical()
    french_historical_links = french_historical.get_event_links()
    events_french_historical = french_historical.get_event_list(french_historical.scrap(french_historical_links))
    #french_historical.add_to_db(events_french_historical)

    leagueOfLegends = league_of_legends()
    leagueOfLegends.make_query()
    events_league = leagueOfLegends.get_event_list()
    #leagueOfLegends.add_to_db(events_league)


    #example querying all events between 1990 and 1992 from wikipedia using vizgr api
    #wikipedia = vizgr_api_wrapper()
    #wikipedia.make_query(begin_date='19900000', end_date='19900200')
    #wikipedia_events = wikipedia.get_event_list()    


    #database = mysql_database()
    #for event in wikipedia_events:
    #    print('Trying to insert event: \n', event, '\n')
    #    insert_event_query = ('INSERT INTO events '
    #                          '(date, description, source) '
    #                          'VALUES (%s, %s, %s)')
    #   database.query(insert_event_query, (event.date, event.description, event.source))
    #    print(len(event.description))
    #database.cnx.commit()
