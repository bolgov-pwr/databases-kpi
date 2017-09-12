from author import Author
from authors import Authors
from book import Book
from books import Books
import ui
import pickle

def Start():
    authors = Authors()
    books = Books()
    
    try :
        with open('authors.pickle', 'rb') as f:
            authors = pickle.load(f)
        with open('books.pickle', 'rb') as f:
            books = pickle.load(f)
    except EOFError as e:
            pass
    aid = len(authors.authors)
    bid = len(books.books)
    try:
        while(True):
            check = ui.menu()
            if (check == 1):
                print("\nAll Authors:")
                print(authors)
                print("\nAll Books:")
                print(books)
            
            elif (check == 2):
                aname = raw_input("Author name: ")
                acountry = raw_input("Country: ")
                authors.add(Author(aid, aname, acountry))
                aid += 1
            elif (check == 3):
                aname = raw_input("Author name: ")
                acountry = raw_input("Country: ")
                bname = raw_input("Book name: ")
                pages = int(raw_input("Pages : "))
                c = authors.add(Author(aid, aname, acountry))
                if c > -1:
                    books.add(Book(c, bid, bname, authors,  pages))
                else:
                    books.add(Book(aid, bid, bname, authors,  pages))
                aid += 1
                bid += 1
            elif (check == 4):
                id = int(raw_input("Author's ID for Delete: "))
                authors.delete(id, books)
            elif (check == 5):
                id = int(raw_input("Book's ID for Delete"))
                books.delete(id)
            elif (check == 6):
                id = int(raw_input("Author's ID for Edit"))
                if authors.exists(id):
                    aname = raw_input("Author name: ")
                    authors.authors[id].aname = aname
                    authors.authors[id].country = raw_input("Country: ")
                
                else:
                    print("No Authors fond")

            elif (check == 7):
                id = int(raw_input("Book's ID for Edit"))
                if books.exists(id):
                    bname = raw_input("Book's name: ")
                    pages = int(raw_input("Pages: "))
                    books.books[id].bname = bname
                    authors.authors[id].bpages = pages
                else:
                    print("No Authors fond")
            elif (check == 8):
                authors.search(books)
            elif (check == 0):
                exit()
                    
    except Exception as e:
        print(e)
    finally:
        with open('authors.pickle', 'wb') as f:
            pickle.dump(authors, f)
        with open('books.pickle', 'wb') as f:
            pickle.dump(books, f)

Start()
