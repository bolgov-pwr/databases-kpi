class Books(object):
    def __init__(self):
        self.books=[]
    
    def add(self, book):
        self.books.append(book)
    
    def __str__(self):
        return '\n'.join(str(book) for book in self.books)
    
    def exists(self, aid):
        for book in self.books:
            if book.aid == aid:
                return True
        return False
    def delete(self, bid):
        index = -1
        for i, book in enumerate(self.books):
            if book.bid == bid:
                index = i
        if (index > -1):
            return self.books.pop(index)
