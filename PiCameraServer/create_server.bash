#!/bin/bash
# This script will create the needed connections for the PiServer

echo "Starting Server Instantiation"


echo "auto lo" > /etc/network/interfaces-adhoc
echo "iface lo inet loopback" >> /etc/network/interfaces-adhoc
echo "iface eth0 inet dhcp" >> /etc/network/interfaces-adhoc
echo "\n" >> /etc/network/interfaces-adhoc
echo "auto wlan0" >> /etc/network/interfaces-adhoc
echo "iface wlan0 inet static" >> /etc/network/interfaces-adhoc
echo "  address 192.168.1.1" >> /etc/network/interfaces-adhoc
echo "  netmask 255.255.255.0" >> /etc/network/interfaces-adhoc
echo "  wireless-channel 1" >> /etc/network/interfaces-adhoc
echo "  wireless-essid RPiAdHocNetwork" >> /etc/network/interfaces-adhoc
echo "  wireless-mode ad-hoc" >> /etc/network/interfaces-adhoc

echo 'sudo cp /etc/default/ifplugd /etc/default/ifplugd_backup'

# Install the isc-dhcp-server
echo 'sudo dpkg -i isc-dhcp-server_4.2.2.dfsg.1-5+deb70u8_armhf.deb'
echo 'sudo apt-get install -f'

echo "INTERFACES=\"eth0\"" > /etc/default/ifplugd
echo "HOTPLUG_INTERFACES=\"eth0\"" >> /etc/default/ifplugd
echo "ARGS=\"-q -f -u0 -d10 -w -I\"" >> /etc/default/ifplugd
echo "SUSPEND_ACTION=\"stop\"" >> /etc/default/ifplugd

echo "Backing up /etc/network/interfaces as /etc/network/interfaces_backup"

echo 'sudo cp /etc/network/interfaces /etc/network/interfaces_backup'

echo "Starting up new interface"

echo 'sudo ifdown wlan0'
echo 'sudo cp /etc/network/interfaces-adhoc /etc/network/interfaces'
echo 'sudo ifup wlan0'

echo "Finished Installing Setting up and Installing Server"