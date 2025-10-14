#!/bin/bash

set -euo pipefail

sudo -v

sudo apt update && sudo apt upgrade

# Remove some packages that we don't need - these sometimes cause trouble.
sudo apt purge bluez wpasupplicant modemmanager triggerhappy && sudo apt autoremove

# Install new packages for a very minimal kiosk environment.

sudo apt install --no-install-recommends xserver-xorg matchbox-window-manager lightdm overlayroot vlc ffmpeg cifs-utils

# Edit the lightdm configuration to enable auto login
sed -i 's/#autologin-user=/autologin-user='"$USER"'/' /etc/lightdm/lightdm.conf

# set up xsession config
echo << EOF > ~/.xsession
xset s off
xset -dpms

exec matchbox-window-manager -use_titlebar no &

while true
do
  vlc -Z -L -f --no-osd "/mnt/digilib/Bob Ross"
done
EOF

# Because we're adding a graphical environment, we need to change the default target
sudo systemctl set-default graphical.target

# Enable overlayroot
sudo sed -i 's/overlayroot=.*/overlayroot="tmpfs"/' /etc/overlayroot.conf

# Mount the SMB share
sudo systemctl daemon-reload
sudo mount -a

sudo systemctl enable --now lightdm.service
