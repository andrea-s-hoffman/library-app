from library import gc_library


def print_books(book_list):
    list_num = 0
    for book in book_list:
        list_num = list_num + 1
        print(str(list_num) + ". '" + book.title + "', by: " + book.author + " (" + book.status +
              " and due by: " + str(book.due_date) + ") " + "——— condition: " + str(book.condition) + "/10")


def checkout_this_book(book_list):
    valid_choice = False
    while not valid_choice:
        print_books(book_list)
        choice = int(input("Which book would you look to checkout? > "))
        if 0 < choice <= len(book_list):
            chosen_book = book_list[choice - 1]
            if chosen_book.status == "Checked Out":
                print("This book is not available")
            else:
                chosen_book.checkout_book()
                print("You have checked out " + chosen_book.title + " and it is due in 2 weeks on: " +
                      str(chosen_book.due_date))
                library_menu()
                break
        else:
            print("Please choose a valid number from the list!")


def return_this_book(book_list):
    valid_choice = False
    while not valid_choice:
        print_books(book_list)
        choice = int(input("Which book would you look to return? > "))
        if 0 < choice <= len(book_list):
            chosen_book = book_list[choice - 1]
            if chosen_book.status == "On Shelf":
                print("This book is already in the library")
            else:
                chosen_book.return_book()
                print("You have returned " + chosen_book.title + ". Thank you!" +
                      str(chosen_book.due_date))
                library_menu()
                break
        else:
            print("Please choose a valid number from the list!")


def search_books_by(param):
    if param == 1:
        search_word = input("Please provide an author: ")
        filtered = [book for book in gc_library if search_word.lower() in book.author.lower()]
    else:
        search_word = input("Please provide a title keyword: ")
        filtered = [book for book in gc_library if search_word.lower() in book.title.lower()]

    if len(filtered) > 0:
        book_num = 1
        for book in filtered:
            print(str(book_num) + ". " + book.title)
            book_num = book_num + 1
        print("Would you like to check out a book?")
        valid_resp = False
        while not valid_resp:
            print("""
                1. Yes, please!
                2. Nah, man
                """)
            inp = int(input("> "))
            if inp == 1:
                checkout_this_book(filtered)
            elif inp == 2:
                print("Ok!")
                break
                library_menu()
    else:
        while True:
            print("""There were no books matching that author. Please choose an option...
                1. Search by author
                2. Search by title
                3. Go back
                4. Exit library
                """)
            res = int(input("Provide a number: "))
            if res == 1:
                break
                search_books_by(1)
            elif res == 2:
                break
                search_books_by(2)
            elif res == 3:
                break
                library_menu()
            elif res == 4:
                print("Thanks and have a beautiful day!")
                break
            else:
                print("Please provide a valid number from the list...")


def library_menu():
    print("-----------------------------------------")
    while True:
        while True:
            print("""Welcome to the GC community library! Please select an option:
                  1. View all books
                  2. Search for a book
                  3. Return a book
                  4. Exit library
                  """)
            response = int(input("Please provide a number: "))
            if response == 1:
                print_books(gc_library)
                valid_next_opt = False
                while not valid_next_opt:
                    res = int(input("""Would you like to...
                1. Check out a book
                2. Return a book
                3. (Go back)
                """))
                    if res == 1:
                        checkout_this_book(gc_library)
                        break
                        library_menu()
                    elif res == 2:
                        return_this_book(gc_library)
                        break
                        library_menu()
                    elif res == 3:
                        break
                        library_menu()
                    else:
                        print("please provide a valid number from the list!")
            elif response == 2:
                valid_next_opt = False
                while not valid_next_opt:
                    res = int(input("""Search by...
                 1. Author
                 2. Title
                 3. (Go back)
                 """))
                    if res == 1 or res == 2:
                        search_books_by(res)
                        break
                        library_menu()
                    elif res == 3:
                        break
                        library_menu()
                    else:
                        print("please provide a valid number from the list!")
            elif response == 3:
                return_this_book(gc_library)
                break
                library_menu()
            elif response == 4:
                print("Thank you and have a nice day!")
                break
            else:
                print("please provide a valid number from the list!")


library_menu()