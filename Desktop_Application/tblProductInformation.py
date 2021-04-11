import sqlite3

#connect to the database
conn = sqlite3.connect('CustomerOrders.db')

# Create a cursor
c = conn.cursor()

print("\nAdding new records")

ProductInformation = [
    (1,"Samsung Galaxy S21 Ultra", 799 ,"A01"),
    (2,"OnePlus 8 Pro",            429 ,"B02"),
    (3,"iPhone 12",                1299,"C01"),
    (4,"Oppo Find X2 Pro",         899 ,"C03"),
    (5,"Motorola Edge Plus",       300 ,"D04"),
    (6,"Xiaomi Mi Note 10",        250 ,"A03"),
    (7,"Sony Xperia 1",            479 ,"E02"),
    (8,"Nokia 3310",               39  ,"B01")]

c.executemany('INSERT INTO tblProductInformation VALUES (?,?,?,?);',ProductInformation)

#Verifies the data has been added
print("\nAdded new records successfully")

#Commit our changes
conn.commit()