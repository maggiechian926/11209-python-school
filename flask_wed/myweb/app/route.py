
from flask import render_template
import dash


def hello_world():
    return "Hello, maggie!"

def index():
    title = "Suicide Ideation"
    big_word = "Suicide Ideation"
    return render_template('index.html',title=title,big_word=big_word) 
