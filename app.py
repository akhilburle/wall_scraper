from flask import *
from src.scrape import scrape
import os

# template_dir = os.path.abspath('../templates')
app = Flask(__name__)

@app.route("/")
def indexpage():
    return redirect(url_for("home"))

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/getdata")
def getData():
    ticker = request.args.get("ticker")
    scrape(ticker)
    return render_template("download.html", ticker=ticker)
    # print("ticker is: ", ticker)
    # return "ticker is: " + ticker

@app.route("/download/<int:random>/<string:ticker>")
def download(random, ticker):
    return send_file("deliverables/download.csv", as_attachment=True, attachment_filename=ticker+"BalanceSheet.csv", cache_timeout=0)

if __name__ == '__main__':
    app.run(port=5000, debug=True)