# Written by Doug McGeehan (djmvfb@mst.edu)
#
# Upon boot, do the following:
# 1. Create a playlist file (.m3u) that contains all video files in randomized 
#    order.
# 2. Auto-start Kodi
#
# This has only been tested on a Raspberry Pi 3 running Raspbian Lite.
# RetroPie was installed on top of Raspbian, and Kodi was installed through
# RetroPie.
# This ought to also work for any OSMC- or OpenELEC-running Raspberry Pi.
#
# For more information, see the following links.
#     http://forum.kodi.tv/showthread.php?tid=157120
#     http://kodi.wiki/view/autoexec.py
#

import xbmc
import os
import random
import time
random.seed(time.time())


PLAYLIST_FILEPATH = "/home/pi/.kodi/userdata/playlists/video/randomized.m3u"
VIDEO_DIRECTORY = "/media/usb"
RECOGNIZED_MEDIA_EXTENSIONS = [
    '.avi',
    '.mkv',
    '.mp4',
]


def create_playlist(at, with_files_in):
    # If the playlist already exists, just exit
    if os.path.exists(at):
        return

    # Verify the directory into which the playlist is stored exists
    playlist_destination_directory = os.path.dirname(at)
    if not os.path.exists(playlist_destination_directory):
        os.makedirs(playlist_destination_directory)

    # Recursively walk through the directory given.
    media_files = []
    for directory, _, filenames in os.walk(with_files_in):
        # Iterate over files in 'directory'
        for f in filenames:
            # Extract the extension from the filename
            _, extension = os.path.splitext(f)
            if extension in RECOGNIZED_MEDIA_EXTENSIONS:
                # The current file is a recognized media file
                absolute_path = os.path.join(directory, f)
                media_files.append(absolute_path)

    # Shuffle the file paths
    random.shuffle(media_files)

    # Write out filepaths to a playlist file
    with open(at, 'w') as playlist_file:
        playlist_file.write('\n'.join(media_files))



create_playlist(at=PLAYLIST_FILEPATH,
                with_files_in=VIDEO_DIRECTORY)

# Let kodi (previously named XBMC) do it's shit
xbmc.executebuiltin("PlayMedia({playlist_filepath})".format(
    playlist_filepath=PLAYLIST_FILEPATH))
xbmc.executebuiltin("PlayerControl(RandomOn)") 
xbmc.executebuiltin("PlayerControl(RepeatAll)")
