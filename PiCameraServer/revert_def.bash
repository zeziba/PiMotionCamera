#!/bin/bash
# /Created By: Charles Engen
# 10/7/2016
# Script reverts settings back to original from ad-hoc mode

echo "Reverting back to regular wifi"

sudo ifdown wlan0

sudo cp /etc/default/ifplugd_backup /etc/default/ifplugd

sudo cp /etc/network/interfaces_backup /etc/network/interfaces

sudo ifup wlan0
