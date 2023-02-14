Distributions
-------------

I have tested a couple of distributions. With the `Evo Sabre <https://www.audiophonics.fr/en/network-audio-players-raspdac/audiophonics-evo-sabre-pack-diy-balanced-dac-2xes9038q2m-streamer-for-raspberry-pi-4-p-14639.html>`_ i am limited to the audiophonics distributions of
volumio, moode and lms until i find out how to install the oled code on a fresh install.
The following is my _personal_ take on the distributions i tried so far.

Raudio 1
--------------

`Raudio 1 <https://github.com/rern/rAudio-1>`_ is a successor to runeaudio.
It is based on arch linux. Technology stack is php and bash scripts.
Setup and operation was smooth. Library import of a large Audiocollection (400GB+) took several hours, yet it succeeded without crashing.

Plus
____

* Tageditor

Minus
_____

* Functionality is somewhoat limited.

* No DSP

* Streaming Services via Airplay/UPnP only

Verdict
_______

I liked the distributions. Recommended for a troublefree experience. Should be possible to add CamillaDSP.
Probably would have done some tinkering if the `Evo Sabre`_ was supported. Replacing mpd for mopidy and its plugins seems promising.

Volumio
-------

`Volumio <https://github.com/volumio?tab=repositories>`_ is based on debian linux.
Technology stack is nodejs. Underneath the typical components mpd, shairplay, upnpmpdcli.
Setup and operation was smooth. Library import of a large Audiocollection (400GB+) repeatedly crashed mpd.
Restart of mpd service or reboot was requiered.

Plus
____

* Qobuz Support

* Interface for reporting stack traces.

Minus
_____

* not very stable (Volumio 2, Volumio 3 Beta) this might change with newer versions. Also it might be my personal setup.

* commercial

Verdict
_______

Volumio is a very popular distribution and rightly so. There are a couple of things i personaly dislike though.
Nodejs is not a favourite of mine. Volumio some what seems to try to become the poor mans ROON.
There is a lot of 'audiophile' chatter. Like the importance of expensive USB-Cables and hearing diffrences in the high frequencies after upgrading the OS-Versions.
The latter of course is not a problem of volumio per se but gets more encouraged as with other distributions.

MoOde
-----

`MoOde`_ shares a common ancestry with Volumio. Technology stack is php and jquery.
I have so far given MoOde only a brief spin. It failed to even attempt to import my nfs share.
No error message in the GUI. I did not investigate further since there are so many alternatives.
I liked the EQ section, although it felt a bit to loosely integrated with a extra section for CamillaDSP in parallel to
EQ and PEQ sections. But then i have spent too little time with Moode to come up with an evaluation.

