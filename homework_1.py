from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("chinook.sqlite")

print("Artist names:")
db.pretty_print("SELECT Name FROM Artist")

print("Germany invoices:")
db.pretty_print("SELECT * FROM Invoice Where BillingCountry = 'Germany'")

print("Number of albums:")
db.pretty_print("SELECT COUNT(*) FROM Album")

print("Number of french customers:")
db.pretty_print("SELECT COUNT(*) FROM Invoice WHERE BillingCountry = 'France'")