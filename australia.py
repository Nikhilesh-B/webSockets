import socketio
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print("I'm connected!")
    form_data = {
        'firstName': 'John',
        'lastName': 'Doe',
        'description': 'Sample description',
        'resolved': False,
        'lock': True
    }
    sio.emit('formSubmit', form_data)

@sio.on('message')
def on_message(data):
    print('Message received:', data)

@sio.on('disconnect')
def on_disconnect():
    print("I'm disconnected!")

# Connect to the server
sio.connect('http://localhost:3001')  # Adjust the URL to your Socket.IO server