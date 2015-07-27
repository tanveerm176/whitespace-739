from flask import Flask, request, render_template
import time_calc

new_flask = Flask(__name__)

@new_flask.route('/', methods=["POST", "GET"])


