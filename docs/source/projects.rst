************
Projects
************

SSH Setup
---------

All my projects, add ons and customizations are done on the commandline.
So making the terminal access as easy as possible pays of.

Copy Keys
_________

If you have no ssh keys set the up with ssh-keygen.
Then copy them with ssh-copy-id to the target machine.
Like
    ssh-copy-id pi@192.168.0.57
now you can login without the use of a password.

SSH Config
__________

Add an entry in ~/.ssh/config like

    ``Host moode
        Hostname 192.168.0.57
        User pi``

you can login with ssh moode now.

Remote Power Switch
-------------------



Objective
_________

Conveniently control `Power Amps </hardware.html#amplification>`_

Rational
________

My DAC RME ADI-2 DAC FS is located at my listening position and connected via balanced XLR cables to the NC500 Monoblocks sitting next to the speakers.
I would like my monoblocks to be switched on (and off) when my DAC power button is pressed.
Now the RME ADI-2 has no trigger out and the monoblocks have a trigger out, but not the trigger in that i would require for this setup.
Power consumption of the RME ADI-2 and the general electric layout are not sufficient for a master/slave power setup.
Udev Rules to the rescue.

Details
________

The DAC is connected via USB to a Raspberry Pi 4. It is also connected via S/PDIF Coax to a Allo Digione Interface.
The Digione provides a audio interface when the DAC is switched off. When the DAC is switched of its USB audio interface
gets removed. Now this action is what i want to utilize to trigger the power switching of the monoblocks.

Hardware
_________

There are radio controlled (433,92 MHz) Power Plugs that are quite cheap, but documentation i found is poor and a addtional transmitter is needed.
In the end i decided to use `Shelly Plugs <https://shelly-api-docs.shelly.cloud/gen1/#shelly-plug-plugs>`_ since they seemed well documented.
They are rated for 2300 Watt which should be sufficient. They have an internal Webserver running on Moongoose OS and do not require a HUB and cloud access is optional.
Also they support MQTT and CoIoT protocol which is nice to have as well as the build in emeter.

Setup
______

EDIT: I found that the udev rules already present in recent moode do not play well with this approach.
I am using a dedicated Tinkerboard now. YMMV

First lets write a little script to switch the plugs:
/home/pi/bin/switchPlugs.sh

::

    #!/bin/bash
    ACTION=$1
    /usr/bin/curl plug0/relay/0?turn=$ACTION
    /usr/bin/curl plug1/relay/0?turn=$ACTION

For this to work obviously entries in /etc/hosts are requirerd

::

    192.168.0.201	plug0 shellyplug-s-E43746
    192.168.0.202	plug1 shellyplug-s-A7874A

We could have used the IP adresses in the script directly, but this way is more flexible.
Now lets test what we have so far

::

    chmod +x /home/pi/bin/switchPlugs.sh
    /home/pi/bin/switchPlugs.sh on
    /home/pi/bin/switchPlugs.sh off


Now lets define the udev rules to trigger our script. There is an abundance of documentation on udev and setting up udev rules.
Monitor what is going on with udevadm

::

    udevadm monitor
    monitor will print the received events for:
    UDEV - the event which udev sends out after rule processing
    KERNEL - the kernel uevent

    KERNEL[91888.842270] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.2/1-1.2:1.0/sound/card1/controlC1 (sound)
    KERNEL[91888.842424] remove   /devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.2/1-1.2:1.0/sound/card1/pcmC1D0p (sound)
    ...
 /devices/platform/ff540000.usb/usb1/1-1/1-1.1/1-1.1:1.0/sound/card1
This is the log entry triggered when switching off the DAC. This tells us the Dac is registered as card1 controlC1. This might change when amother soundcard is added.
So we search for a more specific identifier.

::

    udevadm info -a /sys/devices/platform/ff540000.usb/usb1/1-1/1-1.3/1-1.3:1.0/sound/card1/

    looking at device '/devices/platform/ff540000.usb/usb1/1-1/1-1.3/1-1.3:1.0/sound/card1':
    KERNEL=="card1"
    SUBSYSTEM=="sound"
    DRIVER==""
    ATTR{id}=="DAC54695303"
    ......


    udevadm info /sys/devices/platform/ff540000.usb/usb1/1-1/1-1.3/1-1.3:1.0/sound/card1/

    E: ID_SERIAL=RME_ADI-2_DAC__54695303__BE6142A734D3AC8
    ....

Now lets create our rule in /etc/udev/rules.d/80-local.rules

::

    ACTION=="add", SUBSYSTEM=="sound", ATTR{id}=="DAC54695303"  RUN+="/root/bin/switchPlugs.sh on"
    ACTION=="remove",  SUBSYSTEM=="sound", ENV{ID_SERIAL}=="RME_ADI-2_DAC__54695303__BE6142A734D3AC8" ,  RUN+="/root/bin/switchPlugs.sh off"

Lets activate the rules

::

    sudo udevadm control --reload

And that's that. Next we could extend the script to also start playback....