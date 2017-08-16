from flask import Flask,render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
socketio = SocketIO(app)
print('127.0.0.1:5000 Port Start')

@app.route( '/' )
def index():
  return render_template( './index.html' )



@socketio.on('sender')
def sender_value(msg):
    emit('sender',msg , broadcast=True)
    print(msg)




if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0')