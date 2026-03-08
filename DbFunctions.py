import sqlite3

def GetSchedule(day = 7):
    conn = sqlite3.connect("./HeaterSchedules")
    cur = conn.cursor()
    if day == 7:
        cur.execute("SELECT * FROM Schedules")
        data = cur.fetchall()
        conn.close()
        return data
    
    else:
        cur.execute("SELECT * FROM Schedules WHERE day = ?", (day,))
        data = cur.fetchall()
        conn.close()
        return data

def RemoveSchedule(id):
    id = str(id)
    conn = sqlite3.connect("./HeaterSchedules")
    cur = conn.cursor()
    cur.execute("DELETE FROM Schedules where ID = ?", (id,))
    conn.commit()
    conn.close()

def InsertRecord(day, hour, mins, active):
    if active == None:
        active = 0
    conn = sqlite3.connect("./HeaterSchedules")
    cur = conn.cursor()
    cur.execute("INSERT INTO Schedules (Day, Hour, Min, Active) VALUES (?, ?, ?, ?)", (day, hour, mins, active))
    conn.commit()
    conn.close()

def CheckActive(id):
    id = str(id)
    conn = sqlite3.connect("./HeaterSchedules")
    cur = conn.cursor()
    cur.execute("SELECT Active FROM Schedules where id = ?", (id,))
    data = cur.fetchall()
    if data == [(0,)]:
        RemoveSchedule(id)
    else:
        return


print(GetSchedule())

