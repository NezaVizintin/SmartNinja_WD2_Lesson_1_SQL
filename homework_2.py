from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("chinook.sqlite")

print("Cheapest order:")
db.pretty_print("SELECT MIN(Total) FROM Invoice")

print("Most expensive order:")
db.pretty_print("SELECT MAX(Total) FROM Invoice")

print("City with the most orders:")
db.pretty_print("""
                    SELECT BillingCity, COUNT(*) as mycount FROM Invoice GROUP BY BillingCity HAVING COUNT(BillingCity) =
                        (SELECT MAX(mycount) FROM
                            (SELECT COUNT(BillingCity) AS mycount FROM Invoice GROUP BY BillingCity)
                        )
                """)

print("Track with MediaType Protected AAC audio file:")
db.pretty_print("SELECT Track.Name FROM Track INNER JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId Where MediaType.Name = 'Protected AAC audio file'")

print("Artist with the most albums:")
db.pretty_print("SELECT Artist.Name, COUNT(Artist.Name) as AlbumCount FROM Album INNER JOIN Artist ON Album.ArtistId=Artist.ArtistId GROUP BY Album.ArtistId  ORDER BY AlbumCount DESC LIMIT 1")

print("Genre with the most tracks:")
db.pretty_print("SELECT Genre.Name, COUNT(Genre.Name) as GenreCount FROM Track INNER JOIN Genre ON Track.GenreId=Genre.GenreId GROUP BY Track.GenreId  ORDER BY GenreCount DESC LIMIT 1")

print("Customer that has spent the most money:")
db.pretty_print("SELECT MAX(Invoice.Total), Customer.FirstName, Customer.LastName FROM Invoice INNER JOIN Customer ON Invoice.CustomerId=Customer.CustomerId")

print("Songs that were bought with each order:")
db.pretty_print("SELECT Track.Name, Invoice.* FROM Track INNER JOIN InvoiceLine ON InvoiceLine.TrackId=Track.TrackId JOIN Invoice ON InvoiceLine.InvoiceId=Invoice.InvoiceId")