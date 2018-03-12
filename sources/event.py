class event:
    def __init__(self, name, date, description, url, source):
        self.name = name
        self.date = date
        self.description = description
        self.url = url
        self.source = source

    def __str__(self):
        return(self.name, self.date, self.description, self.url, self.source)
