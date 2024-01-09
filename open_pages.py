import webbrowser
import keyboard
import sqlite3
import time
from datetime import datetime

db_loc = r"C:\Users\yse\Desktop\prog\python\scraper\Gp\items.db"
conn = sqlite3.connect(db_loc)
c = conn.cursor()

today = datetime.now().strftime("%d_%m_%Y")

gp = []
sb = []
url1 = c.execute(f'SELECT url FROM items WHERE bargian LIKE "True" AND date LIKE "{today}"')
for url in url1.fetchall():
    gp.append(url[0])
url2 = c.execute(f'SELECT url FROM skinbid WHERE bargian LIKE "True" AND date LIKE "{today}" AND percent_diff BETWEEN -0.1 AND 0.1')
for url in url2.fetchall():
    sb.append(url[0])

i = 0
o = 0
while True:
    time.sleep(0.01)
    if keyboard.is_pressed('f2'):
        time.sleep(0.1)
        for z in range(i, i+10):
            # print(url_list[0])
            webbrowser.open_new_tab(gp[z])
        i = i + 10
    if keyboard.is_pressed('f3'):
        time.sleep(0.1)
        for z in range(o, o+10):
            # print(url_list[0])
            print(sb[z])
            webbrowser.open_new_tab(str(sb[z]))
        o = o + 10

conn.close()