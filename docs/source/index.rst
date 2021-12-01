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

    come up with a general structure.

Structure
#########
All audio listening setups are divided in three parts:

#. the repository aka storage of audio information

#. the controller aka the UI or GUI

#. the renderer aka the player

Not all solutions have such a strict division of components, but integrate some or all of them.

Local Player
_____________

local player like iTunes, foobar, vlc .... have the controller and render in one Applikation.
Repository van be local files or streaming services.

Other Player (Renderer)
-----------------------

* mpd
* mopidy

Alsa
____
I prefer my audio renderer on linux to use alsa and have it connect to my :doc:`hardware`

* Alsa -> Soundcard (internal)
My first Media Server had a `M-Audio Audiophile 2496 <http://ixbtlabs.com/articles/maudioaudiophile/index.html>`_ and then `Infrasonic Quartet <http://ixbtlabs.com/articles2/proaudio/infrasonic-quartet.htmlin>`_ a huge X86 Silent PC Setup.
I did my first steps with Jack and REW, but found the Cards to overly complex.
As the next mainboard did not have a PCI slot, the card had to be retired.

* Alsa -> i2S Transport
I have 2 Raspberry 4 with the Allo Digione Transport.
So far i have not been able to distinguish SQ using an i2s connection vs a USB connected DAC.

* Alsa -> i2S DAC
I have 2 Odroid C2 with Hifi Shield DAC. I quite prefer the Odroid over the raspberry, yet there is way more
accessories, software and distributions available for the raspi.

* Alsa -> USB DAC
* Alsa -> HDMI


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