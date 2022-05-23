# import
import datetime
from flask import Flask, request, make_response, jsonify, render_template
import RPi.GPIO as GPIO
import os
import json
##


# led = [31, 35, 37]
ir = [32, 36, 38]

# gpio init


def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    # GPIO.setup(7, GPIO.OUT)


def gpio_set_input():
    for i in ir:
        GPIO.setup(i, GPIO.IN)


# create flask app
app = Flask(__name__)
log = app.logger


# home page
@app.route('/', methods=['GET'])
def index():
    print("start webpage")
    return render_template('index.html')


@app.route('/update', methods=['GET'])
def update():
    now = datetime.datetime.now()
    timeString = "TIME: " + now.strftime("%H:%M:%S")
    UpdateTimeOnweb = {
        'value': get_remain(),
        'time': timeString
    }
    return jsonify(**UpdateTimeOnweb)

# recieve request from webhook


@app.route("/", methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
#    print(req.get('queryResult').get('parameters').get('place'))

    try:
        action = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'
    # action switcher
    res = ""
    if action == 'Check':
        res = get_remain()
    else:
        log.error('Unexpected action.')

    print('Action: ' + str(action))
    print('Response: ' + res)
    # print(json.dumps(req, indent=2, sort_keys=True))
    # return response
    return make_response(jsonify({'fulfillmentText': res}))


def get_remain():
    max_slot = len(ir)
    remain = len([sensor for sensor in ir if GPIO.input(sensor) == GPIO.HIGH])

    return f'remaining: {remain}/{max_slot}'


# run flask app
if __name__ == '__main__':
    gpio_init()
    gpio_set_input()
    app.run(host='0.0.0.0', debug=True, port=int(
        os.environ.get('PORT', '5000')))
