#!/bin/bash
# This script will create the needed connections for the PiServer

echo "Starting Server Instantiation"

sudo cp interfaces-adhoc /etc/network/interfaces-adhoc

sudo cp /etc/default/ifplugd /etc/default/ifplugd_backup

# Install the isc-dhcp-server
sudo dpkg -i isc-dhcp-server_4.2.2.dfsg.1-5+deb70u8_armhf.deb
sudo apt-get install -f

echo "INTERFACES=\"eth0\"" > /etc/default/ifplugd
echo "HOTPLUG_INTERFACES=\"eth0\"" >> /etc/default/ifplugd
echo "ARGS=\"-q -f -u0 -d10 -w -I\"" >> /etc/default/ifplugd
echo "SUSPEND_ACTION=\"stop\"" >> /etc/default/ifplugd

echo 'Backing up /etc/network/interfaces as /etc/network/interfaces_backup'

cp /etc/network/interfaces /etc/network/interfaces_backup

echo "Starting up new interface"

sudo ifdown wlan0
sudo cp /etc/network/interfaces-adhoc /etc/network/interfaces
sudo ifup wlan0

echo 'Finished Installing Setting up and Installing Server'

read  -n 1 -p "Input Selection:" mainmenuinput