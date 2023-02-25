.. _beets:

#####
Beets
#####


My Common Commands
------------------

Move Album to Grouping Dir

.. code-block:: bash

    beet import -A /data/music/music_data/beets/1/101_Strings --set album_grouping=World

Move a Singleton to Grouping Dir

.. code-block:: bash

    beet import -As  /data/music/music_data/beets/1/17_trouser_press_\(saturday_cl/11_-_17_trouser_press_.mp3 --set grouping=Rock

Modify album fields

.. code-block:: bash

    beet modify -a genre:balkan genre='Balkan Pop'

In the context of album the artist field is albumartist.
The advantage of using modify vs import -A and --set is the Overview of changes
which can be cancelled. On the other hand a path does not work well in the album context.

Delete File

.. code-block:: bash

    beet remove -df /data/music/music_data/beets/2/20_humanoid_boogie_\(radio_1_c/11_-_20_humanoid_boogie_.mp3

Edit an Album

.. code-block:: bash

    beet edit -a -f albumartist_sort  -f genre -f album_grouping albumartist:A.R.E

Find exact expression

.. code-block:: bash

    beet ls -a genre::^ambient$

this excludes genres like 'Dark Ambient' which would otherwise be in the resultset

Merge 2 or more albums
----------------------

Different values for original_year, year, genre etc can cause beet to distribute files in separate albums. These albums can have the same name yet have diferent ids.

Remove Files from existing albums

.. code-block:: bash

    beet remove album_id:5797

Move Files to same Dir. Delete Duplicates

Write consistent Tags

.. code-block:: bash

    mid3v2 -A "Peel Session" -a "cLOUDDEAD" -y 2002 /path/*

Import Album

.. code-block:: bash

    beet import -A /data/music/music_data/beets/-Indie/cLOUDDEAD/2002-Peel_Session --set album_grouping=Indie --set genre='Hip Hop' --set original_year=2002

Using beets and mopidy
Play Songs from the commandline
You can add the result of a beets query to mopidy tracklist like so:

.. code-block:: bash

    beet ls -f 'file://$path' artist:Brian Eno album:Before And After Science | mpc add

Play Contents of a Dir

.. code-block:: bash

    mpc clear
    find $1 -type f -exec mpc add file://{} \;
    mpc play

Cleanup Filesystem with find
----------------------------

Delete empty Dirs
.. code::

    find .  -type d -empty -delete

Delete hidden files

.. code::

    find . -type f -name ".*" -delete

Delete @eaDir
.. code::

    find .  -type d -name "@eaDir" -exec rm -rf {} \;

list Dirs and No. of files comtained
.. code::

    find . -type 'f' -printf '%h\n' | sort | uniq -c | sort -g

Script to import as album when Dir has more than 3 files (using parent dir)
.. code-block:: bash

    #!/bin/bash
    find "$PWD/$1" -type 'f' -printf '%h\n' | sort | uniq -c | sort -g | awk -F " " '$1>3{ print $NF "/.."}' | xargs -n 1 beet import -A

Need to use absolute path otherwise beets creates duplicate entries.

import as Singleton when Dir contains only 1 file
.. code-block:: bash

 #!/bin/bash
 find "$PWD/$1" -type 'f' -printf '%h\n' | sort | uniq -c | sort -g | awk -F " " '$1<2{ print $NF }' | xargs -n 1 beet import -As
