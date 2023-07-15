from flask import Flask, render_template

app = False(__name__)

@app.route('/')
def hello_world():
    return "<p>Deployed</p>"