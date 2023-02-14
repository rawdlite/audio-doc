*******
Mopidy
*******

Docker Compose
______________

Create a docker-compose.yml file:

.. code::

    version: "3"
    services:
      mopidy:
        image: rawdlite/mopidy
        container_name: mopidy
        devices:
          - "/dev/snd"
        ports:
          - "6600:6600"
          - "6680:6680"
        restart: always
        volumes:
          - ~/.config/:/root/.config/
          - /data/music/:/data/music/
      mysql:
        image: linuxserver/mariadb
        restart: unless-stopped
        container_name: mysql
        environment:
          - PUID=1000
          - PGID=1000
          - MYSQL_ROOT_PASSWORD=b4FUk4mF>3As3aA
          - TZ=Europe/Berlin
          - MYSQL_DATABASE=romprdb
          - MYSQL_USER=rompr
          - MYSQL_PASSWORD=romprdbpass
        volumes:
          - ./db_config:/config
        ports:
          - "3306:3306"
      rompr:
        image: rawdlite/rompr
        container_name: rompr
        restart: always
        ports:
          - "80:80"


Now lets start the containers

``docker-compose up -d``

If this gets an error on the tinkerboard.
Edit /boot/boot.scr

.. code::

    setenv bootargs "... systemd.unified_cgroup_hierarchy=0 ...

then

.. code::

    mkimage -C none -A arm -T script -d /boot/boot.cmd /boot/boot.scr

reboot and test with

.. code::

    cat /proc/cmdline

it should say systemd.unified_cgroup_hierarchy=0. Docker should now run.
We can test this with

``docker ps``


Config Mopidy
_____________

Mopidy configfile is ~/.config/mopidy/mopidy.conf

.. code::

    [core]
    max_tracklist_length = 5000
    restore_state = true

    [audio]
    mixer = none
    output = alsasink device="hw:CARD=OnBoard,DEV=2"

    [file]
    enabled = true
    media_dirs =
      /data/music/music_data|MUSIC
    follow_symlinks = true
    metadata_timeout = 1000
    excluded_file_extensions =
      .directory
      .html
      .jpeg
      .jpg
      .log
      .nfo
      .pdf
      .png
      .txt
      .zip
    show_dotfiles = false

    [softwaremixer]
    enabled = false

    [mpd]
    enabled = true
    hostname = ::
    port = 6600

    [http]
    enabled = true
    hostname = ::
    port = 6680

To see how mopidy is doing:

``docker logs mopidy``

To see the effective configuration

``docker exec -it mopidy mopidy config``

Run Rompr
_________

Browse to the ip of the tinder board. Setup Rompr.
This gives an missing super privilege error.

.. code::

    docker exec -it mysql mysql -u root -p

Use password from docker-compose.yml file.

.. code::

    SET GLOBAL log_bin_trust_function_creators = 1;

Now rompr can use mysql. Now enter the ip of the tinder board in the field MPD SErver.
And RompR should start.
Other interfaces can be used through http://<ip address>:6680

This concludes the player setup for now.
