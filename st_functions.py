from datetime import datetime

CONN = None

## 
## STATISTIC FUNCTIONS
##

"""
The database must store a history of every time a book has been borrowed or lent
This helps the staff to keep track of recent activity in the library

The history must have the following structure

	BOOKID
	USERID
	DATE
	OPERATIONCODE (int)
	OPERATIONTYPE ("lending" or "returning")

"""

def print_history(length=10):
	"""
	Print the last items in the history of movements
	"""
	return

def best_books():
	"""
	Print a list contaning the 3 books that have been lent the most.
	This will aid the staff for the next book purchase for the library
	"""
	return

def most_active_users():
	"""
	Print a list of the 3 most active users
	"""
	return
