from flask import Flask
from app import create_app
from flask import Flask,render_template,url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from dash_file.dash_app1 import dash1
from flask import render_template
import dash
from dash import html

app = create_app()


if __name__ == "__main__":
    
    app.run(debug=True, port=8000)