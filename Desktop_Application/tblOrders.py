import sqlite3

#connect to the database
conn = sqlite3.connect('CustomerOrders.db')

# Create a cursor
c = conn.cursor()

#Inserts addresses into the address table, starting the automatic numbering process for addresses
c.execute("""INSERT INTO tblOrders (CustomerID,AddressID,ProductID, ProductName, Quantity, TotalCost,OrderStatus) 
VALUES ()""")

#Confrims record insertion
print('We have inserted', c.rowcount, 'address(es) into the table.')

#Defines address information to be inserted
Addresses = [
    ("Cadbury World","Linden Rd", "Birmingham", "B30 1JR", "United Kingdom"),
    ("GCHQ Cheltenham","Hubble Rd", "Cheltenham", "GL51 0EX","United Kingdom")
    ]

#Inserts address information into table
c.executemany('INSERT INTO tblAddress (Street, City, County, Postcode, Country) VALUES (?,?,?,?,?);',Addresses)

#Verifies the data has been added
print("\nAdded new records successfully")

#Commit our changes
conn.commit()