import sqlite3

#connect to the database
conn = sqlite3.connect('CustomerOrders.db')

# Create a cursor
c = conn.cursor()

#Defines Customer Data
CustomerData = [
    ("Jane", "Doe","Jane.Doe@domain.com",3),
    ("Peter","Griffin","example@fomain.com",2)
    ]

#Inserts customer data into table
c.executemany('INSERT INTO tblCustomerData (FirstName, LastName, Email, AddressID) VALUES (?,?,?,?);',CustomerData)

#Verifies the data has been added
print("\nAdded new records successfully")

#fetches and displayes all data from the table
print(c.fetchall())

#Commit our changes
conn.commit()