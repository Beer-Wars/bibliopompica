import os
from flask import Flask, escape, render_template, request
from flask_assets import Environment, Bundle
from webassets.loaders import YAMLLoader

app = Flask(__name__)
assets = Environment(app)
assets.from_yaml(os.path.dirname(__file__) + "/assets.yml")

@app.route('/')
def index():
    name = request.args.get("name", "World")
    return render_template('pages/index.html', name=name)
