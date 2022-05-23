# Natthawee Koengfak 6213125

import time
from datetime import datetime
import requests
from json import dumps


def main():
    main_class = Main()
    main_class.run()


class Main:
    # 10 sec interval
    interval = 10

    def __init__(self):
        pass

    def run(self):
        while True:
            for e in self.get_noti():
                self.line_notify(e['token'], e['message'])
                time.sleep(self.interval)

    def line_notify(self, token, message):
        # notify to line server
        url = 'https://notify-api.line.me/api/notify'
        data = f"message={message}"
        headers = {'Authorization': f'Bearer {token}',
                   'Content-Type': 'application/x-www-form-urlencoded'}

        x = requests.post(url, data, headers=headers)

        print('line', x.text)

    def get_noti(self):
        # get token from node server
        # change to heroku later
        # url = 'http://192.168.69.5:5000/notification'
        url = 'http://192.168.1.60:5000/notification'
        x = requests.get(url)
        print(x.json())
        return x.json()


if __name__ == "__main__":
    main()
