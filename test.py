"""
You shall write some code to test that the functions you've implemented work
"""

import db_functions as db
import mv_functions as mv
import st_functions as st

##
## EXAMPLE: test db_functions.py
##

db.mysql_connect()
mv.CONN = db.CONN
st.CONN = db.CONN

db.load_books_from_file(db.BOOKS_BACKUP)
db.load_users_from_file(db.USERS_BACKUP)

db.insert_individual_book("12501","Harry Potter and the Philosopher's stone", "JK Rowling", "UK", "1997", "978-0747532743")
db.insert_individual_book("12502","Harry Potter and the Philosopher's stone", "JK Rowling", "UK", "1997", "978-0747532743")
db.insert_individual_book("12503","Harry Potter and the Philosopher's stone", "JK Rowling", "UK", "1997", "978-0747532743")

db.save_books_to_file(db.BOOKS_BACKUP)

db.print_book_list()

print(db.find_book_by_name("The lord of the rings"))
print(db.find_book_by_name("Harry potter"))
print(db.find_book_by_name("Pride and prejudice"))

db.save_users_to_file(db.USERS_BACKUP)

db.add_user("38819218","Francisco Kovacevich")
db.add_user("11316222","María Inés García")
db.remove_user("38819218")
