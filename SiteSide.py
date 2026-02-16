from flask import Flask, render_template, request, jsonify
#from ConnectTo import SendData
import time
import datetime as dt

daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
days = []
hour = int
minute = int

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('FrontPage.html')

@app.route('/submit', methods=['POST'])
def submit():
    selectedDays = request.form.getlist('days')
    selectedTime = request.form.get('time')

    for day in selectedDays:
        for dayWeek in daysOfTheWeek:
            if day == dayWeek:
                days.append(daysOfTheWeek.index(dayWeek)+1)

    print(selectedTime)
    print(days)
    return "OK"

@app.route('/heater', methods=['POST'])
def Heater():
    data = request.json
    response = {
        "days": days,
        "hour": hour,
        "minute": minute
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()
