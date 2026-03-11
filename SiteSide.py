from flask import Flask, render_template, request, jsonify
from DbFunctions import GetSchedule, RemoveSchedule, InsertRecord, CheckActive
from datetime import datetime, timedelta

now = datetime.now()
daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

app = Flask(__name__)

def formatData(day = 7):
    global data
    data = GetSchedule(day)
    FormattedData = []
    for record in data:
        DataTuple = (
            record[0],
            daysOfTheWeek[record[1] - 1],  
            f"{record[2]:02}:{record[3]:02}",
            record[4])        
        FormattedData.append(DataTuple)

    return FormattedData

def ClosestTime():
    dates = {}
    for record in data:
        record_datetime = datetime(
            now.year,
            now.month,
            now.day,
            record[2],  # hour
            record[3],  # minute
            0)
        dates[record] = record_datetime

    closest = min(dates, key=lambda r: abs((dates[r] - now).total_seconds()))

    print(closest)
    return closest

def InsertSchedule(days, hour, minute, active):
    if not isinstance(days, (list, tuple)):
        days = [days]
    for day in days:
        if day == 7:
            InsertRecord(0, hour, minute, active)
            print(1)
        else:
            InsertRecord(day, hour, minute, active)
            print(2)

@app.route('/')
def index():
    return render_template('FrontPage.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    global days, hour, minute

    days = []

    selectedDays = request.form.getlist('days')
    selectedTime = request.form.get('time')
    active = request.form.get('repeat')
    print(dict(request.form))

    for day in selectedDays:
        if day in daysOfTheWeek:
            days.append(daysOfTheWeek.index(day) + 1)

    if selectedTime:
        hour, minute = map(int, selectedTime.split(":"))

    print(days, hour, minute, active)
    InsertSchedule(days, hour, minute, active)
    formatData()
    return "OK"

@app.route('/heater', methods=['POST'])
def Heater():
    closest = ClosestTime()
    response = {
        "id": closest[0],
        "day": closest[1],
        "hour": closest[2],
        "minute": closest[3]
    }
    print(response)
    return jsonify(response)

@app.route('/heaterRan', methods=['POST'])
def HeaterRan():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON received"}), 400
    
    CheckActive(data.get("id"))
    formatData()

    return jsonify({"status": "received"}), 200
    

@app.route("/delete", methods=["POST"])
def delete():
    ItemId = request.form["item_id"]
    RemoveSchedule(ItemId)
    return "Deleted"

if __name__ == "__main__":
    formatData()
    app.run(host="0.0.0.0", port=5000)