from pic import PiCamera
import pigpio
from datetime import datetime
camera = PiCamera()
def capture():
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi%s.jpg' % timestamp)
capture()