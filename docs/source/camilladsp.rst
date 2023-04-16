.. _camilladsp:

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
    mkdir -p ~/camilladsp/configs
    mkdir -p ~/camilladsp/coeffs
    mkdir -p ~/camilladsp/templates


How to continue
_______________

There are two ways to install camilladsp:

1) Loopback Device
2) Alsa Plugin

There a pros and cons to each approach.
The cdsp plugin allows to switch samplingrates.
Basically it uses a Template Configuration and replaces variables for samplerate etc and restarts camilladsp.
On the downside you loose the ability to edit the configuration through the GUI.
OTOH The Loopback is easy to setup and allows for config editing through the GUI.
Yet you are limited to using a single samplerate. In case you want to also use shairport-sync samplerat is limited to 44100 or 88200 for all sound applications.

Fortunately both approaches are not exclusive. How they can be used simultaneously will be shown later on.


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

We have a Loopback Device.
Now create a minimal Config in camilladsp/configs/default_config.yml

.. code::

    devices:
      adjust_period: 10
      capture: {channels: 2, device: 'hw:CARD=Loopback,DEV=1', format: S16LE, type: Alsa}
      capture_samplerate: 0
      chunksize: 1024
      enable_rate_adjust: false
      enable_resampling: false
      playback: {channels: 2, device: 'plughw:CARD=sndallodigione,DEV=0', format: S32LE,
        type: Alsa}
      queuelimit: 1
      rate_measure_interval: 1
      resampler_type: Synchronous
      samplerate: 48000
      silence_threshold: -60
      silence_timeout: 3
      stop_on_rate_change: false
      target_level: 0
    filters: {}
    mixers:
      stereo:
        channels: {in: 2, out: 2}
        mapping:
        - dest: 0
          mute: false
          sources:
          - {channel: 0, gain: -3, inverted: false, mute: false}
        - dest: 1
          mute: false
          sources:
          - {channel: 1, gain: -3, inverted: false, mute: false}
    pipeline:
    - {name: stereo, type: Mixer}

Note: 'hw:CARD=Loopback,DEV=1' is the Output Device of the AlsaLoopback to the Input of hw:CARD=Loopback,DEV=0.
Adapt 'plughw:CARD=sndallodigione,DEV=0' to your actual Device found with aplay -L and link it.


.. code::

    ln -s configs/default_config.yml /home/dietpi/camilladsp/active_config.yml

Start camilladsp

.. code::

    /usr/local/bin/camilladsp -o /home/dietpi/camilladsp/camilladsp.log -p 1234 /home/dietpi/camilladsp/active_config.yml &

Test with

.. code::

    speaker-test -D hw:CARD=Loopback,DEV=0 -c 2 -t wav

Install CamillaDSP Alsa Plugin
______________________________

.. code-block::

    apt install libasound2-dev build-essential
    git clone https://github.com/scripple/alsa_cdsp.git
    apt install libasound2-dev build-essential
    cd alsa_cdsp/
    make
    make install
    mv /alsa-lib/ /usr/lib/arm-linux-gnueabihf/
    cat asound.conf >> /etc/asound.conf


edit /etc/asound.conf

.. code::

    pcm.camilladsp {
    type cdsp
       cpath "/usr/local/bin/camilladsp"
       config_out "/root/camilladsp/configs/config_out.yaml"
       config_in "/root/camilladsp/templates/config_in.yaml"
       channels 2
       rates = [
           44100
           48000
           88200
           96000
          192000
       ]
       cargs [
           -p "1234"
           -a "0.0.0.0"
           -l warn
       ]
       #start_cmd "/opt/bin/switchPlugs.sh on"
    }


edit /root/camilladsp/templates/config_in.yaml

.. code::

    devices:
      samplerate: $samplerate$
      chunksize: 1024
      queuelimit: 1
      capture: {
        type: File,
        channels: $channels$,
        filename: "/dev/stdin",
        format: $format$
      }
      playback: {channels: 2, device: 'plughw:CARD=DAC54695303,DEV=0', format: S32LE,
        type: Alsa}
      rate_measure_interval: 1
      resampler_type: Synchronous
      silence_threshold: -60
      silence_timeout: 3
      stop_on_rate_change: false
    filters: {}
    mixers:
      stereo:
        channels: {in: 2, out: 2}
        mapping:
        - dest: 0
          mute: false
          sources:
          - {channel: 0, gain: -3, inverted: false, mute: false}
        - dest: 1
          mute: false
          sources:
          - {channel: 1, gain: -3, inverted: false, mute: false}
    pipeline:
    - {name: stereo, type: Mixer}

.. code::

    alsactl restore

Test with:

.. code::

    speaker-test -D camilladsp -c 2 -r 48000