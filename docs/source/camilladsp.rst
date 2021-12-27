CamillaDSP
----------

install camilladsp
__________________

Get camilladsp-linux-armv7.tar.gz

``wget https://github.com/HEnquist/camilladsp/releases/download/v0.6.3/camilladsp-linux-armv7.tar.gz``

Unpack

``tar xzf camilladsp-linux-armv7.tar.gz
  mv camilladsp /usr/local/bin/``

Install CamillaDSP Alsa Plugin
______________________________

``git clone https://github.com/scripple/alsa_cdsp.git``
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

``alsactl nrestore``

python3 -m pip install git+https://github.com/HEnquist/pycamilladsp.git@v0.6.0
python3 -m pip install git+https://github.com/HEnquist/pycamilladsp-plot.git@v0.6.0

wget https://github.com/HEnquist/camillagui-backend/releases/download/v0.8.0/camillagui.zip




