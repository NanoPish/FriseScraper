from wikipedia import query_wrapper

if __name__ == '__main__':
    #example querying all events between 1990 and 1992 from wikipedia using vizgr api
    wikipedia = query_wrapper()
    wikipedia.make_query('19900000', '19900200')
    wikipedia.print_query_result()
    
