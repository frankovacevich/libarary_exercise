
## Number of days a book is lent to a user.
LENDING_PERIOD = 7;

"""
Basic rules for lending:
 - A user can only borrow 1 book at a time
 - If the user does not return a book in the given period, he gets a sanction and cannot
   borrow any book for the next seven days.
"""

def lend_book(book_code, user_DNI):
	"""
	This function lends a book to a user

	Perform the necessary operations on the database and print a message containing the information
	of the operation, something like:

		Book lending
		==============================
		BOOK: book name
		USER: user name, user DNI
		LIMIT DATE: limit date
		CURRENT DATE: current date
		OPEARTION CODE: operation code

	Generate an "operation code" for each lending operation (in case the user has a
	complaint or something). The operation code must be an 32bit int
	
	If the book is already lent or the user already has a book print an error message
	"""

	return

def find_available_books(book_name):
	"""
	Print a list of books [BookName, BookCode] that are available for lending

	This is useful for the staff when someone comes asking for a book by its name
	This function lets the staff know if a book with that name (or similar) is available
	It also lets the staff know the book code before calling the function lend_book
	"""

	return

def return_book(user_DNI):
	"""
	This function shall be called when the user returns a book

	If the user has not exceeded the lending period, then everything is OK
	Else, the user has to be sanctioned (i.e. he cannot borrow books for seven days)

	Print the information of the operation, something like:

		Book returning
		==============================
		BOOK: book name
		USER: user name, user DNI
		LIMIT DATE: limit date
		CURRENT DATE: current date
		OPEARTION CODE: operation code

	The "operation code" has to be the same code that was given during the lending
	opeartion.

	"""
	return
