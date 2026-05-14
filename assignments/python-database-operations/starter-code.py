import sqlite3

# Connect to the database (creates file if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Your code here

# Close the connection
conn.close()