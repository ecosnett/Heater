import sqlite3 

conn = sqlite3.connect("./HeaterSchedules.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Schedules (id INTEGER PRIMARY KEY AUTOINCREMENT, Day INTEGER, Hour INTEGER, Min INTEGER, Active INTEGER)")



#cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (1, 08, 00, true)")
# cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (2, 08, 00, true)") 
# cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (3,08, 00, true)") 
# cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (4, 08, 00, true)") 
# cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (5, 08, 00, true)") 

conn.commit()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
 


