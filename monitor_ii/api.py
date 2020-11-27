from flask import Flask, render_template
from monitor import GetLoad
from monitor_ii.monitor_enviro import get_last_temperature,get_last_humidity,get_last_pressure
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/device-load')
def DeviceLoad():
    return ("{cpu : \"" + str(GetLoad()) + "\"}")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')


@app.route("/api/environment")
def get_api_environment():
    return {"error": "Route no implemented",
            "temperature": None,
            "pressure": None,
            "humidity": None}


@app.route("/api/temperature/<count>")
def get_api_temperature_multi(count =1):
    var = get_last_temperature(int(count))
    for ind in range(len(var)):
        var[ind] = str(var[ind]).replace(',','')
        var[ind] = var[ind].replace('(','')
        var[ind] = float(var[ind].replace(')',''))
    return {"temperature" : var}

@app.route("/api/humidity/<count>")
def get_api_humidity_multi(count =1):
    var = get_last_humidity(int(count))
    for ind in range(len(var)):
        var[ind] = str(var[ind]).replace(',','')
        var[ind] = var[ind].replace('(','')
        var[ind] = float(var[ind].replace(')',''))
    return {"humidity" : var}

@app.route("/api/pressure/<count>")
def get_api_pressure_multi(count =1):
    var = get_last_pressure(int(count))
    for ind in range(len(var)):
        var[ind] = str(var[ind]).replace(',','')
        var[ind] = var[ind].replace('(','')
        var[ind] = float(var[ind].replace(')',''))
    return {"pressure" : var}

@app.route("/api/temperature")
def get_api_temperature():
    var = get_last_temperature(1)
    val = list(list(zip(*var))[0])
    print(str(val))
    print(var[0])
    return {"temperature" : val}



@app.route("/api/pressure")
def get_api_pressure():
    var = get_last_pressure(1)
    for ind in range(len(var)):
        var[ind] = str(var[ind]).replace(',', '')
        var[ind] = var[ind].replace('(', '')
        var[ind] = float(var[ind].replace(')', ''))
    return {"pressure": var[0]}


@app.route("/api/humidity")
def get_api_humidity():
    var = get_last_humidity(1)
    for ind in range(len(var)):
        var[ind] = str(var[ind]).replace(',', '')
        var[ind] = var[ind].replace('(', '')
        var[ind] = float(var[ind].replace(')', ''))
    return {"humidity": var[0]}


if __name__ == '__main__':
    app.run("127.0.0.1",5555)