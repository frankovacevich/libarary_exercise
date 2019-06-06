
BOOKS_BACKUP = "books.csv"
USERS_BACKUP = "users.csv"


## DATABASE CONNECTION
## this is a global variable to perform database querys
## it's loaded with the function mysql_connect()
CONN = None

##
## DATABASE FUNCTIONS
##

def mysql_connect():
	"""
	Connects to the database and saves the connection to CONN
	(Create the database before with the mysql console)
	"""
	return


##
## BOOK FUNCTIONS
##

def load_books_from_file(file):
	"""
	This function loads a file and inserts the contents in the database
	The file has to be in CSV format (see books.csv).
	
	If the database already contains a book with the same CODE, the book should not be inserted in
	the database.
	"""

	return

def save_books_to_file(file):
	"""
	Save the books in the database to the file (in CSV format)
	The file stores the main properties of the book (see books.csv), and serves as a backup file
	"""

	return

def insert_individual_book(name, author, country, year, ISBN):
	"""
	Insert a book in the database.
	"""

	return

def print_book_list():
	"""
	Prints the list of books on the screen.
	The list of books shall be grouped by the ISBN, and the number of samples for each
	book also has to be printed.

	For example:

		Book name			ISBN	samples
		===================================
		The hunger games	···		5	
				.
				.
				.

	"""

	return

def find_book_by_name(book_name):
	"""
	Return the code of the book that has a similar name to the one given
	"""
	return

##
## USER FUNCTIONS
##

def load_users_from_file(file):
	"""
	This function loads a file and inserts the contents in the database
	The file has to be in CSV format (see users.csv).

	If a user with the same DNI is already in the database, update it's name and info only
	"""

	return

def save_users_to_file(file):
	"""
	This function loads a file and inserts the contents in the database
	The file has to be in CSV format (see users.csv).
	"""

	return

def add_user(DNI, Name):
	"""
	Add user to the database
	If the user is already on the database (same DNI), then update the user name
	"""

	return

def remove_user(DNI):
	import mv_functions as mv
	"""
	Remove a user from the database given it's DNI (the DNI can be a string or an int, and if
	it's a string it can contain "." or spaces, be careful with those!)

	If the user has a book lent, perform the function return_book(DNI) (see mv_functions.py)

	After removing the user, call the function save_users_to_file(USERS_BACKUP) to
	update the backup file

	"""
