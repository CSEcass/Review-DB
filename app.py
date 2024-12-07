from tinydb import TinyDB, Query

db = TinyDB('db.json')
books = Query()
# Insert Function
# books = {
#     'title': 'A Good Girls Guide to Murder',
#     'author': 'Holly Jackson',
#     'genre(s)': ['Mystery', 'Young Adult Literature'],
#     'rating': 5,
# }
# db.insert(books)

# NOTE You can add multiple things just by putting them into lists []!

#Search Function
# my_book = db.search(books.date < 2000)
# my_book2 = db.insert(books.rating < 5 & books.rating > 4)
# print(my_book)
# print(my_book2)

#All Function
# all_books = db.all()
# print(all_books)

#CHALLENGE return & print all authors/genre(s)
all_books = db.all()
for book in all_books:
    print(book['author'])

for book in all_books:
    #As a list
    print(book['genre(s)'])
    for genre in book['genre(s)']:
        #Each seperate list item
        print(genre)

# NOTE https://www.tutorialspoint.com/tinydb/tinydb_update_data.htm is TinyDB's Website