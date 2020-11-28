from flask import Flask, render_template
from monitor_ii.monitor_cpu import get_load_last
from monitor_ii.monitor_enviro import get_last_temperature,get_last_humidity,get_last_pressure
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/device-load')
def DeviceLoad():
    var = get_load_last(1)
    val = list(zip(*var))[0]
    return {"load": val}


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')


@app.route("/api/environment")
def get_api_environment():
        var = get_last_temperature(1)
        temp = list(zip(*var))[0]

        var = get_last_pressure(1)
        pressure = list(zip(*var))[0]

        var = get_last_humidity(1)
        humidity = list(zip(*var))[0]
        return {"temperature" : temp,"pressure":pressure,"humidity" : humidity}

@app.route("/api/temperature/<count>")
def get_api_temperature_multi(count =1):
    var = get_last_temperature(count)
    val = list(zip(*var))[0]
    return {"temperature": val}

@app.route("/api/humidity/<count>")
def get_api_humidity_multi(count =1):
    var = get_last_humidity(count)
    val = list(zip(*var))[0]
    return {"humidity": val}

@app.route("/api/pressure/<count>")
def get_api_pressure_multi(count =1):
    var = get_last_pressure(count)
    val = list(zip(*var))[0]
    return {"pressure" : val}

@app.route("/api/temperature")
def get_api_temperature():
    var = get_last_temperature(1)
    val = list(zip(*var))[0]
    return {"temperature" : val}



@app.route("/api/pressure")
def get_api_pressure():
    var = get_last_pressure(1)
    val = list(zip(*var))[0]
    return {"pressure": val}


@app.route("/api/humidity")
def get_api_humidity():
    var = get_last_humidity(1)
    val = list(zip(*var))[0]
    return {"humidity": val}


if __name__ == '__main__':
    app.run("127.0.0.1",5555)