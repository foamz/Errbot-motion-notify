#!/bin/bash
# This script alerts you via Gtalk/Jabber when motion is detected.
# You can put this script next to "on_event_start" in your motion.conf file

# We grab the config for each user that can be notified
CONFIGPATH=/opt/motion/conf/*

# Path to your sendxmpprc file. Must be owned by Motion
SENDXMPPCONF=/etc/sendxmpprc.motion

# Define the message you want to send
ALERTMSG="ALERT: Motion detected in the house"
DATE=`date`


# Don't modify anything below, unless you know what you are doing
TIME=$(date +%k%M)
TODAY=$(date +%a)

for CONFIG in ${CONFIGPATH}
do
  source ${CONFIG}
  if [ ${FORCEON} == "1" ]; then
    echo "${ALERTMSG} - ${DATE}" |sendxmpp -f ${SENDXMPPCONF} --tls ${EMAIL}
    echo "{$DATE} - ${ALERTMSG}. Notified ${EMAIL}" >> /var/log/motion-custom.log
  else
    for i in ${DAYOFWEEK[@]}
    do
       if [[ "${TIME}" -ge ${FROMTIME} ]] && [[ "${TIME}" -le ${TOTIME} ]] && [[ "${TODAY}" == "$i" ]] && [[ "${ONOFF}" == "1" ]]; then
         echo "${ALERTMSG} - ${DATE}" |sendxmpp -f ${SENDXMPPCONF} --tls ${EMAIL}
         echo "{$DATE} - ${ALERTMSG}. Notified ${EMAIL}" >> /var/log/motion-custom.log
       else
         echo "Not allowed to notify now"
       fi
    done
  fi
done

