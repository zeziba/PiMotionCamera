#!/usr/bin/env bash
# /Created By: Charles Engen
# 11/4/2016
# Connects the Pi to the PINAS server to store images

declare dir_loc
delcare network_name="RPINAS"
declare default_mnt="/mnt/smbServer"


if [ -d "/mnt/smbServer" ] ; then
    echo "$1 Exists: Starting connection"
else
    echo "$1 does not Exist: Creating directory, setting permissions"
    echo sudo mkdir ${default_mnt}
    echo sudo chmod 1777 ${default_mnt}
fi

echo dir_loc=$(nmblookup ${network_name} | grep -Pom 1 '[0-9.]{7,15}')

echo mount -t cifs -o username=root,password=pi //${dir_loc}/data ${default_mnt} || echo "Failed to connect"



