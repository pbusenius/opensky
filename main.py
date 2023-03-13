import os
import tqdm
import time
import json
import requests

from requests.auth import HTTPBasicAuth


WAIT_TIME = 5 * 60


def main(username: str, password: str):
    response = requests.get("https://opensky-network.org/api/states/all", auth=HTTPBasicAuth(username, password))
    json_data = response.json()

    with open(f"{int(time.time())}.json", "w") as file:
        file.write(json.dumps(json_data, indent=4))


if __name__ == "__main__":
    username = os.environ.get("OPENSKY_USER")
    password = os.environ.get("OPENSKY_PASSWORD")

    for i in tqdm.tqdm(range(12)):
        main(username, password)
        time.sleep(WAIT_TIME)
