.. lms:

***
LMS
***

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

Reasons to use LMS
__________________
* Supports Qobuz

* Setup on a central Server

* Runs on the NAS -> No nfs shares needed

* Supports UPnP Renderer -> i can control my other ref:players

* An abundance of plugins.

* Qobuz, Spotify, Deezer, Tidal

* Native Controller Apps for many platforms

.. _lms_on_nas:

LMS on Synology
---------------

Since the audio files reside on the NAS it makes sense to run the LMS on the NAS.
This is not supported by Synology by an App any longer. So its docker to the rescue.
The difficulties of getting docker installed depend on the NAS model used.
I was successful downloading a paket direct from the synology repository and doing a manual upload. YMMV
The setup in the synology docker app did not quite work for me, so i set it up via ssh.
Create a docker-compose.yml file in /volume1/docker/lms/:

.. code-block:: yaml

    version: '3'
    services:
      lms:
        container_name: lms
        network_mode: host
        image: lmscommunity/logitechmediaserver
        volumes:
          - /volume1/docker/lms/config:/config:rw
          - /volume1/music/music_data:/music:ro
          - /volume1/docker/lms/playlist:/playlist:rw
          - /etc/localtime:/etc/localtime:ro
          - /etc/TZ:/etc/timezone:ro
        environment:
          - PUID=1026
          - PGID=100
        restart: always

Note: /volume1/music/music_data needs to be adapted of course.
Important is to set the User and Group ID correctly or local media can not be accessed.

Run

.. code::

    docker-compose up -d and enjoy

One has to understand that with LMS the server looks for client and the connection is controlled by the server.
So next we go on the servers Webpage  http://<NAS IP>:9000 and select our player.

On the `Evo Sabre`_ the second Display now kept complaining 'No Player connected'.
The display is driven by /home/dietpi/oled...
In that script the IP of our NAS has to be inserted instead of localhost.

