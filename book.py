class Book(object):
    def __init__(self, aid, bid, bname, authors, bpages):
        if not authors.exists(aid):
            raise Exception("Author's ID isn't found")
        self.aid = aid
        self.bid = bid
        self.bname = bname
        self.bpages = bpages
    def __str__(self):
        return "Author's ID=%d, Book ID=%d, Title=%s, Pages=%d "%(self.aid, self.bid, self.bname, self.bpages)
