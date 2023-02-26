.. _beet:

#####
Beets
#####

Having local audio files well organised in a directory tree has the advantage that it can be mounted via :ref:`nfs`.
to a plethora of applications with a consistent navigation.

* LMS
* Kodi
* Ampache
* Subsonic
* UPnP / DLNA
* Mopidy / MPD
* Yamaha Musicast

The best way to achieve this is the commandline tool `beets <https://beets.io/>`_

My Most Common Commands
-----------------------

Here are the most useful commands i figured out over the years.

Move Album to Grouping Dir
""""""""""""""""""""""""""
I started out to organize my music by genre. The result was some overcrowded genres and a lot of obscure genre directories with just a few songs in there.
I tried setting up a genre tree with subgenres etc, yet this proved to be to complicated as genres are more like a matrix than a tree.
( a specific subgenre often has more than one parent)
Finally i came up with the idea to organize the top level by the field album_grouping.

In the config.yaml i have:

.. code-block::

    paths:
        default: %if{%ifdef{album_grouping},_${album_grouping}%if{%ifdef{subgroup},/-${subgroup}},$genre}/%asciify{%if{$albumartist_sort,$albumartist_sort,$albumartist}}/%if{$original_year,${original_year}-,%if{$year,${year}-}}%asciify{$album}/%if{$disc,$disc-}%if{$track,${track}_-_}%asciify{${artist}_-_${album}_-_$title}

Now albums are sorted to groupings like so

.. code-block:: bash

    beet import -A /data/music/music_data/beets/1/101_Strings --set album_grouping=World

To reorganize your existing collection

.. code-block::

    beet modify -a albumartist::^CAN$ album_grouping=Rock subgroup=Krautrock

Two things are noteworthy here. When you query in the album context (-a) it is albumartist not artist
to query for. And second, if i would use the query albumartist:CAN i would also reorganize Laura Cantrell, Dead Can Dance and Boards of Canada.

No Album
""""""""

Some albums i have only 1 or 2 songs of or dont know the name of the album.
For this songs i use a no-album configuration

.. code-block::

    album:no-album:  %if{%ifdef{album_grouping},_${album_grouping}%if{%ifdef{subgroup},/-${subgroup}},$genre}/%asciify{$albumartist}/%asciify{${artist}_-_$title}

Move a Singleton to Grouping Dir
""""""""""""""""""""""""""""""""

It is important to note that beet by default works o whole albums.
Yet when you want to work on a single song (-s) the name of the field is grouping.

.. code-block:: bash

    beet import -As  /data/music/music_data/beets/1/17_trouser_press_\(saturday_cl/11_-_17_trouser_press_.mp3 --set grouping=Rock

Some artists i have just 1 or 2 songs of. Having this songs organised under the artists name would result i a very cluttered directory tree.
I organise these songs in a directory 00_Singletons under their grouping (and optionally subgroup) directory.

.. code-block::

    singleton: %if{${grouping},_${grouping}/%if{%ifdef{subgroup},-${subgroup}/}00_Singletons,00_Singletons/-${genre}}/%asciify{${artist}_-_$title}

Note, there is a difference between the genre of a song and the genre of an album. Easy to get confused when writing path configurations.

Radioplays
""""""""""

I have special path configuration for radio plays that i record with tvheadend.

.. code::

    genre:"Radio Play": 00_HOERSPIELE/%if{${grouping},${grouping},%if{${album},${album},Hoerspiel}}/%asciify{${title}%if{${artist},_-_${artist}}}%if{$original_year,-${original_year},%if{$year,-${year}}}%if{$track,-Teil_$track}%if{$tracktotal,_von_$tracktotal}

When changing the path definition in config.yaml you can reimport the files

.. code::

    beet import -As $PWD/Hungern_un_Freten-2023.mp3

Modify tags
"""""""""""

You can change a files tags

.. code::

    beet modify $PWD/Hungern_un_Freten-2023.mp3 album='Niederdeutsches_Hoerspiel'

Note this is the same as path:$PWD/Hungern_un_Freten-2023.mp3. Beets recocgises a path and does a path query automatically.
You could also do this like:

.. code::

    beet modify album:'Plattdeutsches Hoerspiel' album='Niederdeutsches_Hoerspiel'

Modify album fields
"""""""""""""""""""

modify by default works on single files. To work on album use -a

.. code-block:: bash

    beet modify -a genre:balkan genre='Balkan Pop'

Note: In the context of album the artist field is albumartist.
The advantage of using modify vs import -A and --set is the Overview of changes
which can be cancelled. On the other hand a path does not work well in the album context.

Edit
""""

Another great way change some tags is the edit command

.. code-block::

    beet edit $PWD/Seker_is_seker-Teil_04_von_04.mp3

Even better you can edit multiple files in one go

.. code-block::

    beet edit $PWD

Also you can edit all songs of an Album. You can specify field you want to edit with -f.

.. code-block:: bash

    beet edit -a -f albumartist_sort  -f genre -f album_grouping albumartist:A.R.E

Delete File
"""""""""""

By default beet removes files only from its library, leaving the file on disk.
to also remove from disk, use the -d option. With -f you will not be asked for confirmation.

.. code-block:: bash

    beet remove -d /data/music/music_data/beets/2/20_humanoid_boogie_\(radio_1_c/11_-_20_humanoid_boogie_.mp3

Sometimes i find it easier to delete files on disk first and update beets library later.

.. code-block::

    ls *.[1-9].mp3 #better save than sorry
    rm *.[1-9].mp3
    beet update $PWD

Find exact expression
"""""""""""""""""""""

By default beet queries look for anything that contains your searchstring.
( like %search% in sql)
Sometimes you want to narrow it down.

.. code-block:: bash

    beet ls -a genre::^ambient$

this excludes genres like 'Dark Ambient' which would otherwise be in the resultset

Merge 2 or more albums
______________________

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
______________________

Play Songs from the commandline
"""""""""""""""""""""""""""""""

You can add the result of a beets query to mopidy tracklist like so:

.. code-block:: bash

    beet ls -f 'file://$path' artist:Brian Eno album:Before And After Science | mpc add

Play Contents of a Dir
""""""""""""""""""""""

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
