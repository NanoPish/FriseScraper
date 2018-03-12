from wikipedia import vizgr_api_wrapper
from historical_event import historical_event

if __name__ == '__main__':
    #example querying all events between 1990 and 1992 from wikipedia using vizgr api
    wikipedia = vizgr_api_wrapper()
    wikipedia.make_query('19900000', '19900200')
    wikipedia_events = wikipedia.get_event_list()
    for event in wikipedia_events:
        print(event)
    
