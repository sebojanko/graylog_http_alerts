from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        print request.data

    return "success", 200