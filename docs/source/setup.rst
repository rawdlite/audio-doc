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

5. `Install camilladsp <camilladsp>`_

6. Whats more

    organising Files with :ref:`beets`

    * Local Storage
    * NAS -> :doc:`nfs`