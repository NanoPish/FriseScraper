class historical_event:
    def __init__(self, date, description, source, name=None, url=None):
        self.date = date
        self.description = description
        self.source = source
        self.name = name
        self.url = url

    def __str__(self):
        items = [self.name, self.date, self.description, self.url, self.source]
        return ', '.join(str(item) for item in items)
