import os
from flask import Flask, escape, render_template, request
from flask_assets import Environment, Bundle
from webassets.loaders import YAMLLoader
from bibliopompica.blueprints.book_blueprint import book_blueprint
from bibliopompica.blueprints.recommendation_blueprint import recommendation_blueprint

app = Flask(__name__)
app.register_blueprint(book_blueprint)
app.register_blueprint(recommendation_blueprint)

assets = Environment(app)
assets.from_yaml(os.path.dirname(__file__) + "/assets.yml")

@app.route('/')
def index():
    name = request.args.get("name", "World")
    return render_template('pages/index.html', name=name)
