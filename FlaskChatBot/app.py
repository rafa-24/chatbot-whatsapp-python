from flask import Flask, request
import sett

# create instace of Flask
app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello, World!'


@app.route('/webhook', methods=['GET', 'POST'])
def verify_token():
  try:
    if request.method == 'GET':
      if request.args.get('hub.verify_token') == sett.token: # validate token
        return request.args.get('hub.challenge'), 200
      return 'Invalid token', 403
    elif request.method == 'POST':
      data = request.get_json()
      print(data)
      return 'Event received', 200
  except Exception as e:
    return e,403
