# Is the Cube open?

Script that shows if the Cube is open or not, by checking the status of a door sensor attached to the door to the club room. If the door is open, the site reports that the Cube is open.

## Installation

Obtain a Raspberry Pi with a Debian OS installed.

```sh
sudo apt-get install python-dev python-rpi.gpio git
python3 -m pip install Flask
```

## Usage

Set `pin.DOOR_SENSOR_PIN` in `door.py` to be the correct pin number.

```sh
python3 server.py
```

---

Based on [Playing with Raspberry Pi: Door Sensor Fun](https://medium.com/conectric-networks/playing-with-raspberry-pi-door-sensor-fun-ab89ad499964).
