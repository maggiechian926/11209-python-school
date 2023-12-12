from flask import Flask
from app.route import hello_world, index

def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', '/', index)
    app.add_url_rule('/index', 'index', hello_world)
    
    return app