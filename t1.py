import sqlite3

db_loc = r"C:\Users\yse\Desktop\prog\python\scraper\Gp\items.db"
conn = sqlite3.connect(db_loc)


c = conn.cursor()

# c.execute("""CREATE TABLE items (
#                 item text,
#                 price real,
#                 buff_price real,
#                 bargian text,
#                 url text,
#                 date text
#                 )""")

# print(c.execute("""SELECT * FROM items WHERE item LIKE """))

# c.execute("DELETE FROM skinbid WHERE bargian LIKE 'False'")
c.execute("DELETE FROM skinbid WHERE date LIKE '09_01_2024'")
# c.execute("DELETE FROM skinbid WHERE bargian LIKE 'True'")
# c.execute("SELECT * FROM items")

# print(c.fetchone())

conn.commit()
conn.close()