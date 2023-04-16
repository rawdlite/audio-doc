.. _ultimate_solution:

#####
Setup
#####

My ultimate solution now consists of theses components:

* `dietpi`_
* `lms`_ aka Logitech Media Server
* Squeezelite as a LMS client
* shairport
* camilladsp
* some :ref:`custom scripts <custom>` for my convenience


1. Install `dietpi <https://dietpi.com/>`_
    See Details `setup dietpi <dietpi>`_

2. Install an LMS Server. You have a couple of options:

    * use a dedicated server
    * use NAS to run a docker container :ref:`lms_on_nas`

.. _squeezelite:

-----------
squeezelite
-----------

3. Install squeezelite as a client

    i recommend dietpi
    .. code::

        sudo dietpi-software

    choose (36) squeezelite

    /lib/systemd/system/squeezelite.service should look like
    .. code::
        [Unit]
        Description=Squeezelite (DietPi)
        Documentation=man:squeezelite(1) https://ralph-irving.github.io/squeezelite.html
        After=sound.target

        [Service]
        User=squeezelite
        EnvironmentFile=/etc/default/squeezelite
        ExecStart=/usr/bin/squeezelite $ARGS

        [Install]
        WantedBy=multi-user.target

    edit /etc/default/squeezelite
    .. code::

        ARGS='-W -C 5 -n DietPi3 -s 192.168.1.4 -o hw:CARD=Loopback,DEV=0 -r 48000-48000 -R hLE:::28'

    parameters:
    .. code::

        -C 5 close audio device after 5 seconds when idle. Needed for the autoswitch of the amps.
        -n DietPi3 Name of the client
        -s LMS Server Address
        -o Sounddevice (check with aplay -L)
        -r <minrate>-<maxrate> needed to give camilladsp a fixed rate
        -R Recipe for resampling


    test your parameters with speaker-test:
    .. code::

        speaker-test -D plughw:CARD=DAC54695303,DEV=0 -c 2 -t wav

    make sure your audio group is populated by squeezelite
    .. code::

        audio:x:29:squeezelite,dietpi,shairport-sync

    Now start/restart the squeezelite service and check that the client appears on the LMS Server.

.. _shairplay:

-----------
shairplay
-----------

4. Install shairplay

    in /usr/local/etc/shairport-sync.conf edit the alsa section
    output_device = "hw:Loopback for camilla
    output_rate = 44100;

5. `Install camilladsp <camilladsp>`_

6. Whats more

    organising Files with :ref:`beets`

    * Local Storage
    * NAS -> :doc:`nfs`