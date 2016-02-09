from gevent import monkey
 
monkey.patch_all()
 
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, send, leave_room
 
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'chatappkey'
app.config['DEBUG'] = True
socketio = SocketIO(app)



@app.route('/')
def chat():
    return render_template('chat.html')


@app.route('/login')
def login():
    return render_template('login.html')


@socketio.on('typing', namespace='/chatapp')
def typing(data, room, namespace):
    emit("typing", data, room=room, namespace=namespace)


@socketio.on('nottyping', namespace='/chatapp')
def typing(data, room, namespace):
    emit("nottyping", data, room=room, namespace=namespace)


@socketio.on('logging', namespace='/chatapp')
def logging(data, room, namespace):
    message = data.get("message", "user")
    emit("logging", message, room=room, namespace=namespace)


@socketio.on('rooms', namespace='/chatapp')
def get_rooms(data):
    rooms_d = socketio.rooms.get("/chatapp", {})
    room_l = []
    for room_t in rooms_d.iteritems():
        room_name = room_t[0]
        room_l.append(room_name)
    emit("rooms", {"rooms": room_l})


@socketio.on('join', namespace='/chatapp')
def on_join(data):
    alias = data['alias']
    room = data['room']
    join_room(room)
    emit(alias + ' has entered the room.', room=room)


@socketio.on('leave', namespace='/chatapp')
def on_leave(data):
    alias = data['alias']
    room = data['room']
    leave_room(room)
    emit(alias + ' has left the room.', room=room)


@socketio.on('message', namespace='/chatapp')
def chat_message(message, room, namespace):
    emit('message', {'data': message['data']}, room=room, namespace=namespace)

 
@socketio.on('connect', namespace='/chatapp')
def test_connect():
    emit('test_connect', {'data': 'Connected', 'count': 0})


@socketio.on('disconnect', namespace='/chatapp')
def test_disconnect():
    emit('test_connect', "Client disconnected")
 
 
if __name__ == '__main__':
    socketio.run(app)
