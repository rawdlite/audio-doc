Welcome To The Ultimate Audio Setup!
====================================

There is of cause no ultimate Audio Setup.

I tried quite a lot of setups thinking this is the ultimate solution.
At long last i ended up with a setup, that is stable, convenient and provides what i want.

You are invited to leave a comment in the `issues <https://github.com/rawdlite/audio-doc/issues>`_ section

On my quest i tried quite a few :ref:`distributions`.
In the end i found them lacking functionality, like supporting Qobuz my Streamingservice of choice.
Or in the case of :ref:`moode`  they are so overengineered that neither my udev scripts nor my amp switch works under moode.
Also almost every distribution i came across uses mpd, which is crashing a lot on my extensive collection.

I used :ref:`mopidy` as an alternative to mpd and RompR for a long time.
I even composed a docker environment to create my setup in an instant.
In the end it was a great solution to play my local files, yet there is no way to play Qobuz this way.
I tried to write a plugin, but Qobuz is not giving access to its api.

.. _ultimate_solution:

My ultimate solution now consists of theses components:

* :ref:`dietpi`
* :ref:`lms` aka Logitech Media Server
* Squeezelite as a LMS client
* shairport
* camilladsp
* some :ref:`custom scripts <custom>` for my convenience


1. Install `dietpi <https://dietpi.com/>`_
    See Details :ref:`dietpi`

2. Install an LMS Server. You have a couple of options:

    * use a dedicated server
    * use NAS to run a docker container :ref:`lms_on_nas'

3. Install squeezelite as a client

    i recommend dietpi
    .. code::

        sudo dietpi-software

    edit /etc/default/squeezelite
    .. code::

        ARGS='-W -C 5 -n DietPi3 -s 192.168.1.4 -o hw:CARD=Loopback,DEV=0 -r 48000-48000 -R hLE:::28'

    make sure your audio group is populated by squeezelite
    .. code::

        audio:x:29:squeezelite,dietpi,shairport-sync

    Now start/restart the squuzelite service and check that the clent appears on the LMS Server.

4. Install shairplay
in /usr/local/etc/shairport-sync.conf edit the alsa section
output_device = "hw:Loopback for camilla
output_rate = 44100;

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

.. todo::

    - elaborate on file maintainance
        - beets
        - add sample scripts


.. toctree::
    :maxdepth: 2
    :numbered:
    :titlesonly:
    :glob:
    :hidden:

    cooperation.rst
    dietpi.rst
    lms.rst
    camiladsp.rst
    projects.rst
    hardware.rst
    mopidy.rst
    distributions.rst
