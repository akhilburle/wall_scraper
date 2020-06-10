from flask import *
from src.scrape import scrape
import os

# template_dir = os.path.abspath('../templates')
app = Flask(__name__)

@app.route("/")
def indexpage():
    return "Hello World!"

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/download")
def download():
    ticker = request.args.get("ticker")
    scrape(ticker)
    print("ticker is: ", ticker)
    return "ticker is: " + ticker


if __name__ == '__main__':
    app.run(port=5000, debug=True)