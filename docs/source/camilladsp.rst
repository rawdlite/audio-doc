**********
CamillaDSP
**********


Install camillagui
__________________

.. code-block::

    wget https://github.com/HEnquist/camillagui-backend/releases/download/v1.0.1/camillagui.zip -P ~/camilladsp
    unzip ~/camilladsp/camillagui.zip -d ~/camilladsp/camillagui
    sudo apt-get install python3-setuptools git python3 python3-pip python3-websocket python3-aiohttp python3-jsonschema python3-numpy python3-matplotlib unzip
    python3 -m pip install --upgrade jsonschema
    sudo python3 -m pip install git+https://github.com/HEnquist/pycamilladsp.git
    sudo python3 -m pip install git+https://github.com/HEnquist/pycamilladsp-plot.git
    vim ~/camilladsp/camillagui/config/camillagui.yml


.. code::

    camilla_host: "192.168.0.100"

    update_config_symlink: true

======== Running on http://0.0.0.0:5000 ========
(Press CTRL+C to quit)

install camilladsp
__________________

Get camilladsp-linux-armv7.tar.gz

.. code-block::

    wget https://github.com/HEnquist/camilladsp/releases/download/v1.0.3/camilladsp-linux-armv7.tar.gz

Unpack

.. code-block::

    xzf camilladsp-linux-armv7.tar.gz
    mv camilladsp /usr/local/bin/


How to continue
_______________

There are two ways to install camilladsp:

1) Loopback Device
2) Alsa Plugin

Loopback Device
_______________

.. code-block::

    sudo apt install linux-modules-extra-raspi
    sudo vim /etc/modules-load.d/snd-aloop.conf

add
.. code::

    snd-aloop

reboot

.. code::

    aplay -L

Output
.. code::

    hw:CARD=Loopback,DEV=0
        Loopback, Loopback PCM
        Direct hardware device without any conversions
    hw:CARD=Loopback,DEV=1
        Loopback, Loopback PCM
        Direct hardware device without any conversions

.. code::

    arecord -L

Output:
.. code::

    hw:CARD=Loopback,DEV=0
        Loopback, Loopback PCM
        Direct hardware device without any conversions
    hw:CARD=Loopback,DEV=1
        Loopback, Loopback PCM
        Direct hardware device without any conversions






Install CamillaDSP Alsa Plugin
______________________________

.. code-block::

    git clone https://github.com/scripple/alsa_cdsp.git
    cd alsa_cdsp/
    apt install libasound2-dev build-essential
    make
    make install
    mv /alsa-lib/ /usr/lib/arm-linux-gnueabihf/
    cat asound.conf >> /etc/asound.conf
    mkdir /opt/camilladsp
    cp config_in.yaml /opt/camilladsp

edit /etc/asound.conf

.. code::

    cpath "/usr/loal/bin/camilladsp"
    config_out "/opt/camilladsp/config_out.yaml"
    config_in "/opt/camilladsp/config_in.yaml"

edit /opt/camilladsp/config_out.yaml

.. code::

    devices:
      samplerate: 44100
      chunksize: 1024
      queuelimit: 1
      capture:
        type: File
        channels: 2
        filename: "/dev/stdin"
        format: S16LE
        extra_samples: 8192
      playback:
        type: Alsa
        channels: 2
        device: "hw:CARD=OnBoard,DEV=2"
        format: S32LE

.. code::

    alsactl restore



