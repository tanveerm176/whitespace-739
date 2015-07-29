from flask import Flask,render_template
import time_calc

time_flask = Flask(__name__)

@time_flask.route('/')
def time(lightyears=30):
    t = time_calc.time(lightyears)
    return render_template('time_flask.html', z = t)

if __name__ == "__main__":
        time_flask.debug = True
        time_flask.run()



