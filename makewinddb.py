# Sebastian Raschka, 2014
# Creating a new SQLite database

import sqlite3

sqlite_file = 'windlog.db'    # name of the sqlite database file
table_name = 'windlog'	# name of the table to be created
new_field1 = 'date' # name of the column
new_field2 = 'mph' # name of the column
field_type1 = 'DATETIME'  # column data type
field_type2 = 'NUMERIC'  # column data type


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name, nf=new_field1, ft=field_type1))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_field2, ct=field_type2))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()