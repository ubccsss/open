import RPi.GPIO as GPIO

class DoorSensor:
    """Manages door sensor IO."""

    def __init__(self):
        # Set Broadcom mode so we can address GPIO pins by number.
        GPIO.setmode(GPIO.BCM)

        # This is the GPIO pin number we have one of the door sensor
        # wires attached to, the other should be attached to a ground
        pin.DOOR_SENSOR_PIN = 18

        # Set up the door sensor pin.
        GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

    def cleanup(self):
        """Clean up when the user exits."""
        GPIO.cleanup()

    def is_open(self):
        """Returns True if the door is currently open."""
        return GPIO.input(DOOR_SENSOR_PIN)
