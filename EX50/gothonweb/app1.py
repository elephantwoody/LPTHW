from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def intro():
    introduction = "Ellie Cheng"
    render = render_template('foo.html', intro=introduction)
    return render

if __name__ == "__main__":
    app.run()
