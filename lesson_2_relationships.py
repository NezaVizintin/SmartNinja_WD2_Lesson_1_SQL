from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("chinook.sqlite")

# lists tables that will be displayed FROM the joined tables (table Customer and Invoiced based on CutomerId)
db.pretty_print("""SELECT Invoice.CustomerId, Invoice.BillingCity, Customer.FirstName,
                    Customer.LastName, Invoice.Total
                    FROM Invoice FULL OUTER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId""")

# same as above but only shows invoices from Stockholm customers using WHERE
db.pretty_print("""SELECT Invoice.CustomerId, Invoice.BillingCity, Customer.FirstName,
                    Customer.LastName, Invoice.Total
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")

# calculate SUM of all orders from Stockholm
db.pretty_print("""SELECT SUM(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")

# calculate AVERAGE of all orders from Stockholm
db.pretty_print("""SELECT AVG(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")

# COUNTS all orders from Stockholm
db.pretty_print("""SELECT COUNT(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")

# the order with the MINIMUM (lowest) value from all the orders from Stockholm
db.pretty_print("""SELECT MIN(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")

# the order with the MAXIMUM (highest) value from all the orders from Stockholm
db.pretty_print("""SELECT MAX(Invoice.Total)
                    FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId
                    WHERE Invoice.BillingCity='Stockholm';""")