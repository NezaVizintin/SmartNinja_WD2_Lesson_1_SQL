from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("hiking_trip.sqlite")

#create
db.execute("""
            CREATE TABLE IF NOT EXISTS user (
            id integer primary key autoincrement,
            name text,
            age integer)
            """) #v sqlu whitespace ni pomemben, razen en presledek med besedami


db.execute("INSERT INTO user (name, age) VALUES ('Legolas', 3)")

# create, read, update, delete --> CRUD

#read
user_names = db.execute("SELECT name FROM user")

print("Verbose:")
db.print_tables(verbose=True)

print("Not verbose:")
db.print_tables(verbose=False)

print("User names:")
print(user_names)

print("User all:")
db.pretty_print("SELECT * FROM user")

#update
db.execute("UPDATE user SET age = 4 where id = 2")
print("User all after update:")
db.pretty_print("SELECT * FROM user")

#delete
db.execute("DELETE FROM user WHERE id > 3")
db.pretty_print("SELECT * FROM user")

#spremeni tabelo (ne vsebino tabele)
db.execute("ALTER TABLE user ADD email text")
db.pretty_print("SELECT * FROM user")

#delete table
#db.execute("DROP TABLE use")