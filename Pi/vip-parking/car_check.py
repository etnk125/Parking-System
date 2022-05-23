# Natthawee Koengfak 6213125

import time
from datetime import datetime
import requests
from json import dumps


def main():
    main_class = Main()
    main_class.run()


class Main:
    # sampling 1 hour -> interval every 30 min
    interval = 60*30
    # for presentation
    # interval = 5

    def __init__(self):
        pass

    def run(self):
        while True:
            for e in self.get_token():
                now = datetime.now()
                start_time = datetime.strptime(
                    e['date'], "%Y-%m-%dT%H:%M:%S.%f%z").replace(tzinfo=None)
                sec = (now-start_time).total_seconds()
                min = int((sec/60) % 60)
                hour = int(sec/60/60)
                self.line_notify(
                    e['token'], f"you have been parked for {hour} hour {min} min")
            time.sleep(self.interval)

    def line_notify(self, token, message):
        # notify to line server
        url = 'https://notify-api.line.me/api/notify'
        data = f"message={message}"
        headers = {'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}

        x = requests.post(url, data, headers=headers)

        print('line', x.text)

    def get_token(self):
        # get token from node server
        # change to heroku later
        url = 'http://192.168.69.5:5000/token'
        x = requests.get(url)
        print(x.json())
        return x.json()


if __name__ == "__main__":
    main()
