"""
A sample showing how to make a Python script as an app.
"""

__version__ = "0.0.8"

__copyright__ = "Copyright 2015, Aldebaran Robotics"
__author__ = 'YOURNAME'
__email__ = 'YOUREMAIL@aldebaran.com'

import stk.runner
import stk.events
import stk.services
import stk.logging
import argparse
from naoqi import ALProxy
'''
def main(robot_ip, robot_port, topf_path):
    dialog_p = ALProxy('ALDialog', robot_ip, robot_port)
    dialog_p.setLanguage("English")

    # Load topic - absolute path is required
    topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

    # Start dialog
    dialog_p.subscribe('myModule')

    # Activate dialog
    dialog_p.activateTopic(topic)

    raw_input(u"Press 'Enter' to exit.")

    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe('myModule')
'''

class Activity(object):
    "A sample standalone app, that demonstrates simple Python usage"
    APP_ID = "com.aldebaran.nefach"
    def __init__(self, qiapp):
        self.qiapp = qiapp
        self.events = stk.events.EventHelper(qiapp.session)
        self.s = stk.services.ServiceCache(qiapp.session)
        self.logger = stk.logging.get_logger(qiapp.session, self.APP_ID)

    def on_touched(self, *args):
        "Callback for tablet touched."
        if args:
            self.events.disconnect("ALTabletService.onTouchDown")
            self.logger.info("Tablet touched: " + str(args))
            self.s.ALTextToSpeech.say("Yay!")
            self.stop()

    def on_start(self):
        "Ask to be touched, waits, and exits."
        # Two ways of waiting for events
        # 1) block until it's called
        self.s.ALTextToSpeech.say("Hey Neel You Are Awesome. Touch my forehead.")
        self.logger.warning("Listening for touch...")
        while not self.events.wait_for("FrontTactilTouched"):
            pass

        # 2) explicitly connect a callback
        if self.s.ALTabletService:
            self.events.connect("ALTabletService.onTouchDown", self.on_touched)
            self.s.ALTextToSpeech.say("okay, now touch my tablet.")
            # (this allows to simltaneously speak and watch an event)
        else:
            self.s.ALTextToSpeech.say("touch my tablet ... oh. " + \
                "I don't have one.")
            self.stop()

    def stop(self):
        "Standard way of stopping the application."
        self.qiapp.stop()
        

    def on_stop(self):
        "Cleanup"
        self.logger.info("Application finished.")
        self.events.clear()

if __name__ == "__main__":
    stk.runner.run_activity(Activity)
    
'''  
    parser = argparse.ArgumentParser()
    parser.add_argument("path",
                        type=str,
                        help="Absolute path of the dialog topic file"
                             " (on the robot).")
    parser.add_argument("--ip",
                        type=str,
                        default="10.132.61.99",
                        help="Robot ip address.")
    parser.add_argument("--port",
                        type=int,
                        default=9559,
                        help="Robot port number.")

    args = parser.parse_args()
    main(args.ip, args.port, args.path)
'''