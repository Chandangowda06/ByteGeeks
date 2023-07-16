from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    cur_year = datetime.now().year
    return render_template('home.html',year=cur_year )

@app.route('/chat-bot')
def chat():
    return render_template('chat.html')
if __name__ == '__main__':
    app.run(debug=True)