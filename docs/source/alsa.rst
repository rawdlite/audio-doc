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
    And then there is the :ref:`RME ADI-2 FS <rme>` Dac and the :ref:`Citypulse DA 3.2 <citypulse>` Headphone Amp that can also be connected via usb.
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

