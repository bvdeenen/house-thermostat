
import json, time, datetime
import bottle

app = bottle.Bottle() # pylint: disable=no-member

def interpret_schedule():
    with open("schedule.json","r") as fptr:
        schedule = json.load(fptr)
    now = datetime.datetime.now()
    weekday = now.weekday()
    active = None
    for s in schedule['schedules']:
        if s['type'] == 'weekly' and weekday in s['valid']:
            active = s['schedule']
    if not active:
        return schedule['Tdefault']

    hm = now.strftime("%H:%M")
    Temp = None
    for d in active:
        if hm > d['t']:
            Temp = d['T']

    return Temp if Temp else schedule['Tdefault']



@app.post('/control')
def control():
    print(bottle.request.json)
    setpoint = interpret_schedule()
    return {"setpoint": setpoint}


@app.get('/')
def index():
    return {"setpoint": setpoint}



if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, reloader=True)
