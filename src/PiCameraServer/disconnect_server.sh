#!/usr/bin/env bash
# Written by Charles Engen

# No longer used, keeping for reference

declare mnt_location="/mnt/smbServer"

echo "Starting release of ${mnt_location}"

sudo umount -t auto ${mnt_location}

echo "Server Disconnected from ${mnt_location}"
