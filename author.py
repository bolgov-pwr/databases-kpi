class Author(object):
    global id 
    def __init__(self, aid, aname, country):
        self.aid = aid
        self.aname = aname
        self.country = country
    def __str__(self):
        return "Id=%d, Name=%s, Country=%s"%(self.aid, self.aname, self.country)
