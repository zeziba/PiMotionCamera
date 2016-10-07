#!/bin/bash
# /Created By: Charles Engen
# 10/7/2016
# Script reverts settings back to original from ad-hoc mode

echo "Reverting back to regular wifi"

sudo ifdown wlan0

if [! -f /etc/network/ifplugd-adhoc]; then
    sudo cp /etc/default/ifplugd /etc/default/ifplugd-adhoc
fi

sudo cp /etc/default/ifplugd_backup /etc/default/ifplugd

sudo cp /etc/network/interfaces_backup /etc/network/interfaces

sudo ifup wlan0
