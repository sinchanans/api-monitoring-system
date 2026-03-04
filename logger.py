import json
from datetime import datetime

LOG_FILE = "logs.json"

def log_event(api_name, status):

    try:
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    except:
        logs = []

    if logs:
        last_log = logs[-1]

        if last_log["api"] == api_name and last_log["status"] == status:
            return

    event = {
        "api": api_name,
        "status": status,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    logs.append(event)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)