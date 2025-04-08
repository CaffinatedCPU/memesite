from flask import Flask, render_template
from reddit_api import get_memes

app = Flask(__name__)

@app.route('/')
def home():
    memes = get_memes()
    return render_template('index.html', memes=memes)

if __name__ == '__main__':
    app.run(debug=True)
