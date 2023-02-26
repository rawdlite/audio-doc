Welcome To My Ultimate Audio Setup!
====================================

There is of course no ultimate Audio Setup.

I tried quite a lot of setups thinking this is the ultimate solution.
At long last i ended up with a setup, that is stable, convenient and provides what i want.

You are invited to leave a comment in the `issues <https://github.com/rawdlite/audio-doc/issues>`_ section

On my quest i tried quite a few :ref:`distributions`.
In the end i found them lacking functionality, like supporting Qobuz my Streamingservice of choice.
Or in the case of :ref:`moode_dist`  they are so overengineered that neither my udev scripts nor my amp switch works under moode.
Also almost every distribution i came across uses mpd, which is crashing a lot on my extensive collection.

I used :ref:`mopidy` as an alternative to mpd and RompR for a long time.
I even composed a docker environment to create my setup in an instant.
In the end it was a great solution to play my local files, yet there is no way to play Qobuz this way.
I tried to write a plugin, but Qobuz is not giving access to its api.

So i ended up with a minimal :ref:`Setup <ultimate_solution>` based on :ref:`dietpi <dietpi_anchor>`, :ref:`Logitechmedia Server <lms>`,
:ref:`squeezelite`, and :ref:`camilladsp`


In addition i created some custom :ref:`scripts for convenience <projects>`

And then there is my approach to :ref:`organize <beet>` my local files.

Finally i try to document :ref:`hardware`.



.. toctree::
    :maxdepth: 2
    :numbered:
    :glob:
    :caption: Table of Contents
    :hidden:

    Home <self>
    setup.rst
    dietpi.rst
    lms.rst
    camilladsp.rst
    custom
    beets.rst
    distributions.rst
    mopidy.rst
    projects.rst
    hardware.rst
    nfs
    alsa.rst

