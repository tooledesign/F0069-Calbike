# OSM Data Editing Instructions

These instructions describe the process of editing OSM data for the Calbike BNA
project. There are five main sections:

1. Software needs
2. Downloading OSM
3. Editing OSM
4. Syncing with the main OSM database
5. Working with the planned bike network

## Software Needs

The training will use [JOSM](https://josm.openstreetmap.de/) as the OSM editor.
This is open source software and can be downloaded and used freely for updating
OSM data. The software can be downloaded from the link. JOSM also requires Java.
The installation will automatically search for Java on your system and suggest
an installation if it can't find one.

There are many other OSM editors, including the online iD editor, which are
suitable for making changes to OSM based on existing conditions. However, care
should be taken not to submit edits to OSM based on the _planned_ network, since
these conditions are not relevant to the current OSM dataset.

The actual BNA runs on Python. Instructions specific to running the BNA will be
provided at a future training.

## Downloading OSM

You may download OSM data from various sources. JOSM includes the ability to
download OSM data directly to the editor. This works well for small areas like
the station areas we will be looking at. If a larger area is needed you can
download an .osm from any number of good sources, such as
[bbbike.org](https://extract.bbbike.org/).

To download data for the area you wish to work on, open JOSM and select the
Download Data tool.

[image]

Navigate the map to the area you wish to download and draw a rectangle around
it. JOSM will automatically download this data for you. At this point, you will
want to save the data as an .osm file on your machine. This will allow you to
work on local data and will also make it easy to create a copy for when you're
ready to work on the planned network.

## Editing OSM

OSM is based on a key=value scheme. Each key=value pair is called a tag. When
you edit OSM, your work will be to add or edit tags on the transportation
network to accurately reflect conditions for bicycling.

To edit a tag on an individual feature, you can simply click on the feature to
select it. The interface will show a list of tags. If you're editing an existing
tag, simply click on the tag and enter a new value. If you need to add a tag,
select the `+` symbol to bring up the new tag dialog. This will ask you for a
key and the value.

PeopleForBikes has published [tagging
guidelines](https://docs.google.com/document/d/1HuAXQUnCEcv9aLZyIDHkLTJ5ZSKfB-U4MlJSmN-1BLk/edit?usp=sharing)
for the BNA that should cover most of the conditions you will come across.

The main conditions you need to pay attention to are:

- Speed limits
- Bike facilities
- Number of lanes
- Parking

You can edit multiple features at once by shift+clicking on all the features you
want to edit and then updating/adding a tag as needed. This is convenient for
updating a speed limit that extends the length of a corridor, for example.

## Syncing with the Main OSM Database

When you have completed edits to the _existing conditions_ you can upload your
changes to the main OSM database by clicking the Upload tool. This will ask for
your OSM user credentials and a description of the changes you've made.

**Please note**: It is recommended that you upload your changes in small batches
of edits that all share a similar theme. For example, you could update speed
limits across an area and then upload those changes. The OSM community tends not
to like massive single updates that contain tons of changes of many different
attributes.

## Working with the Planned Network

Save copy of .osm file
DO NOT UPLOAD TO OSM!
