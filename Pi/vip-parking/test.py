import requests

url = 'https://notify-api.line.me/api/notify'
data = "message=Hello"
headers = {'Authorization': 'Bearer Cbj5qHB1G1PTjGnitAuRQc0CyZcV0H8mjpuIhYkLCEg',
           'Content-Type': 'application/x-www-form-urlencoded'}

x = requests.post(url, data, headers=headers)

print(x.text)
