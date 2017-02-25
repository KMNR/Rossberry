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

if __name__ != '__main__':
    import xbmc

import os
import random
import time
import itertools
import pprint
random.seed(time.time())


PLAYLIST_FILEPATH = "/opt/retropie/configs/ports/kodi/userdata/playlists/video/randomized.m3u"
VIDEO_DIRECTORY =        "/media/rossberry/TV"
TRANSITIONS_DIRECTORY =   "/media/rossberry/Transitions"
RECOGNIZED_MEDIA_EXTENSIONS = [
    '.avi',
    '.mkv',
    '.mp4',
]


def create_playlist(at, with_files_in, transitions_in):
    media_files = find_media_files(with_files_in)
    transition_files = find_media_files(transitions_in)

    # Shuffle the file paths
    random.shuffle(media_files)

    # Interweave transition videos between each media file
    playlist = []
    transition_cycle = itertools.cycle(transition_files)
    for path in media_files:
        playlist.append(path)
        playlist.append(next(transition_cycle))

    # print some helpful stuff if this script is called from the command line
    if __name__ == '__main__':
        line_break_fmt = '{bookend}: {title} :{bookend}'
        print(line_break_fmt.format(bookend='='*30,
                                    title='TV'))
        pprint.pprint(media_files)
        print(line_break_fmt.format(bookend='='*30,
                                    title='Transitions'))
        pprint.pprint(transition_files)
        print(line_break_fmt.format(bookend='='*30,
                                    title='Interweaved'))
        pprint.pprint(playlist)

    # Write out filepaths to a playlist file
    with open(at, 'w') as playlist_file:
        playlist_file.write('\n'.join(playlist))


# Recursively walk through the directory given.
def find_media_files(directory):
    media_files = []
    for directory, _, filenames in os.walk(directory):
        # Iterate over files in 'directory'
        for f in filenames:
            # Extract the extension from the filename
            _, extension = os.path.splitext(f)
            if extension in RECOGNIZED_MEDIA_EXTENSIONS:
                # The current file is a recognized media file
                absolute_path = os.path.join(directory, f)
                media_files.append(absolute_path)
    return media_files


create_playlist(at=PLAYLIST_FILEPATH,
                with_files_in=VIDEO_DIRECTORY,
                transitions_in=TRANSITIONS_DIRECTORY)

# Let kodi (previously named XBMC) do it's shit
if __name__ != '__main__':
    xbmc.executebuiltin("PlayMedia({playlist_filepath})".format(
        playlist_filepath=PLAYLIST_FILEPATH))
    xbmc.executebuiltin("PlayerControl(RandomOn)") 
    xbmc.executebuiltin("PlayerControl(RepeatAll)")

