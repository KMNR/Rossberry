# Rossberry
Instructions and scripts to set up a Bob Ross auto-playing Raspberry Pi.

# Instructions
1. Install Raspbian lite image:
   https://www.raspberrypi.org/documentation/installation/installing-images/linux.md
2. Update raspi-config script,
          set locale to US/English/UTF-8,
          hostname to 'rossberry',
          enable SSH support,
          correct HDMI with overscan correction:  
   $ sudo raspi-config
3. Reboot.
4. Change password from default ('raspberry') to something secure.  
   $ passwd  
   *Important!* Change password only after changing locale / keyboard layout and rebooting!
5. You can now login through ssh instead of being locked in front of the TV
   with a keyboard in your lap.
6. Change ssh port to 22222  
   $ sudo nano /etc/ssh/sshd_conf
7. Reboot
8. $ ssh -p 22222 pi@rossberry
9. $ sudo apt-get update && sudo apt-get tmux
10. $ tmux
11. $ sudo apt-get dist-upgrade -y
12. Eat a snack or something.
13. Install RetroPie:  
    https://github.com/retropie/retropie-setup/wiki/Manual-Installation
14. Install Kodi:  
    https://github.com/retropie/retropie-setup/wiki/KODI
15. Set Kodi to start on boot - configurable through RetroPie.
16. Reboot.
17. Plug in USB drive containing Bob Ross.
18. Set to auto-mount:  
    $ sudo mkdir /media/usb  
    $ sudo su  
    # echo "UUID=WHATEVER_YOUR_DRIVE_UUID_IS /media/usb vfat defaults,ro 0 0" >> /etc/fstab  
    # reboot
19. Import media library into Kodi.
20. Copy 'autoexec.py' into '/home/pi/.kodi/userdata/'
21. Reboot.
22. Confirm Bob Ross plays upon bootup. If not, figure it out for yourself.

