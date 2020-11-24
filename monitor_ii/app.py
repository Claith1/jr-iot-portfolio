from flask import Flask, render_template
from monitor import GetLoad

app = Flask(__name__)




@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')

@app.route('/api/environment')
def get_api_enviroment():

    obj = {'error': 'Route no implemented',
            'temperature': '0',
            'pressure': '0',
            'humidity': '0'}
    print(obj)
    return obj


@app.route("/api/temperature")
def get_api_temperature():
    return {"error": "Route no implemented",
            "temperature": None}

@app.route("/api/pressure")
def get_api_pressure():
    return str({"error": "Route no implemented",
            "pressure": None})

@app.route("/api/humidity")
def get_api_humidity():
    return {"error": "Route no implemented",
            "humidity": None}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/device-load')
def DeviceLoad():
    return "{cpu : \"" + str(GetLoad()) + "\"}"



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run("127.0.0.1",5555)