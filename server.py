import sys
import signal
from flask import Flask, jsonify
from door import DoorSensor

app = Flask(__name__)
door = DoorSensor()

@app.route("/", methods=['GET'])
def is_open_route():
    """API to check if door is open."""
    return jsonify({'is_open': door.is_open()})

def shutdown(signal, frame):
    """Clean up when the user exits with keyboard interrupt."""
    door.cleanup()
    sys.exit(0)

if __name__ == '__main__':
    # Start running the Flask server
    app.run(debug=True)
    # Set the cleanup handler for when user hits Ctrl-C to exit
    signal.signal(signal.SIGINT, shutdown)
