from author import Author
from authors import Authors
from book import Book
from books import Books

def menu():
    print ("1 - Show the tables")
    print ("2 - Add  to [Authors]")
    print ("3 - Add to [Books]")
    print ("4 - Remove from [Authors]")
    print ("5 - Remove from [Books]")
    print ("6 - Edit [Authors]")
    print ("7 - Edit [Books]")
    print ("8 - Search")
    print ("0 - Exit")
    return int(input())


