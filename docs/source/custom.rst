.. _custom:

***************
Custom Scripts
***************

Autoswitch on for my Monoamps

SSH Setup
_________

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

    ``Host dietpi
        Hostname 192.168.0.57
        User dietpi``

you can login with ssh dietpi now.


check for sound
_______________

.. code-block:: python

    #!/usr/bin/python3

    SOUNDCARD_DEVICE_FILE = "/proc/asound/sndallodigione/pcm0p/sub0/status" # Path of souncard status file
    SHUTDOWN_TIMEOUT = 15 # Delay before amplifier power down after soundcard released

    #-----------------------------------
    import os
    import time
    import ShellyPy

    def Now():
        return int(time.time())

    def CheckSoundcardStatus():
        global deviceFile
        buf = ""
        lastException = None
        for i in range(3):
            try:
                os.lseek(deviceFile, 0, os.SEEK_SET)
                buf = os.read(deviceFile, 14)
                return (len(buf) == 14 and buf[7] == 82 and buf[8] == 85 and \
                    buf[9] == 78 and buf[10] == 78 and buf[11] == 73 and \
                    buf[12] == 78 and buf[13] == 71) # Check for "RUNNING"
            except Exception as ex: # Attempt to open device file again
                try:
                    os.close(deviceFile)
                except:
                    pass
                try:
                    deviceFile = os.open(SOUNDCARD_DEVICE_FILE, os.O_RDONLY)
                except Exception as ex:
                    lastException = ex
        raise lastException # All attempt failed

    def CheckAmpStatus():
        status_left = amp_switch_left.status()
        status_right = amp_switch_right.status()
        if status_left.get('relay') and status_right.get('relay') and status_left['relay']['json'] and status_right['relay']['json']:
            return True
        else:
            return False

    def PowerOn():
        print("Power ON Amplifier")
        amp_switch_left.relay(0, turn=True)
        amp_switch_right.relay(0, turn=True)

    def PowerOff():
        print("Power OFF Amplifier")
        amp_switch_left.relay(0, turn=False)
        amp_switch_right.relay(0, turn=False)

    amp_switch_left = ShellyPy.Shelly("192.168.1.21")
    amp_switch_right = ShellyPy.Shelly("192.168.1.22")
    deviceFile = None
    lastStatus = CheckAmpStatus()
    newStatus = lastStatus
    lastIdle = -1

    while True:
        try:
            nowStatus = CheckSoundcardStatus()
        except Exception as ex:
            print(ex)
            time.sleep(1)
            continue

        if nowStatus:
            if not lastStatus:
                print("Soundcard Working")
                PowerOn()
                lastStatus = True
        else:
            if lastStatus:
                print("Soundcard Released")
                lastStatus = False
                lastIdle = Now()
            elif (not lastStatus) and (lastIdle != -1):
                if Now() - lastIdle >= SHUTDOWN_TIMEOUT:
                    print("Timeout Reached")
                    PowerOff()
                    lastIdle = -1
        time.sleep(0.2)

