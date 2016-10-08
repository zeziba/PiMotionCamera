#!/bin/bash
# /Created By: Charles Engen
# 10/7/2016
# Script reverts settings back to original from ad-hoc mode

echo "Starting Ad-hoc mode"

sudo ifdown wlan0

sudo cp /etc/network/interfaces-adhoc /etc/network/interfaces
sudo cp /etc/default/ifplugd-adhoc /etc/default/ifplugd
sudo cp dhcpd.conf /etc/dhcp/dhcpd.conf
sudo cp isc-dhcp-server /etc/default/isc-dhcp-server

sudo ifup wlan0

sudo /etc/init.d/networking restart
sudo /etc/init.d/isc-dhcp-server restart
sudo service isc-dhcp-server restart


read  -n 1 -p "Input Selection:" mainmenuinput