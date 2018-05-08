__version__ = "0.0.1"
__python_version__ ="2.7 x86"

__copyright__ = "Copyright 2018, St. John's University"
__author__ = 'Neelesh Rastogi'
__email__ = 'neelesh.rastogi15@stjohns.edu'

import stk.runner
import stk.events
import stk.services
import stk.logging
import argparse
from naoqi import ALProxy

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
            self.s.ALTextToSpeech.say("Yay!");

            self.s.ALTextToSpeech.say("I am still being coded, So far in NeFaCh Module thats all i can do.")
            self.s.ALTextToSpeech.say("But if you wish to learn more about me please contact Neel.")
            self.stop()

    def nefach(topf_path):
        dialog_p = ALProxy('ALDialog', "10.132.61.99", "9559")
        dialog_p.setLanguage("English")

        # Load topic - absolute path is required
        topf_path = topf_path.decode('utf-8')
        topic = dialog_p.loadTopic(topf_path.encode('utf-8'))
        # Start dialog
        dialog_p.subscribe('nefach_module')
        # Activate dialog
        dialog_p.activateTopic(topic)

        raw_input(u"Press 'Enter' to exit.")

        # Deactivate topic
        dialog_p.deactivateTopic(topic)
        # Unload topic
        dialog_p.unloadTopic(topic)
        # Stop dialog
        dialog_p.unsubscribe('nefach_module')

    def on_start(self):
        "Ask to be touched, waits, and exits."
        # Two ways of waiting for events
        # 1) block until it's called
        self.s.ALTextToSpeech.say("Hello Class, Hope you are doing good. For this, I need a Volunteer. As a Test, Touch my forehead.")
        self.logger.warning("Listening for touch...")
        while not self.events.wait_for("FrontTactilTouched"):
            pass

        #NeFaCh Call to TOpic File and execute.
            nefach("C:\Users\invis\Documents\Github\NeFaCh-Module\nefach\app\scripts\Introduction.top")

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