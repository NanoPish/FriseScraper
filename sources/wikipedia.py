import requests
from xml.etree import ElementTree

class query_wrapper:
    url_endpoint = "http://www.vizgr.org/historical-events/search.php"
    def __init__(self):
        self.query_result = None

        
    def make_query(self, begin_date, end_date, lang='en', keyword=None, format='xml', html_link='false', links='true', limit=None, order='asc', category=None, granularity='year', related='false'):
        query_dict = {
            'begin_date':begin_date,
            'end_date':end_date,
            'format':format,
            'html_link':html_link,
            'links':links,
            'order':order,
            'related':related
        }
        if keyword is not None:
            query_dict['keyword'] = keyword
        if limit is not None:
            query_dict['limit'] = limit
        if category is not None:
            query_dict['category'] = category
        self.query_result = requests.get(query_wrapper.url_endpoint, params=query_dict)

        
    def print_query_result(self):
        tree = ElementTree.fromstring(self.query_result.content)
        for event in tree.findall('event'):
            for link in event.findall('link'):
                print(link.find('text_in_event').text)
                print(link.find('url').text)
            print(event.find('date').text + " " + event.find('description').text)
            print('------')
