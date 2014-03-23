Errbot-motion-notify
====================

Errbot plugin and bash scripts to notify when Motion detects activity

This collection of bash scripts and Errbot plugins, allows you to receive Gtalk/Jabber notifications when Motion detects... uhm, motion.
The Errbot plugin allows you to interact with the bash scripts, allowing you to turn notifications on and off.

Apps used:
* sendxmpp
* motion
* errbot

The low-down:
=============

* Copy sendxmpprc.motion somewhere appropriately, eg /etc/sendxmpprc.motion
* Make sure motion owns this file, chown motion. /etc/sendxmpprc.motion

* Copy the motion scripts somewhere, eg /opt/motion
* Make sure motion owns these files as well, chown -R motion. /opt/motion
* Create your config files for each user that will be notified in conf/config.*
* Change the values of your config.* file to fit your needs
* Go through motion-onoff.sh, motion-forceon.sh and on-motion-alert.sh to change the values relevant to you.

* Go through notify.py (errbot plugin) and modify the relevant values to fit your needs.

* Now you can fire up motion and errbot, you should be receiving messages from motion via sendxmpp and you can disable/enable it via errbot.


If you have any ideas to improve the plugin or bash scripts, feel free to share your thoughts.


Thanks:
=======
Nick Groenen for helping me out on the Errbot community page

