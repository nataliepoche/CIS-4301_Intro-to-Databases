# Import needed module
import mysql.connector as mariadb

# Create a dictionary (Python's version of a map) to store the configuration info
config = {
    "user": "new_username", # Change to match your MariaDB Username and Password
    "password": "new_password",
    "host": "localhost",
    "database": "cis4301_test",
    # If you specified a port other than 3306, include entry - "port": "port_number"
}

# Connect to MariaDB Server
conn = mariadb.connect(user=config["user"], password=config["password"], host=config["host"],
collation='utf8mb4_unicode_ci')  # I needed this collation thing due to some text encoding error

cur = conn.cursor()
# If specified port other than 3306, include following entry in connection - port=config['port']

# Create the database if it doesn't exist, then use it
cur.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']};")
cur.execute(f"USE {config['database']};")

# Create a table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name varchar(100), 
    email varchar(100) UNIQUE
    )
""")

# Insert a row into the table
# If there is an error similar to "Unknown collation: utf8mb4_0900_ai_ci'", add
# the additional argument "collation='utf8mb4_unicode_ci'" to the connect function
cur.execute("INSERT INTO users (name, email) VALUES (%s, %s);",
            ("Test User", "test@gmail.com"))
# Save the change
conn.commit()

# Retrieve records from the table
# Read all rows and attributes form the users table
cur.execute("SELECT id, name, email FROM users;")

# Get all rows from the table and print them
rows = cur.fetchall()
print(rows)

# Close the connection
cur.close()
conn.close()