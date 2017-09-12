class Authors(object):
    def __init__(self):
        self.authors=[]
    
    def add(self, author):
        for i, p in enumerate(self.authors):
            if p.aname == author.aname:
                return i

        self.authors.append(author)
        return -1
                
    def __str__(self):
        return '\n'.join(str(author) for author in self.authors)
    
    def exists(self, aid):
        for author in self.authors:
            if author.aid == aid:
                return True
        return False
    
    def delete (self, aid, books):
        if books.exists(aid):
            print ("Cant delete")
            return
        index = -1
        for i, author in enumerate (self.authors):
            if author.aid == aid:
                index = i
        if index > -1:
            self.authors.pop(index)


    def search(self, books):
        for author in self.authors:
            for book in books.books:
                if (book.aid == author.aid and book.bpages > 100):
                    print(author)
                    print(book)
                    print("\n")


