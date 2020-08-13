import sqlite3

conn = sqlite3.connect("contacts.sqlite")

# for row in conn.execute("SELECT * FROM contacts"):
#     print(row)

name = input("Enter the name you want? ")
li = list(name.split(" "))

retriever = "SELECT DISTINCT * from contacts WHERE name LIKE ? "
retrieve = conn.cursor()
for name,phone,email in retrieve.execute(retriever, tuple(li)):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)
retrieve.close()

conn.close()