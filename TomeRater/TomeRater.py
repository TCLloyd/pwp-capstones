class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
    def get_email(self):
        return self.email
    def change_email(self, address):
        self.email = address
        print("Email has been changed to {}".format(address))
    def __repr__(self):
        return "User: {name}, Email:{email}, Books read: {b}".format(name = self.name, email = self.email, b = len(self.books.keys()))
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
    def read_book(self, book, rating = None):
        self.books[book] = rating
    def get_average_rating(self):
        total = 0
        for value in self.books.values():
            if value != None:
                total += value
        return (total / len(self.books.values()))


class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    def get_title(self):
        return self.title
    def get_isbn(self):
        return self.isbn
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
    def add_rating(self, rating):
        if rating != None:
            if rating < 0 or rating > 4:
                print("Invalid Rating")
            else:
                self.ratings.append(rating)
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        return (total / len(self.ratings))
    def __hash__(self):
        return hash((self.title, self.isbn))
    def __repr__(self):
        return "{title}".format(title = self.title)





class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    def get_author(self):
        return self.author
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)



class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    def get_subject(self):
        return self.subject
    def get_level(self):
        return self.level
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)



class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
        self.isbns = []
    def __repr__(self):
        return "TomeRater has {users} users rating {books} books and counting!".format(users = len(self.users.keys()), books = len(self.books.keys()))
    def __eq__(self, other_tr):
        if self.users == other_tr.users and self.books == other_tr.books:
            return True
        else:
            return False
    def create_book(self, title, isbn):
        if isbn in self.isbns:
            print("A book with that ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return Book(title, isbn)
    def create_novel(self, title, author, isbn):
        if isbn in self.isbns:
            print("A book with that ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return Fiction(title, author, isbn)
    def create_non_fiction(self, title, subject, level, isbn):
        if isbn in self.isbns:
            print("A book with that ISBN already exists!")
        else:
            self.isbns.append(isbn)
            return Non_Fiction(title, subject, level, isbn)
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}".format(email = self.email))
    def add_user(self, name, email, user_books = None):
        if "@" in email and (".com" or ".edu" or ".org" in email):
            if email in self.users.keys():
                print("A user with that email already exists!")
            else:
                self.users[email] = User(name, email)
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
        else:
            print("Not a valid email address!")
    def print_catalog(self):
        for key in self.books.keys():
            print(key)
    def print_users(self):
        for value in self.users.values():
            print(value)
    def get_most_read_book(self):
        highest = -1
        highest_book = None
        for key, value in self.books.items():
            if value > highest:
                highest = value
                highest_book = key
        return highest_book

    def highest_rated_book(self):
        highest = -1
        highest_book = None
        for book in self.books.keys():
            if book.get_average_rating() > highest:
                highest = book.get_average_rating()
                highest_book = book
        return highest_book
    def most_positive_user(self):
        highest = -1
        highest_user = None
        for user in self.users.values():
            if user.get_average_rating() > highest:
                highest = user.get_average_rating()
                highest_user = user
        return highest_user
