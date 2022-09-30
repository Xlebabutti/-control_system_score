
from concurrent.futures import thread
from glob import glob
from unittest import result
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, send, emit, join_room, leave_room,  Namespace, disconnect
from vmix import Main
import _thread


app = Flask(__name__)
sio = SocketIO(app, acync_mode="eventlet")

Team_1 = 0
Tema_2 = 0



@app.route("/", methods=["GET", "POST"])
def hello_world():
    # pgm = Main.PGM_in()
    pgm_vmix = Main()
    return render_template("Main.html", pgm_vmix = pgm_vmix)

@app.route('/vmix', methods=['GET'])
def remout():
    pgm_vmix = Main()
    print(pgm_vmix)
    print(jsonify(result=pgm_vmix))
    return jsonify(result=pgm_vmix[0], result2=pgm_vmix[1])


@sio.on('vmix_socet', namespace='/test')
def input_pgm_vmix(msg):   
    global Team_1
    global Tema_2
    sio.emit(msg, namespace='/test')

    sio.emit('Team_1', Team_1, namespace = '/test')
    sio.emit('Team_2', Tema_2, namespace = '/test')
    print('client connected!')

if __name__ == '__main__':
   _thread.start_new_thread(Main, ())
   sio.run(app, host = '127.0.0.1', port=5050, debug = True)