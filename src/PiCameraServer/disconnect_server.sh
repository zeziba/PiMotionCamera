#!/usr/bin/env bash
# Written by Charles Engen

declare mnt_location="/mnt/smbServer"

echo "Starting release of ${mnt_location}"

sudo umount -t auto ${mnt_location}

echo "Server Disconnected from ${mnt_location}"
