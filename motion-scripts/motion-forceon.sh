#!/bin/bash
# we need to pass two values to this script 
# $1 would be 1 or 0, to enable/disable notifications
# $2 would be the username we are disabling

CONFPATH=/opt/motion/conf

sed -i "s/^\(FORCEON\s*=\s*\).*$/\1${1}/" ${CONFPATH}/config.${2}
