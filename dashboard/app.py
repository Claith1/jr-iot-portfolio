from flask import Flask, render_template
from db import Database

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/device-load')
def DeviceLoad():
    return



@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/cpu')
def chart_cpu():
    return render_template('chart-cpu.html')


if __name__ == '__main__':
    app.run("127.0.0.1",5555)
