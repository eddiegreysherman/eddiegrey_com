from flask import Flask

app = Flask(__name__)
app.config.from_object('config')
app.secret_key = "123fornow"

@app.route('/')
def index():
    return "Welcome to my blog..."