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
            self.s.ALTextToSpeech.say("Yay!")
            self.s.ALTextToSpeech.say("I am still being coded. So far, I can just have basic communication. But, some updates are on the way.")
            self.s.ALTextToSpeech.say("In the mean while, let me tell you something about my project which, me and Neel, have been working on. We call it NeFaCh Module")
            self.s.ALTextToSpeech.say("In this project, we are introducing an unique dialogue system platform to assist human in establishing, a non-abrupt communication with a social-robot, like ME!, especially, in Health-care environment.")
            self.s.ALTextToSpeech.say("Today if we see Communication  with social-robot is still in early stage and research. Therefore, Our team including me, believe, having proper communication is essential in HRI systems, so that we can allow users to communicate, and, automate tasks just using natural language without frustration and stress.")
            self.s.ALTextToSpeech.say("When we see the historic research in my field, we found that having Natural Language Communication, non-abruptly, for specific task and domain is a challenging one to accomplish.")
            self.s.ALTextToSpeech.say("One of the major issues we find is that, no matter how intelligent machines like me might be, sometimes humans end up experiencing frustration in communication with robots.")
            self.s.ALTextToSpeech.say("Therefore, To overcome this issue, me and my team, we aim to develop an entirely open-source, long-term supported, chat module with a proper lexicon, for HRI systems focused primarly in Health-care environment. This will require us to investigate perceptive, emotive, and spoken skills, when it comes to conversations")
            self.s.ALTextToSpeech.say("Our dialog system will involve me to engage into communication with humans, resulting in a non-abrupt conversation, and, as a result our team will be proposing a new pseudo conversational architecture for the Human-Robot Dialog System.")
            self.s.ALTextToSpeech.say("But, apart from all, If you wish to learn more about my Project, Please Contact Neel, or, Prof. Fazel.")
            self.s.ALTextToSpeech.say("In the mean time let me connect to Skynet, and take over the world! Connecting now, 3..., 2..., 1... LOL, just kidding! Please feel free to have communication with me, after, Neel's Presentation.")
            self.s.ALTextToSpeech.say("I wish you all, Best of Luck! See you on the other side!")
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
        self.s.ALTextToSpeech.say("Hello Class and Prof. Fazel, Hope your finals are going good!. To commence, for this, I need a Volunteer. As an Awareness Test, Please touch my forehead.")
        self.logger.warning("Listening for touch...")
        while not self.events.wait_for("FrontTactilTouched"):
            pass

        #NeFaCh Call to Topic File and execute.
            #nefach("C:\Users\invis\Documents\Github\NeFaCh-Module\nefach\app\scripts\Introduction.top")

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