from wikipedia import vizgr_api_wrapper
from historical_event import historical_event
from mysql_database import mysql_database

if __name__ == '__main__':
    #example querying all events between 1990 and 1992 from wikipedia using vizgr api
    wikipedia = vizgr_api_wrapper()
    wikipedia.make_query(begin_date='19900000', end_date='19900200')
    wikipedia_events = wikipedia.get_event_list()
    database = mysql_database()
    for event in wikipedia_events:
        print('Trying to insert event: \n', event, '\n')
        insert_event_query = ("INSERT INTO events "
                              "(date, description, source) "
                              "VALUES (%s, %s, %s)")
        database.query(insert_event_query, (event.date, event.description, event.source))
    database.commit()
