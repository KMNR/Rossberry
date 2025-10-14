# Instructions for setting up the Bob Ross player

## Set up base Raspbian image

Use Raspberry Pi Imager (the official imaging program) to image an SD card as follows:

1. Select **Raspberry Pi OS Lite (64-bit)** as the OS (under Raspberry Pi OS (Other))
1. Select the SD card as the storage, and when prompted to apply a configuration, edit the configuration as follows:
1. Set the hostname to `rossberry` (or otherwise as appropriate)
1. Set the username to `kmnr`, and password as appropriate
1. Set the locale to `en-US` and the time zone to `America/Chicago`
1. On the services tab, enable SSH with password authentication

Burn the image to the SD card and install it in the Pi.

## Configuration

What we've got here is a raspberry pi, and we've just ~~applied a very thin coat of the liquid white to it~~ set it up with a base image.

Power on the pi. It will reboot at least one time - this can take up to 10 minutes. While you do that, I'm going to just have them run all the packages across the screen that you'll need to paint along with us today. Then, perform the following steps:

Log in as `kmnr` with the password set above.

Run the rossberry.sh script, which will take quite some time. If you receive an error about the InRelease file not being valid, wait a minute and try again - the Pi's clock has not yet synchronized.

VLC should start, and you should start seeing some happy little trees! If you don't, that's okay - no mistakes here, just happy accidents! (You're probably using an older pi that doesn't have support for hardware-accelerated decode of some video codecs.) In VLC, navigate to Tools > Preferences > Codecs, and under Hardware Accelerated Decoding, choose "Disabled". Now, use Ctrl+Alt+F1 to switch back to the first virtual console and run `sudo systemctl restart lightdm`.

And I think we just about have a finished rossberry here. So let's grab a bit of our bright red and sign it. All we need is to use Ctrl+Alt+F1 to switch back to the first virtual console, run `sudo reboot` and you should be all set!

So, from all of us here, I'd like to wish you happy painting, and god bless, my friend.
