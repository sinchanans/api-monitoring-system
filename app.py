from flask import Flask, render_template
import json
from apscheduler.schedulers.background import BackgroundScheduler
from monitor import check_apis

app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_job(check_apis, "interval", minutes=1)
scheduler.start()

@app.route("/")
def dashboard():

    with open("logs.json") as f:
        logs = json.load(f)

    return render_template("dashboard.html", logs=logs)

@app.route("/status")
def status():

    with open("logs.json") as f:
        logs = json.load(f)

    return {"status": logs[-5:]}

if __name__ == "__main__":
    app.run(debug=True)