import sqlite3

#connect to the database
conn = sqlite3.connect('TestDB.db')

# Create a cursor
c = conn.cursor()

#Create table to store customer details
c.execute("""CREATE TABLE tblCustomerData (
    CustomerID INTEGER NULL PRIMARY KEY,
    FirstName text NOT NULL,
    LastName text NOT NULL,
    Email varchar NOT NULL,
    AddressID INTEGER NOT NULL,
    FOREIGN KEY(AddressID) REFERENCES tblAddress(AddressID)
    )""")

#Inserts addresses into the address table, starting the automatic numbering process for addresses
# c.execute("""INSERT INTO tblCustomerData (CustomerID,FirstName,LastName,Email,AddressID) 
# VALUES ( 1,"Ministry of Defence","Whitehall","London","W1A 2HB","United Kingdom")""")

# #Confrims record insertion
# print('We have inserted', c.rowcount, 'address(es) into the table.')

#Defines address information to be inserted
#Defines Customer Data

CustomerData = [
    ("Jane", "Doe","Jane.Doe@domain.com"),
    ("Peter","Griffin","example@fomain.com")
    ]

#Inserts customer data into table
c.executemany('INSERT INTO tblCustomerData (FirstName, LastName, Email) VALUES (?,?,?);',CustomerData)

#Verifies the data has been added
print("\nAdded new records successfully")

#Commit our changes
conn.commit()