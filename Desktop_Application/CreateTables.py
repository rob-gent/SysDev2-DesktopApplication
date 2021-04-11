import sqlite3

#connect to the database
conn = sqlite3.connect('CustomerOrders.db')

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

#Create table to store addresses
c.execute("""CREATE TABLE tblAddress (
    AddressID INTEGER PRIMARY KEY,
    Street varchar NOT NULL,
    City text NOT NULL,
    County text NOT NULL,
    Postcode varchar NOT NULL,
    Country text NOT NULL
    )""")

#Create table to store product information
c.execute("""CREATE TABLE tblProductInformation (
    ProdID INTEGER NOT NULL PRIMARY KEY,
    ProductName varchar NOT NULL,
    ProdCost INTEGER NOT NULL,
    ProdLocation varchar NOT NULL
    )""")

#Create table to store order information
c.execute("""CREATE TABLE tblOrders (
    OrderID INTEGER NOT NULL PRIMARY KEY,
    CustomerID INTEGER NOT NULL,
    AddressID INTEGER NOT NULL,
    ProductID INTEGER NOT NULL,
    ProductName varchar NOT NULL,
    Quanitity INTEGER NOT NULL,
    TotalCost INTEGER NOT NULL,
    OrderStatus text NOT NULL,
    FOREIGN KEY(CustomerID) REFERENCES tblCustomerData(CustomerID)
    FOREIGN KEY(AddressID) REFERENCES tblAddress(AddressID)
    FOREIGN KEY(ProductID) REFERENCES tblProductInformation(ProductID)
    )""")

#Commit our changes
conn.commit()

#Close Database connection
conn.close()
print("\nThe SQLite connection is closed.")

