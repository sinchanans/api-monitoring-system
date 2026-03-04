import requests
import json
from recovery import trigger_recovery
from notifier import send_alert
from logger import log_event

with open("config.json") as f:
    config = json.load(f)

def check_apis():

    for api in config["apis"]:

        try:
            response = requests.get(api["url"], timeout=5)

            if response.status_code == 200:
                print(f"{api['name']} is healthy")
                log_event(api["name"], "HEALTHY")

            else:
                handle_failure(api)

        except Exception:
            handle_failure(api)

def handle_failure(api):

    print(f"{api['name']} failed")

    log_event(api["name"], "FAILED")

    trigger_recovery(api)

    send_alert(api["name"])