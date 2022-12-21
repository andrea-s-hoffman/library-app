from datetime import date
import pandas as pd


class Book:

    def __init__(self, title, author, status, condition, due_date="N/A"):
        self.title = title
        self.author = author
        self.status = status
        self.condition = condition
        self.due_date = due_date

    def checkout_book(self):
        self.status = "Checked Out"
        self.condition = self.condition - 1
        today = date.today()
        print(today)
        due = pd.to_datetime(today)+pd.DateOffset(weeks=2)
        self.due_date = due

    def return_book(self):
        self.status = "On Shelf"
        self.due_date = "N/A"
        if self.condition < 1:
            print("Due to the poor condition of " + self.title + ", this book is being recycled.")
            del self

# My_book = Book("it's me", "andrea", "On Shelf", 7)
# print(My_book.title, My_book.author, My_book.status, My_book.condition, My_book.due_date)
# My_book.checkout_book()
# print(My_book.title, My_book.author, My_book.status, My_book.condition, My_book.due_date)