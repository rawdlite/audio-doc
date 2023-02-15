.. _dietpi:

******
Dietpi
******

I used to customise fresh os images with a couple of ansible scripts. This became obsolet when i discovered `dietpi <https://dietpi.com/>`_.
Dietpi provides os images for every SBC platform i care about and then some.
Dietpi then provides a terminal based interface for system configuration and maintainance.
Other than with many ready made audio distributions it is easy to keep the system up to date and install security patches.

Network Setup
_____________

Since almost everything relies on it, it makes sense to setup the network first.

    * wired ethernet

        if one is so lucky as to have wired ethernet available, just plugin a network cable and that is the network setup.

    * Wlan manual setup

        Dietpi provides an easy to use terminal interface to set up WiFi.
        Either do a temporary wired ethernet connect and then ssh into the system or connect a screen and a keyboard.
        Login with user: root and password: dietpi
        Run dietpi-config

    * Wlan scripted setup

        In the file /boot/dietpi-wifi.txt up to 4 WiFi credentials can be configured.
        On dietpi images for raspberry is a Fat32 partition that holds the /boot directory.
        This partition can be mounted with any OS (Windows, Mac, Linux)

        On the dietpi image for the tinkerboard is only one extfs4 partition that contains the /boot directory.
        This makes things a bit more complicated.
        Since we need write access the ext4 partition is best mounted on a linux machine. If a linux machine
        is not available it is best to run a virtual machine like Virtualbox. It is necessary to enable the USB Port
        in settings while the instance is not running. Setting up the instance can be done in the virtualbox gui or with vagrant on the cmdline.

        .. code::

            vagrant init ubuntu/focal64

            vagrant up

            vagrant ssh

        once we are in the virtual instance we need to mount the ext4 partition in the usb slot.
        First we need to find out which device we want o mount.

        .. code::

            sudo fdisk -l

        When we identified /dev/sdc1 as the partition in question we can mount with

        .. code::

            sudo mount /dev/sdc1 /mnt

        Now we can edit /mnt/boot/dietpi-wifi.txt. After saving the changes dont forget to umount the partition before removing the sd-card.

Software Setup
______________

Much like the Wifi setup a software setup can be scripted in dietpi. This is done in /boot/dietpi.txt.

.. code::

    AUTO_SETUP_ACCEPT_LICENSE=1
    AUTO_SETUP_KEYBOARD_LAYOUT=de
    AUTO_SETUP_TIMEZONE=Europe/Berlin
    AUTO_SETUP_NET_ETHERNET_ENABLED=1
    AUTO_SETUP_NET_WIFI_ENABLED=1
    AUTO_SETUP_BOOT_WAIT_FOR_NETWORK=0
    AUTO_SETUP_SSH_SERVER_INDEX=-2
    AUTO_SETUP_AUTOSTART_TARGET_INDEX=11
    AUTO_SETUP_AUTOMATED=1
    #AUTO_SETUP_INSTALL_SOFTWARE_ID=23
    AUTO_SETUP_INSTALL_SOFTWARE_ID=5
    AUTO_SETUP_INSTALL_SOFTWARE_ID=7
    AUTO_SETUP_INSTALL_SOFTWARE_ID=17
    AUTO_SETUP_INSTALL_SOFTWARE_ID=20
    AUTO_SETUP_INSTALL_SOFTWARE_ID=36
    AUTO_SETUP_INSTALL_SOFTWARE_ID=37
    AUTO_SETUP_INSTALL_SOFTWARE_ID=113
    AUTO_SETUP_INSTALL_SOFTWARE_ID=130
    AUTO_SETUP_INSTALL_SOFTWARE_ID=134
    AUTO_SETUP_INSTALL_SOFTWARE_ID=141
    AUTO_SETUP_INSTALL_SOFTWARE_ID=162
    AUTO_SETUP_INSTALL_SOFTWARE_ID=190
    CONFIG_SOUNDCARD=asus-tb-analogue
    SOFTWARE_CHROMIUM_RES_X=1280
    SOFTWARE_CHROMIUM_RES_Y=720
    SOFTWARE_CHROMIUM_AUTOSTART_URL=https://127.0.0.1:6680/

To work around a problem with docker we add this line to /boot/armbianEnv.txt

    ``systemd.unified_cgroup_hierarchy=0``


Commandline
___________

There is a little left to be done on the commandline.
First lets create some comfort to ssh.
On laptop or workstation:

``ssh-copy-id root@192.168.2.114``

edit ~/.ssh/config

.. code::

    host tinker
        Hostname 192.168.2.114
        User root

Now we can ssh into the tinkerboard like so:

``ssh tinker``

With long running installations it is best to use tmux.
Yet i have not found a package with dietpi. So we install it with apt.

``sudo apt install tmux``

Lets test whether the alsa devices are there:

``aplay -L``

Now lets CHeck if we can play some sound through the device.

``speaker-test -c 2 -D hw:CARD=OnBoard,DEV=2``


Next Stop setup DSP