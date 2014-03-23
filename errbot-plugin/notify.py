from errbot import BotPlugin, botcmd
import subprocess

# I'm not great with python, but the following works for me.
# You need to change the follow values to suit your needs:
# /opt/motion/motion-onoff.sh (Where you store motion-onoff.sh)
# /opt/motion/motion-forceon.sh (Where you store /motion-forceon.sh)
# your-user-1 AND your-user-2 (The username you used on your config file in the motion conf directory)
# your-user-1@public.talk.google.com AND your-user-2@public.talk.google.com

class notify(BotPlugin):
# enable or disable notication during normal time conditions
    @botcmd
    def off(self, mess, args):
        """ usage: off """
        received1 = mess.getFrom().getStripped()
        if received1 == "your-user-1@public.talk.google.com":
		subprocess.call(['/opt/motion/motion-onoff.sh', '0', 'your-user-1'])
        	return 'Notification turned OFF for your-user-1 !'
	elif received1 == "your-user-2@public.talk.google.com":
		subprocess.call(['/opt/motion/motion-onoff.sh', '0', 'your-user-2'])
		return 'Notification turned OFF for your-user-2 !'
        else:
                return 'Who are you?'
    @botcmd
    def on(self, mess, args):
        """ usage: on """
        received1 = mess.getFrom().getStripped()
        if received1 == "your-user-1@public.talk.google.com":
                subprocess.call(['/opt/motion/motion-onoff.sh', '1', 'your-user-1'])
                return 'Notification turned ON for your-user-1 !'
        elif received1 == "your-user-2@public.talk.google.com":
                subprocess.call(['/opt/motion/motion-onoff.sh', '1', 'your-user-2'])
                return 'Notification turned ON for your-user-2 !'
        else:
                return 'Who are you?'


# forced notifications below. by default we don't force
    @botcmd
    def forceoff(self, mess, args):
        """ usage: forceoff """
        received1 = mess.getFrom().getStripped()
        if received1 == "your-user-1@public.talk.google.com":
        	subprocess.call(['/opt/motion/motion-forceon.sh', '0', 'your-user-1'])
        	return 'Forced notification turned OFF for your-user-1 !'
	elif received1 == "your-user-2@public.talk.google.com":
                subprocess.call(['/opt/motion/motion-forceon.sh', '0', 'your-user-2'])
                return 'Forced notification turned OFF for your-user-2 !'
        else:
                return 'Who are you?'
    @botcmd
    def forceon(self, mess, args):
        """ usage: forceon """
        received1 = mess.getFrom().getStripped()
        if received1 == "your-user-1@public.talk.google.com":
                subprocess.call(['/opt/motion/motion-forceon.sh', '1', 'your-user-1'])
                return 'Forced notification turned ON for your-user-1 !'
        elif received1 == "your-user-2@public.talk.google.com":
                subprocess.call(['/opt/motion/motion-forceon.sh', '1', 'your-user-2'])
                return 'Forced notification turned ON for your-user-2 !'
        else:
                return 'Who are you?'

