from flask import *
from src.scrape import scrape
import os

# template_dir = os.path.abspath('../templates')
application = Flask(__name__)

@application.route("/")
def indexpage():
    return redirect(url_for("home"))

@application.route("/home")
def home():
    return render_template("index.html")

@application.route("/getdata")
def getData():
    ticker = request.args.get("ticker")
    scrape(ticker)
    return render_template("download.html", ticker=ticker)
    # print("ticker is: ", ticker)
    # return "ticker is: " + ticker

@application.route("/download/<int:random>/<string:ticker>")
def download(random, ticker):
    return send_file("deliverables/download.csv", as_attachment=True, attachment_filename=ticker+"BalanceSheet.csv", cache_timeout=0)

if __name__ == '__main__':
    application.run(port=5000, debug=True)