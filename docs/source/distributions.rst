Distributions
-------------

I have tested a couple of distributions. With the `Evo Sabre <https://www.audiophonics.fr/en/network-audio-players-raspdac/audiophonics-evo-sabre-pack-diy-balanced-dac-2xes9038q2m-streamer-for-raspberry-pi-4-p-14639.html>`_ i am limited to the audiophonics distributions of
volumio, moode and lms until i find out how to install the oled code on a fresh install.
The following is my _personal_ take on the distributions i tried so far.

Raudio 1
--------------

`Raudio 1 <https://github.com/rern/rAudio-1>`_ is a successor to runeaudio.
It is based on arch linux. Technology stack is php and bash scripts.
Setup and operation was smooth. Library import of a large Audiocollection (400GB+) took several hours, yet it succeeded without crashing.

Plus
____

* Tageditor

Minus
_____

* Functionality is somewhoat limited.

* No DSP

* Streaming Services via Airplay/UPnP only

Verdict
_______

I liked the distributions. Recommended for a troublefree experience. Should be possible to add CamillaDSP.
Probably would have done some tinkering if the `Evo Sabre`_ was supported. Replacing mpd for mopidy and its plugins seems promising.

Volumio
-------

`Volumio <https://github.com/volumio?tab=repositories>`_ is based on debian linux.
Technology stack is nodejs. Underneath the typical components mpd, shairplay, upnpmpdcli.
Setup and operation was smooth. Library import of a large Audiocollection (400GB+) repeatedly crashed mpd.
Restart of mpd service or reboot was requiered.

Plus
____

* Qobuz Support

* Interface for reporting stack traces.

Minus
_____

* not very stable (Volumio 2, Volumio 3 Beta) this might change with newer versions. Also it might be my personal setup.

* commercial

Verdict
_______

Volumio is a very popular distribution and rightly so. There are a couple of things i personaly dislike though.
Nodejs is not a favourite of mine. Volumio some what seems to try to become the poor mans ROON.
There is a lot of 'audiophile' chatter. Like the importance of expensive USB-Cables and hearing diffrences in the high frequencies after upgrading the OS-Versions.
The latter of course is not a problem of volumio per se but gets more encouraged as with other distributions.

MoOde
-----

`MoOde`_ shares a common ancestry with Volumio. Technology stack is php and jquery.
I have so far given MoOde only a brief spin. It failed to even attempt to import my nfs share.
No error message in the GUI. I did not investigate further since there are so many alternatives.
I liked the EQ section, although it felt a bit to loosely integrated with a extra section for CamillaDSP in parallel to
EQ and PEQ sections. But then i have spent too little time with Moode to come up with an evaluation.

LMS
---

`Logitech Media Server <https://en.wikipedia.org/wiki/Logitech_Media_Server>` is a community software project that started as a commercial hardware enterprise.
There are a plethora of ways to install LMS. I used the `dietpi`_ based `Evo Sabre DAC Image <https://www.audiophonics.fr/en/blog-diy-audio/23-start-up-evo-raspdac-rasptouch-raspdac-mini-with-a-pre-configured-image.html>`_
provided by Audiphonics. There are some peculiarities like the Wlan Modul being disabled on first boot.
This could be fixed by editing the dietpi.txt file. Apart from the Evo Sabre Drivers it is a generic `dietpi`_ setup.
The setup consist of two services.

* Logitech Media Server

* Squeezelite Player

The services are preinstalled and work out of the box. The Evo Sabre Display shows the player status.
When the player is connected to a LMServer it shows the servers IP which conveniently is also the IP you need to ssh into dietpi.
I moved the LMS to a Synology NAS where my audio files reside. So only the squeezelite player is needed on the raspberry pi.
Instructions on how to do that are here ref:`LMS on Synology`.

Plus
____

* Supports my Evo Sabre

* Runs on the NAS -> No nfs shares needed

* Supports UPnP Renderer -> i can control my other ref:players

* An abundance of plugins.

* Qobuz, Spotify, Deezer, Tidal

* Native Controller Apps for many platforms

Minus
_____

* There are nicer GUIs out there.

* proprietary protocol

Verdict
_______

So far the best solution for my `Evo Sabre Streamer`_.
Unfortunately my scripts that are based on mpc will not work.
Hmm, maybe running mopidy alongside and a `alsa dmix <https://alsa.opensrc.org/Dmix>`_ configuration?
At the moment i am very happy with the solution. It uses very little resources
on the pi which allows for other applications to be run in parallel like DSP.
Convenient and the most feature rich solution i have come accross so far.


LMS on Synology
---------------

Since the audio files reside on the NAS it makes sense to run the LMS on the NAS.
This is not supported by Synology by an App any longer. So its docker to the rescue.
The difficulties of getting docker installed depend on the NAS model used.
I was successful downloading a paket direct from the synology repository and doing a manual upload. YMMV
The setup in the synology docker app did not work for me, so i set it up via ssh.
Create a docker-compose.yml file in /volume1/docker/lms/:

.. code-block:: yaml

    version: '3'
    services:
      lms:
        container_name: lms
        image: lmscommunity/logitechmediaserver
        volumes:
          - /volume1/docker/lms/config:/config:rw
          - /volume1/music/music_data:/music:ro
          - /volume1/docker/lms/playlist:/playlist:rw
          - /etc/localtime:/etc/localtime:ro
          - /etc/TZ:/etc/timezone:ro
        ports:
          - 9999:9999/tcp
          - 9090:9090/tcp
          - 3483:3483/tcp
          - 3483:3483/udp
        environment:
          - HTTP_PORT=9999
          - PUID=1026
          - PGID=100
        restart: always

Note: /volume1/music/music_data needs to be adapted of course.
Important is to set the User and Group ID correctly or local media can not be accessed.

Run docker-compose up -d and enjoy



