Welcome to Rawdlite's Audio Adventures!
==========================================

**This is a place where i document my journey in the Land of digital Audio**

This is an attempt to sort out the various aspects of computer based audio that i am interested in
and done in the hope that it might be useful to others.
Emphasis is on issues around network streamers based on Raspberry 4 and other SBCs like the asus Tinkerboard and the Odroid C2.
There is a strong preference on solutions based on linux and  `free software <https://www.fsf.org/>`_
Check out the :doc:`cooperation` section for further information, including
how to comment and cooperate on this project.

.. note::

   This project is in its infancy and under active development.

.. todo::

    - come up with a general structure.
    - elaborate on software setup
        - docker compose
    - elaborate on file maintainance
        - beets
        - add sample scripts
    - measuring with REW
    - elaborate on DCR and camillaDSP

General Overview
################
All audio listening setups can be divided in three parts:

#. the controller aka the UI or GUI ->

#. the renderer aka the player ->

#. the repository aka storage of audio information ->

Usecases
########

i find it useful to differentiate between the various situations of music listening.

#. `Nearfield`_
Sitting at a desk in front of a screen and listening to nearfield monitors.
AKA work.

#. `Midfield`_ and Farfield
Pretty much anything else.

Implementations
###############

there are different implementations

#. Single Apps
itunes, bubbleupnp ->

#. `Distributions`_

#. `Free Setups`_


Nearfield
---------
image:: pics/desktop.png
  :width: 400
  :alt: Nearfield Listening

In Nearfield listening there is little advantage in using a SBC based network streamer.
I have my Mac Book connected to my DAC (RME ADI-2 via USB) that is connected to a pair of active Nearfield
Monitors (Genelec 8030 via XLR)
I listen to Spotify, Qobuz and Youtube Music using the native Apps.
Local Files are mounted from the NAS and played by itunes or vlc.
Not missing anything so far.

Midfield
--------


Distributions
-------------
Distributions are an approach to make linux based network streamers accessible to a broader audience.
This is achieved by providing a OS Image that can be written (flashed) to a sd card.
When the sd-card is inserted into a SBC (mostly Raspberry) a GUI guides through the setup process.
The GUI is web based and can be accessed via various devices.
The underlying components are mostly the same across the various distributions.
mpd ->, upmpdcli -> , spotifyd -> etc.

#. volumio
debian

#. raudio (runeaudio)
arch

#. moOde

The convenience of distributions come at a price.
They are hard to maintain. see pimusicbox ->
They are locked to a specific OS by a specific version.
Upgrading to a newer OS Version is a major effort.
To manage this workload ost distributions are limited to the most prominent SBC platform, the raspberry pi.
While the raspberry is a great device, it is not the best platform for audio.
The raspberries shortcomings in the audio domain require additional hardware.
DACs ->, Audio HATs ->

Free Setups
-----------
A 'free setup' is trading convenience for flexibility.
Choose a platform (PC, Mac, Tinkerboard, Odroid ...)
Choose a OS supported by the platform.
Choose best of breed components.
Use the commandline.

#. Setup base system
#. Install components
#. Configuration

Controller UI
-------------

Local Player
_____________
Not all solutions have such a strict seaparation of components, but integrate some or all of them.
Traditional local player applications like iTunes, foobar, vlc .... have the controller and render part combined in one Applikation.
Repository can be local files or streaming services. While easy to setup and configure you are pretty much restricted to use a single device.

Streaming Services
___________________

i regularly use these streaming services

* Spotify

* Qobuz

I like the editorial content of Qobuz as much as the presence of High Res audio.
These streaming services can be seen as a remote :ref:repository_ with a GUI as a native Application for iOs, Android
which are probably the most popular usecases.
Alternative Interfaces provided by volumio or mopidy require access to the streaming services
APIs. This proves to be not an easy task.


Network Player (Renderer)
-------------------------

* mpd
* mopidy

Alsa
____
I prefer my audio renderer on linux to use alsa and have it connect to my :doc:`hardware`.
It is easy to configure alsa for bitperfect transport. This means there is no software volume control.
There are quite a few ways to connect the alsa daemon.

* Alsa -> Soundcard (internal)
My first Media Server had a `M-Audio Audiophile 2496 <http://ixbtlabs.com/articles/maudioaudiophile/index.html>`_ and then `Infrasonic Quartet <http://ixbtlabs.com/articles2/proaudio/infrasonic-quartet.htmlin>`_ a huge X86 Silent PC Setup.
I did my first steps with Jack and REW, but found the Cards to overly complex.
As the next mainboard did not have a PCI slot, the card had to be retired
and the era of internal soundcards had come to an end.

* Alsa -> i2S DAC
I have 2 Odroid C2 with Hifi Shield DAC. I quite prefer the Odroid over the raspberry, yet there is way more
accessories, software and distributions available for the raspi.
In theory i2s is the superior connection over usb on the other hand the dac implementathe on the small sized dac hats is probably more of a limiting factor here.
In the end the odroids are used in secondary chains that are not so demanding and the compact form factor is a big advantage.

* Alsa -> USB DAC
The Adama Artist 5 that i own have an usb connection to their internal DAC.
And then there is the :ref:`RME ADI-2 FS` Dac and the :ref:`Citypulse DA 3.2` Headphone Amp that can also be connected via usb.
Especially with the RME Dac SQ is outstanding, whether connected via USB or S/PDIF.
The biggest advantage of usb is the flexibilty it provides. On the downside alsa might lose the connection when the usb device does a power cycle.

* Alsa -> i2S Transport
I have 2 Raspberry 4 with the `Allo Digione <https://www.audiosciencereview.com/forum/index.php?threads/review-and-measurements-of-allo-digione-rpi-s-pdif.5418/>`_ Transport.
This Raspberry i2s HAT provides a S/PDIF Out only.
The S/PDIF (or AES/EBU) can then be connected to a DAC or AVR.
This pretty much combines the advantages of the two former connections.
Alsa sees a device independently from the power status of the usb device and aqt the same time gives a lot of flexibility on devices to connect with.

* Alsa -> HDMI
With a given AVR connecting via HDMI is an easy option to get digital audio from your SBC.
Identifying the correct HDMI device for alsa might involve a bit of try and error.
While this is a convenient connection it might be not be best for `Sound Quality <https://www.audiosciencereview.com/forum/index.php?threads/a-deep-dive-into-hdmi-audio-performance.56/>`_


Repository
----------

What to play.

Files
_____

    organising Files with :ref:`beets`

    * Local Storage
    * NAS -> :doc:`nfs`

Streaming Services:
___________________
    Spotify

        * Spotify connect -> AVR

        * Spotify connect -> volumio

        * Spotify connect -> raspotify

        * Bubbleupnp -> Spotify

        * AVR -> Spotify

        * Rompr -> mopidy -> Spotify

        * Volumio -> Spotify

    Qobuz

        * Qobuz -> Bubbleupnp

        * Bubbleupnp -> Qobuz

    *Youtube Music*
        * todo: explore




Chains
------
* Odroid C2 - Hifi Shield -> AVR2 -> LS1
* Raspi4 -> AVR1 -> Zone1: LS2, Zone2: LS4
* Odroid C2 -> LS3

Chain Links
-----------








.. toctree::
    :maxdepth: 2
    :numbered:
    :titlesonly:
    :glob:
    :hidden:

    nfs.rst
    cooperation.rst
    hardware.rst