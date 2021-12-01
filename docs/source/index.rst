Welcome to Rawdlite's Audio Adventures!
==========================================

**This is a place where i document my journey in the Land of digital Audio**

Emphasis is on issues around network streamers based on Raspberry 4 and other SBCs like the asus Tinkerboard and the Odroid C2.
There are an abundance of ready made solutions one can install via a complette image. Yet sooner or later i find something i want to tinker with and this approach feels to limiting for my taste.

If you enjoy the indepedence of `free software <https://www.fsf.org/>`_, like to know how thinks work and to optimize your listening experience, then this documentation might be for you.

Check out the :doc:`cooperation` section for further information, including
how to comment and cooperate on this project.

.. note::

   This project is under active development.

.. todo::

    - come up with a general structure.
    - elaborate on software setup
        - docker compose
    - elaborate on file maintainance
        - add sample scripts
    - measuring with REW
    - elaborate on DCR and camillaDSP

Structure
#########
All audio listening setups are divided in three parts:

#. the repository aka storage of audio information

#. the controller aka the UI or GUI

#. the renderer aka the player

Not all solutions have such a strict division of components, but integrate some or all of them.

Local Player
_____________

Traditional local player applications like iTunes, foobar, vlc .... have the controller and render part combined in one Applikation.
Repository can be local files or streaming services. While easy to setup and configure you are pretty much restricted to use a single device.

Other Player (Renderer)
-----------------------

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

So far i have not been able to distinguish SQ using any of the aforemetioned methods.
But then i don't claim to have the best ears or equipment.


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